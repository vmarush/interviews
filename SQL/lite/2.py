import sqlite3 as sq

con = sq.connect("dz.db")
cur = con.cursor()
with con:
    cur.execute("""CREATE TABLE IF NOT EXISTS book(
            user_id INTEGER,
            book_title TEXT,
            page INTEGER, 
            chapters INTEGER,
            year_of_issue INTEGER
            );
            """)
with con:
    cur.execute("""CREATE TABLE IF NOT EXISTS autor(
            autor_name TEXT,
            days_of_creation INTEGER,
            total_money INTEGER
            );
            """)


def book_standard():
    include_1 = "INSERT INTO book(user_id, book_title, page, chapters, year_of_issue)" \
                "values(?,?,?,?,?)"
    data1 = [(1, "война и мир", 500, 12, 1867),
             (2, "детство", 200, 26, 1852)
             ]
    with con:
        cur.executemany(include_1, data1)


def autor_standard():
    include_2 = "INSERT INTO autor(autor_name,days_of_creation,total_money)" \
                "values(?,?,?)"
    data2 = [("тослтой", 673, 1000000),
             ("тослтой", 412, 24155554)
             ]
    with con:
        cur.executemany(include_2, data2)


# autor_standard()
# book_standard()


def insert_autor(autor_name: str, days_of_creation: int, total_money: int):
    data = (autor_name, days_of_creation, total_money)
    with con:
        cur.execute("INSERT INTO autor(autor_name,days_of_creation,"
                    "total_money) values(?,?,?)", data)


# insert_autor("пушкин", 224, 1241515)


def insert_book(user_id: int, book_title: str, page: int, chapters: int, year_of_issue: int):
    data = (user_id, book_title, page, chapters, year_of_issue)
    with con:
        cur.execute("INSERT INTO book(user_id,book_title,"
                    "page,chapters,year_of_issue) values(?,?,?,?,?)", data)


# insert_book(3, "евгений онегин", 543, 12, 1833)

def read_table_book():
    try:
        nazvanie_stolba = input('nazvanie_stolba')
        print(cur.execute(f"SELECT {nazvanie_stolba} FROM book").fetchall())
    except Exception:
        print('неверный ввод')


def read_table_autor():
    try:
        nazvanie_stolba = input('nazvanie_stolba')
        print(cur.execute(f"SELECT {nazvanie_stolba} FROM book").fetchall())
    except Exception:
        print('неверный ввод')


def my_table():
    a = cur.execute("SELECT autor_name,days_of_creation,book_title,year_of_issue FROM autor " \
                    "LEFT JOIN book ON days_of_creation  >250")
    a = a.fetchone()
    print(a)


def all_in_book():
    a = cur.execute("SELECT * FROM book")
    a = a.fetchall()
    print(a)


def all_in_autor():
    a = cur.execute("SELECT * FROM autor")
    a = a.fetchall()
    print(a)


# print(f'если хотите просмотреть все из таблицы книга введите 1 '
#       f'если хотите просмотреть все из таблицы автор введите 2'
#       f'если хотите прочитать из таблицы автор конкретную строчку 3'
#       f'если хотите прочитать из таблицы книга конкретную строчку 4'
#       f'если хотете добавить в таблицу книги нажмите 5'
#       f'если хотете добавить в таблицу автор нажмите 6'
#       f'если хотете посмотреть мою таблицу  нажмит 7')


def five():
    user_id = int(input('id'))
    book_title = input('book_title')
    page = int(input("page"))
    chapters = int(input("chapters"))
    year_of_issue = int(input("year_of_issue"))
    return insert_book(user_id, book_title, page, chapters, year_of_issue)


def six():
    autor_name = str(input('autor_name'))
    days_of_creation = int(input("days_of_creation"))
    total_money = int(input("total_money"))
    return insert_autor(autor_name, days_of_creation, total_money)


# menu = int(input("введите число"))
# d = {1: all_in_book,
#      2: all_in_autor,
#      3: read_table_autor,
#      4: read_table_book,
#      5: five,
#      6: six,
#      7: my_table}
# print(d[menu]())


def table_exists(table_name):
    cur.execute('''SELECT count(name) FROM sqlite_master WHERE TYPE = 'table' AND name = '{}' '''.format(table_name))
    if cur.fetchone()[0] == 1:
        return True
    return False


# print(table_exists("autor"))

def get_movies():
    cur.execute('''SELECT * FROM autor''')
    data = []
    for row in cur.fetchall():
        data.append(row)
    return data


# a = get_movies()
# print(a)
def get_movie(movie_id):
    cur.execute('''SELECT * FROM book WHERE user_id = {}'''.format(movie_id))
    data = []
    for row in cur.fetchall():
        data.append(row)
    return data


# a = get_movie(5)
# print(a)


def update_movie(user_id, update_dict):
    valid_keys = ['book_title', 'page', 'chapters', 'year_of_issue']
    for key in update_dict.keys():
        if key not in valid_keys:
            raise Exception('Invalid field name!')
    for key in update_dict.keys():
        if type(update_dict[key]) == str:
            stmt = '''UPDATE book SET {} = '{}' WHERE user_id = {}'''.format(key, update_dict[key], user_id)
        else:
            stmt = '''UPDATE book SET {} = '{}' WHERE user_id = {}'''.format(key, update_dict[key], user_id)
        cur.execute(stmt)
    con.commit()


update_movie(4, {'book_title': 'горе от ума', 'page': 155, 'chapters': 12, 'year_of_issue': 1884})


def eror():
        nazvanie_stolba = input('nazvanie_stolba')
        print(cur.execute(f"SELECT {nazvanie_stolba} FROM book").fetchall())
eror()