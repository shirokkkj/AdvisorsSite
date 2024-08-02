from peewee import *
import datetime
db = SqliteDatabase('users.db')

class Users(Model):
    name = CharField()
    password = CharField()
    date = DateField(default=datetime.datetime.now())
    
    class Meta:
        database = db