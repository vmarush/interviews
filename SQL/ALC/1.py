# from sqlalchemy import create_engine, Column, Integer, String
# from sqlalchemy.orm import Session, declarative_base
#
# engine = create_engine("sqlite+pysqlite:///items.db", echo=True, future=True)
# session = Session(bind=engine)
# Base = declarative_base()
#
#
# class Item(Base):
#     __tablename__ = "items"
#     id = Column(Integer(), primary_key=True)
#     name = Column(String(100), nullable=False, unique=True)
#     count = Column(Integer(), nullable=False)
#     category = Column(String(100), nullable=False)
#
#     def __init__(self, name: str, count: int, category: str):
#         self.name = name
#         self.count = count
#         self.category = category
#
#
# # Base.metadata.create_all(engine)
# info = [
#     {"name": "джинсовка",
#      "count": 5,
#      "category": "верхняя"},
#     {"name": "штаны",
#      "count": 5,
#      "category": "нижние"},
#     {"name": "перчатки",
#      "count": 5,
#      "category": "руки"},
#     {"name": "шарф",
#      "count": 5,
#      "category": "верхняя"},
#     {"name": "кепка",
#      "count": 5,
#      "category": "головной убор"}
# ]
#
# items = []
# for item in info:
#     i = Item(name=item['name'], count=item['count'], category=item['category'])
#     items.append(i)
#
# session.add_all(items)
# session.commit()

#
# from sqlalchemy import create_engine, Column, Integer, String, ForeignKey,MetaData
# from sqlalchemy.orm import Session, declarative_base, relationship
#
# engine = create_engine("sqlite+pysqlite:///items.db", echo=True, future=True)
# session = Session(bind=engine)
#
# Base = declarative_base()
#
#
# class Book(Base):
#     __tablename__ = "books"
#     id = Column(Integer(), primary_key=True)
#     title = Column(String(100), nullable=False)
#     genre_id = Column(Integer(), ForeignKey("genres.id"))
#     #новое поле в табле
#     price = Column(Integer())
#
#     def __repr__(self):
#         return f"книга {self.id} {self.title}"
#
#
# class Genre(Base):
#     __tablename__ = "genres"
#     id = Column(Integer(), primary_key=True)
#     title = Column(String(100), nullable=False)
#     books = relationship("Book")
#
#     def __repr__(self):
#         return f"{self.id},{self.title}"
#
#
# # Base.metadata.create_all(engine)
# # genres = ["Фентези", "Детектив", "Художественное"]
# # for genre in genres:
# #     g = Genre(title=genre)
# #     session.add(g)
# #     session.commit()
#
# # b1 = Book(title="гарри Поттер", genre_id=1)
# # b2 = Book(title="властелин колец", genre_id=1)
# # session.add(b1)
# # session.add(b2)
# # session.commit()
#
#
# # b1 = Book(title="Мертвые души", genre_id=3)
# # b2 = Book(title="Детство Никиты ", genre_id=3)
# #
# # session.add(b1)
# # session.add(b2)
# # session.commit()
#
# # #жанр с айди
# # genre = session.get(Genre,3)
# # #печатаем эту запись
# # print(genre)
# # #печатаю список книг который сслынается на запись  Художественное в таблице жанров
# # print(genre.books)
#
#
# # genre = session.query(Genre).first()
# # print(genre.books)
# # for book in genre.books:
# #     print(book.id,book.title)

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, update
from sqlalchemy.orm import Session, declarative_base, relationship

engine = create_engine("sqlite+pysqlite:///items.db", echo=False, future=True)
session = Session(bind=engine)

Base = declarative_base()


class Book(Base):
    __tablename__ = "books"
    id = Column(Integer(), primary_key=True)
    title = Column(String(100), nullable=False)
    genre_id = Column(Integer(), ForeignKey("genres.id"))
    # новая поле в таблице: Цена
    price = Column(Integer(), nullable=False)

    def repr(self):
        return f"Книга {self.id} {self.title}"


class Genre(Base):
    __tablename__ = "genres"
    id = Column(Integer(), primary_key=True)
    title = Column(String(100), nullable=False)
    books = relationship("Book")

    def str(self):
        return f"{self.id}, {self.title}"


# Base.metadata.create_all(engine)
# Base.metadata.drop_all(engine)
genres = ["Фентези", "Детектив", "Художественное"]
for genre in genres:
    g = Genre(title=genre)
    session.add(g)
    session.commit()
