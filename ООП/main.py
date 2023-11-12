# oop============================================================================================
# class Point:
#     color = 'red'
#     circle = 2
#
#     def set_coord(self, x, y):
#         self.x = x
#         self.y = y
#         print('vizov set')
#
#
# pt = Point()
# pt.set_coord(x=10,y=3)
# print(pt.__dict__)
# print(pt.x)

# class Vector:
#     Mincord = 0
#     Maxcord = 100
#     @classmethod
#     def validation(cls,arg):
#         return cls.Mincord <= arg<=cls.Maxcord
#
#     def __init__(self,x,y):
#         self.x=self.y=0
#         if self.validation(x) and self.validation(y):
#             self.x = x
#             self.y = y
#     def get_coord(self):
#         return self.x,self.y
#
#     @staticmethod
#     def norm(x,y):
#         return x*x+y*y

# v1 = Vector(x=3,y=5)
# print(v1.x)
# print(v1.norm(x=1,y=2))

# oop============================================================================================
#
# class Point:
#     Max = 100
#     Min = 0
#
#     @classmethod
#     def vadim(cls, left):
#         cls.Min = left
#
#     def set_bound(self, left):
#         self.Min = left
#
#     def __getattribute__(self, item):  # блок значения в экземпляре
#         if item == 'x':
#             raise ValueError('доступ запрещен')
#         else:
#             return object.__getattribute__(self, item)
#
#     def __setattr__(self, key, value):
#         if key == 'z':
#             raise AttributeError('запрещенo')
#         else:
#             return object.__setattr__(self, key, value)
#
#     def __getattr__(self, item):
#         return False
#
#     def __delattr__(self, item):
#         object.__delattr__(self,item)


# Point.vadim(left=6)
# print(Point.Min)
# v1 = Point()
# v1.set_bound(left=5)
# v1.marush = 'ok'
# print(v1.Min)
# v1.x = 'lll'  # доступ запрещен __getatr
# # print(v1.x)# доступ запрещен на получение значения __getatr
# # v1.z = 'ok'# доступ запрещен на создании значения  __setattr
# print(v1.kkk)  # возвращает False т.k. нету kkk __getattr__
# del v1.marush # удалит атрибут из экзепляра класса
# print(v1.marush)

# oop=================Моносостояние=========================================================================
# моносостояние - экземпляры класса и их значения меняются месте
# class TreadData:
#     __shared_attrs = {
#         'name': 'vadim',
#         'data': {},
#         'id': 1
#     }
#     def __init__(self):
#         self.__dict__ = self.__shared_attrs
#
# v1 = TreadData()
# v2= TreadData()
# v1.id = 3
# print(v1.id)
# print(v2.id)

# oop=================Декоратор Проперти========================================================================
# class Person:
#     def __init__(self, name, old):
#         self.__name = name
#         self.__old = old
#     @property
#     def old(self):
#         return self.__old
#     @old.setter
#     def old(self,old):
#         self.__old = old
#     @old.deleter
#     def old(self):
#         del self.__old
#
# oop============================================================================================
# class Chars:
#     def __init__(self, chars):
#         self.__chars = chars
#
#     def __call__(self, *args, **kwargs):
#         if not isinstance(args[0],str):
#             raise TypeError('неверный тип данных')
#         return args[0].strip(self.__chars)
# q = Chars(';lv')
# test = q('vadim')
# print(test)
# oop==================Булевые значения=========================================================================
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __len__(self): # если len != 0 вернет True, esle - False => вызывает bool
#         return self.x * self.x + self.y * self.y
#
#     def __bool__(self): # __len__ не вызывается т/к есть __bool__
#         print('__bool__')
#         return  self.x == self.y
#
# p = Point(3, 4)
# if p:
#     print('объект р True'
#     )
# else:
#     print('объект р Fasle')
# oop==================ITEM индексы ==========================================================================
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = list(marks)
#
#     def __getitem__(self, item):  # для того чтобы обращаться в экземпляре s1[2] а не s1.marks[2]
#         if 0 <= item < len(self.marks):
#             return self.marks[item]
#         else:
#             raise IndexError('Неверный индекс')
#
#     def __setitem__(self, key, value):  # для замены чисел => s1[2]=4 key = [2] , value =4
#         if not isinstance(key, int) or key < 0:  # проверка на индекс
#             raise TypeError('индекс должен быть целым числом')
#         if key >= len(self.marks):   # если индекса такого нет то мы находим сколько нужно None
#             off = key + 1 - len(self.marks) # вставляем None в спикок и заменяем последний None
#             self.marks.extend([None] * off)
#
#         self.marks[key] = value
#
#     def __delitem__(self, key): # удаляем элемент по индексу
#         if not isinstance(key, int) or key < 0:  # проверка на индекс
#             raise TypeError('индекс должен быть целым числом')
#
#         del self.marks[key]
#
#
# s1 = Student('Cергей', [5, 5, 3, 2, 5])
# s1[2] = 4
# del s1[4]
# print(s1[2])
# oop==============ИТЕРАТОР==============================================================================
# class FRange:
#     def __init__(self, start = 0.0,stop=0.0,step=1.0):
#         self.start = start
#         self.stop = stop
#         self.step = step
#         self.value = self.start - self.step
#
#     def __iter__(self):
#         self.value = self.start - self.step
#         return self
#
#     def __next__(self):
#         if self.value + self.step < self.stop:
#             self.value += self.step
#             return self.value
#         else:
#             raise StopIteration
#
# fr = FRange(0,2,0.5)
# print(next(fr))
# print(next(fr))
# print(next(fr))
# print(fr.__next__())
# oop============================================================================================
# class Geom:
#     name = 'Geom'
#     def __init__(self,x1,y1,x2,y2):
#         print(f'инициадизатор Geom для {self.__class__}')
#         self.x1=x1
#         self.y1=y1
#         self.x2 = x2
#         self.y2 = y2
# class Line(Geom):
#     def dwaw(self):
#         print('Рисуем линии')
# #
# # l1 = Line(x1=1,y1=1,x2=2,y2=2)
# # print(l1.dwaw())
#
# class Rect(Geom):
#     def __init__(self,x1,y1,x2,y2,fill=None):
#         super().__init__(x1,y1,x2,y2)  #делегирование
#         print('инициализатор Rect')
#         self.fill =fill
# r1 = Rect(x1=1,y1=1,x2=2,y2=2)

