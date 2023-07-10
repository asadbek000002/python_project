# name = input("ismingini kriting>")
# ega = int(input("yoshingizni kriting>"))
# year = 2023 - ega
# print(f"assalomu alaykum {name.title()} siz {year} da tugilgansiz ")

# misol_2

# list = [1, 3, 6, 5, 8, 4, 4, 7, 5, ]
#
# a = list[1]
# b = list[3]
# c = list[5]
#
# C = a * b / 2
# P = a + b + c
# print(f"uchburchakning yuzasi {C}. Perimetri esa {P} ga teng")

# misol_3
#
# class User():
#     def __init__(self, ism, familya, t_yil):
#         self.ims = ism
#         self.familya = familya
#         self.t_yil = t_yil
#
#     def get_info(self):
#         return f"ismim {self.ims.title()} familyam {self.familya.title()} tugilgan yilim {self.t_yil}"
#
#
#
# user = User('asadbek', 'tuygunov', '2002')
# print(user.get_info())


# num = [1,2,3,4,6,7,8,9,]
#
# def check(list1,son):
#     # for n in list1:
#         if son in list1:
#             return True
#         else:
#             return False
#
# print(check(num,5))

# num = int(input("son kriting>"))
# if num < 0:
#     num += 1
#     print(num)
#
# else:
#     print(num)

# if num < 0:
#     num += 1
# else:
#     num -= 2
# print(num)

# if num < 0:
#     num += 1
# elif num == 0:
#     num = 10
# else:
#     num -= 2
# print(num)
# c = 0
# s = 0
# son = [3, -5, 6, -9, 5]
# for n in son:
#     if n < 0:
#         s += 1
#     else:
#         c += 1
# print(f"{s} ta musbat son bor {c} ta manfiy son bor")

#
# a = 2
# b = 3
# s = 2
#
# if a + b > s and a + s > b and s + b > a:
#     if a == b == s:
#         print("teng tomonli uchburchak")
#     elif a == b != s or b == s != a or a == s != b:
#         print("teng yonli uchburvhak")
#     elif a != b != s or b != a != s or a != s != b:
#         print("harhil tomonli uchburchak")
# else:
#     print('uchburchak yasab bolmaydi')

# a = 3  # tomonlarni o'zgartitib koring
# b = 5  # yoki impuntga solib tekshuring
# c = 4  # barcha shartlar ishladi

# if a + b > c and a + c > b and b + c > a:
#
#     if a == b and a == c and b == c:
#         print("teng tomonli uchburchak")
#
#     elif a == b or a == c or b == c:
#         print("teng yonli uchburchak")
#
#     elif a * a == b * b + c * c or b * b == a * a + c * c or c * c == a * a + b * b:
#         print("to'g'ri burchakli uchburchak")
#
#     else:
#         print("ixtiyoriy uchburchak")
#
# else:
#     print("Uchburchak hosil bo'lmaydi")
#
# let_person = {'languages': '["JavaScript", "Python", "Ruby"]'}
# print(let_person.items())
# let_person.get('name','asadbek')
# print(let_person.items()) ??????????????????????????????



# let = ['A', 'B', 'C', 'D', 'E', 'L']
# print(let[0], end='')
# print(let[2], end='')
# print(let[0], end='')
# print(let[5])
# juft = []
# toq = []
# index = 0
# number = [2, 3, 13, 18, -5, 38, -10, 11, 0, 104]
# for n in number:
#
#     if n % 2 == 0:
#         juft.append(n)
#
#
#     else:
#         toq.append(index)
#     index += 1
# print(juft, toq)

# number = [2, 3, 13, 18, -5, 38, -10, 11, 0, 104]
#
# for n in number:
#      print(n)?????????

# sanoq = 0
# son = [[0,1,0],[0,1,0],[1,0,1,0]]
# for n in son:
#     # print(n)
#     for i in n:
#         # print(i)
#         if i == 0:
#             sanoq += 1
# print(sanoq)

# x = 21
# list = [0,1]
# n2 = 0
# n1 = 1
# while a<2000:
#     a += 1
#     nf = list[-1] + list[-2]
#     list.append(nf)
# print(list)
# if x in list:
#     print("ushbu son fibonachii")


# key_values = ["name", "age", "languages", "Ali", "20", ["JavaScript", "Go", "python", "Java", "C++"] ]
#
# person = {}
# s = 3
# p = 4
# for n in key_values[0:3]:
#     for c in key_values[s :p]:
#         s += 1
#         p += 1
#         person[n] = c
# print(person)



# array = [1, 5, 3, 7, 2, 4, 6, 1  ]
#
# new_arry = array[:]
#
# new_arry.reverse()
# for m in new_arry:
#     del array[-1]
#     if m in array:
#         a = 'True'
#         break
#     else:
#          a = 'False'
# print(a)


# num = int(input("son kriting"))
# a = num % 100
# d = num % 10
# b = a
# c = b // 10
# s = num // 100
# # print(s)
# # print(c)
# # print(d)
# print(d,c,s )


#    Mevalar narhi ni topuvchi dastur
#
# bana = int(input("necha klagram banan>>"))
# olm = int(input("necha klagram olma>>"))
# narh = 0
# narh1 = 0
# banan = 5000
# olma = 3000
# sikl = 0
# for n in range(bana):
#     sikl += 1
#     narh += banan
# print(f"{sikl} kilogram banan {narh} som")
#
# sikl1 = 0
# for  i in range(olm):
#     sikl1 += 1
#     narh1 += olma
# print(f"{sikl1} kilogram olma {narh1} som")
#
# if banan > olma:
#     farq = narh - narh1
#     print(f"banan olmadan {farq} som qimmat")
# elif olma > banan:
#     farq1 = narh1 - narh
#     print(f"olma banandan {farq1} som qimmat")




