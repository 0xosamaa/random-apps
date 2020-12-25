from DBcm import UseDatabase
from faker import Faker

dbconfig =  {
            'host' : 'localhost',
            'user' : 'root',
            'password' : 'root',
            'database' : 'join_us',
            }

fake = Faker()
bulk = [(fake.name(), fake.email(), fake.past_datetime()) for i in range(500)]

with UseDatabase(dbconfig) as cursor:
    _SQL = """insert into users (name, email, created_at) values (%s, %s, %s);"""
    cursor.executemany(_SQL, bulk)

    _SQL = """select * from users;"""
    cursor.execute(_SQL)
    results = cursor.fetchall()
    print(results)