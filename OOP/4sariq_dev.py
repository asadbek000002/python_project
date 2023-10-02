# def parent():
#     print("Printing from the parent() function")
#
#     def first_child():
#         print("Printing from the first_child() function")
#
#     def second_child():
#         print("Printing from the second_child() function")
#
#     second_child()
#     first_child()
# print(parent())

# def parent(num):
#     def first_child():
#         return "Hi, I am Emma"
#
#     def second_child():
#         return "Call me Liam"
#
#     if num == 1:
#         return first_child
#     else:
#         return second_child
#
# first = parent(1)
# second = parent(2)

# i = 8
# while True:
#     if i % 11 == 0:
#         print(i)
#         break
#     print(i)
#     i += 1

# class MyClass:
#     def method(self):
#         return 'instance method called', self
#
#     @classmethod
#     def classmethod(cls):
#         return 'class method called', cls
#
#     @staticmethod
#     def staticmethod():
#         return 'static method called'
#
# obj = MyClass()
# print(obj.method())`
#
# print(MyClass.classmethod())
#
# print(obj.staticmethod())

# class Pizza:
#     def __init__(self, ingredients):
#         self.ingredients = ingredients
#
#     def __repr__(self):
#         return f'Pizza ritsepi ({self.ingredients!r})'
#
#
# a = Pizza(['cheese', 'tomatoes'])
# b = Pizza(['mozzarella', 'tomatoes', 'ham', 'mushrooms'])
# c = Pizza(['mozzarella'] * 4)
# print(a)
# print(b)
# print(c)

# class Pizza:
#     def __init__(self, ingredients):
#         self.ingredients = ingredients
#
#     def __repr__(self):
#         return f'Pizza({self.ingredients!r})'
#
#     @classmethod
#     def margherita(cls):
#         return cls(['mozzarella', 'tomatoes'])
#
#     @classmethod
#     def prosciutto(cls):
#         return cls(['mozzarella', 'tomatoes', 'ham'])
#
# print(Pizza.margherita())

# import math
#
# class Pizza:
#     def __init__(self,radius, ingredients):
#         self.radius = radius
#         self.ingredients = ingredients
#
#     def __repr__(self):
#         return (f"Pizza ({self.radius!r},"
#                 f"{self.ingredients!r}")
#
#     def area(self):
#         return self.circle_area(self.radius)
#
#     @staticmethod
#     def circle_area(r):
#         return r ** 2 * math.pi
#
#
# p = Pizza(4,['mozzorella', 'tometoes'])
# print(p)
# print(p.area())

# def add_one(number):
#     return number +1
#
# print(add_one(5))

# def say_hello(name):
#     return f"hello {name}"
#
# def be_awesome(name):
#     return f'YO {name} , together we are the awesomest '
#
# def greet_bob(greet_func):
#     return greet_func("Bob")
#
# print(greet_bob(say_hello))
#
# print(greet_bob(be_awesome))


# def parent():
#     print("parent()")
#
#     def first_child():
#        print("first_child()")
#
#     def second_child():
#        print('second_child()')
#
#     second_child()
#     first_child()
#
# print(parent())

# def parent(num):
#     def first_child():
#         return "hi , I am emma"
#
#     def second_child():
#         return "Call me Liam"
#
#     def three_chhild():
#         return "hello"
#
#     if num == 1:
#         return first_child
#
#     if num == 2:
#         return second_child
#
#     else:
#         return three_chhild

# firrs = parent(1)
# second = parent(2)
#
# print(firrs())
# print(second)

# print(parent(1)())
# print(parent(2)())
# print(parent(4)())

# def my_dekorator(func):
#     def wrapper():
#         print("salom hammmaga dostlar")
#         func()
#         print("xayr hammaga ")
#
#     return wrapper
# @my_dekorator
# def say_whee():
#     print("qanday")
#
# #say_whee = my_dekorator(say_whee)()
#
# print(say_whee())

# from datetime import datetime
#
# def not_during_the_nigth(func):
#     def wrapper():
#         if 7 <= datetime.now().hour < 22:
#             func()
#         else:
#              "hush, the neighbors are asleep"
#     return wrapper
# #@not_during_the_nigth
# def say_wee():
#     print("Wee!")
#
# say_wee = not_during_the_nigth(say_wee)()
#
# print(say_wee)


# def my_sum(a,b):
#     return a + b
#
#
# print(my_sum(1,2))
#

