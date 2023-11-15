from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import Session, declarative_base, relationship
from datetime import datetime

engine = create_engine("sqlite+pysqlite:///blogpostuser.db", echo=False, future=True)
session = Session(bind=engine)

Base = declarative_base()


class Blog(Base):
    __tablename__ = "blogs"
    id = Column(Integer(), primary_key=True)
    name = Column(String(100), nullable=False)
    date_create = Column(DateTime(), default=datetime.now)
    description = Column(String(100), nullable=False)
    post = relationship("Post")

    def __repr__(self):
        return f"id: {self.id} name: {self.name} data_create:" \
               f" {self.date_create} description: {self.description}"


class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer(), primary_key=True)
    name = Column(String(100), nullable=False)
    date_create = Column(DateTime(), default=datetime.now)
    description = Column(String(100), nullable=False)
    linkin_for_blog = Column(Integer(), ForeignKey("blogs.id"))
    linkin_for_user = Column(Integer(), ForeignKey("users.id"))

    def __repr__(self):
        return f"id: {self.id} name: {self.name} data_create: {self.date_create} description: {self.description}" \
               f"linkin_for_blog: {self.linkin_for_blog}, linkin_for_user: {self.linkin_for_user}"


class User(Base):
    __tablename__ = "users"
    id = Column(Integer(), primary_key=True)
    name = Column(String(100), nullable=False)
    post = relationship("Post")

    def __repr__(self):
        return f"id: {self.id} name: {self.name}"


# Base.metadata.create_all(engine)
# Base.metadata.drop_all(engine)
def b_and_u():
    b1 = Blog(name="sport", description="спорт - это не физкультура")
    u1 = User(name="Denis")
    u2 = User(name="Vitya")
    session.add(b1)
    session.add(u1)
    session.add(u2)
    session.commit()


def post():
    postlist = [
        {'name': "lesson1",
         "description": "тренировка груди",
         "linkin_for_blog": 1,
         "linkin_for_user": 1},
        {'name': "lesson2",
         "description": "тренировка ног",
         "linkin_for_blog": 1,
         "linkin_for_user": 2},
        {'name': "lesson3",
         "description": "тренировка спины",
         "linkin_for_blog": 1,
         "linkin_for_user": 1},
    ]
    for postl in postlist:
        p = Post(name=postl["name"], description=postl["description"],
                 linkin_for_blog=postl["linkin_for_blog"], linkin_for_user=postl["linkin_for_user"])
        session.add(p)
        session.commit()


def blog_create():
    b = input("название блога")
    b1 = input("описание блога")
    b2 = Blog(name=b, description=b1)
    session.add(b2)
    session.commit()


def post_create():
    a = input("название поста")
    b = input("описание поста")
    try:
        c = int(input("id блога"))
        d = int(input("id юзера"))
        p = Post(name=a, description=b, linkin_for_blog=c, linkin_for_user=d)
        session.add(p)
        session.commit()
    except ValueError:
        print("введено не число")


def all_post():
    a = session.query(Post).all()
    print(a)


def all_blogs():
    a = session.query(Blog).all()
    print(a)


def all_post_in_blog():
    try:
        chislo = int(input('id blog'))
        a = session.query(Post).filter_by(linkin_for_blog=chislo).all
        print(a())
    except ValueError:
        print("введено не число")
all_post_in_blog()

def menu():
    print(f'создать блог =  1 '
          f'создать пост =  2'
          f'все посты =  3'
          f'все блоги = 4'
          f'постов в блоге =  5')

    menu1 = int(input("введите число"))
    d = {1: blog_create,
         2: post_create,
         3: all_post,
         4: all_blogs,
         5: all_post_in_blog}
    print(d[menu1]())
