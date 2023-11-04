# Fruit Basket CSCI3700 Flask SQL Integration

## Project Description
This project integrates a Flask application with PostgreSQL. The project provides a local web interface to display database information. The user can also update the SQL database.

## Getting Started

First, we need to install a Python 3 virtual environment with:

```sh
sudo apt-get install python3-venv
```

Create the virtual environment:

```sh
python3 -m venv python_venv
```

You need to activate the virtual environment when you want to use it:

```sh
source python_venv/bin/activate
```

To fufil all the requirements for the python server, you need to run:

```sh
pip3 install -r requirements.txt
```

Because we are now inside a virtual environment. We do not need sudo.

Then you can start the server with:

```sh
python3 main.py
```

Make sure to run the following SQL commands in your database to ensure the **basket_a** and **basket_b** tables are created.

```sql
CREATE TABLE basket_a (

    a INT PRIMARY KEY,

    fruit_a VARCHAR (100) NOT NULL

);

CREATE TABLE basket_b (

    b INT PRIMARY KEY,

    fruit_b VARCHAR (100) NOT NULL

);
```
```sql
INSERT INTO basket_a (a, fruit_a)

VALUES

    (1, 'Apple'),

    (2, 'Orange'),

    (3, 'Banana'),

    (4, 'Cucumber');

INSERT INTO basket_b (b, fruit_b)

VALUES

    (1, 'Orange'),

    (2, 'Apple'),

    (3, 'Watermelon'),

    (4, 'Pear');
```

You should now be able to navigate to 127.0.0.1:5000 in a web browser to access the application

### It's also important to note the following hardcoded details

username = **raywu1990**

password = **test**

host = **127.0.0.1**

port = **5432**

database = **dvdrental**

The **127.0.0.1** IP address indicates local hosting

## Team Members

Quinton Ross & Beckett Stevens