books = [
    {"title": "Гарри Поттер",
     "genre_id": 1,
     "price": 400},
    {"title": "Властелин колец",
     "genre_id": 1,
     "price": 500},
    {"title": "Черная башня",
     "genre_id": 1,
     "price": 400},
    {"title": "Назад в будущее",
     "genre_id": 1,
     "price": 500},
    {"title": "Гости из прошлого",
     "genre_id": 1,
     "price": 400},
]

# прохожусь циклом по списку из словарей
# for book in books:
#     # создаю запись книги
#     # обращение к словарю book['ключ']
#     b = Book(title = book['title'], genre_id = book['genre_id'], price=book['price'])
#     session.add(b)
#     session.commit()

# def add_three_book():
#     for i in range(0,3):
#         b = Book(title=i,genre_id=1,price=500)
#         session.add(b)
#         session.commit()
#
#     assert session.query(Book).count() ==3

# add_three_book()

# books_count = session.query(Book).count()
# print(books_count)
#
# def add_book(name, genre_id, price):
#     book = Book(name=name, genre_id=genre_id, price=price)
#     session.add(book)
#     session.commit()
#
#
# def update_book(id, name):
#     book_update = (
#         update(Book)
#         .where(Book.id == id)
#         .values(name=name)
#     )
#
# @pytest.fixture()
# def setup_db():
#     engine = create_engine("sqlite+pysqlite:///items.db", echo=False, future=True)
#     session = Session(bind=engine)
#
#     Base = declarative_base()
#
#     class Book(Base):
#         __tablename__ = "books"
#         id = Column(Integer(), primary_key=True)
#         title = Column(String(100), nullable=False)
#         genre_id = Column(Integer(), ForeignKey("genres.id"))
#         # новая поле в таблице: Цена
#         price = Column(Integer(), nullable=False)
#
#         def repr(self):
#             return f"Книга {self.id} {self.title}"
#
#     class Genre(Base):
#         __tablename__ = "genres"
#         id = Column(Integer(), primary_key=True)
#         title = Column(String(100), nullable=False)
#         books = relationship("Book")
#
#         def str(self):
#             return f"{self.id}, {self.title}"
#
#     engine = create_engine("sqlite+pysqlite:///items.db", echo=False, future=True)
#     session = Session(bind=engine)
#
#     Base.metadata.create_all(engine)
#     yield session
# def test_add_book(setup_db):
#     add_book("название книги",1,500)
#     books_count = session.query(Book).count()
#     assert books_count == 1


import pytest
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, update
from sqlalchemy.orm import Session, declarative_base, relationship

engine = create_engine("sqlite+pysqlite:///items.db", echo=False, future=True)
session = Session(bind=engine)

Base = declarative_base()


class Book(Base):
    tablename = "books"
    id = Column(Integer(), primary_key=True)
    title = Column(String(100), nullable=False)
    genre_id = Column(Integer(), ForeignKey("genres.id"))
    # новая поле в таблице: Цена
    price = Column(Integer(), nullable=False)

    def repr(self):
        return f"Книга {self.id} {self.title} {self.price}"


class Genre(Base):
    tablename = "genres"
    id = Column(Integer(), primary_key=True)
    title = Column(String(100), nullable=False)
    books = relationship("Book")

    def str(self):
        return f"{self.id}, {self.title}"


# Base.metadata.create_all(engine)
# Base.metadata.drop_all(engine)

# получаю запись жанра с айди 1

# genre = session.get(Genre, 1)
# print(genre)
# # получаю все книги этого жанра
# print(genre.books)


def add_book(title, genre_id, price):
    book = Book(title=title, genre_id=genre_id, price=price)
    session.add(book)
    session.commit()


def update_book(id, name):
    book_update = (
        update(Book)
        .where(Book.id == id)
        .values(name=name)
    )


@pytest.fixture()
def setup_db():
    print("setup db")

    Base = declarative_base()

    class Book(Base):
        tablename = "books"
        id = Column(Integer(), primary_key=True)
        title = Column(String(100), nullable=False)
        genre_id = Column(Integer(), ForeignKey("genres.id"))
        # новая поле в таблице: Цена
        price = Column(Integer(), nullable=False)

        def repr(self):
            return f"Книга {self.id} {self.title} {self.price}"

    class Genre(Base):
        tablename = "genres"
        id = Column(Integer(), primary_key=True)
        title = Column(String(100), nullable=False)
        books = relationship("Book")

        def str(self):
            return f"{self.id}, {self.title}"

    engine = create_engine("sqlite+pysqlite:///items.db", echo=False, future=True)
    session = Session(bind=engine)

    Base.metadata.create_all(engine)
    yield session


def test_add_book(setup_db):
    add_book("Название книги", 1, 500)
    books_count = setup_db.query(Book).count()
    assert books_count == 1

# books = session.query(Book).all()
# print(books)
