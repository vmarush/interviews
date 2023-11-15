# SOLID - крепкий
# S - Single responsibility (один класс имеет одну зону ответсвенности)
import sys
import time


# class FormatData:
#     def __init__(self, raw_data):
#         self.raw_data = raw_data
#
#     def prepare(self):
#         result = ''
#         for item in self.raw_data:
#             new_line = ','.join(
#                 (
#                     item['name'],
#                     item['surname'],
#                     item['occupation']
#                 )
#             )
#             result += f'{new_line}\n'
#         return result
#
#
# class FileWriter:
#     def __init__(self, filename):
#         self.filenema = filename
#
#     def write_file(self, data):
#         with open(self.filenema, 'w', encoding='UTF8') as f:
#             f.write(self.data)


# 0 - Open-closed(классы можно расширять но лучше не подифицировать а уноследоваться от родителя
# import sys
# class Logger:
#     def __init__(self):
#         self.prefix = time.strftime('%Y-%b-%d %H:%M:%S',time.localtime())
#     def log(self,message):
#         sys.stderr.write(f'{self.prefix} --> {message}\n')
#
# class CustomerLogger(Logger):
#     def __init__(self):
#         super().__init__()
#         self.prefix = time.strftime('%Y-%b-%d',time.localtime())
#
# logger = Logger()
# logger.log('Vadim1!')
# c_logger = CustomerLogger()
# c_logger.log('Vadim2')

# L- Liskov substitution (Наследование должно быть логичным, метод принимать одинаковое кол-во аргементов и иметь похожую логику
# class Animal:
#     def __init__(self,name,age):
#         self.attributes = {'name':name,'age':age}
#
#     def eat(self,_amount = 0):
#         print('Ate some food')
# class Cat(Animal):
#     def __init__(self,name,age):
#         super().__init__(name,age)
#
#     def eat(self,amount=0.1):
#         if amount>0.3:
#             print('Can not eat that much')
#         else:
#             print('Ate some cat food')
#
# class Dog(Animal):
#     def __init__(self, name, age):
#         super().__init__(name, age)
#
#     def eat(self,_amount=0):
#         print('Ate some food')
#
# pluto = Dog('Plito',3)
# goofy = Dog('Goofy',2)
# buttons = Cat('mr.Buttons',4)
# animals =(pluto,goofy,buttons)
# for animal in animals:
#     if animal.attributes['age']>2:
#         print(animal.attributes['name'])

# I - Interface segregation(клиен не должне зависить от методов и не должен подключить те методы которые не использует
# class Creature:
#     def __init__(self, name):
#         self.name = name
#
#
# class SwimmerInrerface:
#     def swim(self):
#         pass
#
#
# class WalkerInrerface:
#     def walk(self):
#         pass
#
#
# class TalkerInrerface:
#     def talk(self):
#         pass
#
#
# class Human(Creature, SwimmerInrerface, WalkerInrerface, TalkerInrerface):
#     def __init__(self, name):
#         super().__init__(name)
#
#     def swim(self):
#         print(f'I {self.name} can swim')
#
#     def walk(self):
#         print(f'I {self.name} can walk')
#
#     def talk(self):
#         print(f'I {self.name} can talk')
#
# class Fish(Creature,SwimmerInrerface):
#     def __init__(self, name):
#         super().__init__(name)
#     def swim(self):
#         print(f'I {self.name} can swim')
#
# class Cat(Creature,SwimmerInrerface,WalkerInrerface):
#     def __init__(self, name):
#         super().__init__(name)
#     def swim(self):
#         print(f'I {self.name} can swim')
#
#     def walk(self):
#         print(f'I {self.name} can walk')
#
# human = Human('Vadim')
# fish = Fish('Nemo')
# cat=Cat('Barsik')

#D - dependency inversion(высокоуровневые модули не должны зависить от низкоуровневых а должны зависить об обстракций)

# def log(self,message,notifier): # где нотифаер мы передаем Class
#     notifier.write(f'{(self.prefix},{massage}')