# def my_sum(my_integers):
#     result = 0
#     for x in my_integers:
#         result += x
#     return result
#
# list_of_intrgers = [1,2,3,4]
# print(my_sum(list_of_intrgers))
#
# def my_sum(*ar):
#     result = 0
#     for x in ar:
#         result += x
#     return result
#
#
#
# print(my_sum(1,2,3,5,7))
#
# mevalar = ['olma', 'anor','anjir','behi']
# print(*mevalar)
# meva = *mevalar, 'baliq'
# print(* meva)

# def avto_info(kompaniya, model, rangi, korobka, yili, narh =None):
#     avto = {'kompaniya': kompaniya,
#             'model': model,
#             'rang': rangi,
#             'koropka':korobka,
#             'yil':yili,
#             'narh':narh}
#     return avto
#
# avto1 = avto_info('GM','Malibu','qora','Avtomat',2018)
# avto2 = avto_info('GM','Gentra','oq','Avtomat',2018,15000)
# avtolar= [avto1,avto2]
# for avto in avtolar:
#     print(avto)
#     for i ,n in avto.items():
#         print(i,n)
#
# print(*avto1)

# def summa(x ,x , *sonlar):
#     yigindi = 0
#     for i in sonlar:
#         yigindi += i
#     return yigindi
#
# print(summa(1,2,3, 4,4, ))

# def myfunc():
#     x = 3
#     print(x)
#
# myfunc()

# def myfunc():
#     x = 300
#     def myinnerfunc():
#         print(x)
#     myinnerfunc()
#
# myfunc()

# x = 300
# def myfunc():
#     print(x)
#
# myfunc()
#
# print(x)

# x = 300
#
# def myfunc():
#     x = 200
#     print(x)
#
# myfunc()
#
# print(x)

# x = 500
# def myfunc():
#     global x
#     x = 300
#
#
# myfunc()
#
# print(x)

# class Person:
#     def __init__(self,fname , lname):
#         self.fname = fname
#         self.lname = lname
#
#     def printname(self):
#         print(self.fname, self.lname)

# info = Person('Asad', 'Tuygunov')
# info1 = Person('shoxrux', 'Tuychiyev')
#print(x.printname())

# class Student(Person):
#     def __init__(self,fname,lname):
#         Person.__init__(self, fname,lname)
#x1 = Student('ali', 'Valiyev')
#print(x1.printname())

#print(info.printname())

# class Student(Person):
#     def __init__(self,fname,lname,yili ):
#         super().__init__( fname, lname)
#         self.tugilganyili = yili
#
#     def get_info(self):
#         return f"welcome, {self.fname} , {self.lname}, {self.tugilganyili}"
#
#
# info3 = Student('Asad', 'Tuygunov',2002)
#
# print(info3.get_info())


# import mymodule as mx
#
# print(mx.greeting("Jaxon"))
#
# a = mx.person1["age"]
# print(a)
#
# import platform
#
# x = platform.system()
# print(x)

# import platform
#
# x = dir(platform)
# print(x)
#
# from mymodule import person1
#
# print(person1["age"])
#
#
# import datetime
#
# x = datetime.datetime.now()
#
# print(x)
#
# import datetime
#
# x = datetime.datetime.now()
#
# print(x.year)
#print(x.strftime('%A'))

# import datetime
#
# x  = datetime.datetime(2023,3,8)
# print(x.strftime("%A"))
# print(x.strftime("%B"))
# print(x.strftime("%w"))
# print(x.strftime("%d"))
# print(x.strftime("%m"))



#
# class Person():
#     def __init__(self,fnamae ,lname):
#         self.fname = fnamae
#         self.lname = lname
#
#     def get_info(self):
#         return f"{self.fname}  {self.lname}"
#
#
# person = Person("Asadbek", "Tuygunov")
#
# print(person.get_info())
#
# class student(Person):
#     def __init__(self,fname,lname):
#         Person().__init__(fname,lname)


"""""
Berilgan son raqamlarini ekranga chiqaring.
Misol uchun, print_digits(154) chaqirilganda, quyidagilar ekranga chiqarishi kerak:
4
5
1
"""""


# lis = []
# def print_digits(num: int):
#     for i in list(str(num)):
#         lis.append(i)
#     lis.sort(reverse=True)
#     for n in lis:
#         print(n)
#
# print(print_digits(154))



"""
Berilgan son raqamlariga teskari son qaytaring.
Misol uchun:
reverse_digits(154) => 451
reverse_digits(710) => 17
"""

