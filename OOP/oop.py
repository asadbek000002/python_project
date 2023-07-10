# Class bu qolib instance(objekt) lar uchun
#instanse classdan oling  objekt

#attr bu class ning xarakterlari oy (noun)

#mehton bu bajaradigan ishlar fe'l (vabr)

# class Dog:
#     def __init__(self, breed,color,age,nicname):
#         self.breed= breed
#         self.color= color
#         self.age= age
#         self.nick= nicname
#
# ozzy = Dog(breed='Golden Retiveve', color='golden', age='1',nicname='ozzy')
# ozzy1 =Dog('bulldog','white','0.5','kacy')
# print(ozzy.nick,ozzy.age)

# class Bola:
#     def __init__(self,ism,familiya,yosh,oqishi):
#         self.ism = ism
#         self.fam = familiya
#         self.yosh = yosh
#         self.oqsh = oqishi
#
#
#     def __str__(self):
#         return f"ism familyasi {self.ism.title()} {self.fam.title()} yoshi {self.yosh}da {self.oqsh} kursoda o'qiydi"
#
# ali = Bola(ism='ali',familiya='valiyev',yosh='18',oqishi='it')
# vali = Bola('hasan','husanov','15','english')
# print(ali)
#print(vali)


class Cars:
    def __init__(self,color,milles): 
        self.color = color
        self.milles = milles

    def drive(self, mile):
        self.milles += mile
    def __str__(self):
        return f" {self.color} car {self.milles} drive"

car = Cars(color = 'blue', milles = 20000)
car2 = Cars('black', 30000)

for c in (car , car2):
    print(f" {car} car {car2} drive")

# print(car)
# print(car2)


def plus_one(number):
    return number + 1


def func(func):
    num = 5
    return func(num)


print(func(plus_one))


def uppercase_decarator(func):
    print(f"{func()}".upper())


# @uppercase_decarator
 def say_hi():
    return 'hello there'


say = uppercase_decarator(say_hi)

print(say_hi)
