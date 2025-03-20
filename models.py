from peewee import *

db = SqliteDatabase('my_database.db')

class Table(Model):
    class Meta:
        database = db

class User(Table):
    user_name = CharField()
    password_hash = CharField()
    surname = CharField()
    name = CharField()
    protonymic = CharField()
    
class Role(Table):
    name = CharField()

class UserRole(Table):
    user = ForeignKeyField(User)
    role = ForeignKeyField(Role)

if __name__ == '__main__':
    db.connect()
    db.create_tables([User, Role, UserRole])
    query = User.select(User).join(UserRole).join(Role).where(Role.name=='Сотрудник')
    for row in query:
        print(row.user_name)