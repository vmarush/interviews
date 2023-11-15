# import sqlite3
import datetime
# # with sq.connect("saper.db") as marush:
# #     cur = marush.cursor()  # зоздает экзепляр класса Cursor
# #
# #     cur.execute("DROP TABLE IF EXISTS people")  # удаляет базу данных
# #
# # cur.execute("""CREATE TABLE IF NOT EXISTS people(
# #     user_id INTEGER PRIMARY KEY AUTOINCREMENT,
# #     school INTEGER NOT NULL DEFAULT 1,
# #     name TEXT NOT NULL,
# #     old INTEGER,
# #     clas INTEGER
# #     )""")
# # Всегда должет быть заполнен (not null)
# # значение по умолчанию (default 1)
# # Содержит уникальные ключи PRIMARY KEY
# # Добавляет единицу к следующему AUTOINCREMENT
#
#
# # вывод из бд
# # with sq.connect("saper.db") as marush:
# #     cur = marush.cursor()
#
#     # print(cur.execute("SELECT * FROM people WHERE old < 7 ORDER BY old DESC LIMIT 5").fetchall())
#
# con = sqlite3.connect("test.db")
# cur = con.cursor()
# with con:
#     cur.execute("""
#         CREATE TABLE user (
#             id INT NOT NULL PRIMARY KEY,
#             name TEXT,
#             age INTEGER
#         );
#     """)
#
# query = 'INSERT INTO USER (id, name, age) values(?, ?, ?)'
# data1 = [
#     (2, 'Vova', 25),
#     (3, 'Anna', 21),
#     (4, 'Kolya', 19)
# ]
# with con:
#     cur.executemany(query, data1)
#
# data = (1, "Sasha", 32)
# with con:
#     cur.execute("INSERT INTO user (id, name, age) values(?, ?, ?)", data)
#
#
#
# with con:
#     cur.execute("""
#         CREATE TABLE language (
#             id INT NOT NULL PRIMARY KEY,
#             name TEXT
#         );
#     """)
#
# with con:
#     cur.execute("""
#         CREATE TABLE user_language (
#             user_id INT,
#             language_id INT,
#             PRIMARY KEY(user_id, language_id),
#             FOREIGN KEY(user_id) REFERENCES user(id),
#             FOREIGN KEY(language_id) REFERENCES language(id)
#         );
#     """)
# data3 = [
#     (1, "english"),
#     (2, "spanish"),
#     (3, "french")
# ]
# with con:
#     cur.executemany("INSERT INTO language VALUES(?, ?)", data3)
#
# data5 = [
#     (1, 2), # Саша знает испанский
#     (2, 1), # Вова знает английский
#     (2, 2), # Вова еще знает испанский
#     (3, 3), # Анна знает французский
# ]
# with con:
#     cur.executemany("INSERT INTO user_language VALUES(?, ?)", data5)
#
# cur.execute("""
#     SELECT user.name, language.name
#     FROM user, language, user_language
#     WHERE (user.id = user_language.user_id AND
#            language.id = user_language.language_id)
#     """).fetchall()
#
# con.close()

a = input()
b = datetime.datetime(a)
print(b)