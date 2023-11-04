from flask import Flask, render_template
import util

# create application instance
app = Flask(__name__)

# Global variables
username = 'raywu1990'
password = 'test'
host = '127.0.0.1'
port = '5432'
database = 'dvdrental'

# Home route
@app.route('/')
def index():
    cursor, connection = util.connect_to_db(username, password, host, port, database)
    record = util.run_and_fetch_sql(cursor, "SELECT * from customer;")
    if record == -1:
        print('Something is wrong with the SQL command')
    else:
        col_names = [desc[0] for desc in cursor.description]
        log = record[:5]
    util.disconnect_from_db(connection, cursor)
    return render_template('index.html', sql_table=log, table_title=col_names)

# Update basket_a
@app.route('/api/update_basket_a')
def update_basket_a():
    cursor, connection = util.connect_to_db(username, password, host, port, database)
    try:
        cursor.execute("INSERT INTO basket_a VALUES (5, 'Cherry');")
        connection.commit()
        message = "Success!"
    except Exception as e:
        message = str(e)
    util.disconnect_from_db(connection, cursor)
    return message

# Showing unique fruits in basket_a and basket_b
@app.route('/api/unique')
def unique():
    cursor, connection = util.connect_to_db(username, password, host, port, database)
    success = False
    error_message = None
    try:
        cursor.execute("SELECT DISTINCT fruit_a FROM basket_a;")
        unique_a = cursor.fetchall()
        cursor.execute("SELECT DISTINCT fruit_b FROM basket_b;")
        unique_b = cursor.fetchall()
        success = True
    except Exception as e:
        error_message = str(e)
    util.disconnect_from_db(connection, cursor)
    return render_template('index.html', unique_a=unique_a, unique_b=unique_b, success=success, error_message=error_message)

if __name__ == '__main__':
    app.debug = True
    ip = '127.0.0.1'
    app.run(host=ip)
