import sqlite3

# con = sqlite3.connect("lesson.bd") # соединились с бд
# cursor = con.cursor() # идет в бд с запросом
# cursor.execute("CREATE TABLE movie(title, year,score)")
# cursor.execute("INSERT INTO movie(title, year,score) VALUES('matrica','2002','10')")
# con.commit()
# cursor.execute("SELECT * FROM movie")
# movies = cursor.fetchall()
# print(movies)
# cursor.execute("UPDATE movie set year ='99' WHERE year = '2000'")
# con.commit()

# cursor.execute("SELECT * FROM movie WHERE title ='matrica'")
# movies = cursor.fetchall()
# print(movies)

# это SQLite---------------------------

# with sqlite3.connect("users.db") as con:
#     # con.execute("CREATE TABLE user("
#     #             "login TEXT NOT NULL,"
#     #             "phone INTEGER NOT NULL,"
#     #             "password TEXT NOT NULL)")
#     pass
# print('----------')
#
#
# def regisration():
#     login = input("введите логин:")
#     phone = int(input("введите номер телефона:"))
#     password = input("введите пароль:")
#     password_2 = input("подтвердите пароль:")
#     if password == password_2:
#         print('ok')
#         with sqlite3.connect("users.db") as con:
#             con.execute("INSERT INTO user(login,phone,password)"
#                         "VALUES (?,?,?)", (login, phone, password))
#     else:
#         print('в доступе отказан')
#
#
# def autorization():
#     login = input("введите логин:")
#     password = input("введите пароль:")
#
#     with sqlite3.connect("users.db") as con:
#         cursor = con.cursor()
#         sql = "SELECT login, password FROM user WHERE login = '%s'" % login
#         cursor.execute(sql)
#         user = cursor.fetchone()
#         if password == user[1]:
#             print("успешно авторизовались!")
#         else:
#             print("Неверный пароль!")

#
#
# def main():
#     print("1.регистрация")
#     print("2.авторизация")
#
#     action = {
#         1: regisration,
#         2: autorization
#     }
#
#     choose = int(input('ваш выбор:'))
#     action[choose]()
#
#
# main()


# ORM---------------------------------
from sqlalchemy import create_engine, Integer, String, Column, DateTime
from sqlalchemy.orm import declarative_base, Session
from sqlalchemy.exc import IntegrityError as sq_IntegrityError
from datetime import datetime

engine = create_engine("sqlite+pysqlite:///books.db", echo=True, future=True)
session = Session(bind=engine)

Base = declarative_base()


class Autor(Base):
    __tablename__ = "autors"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    count_books = Column(Integer, nullable=True)
    birth_year = Column(DateTime())


# Base.metadata.create_all(engine)

a1 = Autor(
    name="Лев Толстой",
    count_books=30,
    birth_year=datetime(1820, 11, 17)
)
session.add(a1)
try:
    session.commit()
except sq_IntegrityError:
    print('дублирование имени')


session.rollback()
autor = session.query(Autor.id, Autor.name).all()
print()