# oop=================Полиморфизм- работа с разными объектами единым образом =(треугол,квадрат,угол)========
# class Geom:
#     def get_pr(self):  # если в дочернем классе нет вызваного метода
#         raise NotImplementedError('не переопределен get_pr')
#         # абстрактный метод
#
#
# class Rectangle(Geom):
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
#
#     def get_pr(self):
#         return 2 * (self.w + self.h)
#
#
# class Square(Geom):
#     def __init__(self, a):
#         self.a = a
#
#     def get_pr(self):
#         return 4 * self.a
#
#
# class Triangle(Geom):
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def get_pr(self):
#         return self.a + self.b + self.c
#
# geom = [Rectangle(1,2),Square(10),Triangle(1,2,3)]
# for g in geom:
#     print(g.get_pr())

# oop===========__slots__=======когда слотс не прописывается в __dict__(x y)===========================
# class Point:
#     def __init__(self,x,y):
#         self.x = x
#         self.y=y
#
# class Point2D:
#     __slots__ = ('x',
#                  'y')
#     def __init__(self,x,y):
#         self.x = x
#         self.y=y
# pt = Point(1,2)
# pt2 = Point2D(5,8)
# # pt2.z=18 ошибка ограничения СЛОТА
# oop============__slots__==============================================================================
# class Point2D:
#     __slots__ = ('x', 'y')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point3D(Point2D):
#     __slots__ = ('z')
#
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
# oop==============Метоклассы===========================================================================
# class Point:
#     MAX_CORD = 100
#     MIN_CORD=0
# # A = type('Point',(),{'MAX_CORD':100,'MIN_CORD':0})
# # А создает метокласс Point
# class B1:
#     pass
# class B2:
#     pass
# # A = type('Point',(B1,B2),{'MAX_CORD':100,'MIN_CORD':0})
#     # А создает метокласс Point,B1,B2
# oop======метокласс===================================================================================
# class Meta(type):
#     def __init__(cls, name, base, attrs):
#         super().__init__(name, base, attrs)
#         cls.MAX_CORD = 100
#         cls.MIN_CORD = 0
# class Point(metaclass=Meta):
#     def get_coords(self):
#         return (0,0)
# #в attrs => get_coods, base=>кортеж из базовых классов, name=>Point, cls=> ссылка на Point
# pt = Point()
# print(pt.MAX_CORD)
# print(pt.get_coords())
# oop==DATA Classes================================================================================
# from dataclasses import dataclass,field
# from  pprint import pprint
#
# @dataclass
# class ThingData:
#     name: str
#     weight: int
#     price: float = 0 # по умолчанию ноль
#     dims: list = field(default_factory=list) # для всех список пустой
# td = ThingData(name='Python',weight=100,price=11100)
# print(td) # автоматически добавлсяется __repr__{self.__dict__}
#         # автоматически __init__ и self.name,weight,price
# oop===========
# from dataclasses import dataclass, field, InitVar
#
#
# @dataclass() #(repr = True,order=True)
# class V3D:
#     x: int = field(repr=False)
#     y: int
#     z: int = field(compare=False)
#     calc_len : InitVar[bool] = True
#     lenght: float = field(init=False, compare=False,default=0)
#
#     def __post_init__(self,calc_len:bool):
#         if calc_len:
#             self.lenght = (self.x * self.x + self.y * self.y + self.z * self.z) ** 0.5
#
#
# v = V3D(1, 2, 3,True)
# v2 = V3D(1, 2, 5)
# print(v == v2)  # z не сравнимается
# print(v)  # x удален из репа

# oop=======Наследование DataClasses=========================================================
# from dataclasses import dataclass, field, InitVar
# from typing import Any
# class GoodsMethodsFactory:
#     @staticmethod
#     def get_init_mea():
#         return [0,0,0]
#
# @dataclass
# class Goods:
#     current_uid = 0
#     uid :int = field(init=False)
#     price: Any = None
#     weight: Any = None
#     def __post_init__(self):
#         print('Goods:pont_init')
#         Goods.current_uid += 1
#         self.uid = Goods.current_uid
#
#
# @dataclass
# class Book(Goods):
#     title:str = ''
#     author:str = ''
#     price: float=0
#     weight: int | float = 0
#     measure: list = field(default_factory=GoodsMethodsFactory.get_init_mea)
#
#     def __post_init__(self):
#         super().__post_init__()
#         print('Book:post_init')
#
# b = Book(1000,100,'Vadim','Marushkevich')
# print(b)