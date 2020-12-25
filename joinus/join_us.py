from flask import Flask
from random import randrange
import mysql.connector
from DBcm import UseDatabase
from flask import render_template
app = Flask(__name__)

dbconfig =  {
            'host' : 'localhost',
            'user' : 'root',
            'password' : 'root',
            'database' : 'join_us',
            }

@app.route('/')
def users_num():
    with UseDatabase(dbconfig) as cursor:
        _SQL = 'select count(*) as count from users;'
        cursor.execute(_SQL)
        count = cursor.fetchall()
        result = str(count).strip('[()],')
        return render_template('home.html', count = result)

@app.route('/cleardb')
def clear_db():
    with UseDatabase(dbconfig) as cursor:
        _SQL = 'delete from users;'
        cursor.execute(_SQL)
    return 'Database cleared'

if __name__ == '__main__':
    app.run(debug = True)