# lis = []
# def print_digits(num: int):
#     for i in list(str(num)):
#         if i != '0':
#             lis.append(i)
#                 # return num
#     lis.sort(reverse=True)
#     for n in lis:
#         print(n, end='')
#
# print(print_digits(170))












"""
Berilgan son ikkining darajasi ekanligiga tekshiring.
Misol uchun:
is_power_of_two(16) => True
is_power_of_two(15) => False
"""

# def is_power_of_two(num: int):
#     x = 2
#     kvadrat = 4 ** 2
#     if kvadrat == num:
#         return True
#     else:
#         return False
#
# print(is_power_of_two(16))

# def onlikdan_ikkilikga(son):
#     ikkilik = ""
#     while son > 0:
#         qoldiq = son % 2
#         # print(qoldiq)
#         ikkilik = str(qoldiq) + ikkilik
#         son = son // 2
#         # print(son)
#     return ikkilik
#
# print(onlikdan_ikkilikga(13))



# class Dog:
#     def __init__(self, laqabi, ovozi, yoshi):
#         self.laqabi = laqabi
#         self.ovozi = ovozi
#         self.yoshi = yoshi
#
#     def getlaqabi(self):
#         return f"laqabi {self.laqabi}"
#
#     def getovozi(self):
#         return f"ovozi {self.ovozi}"
#
# dog = Dog(laqabi='rex', ovozi='vov-vov', yoshi=5)
# print(dog.getovozi())

# class Talaba:
#     def __init__(self, ism, gurux, yosh):
#
#         self.ism = ism
#         self.gurux = gurux
#         self.yosh = yosh
#     # def get(self):
#     #     return self.gurux , self.ism
# b = []
# a = int(input('malumot soni:'))
# for n in range(a):
#     rey = Talaba(ism=input('ism > '), gurux=int(input('guruh> ')), yosh=int(input('yosh> ')))
#     d = rey.ism, rey.gurux, rey.yosh
#     b.append(d)
# talaba = input('talaba:')
# for i in b:
#     if talaba == i[0]:
#         # print(b)
#         print(f'Talaba haqida toliq malumot: Ismi: {i[0]}, guruhi:{i[1]}, yoshi:{i[2]}')
#
#     else:
#         print('Bizda bunaqa talaba o\'qimiydi')

# c = 0
# for i in range(101):
#     if i % 2 == 0 :
#         c += i
#         print(c)

# a = int(input())
# b = int(input())
#
# if a < b:
#     for i in range(a, b + 1):
#         print(i)
# if a > b:
#     while a == b:
#         print(a)
#         a -= 1
# # elif a == b:
# #     print('a = b')

# a = int(input())
# b = int(input())
#
# if a < b:
#     for i in range(a, b+1):
#         print(i)
# else:
#     for i in range(a, b-1, -1):
#         print(i)

# a = int(input('>'))
# b = int(input('>'))
#
# for i in range(a, b, -2):
#     print(i)


# import datetime
#
# sana = datetime.date.today()
# kabisa_yili = []
#
# for yil in range(sana.year, sana.year + 11):
#     if yil % 4 == 0 and (yil % 100 != 0 or yil % 400 == 0):
#         kabisa_yili.append(yil)
#
# print(kabisa_yili)

#
# print("rassiyaning poytaxti")
# while "maskva" != input("javob kiriting>>").lower():
#     print('javob notogri')
# print('javob togri')

# {'G': {'G': 'GG', 'F': 'GF'}, 'F': {'G': 'FG', 'F': 'FF'}}

# l ="GFG"
# dict = {l[0]:  {l[0]: l[0::2],  l[1]: l[2] + l[1]}, l[1]: {l[0]: l[1::-1], l[1]: l[1] + l[1]}}
# print(dict)


# meva = input("Bozordan qaysi mevani qidiryapsiz: ")
# bozor = {
#     "olma": 5000,
#     "nok": 10_000,
#     "banan": 20_000,
#     "anor": 10_000
# }
# print(f"Narxi:"if f"{bozor.get(meva, 'Bunda meva bozorda yoq')}": else: f"{bozor.get(meva, 'Bunda meva bozorda yoq')}"))

meva = input("Bozordan qaysi mevani qidiryapsiz: ")
bozor = {
    "olma": 5000,
    "nok": 10_000,
    "banan": 20_000,
    "anor": 10_000
}
print(f"Narxi: {bozor.get(meva, 'Bunda meva bozorda yoq')}" if bozor.get(meva, 'Bunda meva bozorda yoq') != 'Bunda meva bozorda yoq' else bozor.get(meva, 'Bunda meva bozorda yoq'))