# def get_name_old(ism, t_yil):
#     return f"salom {ism.title()} siz {2023- t_yil} yoshda siz "
#
#
# person = input(" ismingi>> ")
# person1 = int(input(" tugilgan yilingiz "))
# name_old = get_name_old(person, person1)
#
# print(name_old)


# def get_kvatrat(x):
#     return f"{x} ning kvadrat  {x ** 2}\n kubi esa {x ** 3}"
#
# print(get_kvatrat(4))

# def get_odd_dyad(x):
#     sikl = True
#     while sikl:
#         if x % 2 == 0:
#            return f"{x} juft son"
#         else:
#            return f"{x} toq son "
# num = int(input('count down>>'))
#
# print(get_odd_dyad(num))

# def big_num(x , y ):
#     if x > y:
#         return f"{x} katta"
#     if x == y:
#         return f"sonlar teng"
#     else:
#         return f'{y} katta'
# add_num = int(input("1-son kriting>>"))
# add_num1 = int(input("2-son kriting>>"))
#
# print(big_num(add_num,add_num1))

# def x_ning_y_darajasi(x, y = 2):
#     return f"{x} ning {y} darajasi {x ** y}"
#
# print(x_ning_y_darajasi(4))

# def qoldiq(x):
#     for n in range(2,11):
#         if x % n == 0:
#             print(f"{x} {n} ga qoldiqsiz bolinadi")
#
# qoldiq(70)

# def range(min, max):
#     list = []
#     while min < max:
#         list.append(min)
#         min += 1
#     return list
# num = range(2,20)
# print(num)

# def Katta_harf (ismlar):
#     ism = []
#     for n in ismlar:
#         ss = n.title()
#         ism.append(ss)
#     return ism
#
# ismlar = ['ali', 'vali', 'joxon']
# print(Katta_harf(ismlar))

# def Katta_harf (ismlar):
#     ismi = ismlar[:]
#     ism = []
#     for n in ismlar:
#         ss = n.title()
#         ism.append(ss)
#     return f"{ismi}\n{ism}"
#
# ismlar = ['ali', 'vali', 'joxon']
# print(Katta_harf(ismlar))


# def bahola(ismlar):
#     baholar = {}
#     ism = ismlar[:]
#     for n in ism:
#             baho = input(f"Talaba {n.title()}ning bahosini kiriting: ")
#             baholar[n]=baho
#     return f"{baholar}\n{ismlar}"
#
# talabalar = ['ali', 'vali', 'hasan', 'husan']
# Baholar = bahola(talabalar)
# print(Baholar)

# def kopaytma(*sonlar):
#     start = 1
#     for n in sonlar:
#         start *= n
#     return start
#
# print(kopaytma(3,3,3,2))

# def talablar(ism, familya, **malumotlar):
#     malumotlar['ismi'] = ism
#     malumotlar['familyasi'] = familya
#     return malumotlar
#
# talaba = talablar('Asadbek', 'Tuygunov', yoshi = '21', oqish = 'oqiydi')
# print(talaba)


# import math
# uzunlik = lambda pi ,r : \
#     2 * pi * r
# print(uzunlik(math.pi,10,))
#
# product = lambda x, y : x ** y
# print(product(3,2))

# def daraja(s):
#     return lambda n : n ** s
# son_qabul = int(input("qaysi sonning darajalari kerak>"))
# num = range(2,10)
# for n in num:
#     kvadrat = daraja(n)
#     print(f'{son_qabul} ning {n}- darajasi {kvadrat(son_qabul)}')

# Oson-1. longWord(word1, word2) - bu funksiya berilgan ikkita string eng uzunini print qilib bersin.

# def get_uzunlik(word1, word2):
#     uzun1 = len(word1)
#     uzun2 = len(word2)
#     if uzun1 > uzun2:
#         return word1
#     if uzun1 == uzun1:
#         return f"ikkalasi ham teng"
#     else:
#         return word2
#
# print(get_uzunlik('assalomu alaykum', 'dunyo'))

# Oson-2. wordCount(matn) - bu funksiya berilgan matndan nechta so'z borligini aniqlab sonni return qiladi.
# Masalan: "Python Django Hello Apple Network" da 5 ta so'z bor.

# def wordCount(matn):
#     sikl = 0
#     for n in matn:
#         if n == ' ':
#             sikl += 1
#     return f"{matn} da {sikl + 1} so'z bor"
#
# print(wordCount("Python Django Hello Apple Network"))

#Oson-3. findElements(myList) - bu funksiya berilgan myList dan yoq bolgan sonlarni listini return qilsin.
# Masalan: [6, 5, 9, 3, 1] -> [2, 4, 7, 8]

# def findelements(mylist):
#     num = list(range(1,10))
#     list1 = []
#     for n in num:
#             if n not in mylist:
#                 list1.append(n)
#     return  list1
#
# print(findelements([1, 2 , 5, 7]))

#Oson-4. removeElement(myList, elem)-berilgan myList dan elem ni o'chirib tashlang.

# def removeelement(mylist, elem):
#     for n in elem:
#         mylist.remove(n)
#     return mylist
# lis = removeelement(list(range(1,10)),[1,6])
# print(lis)

# Oson-5. findWeekDay(orderNumber) - bu funksiya berilgan orderNumber, yani hafta kuni
# tartibini beradi. Shu tartib boyicha hafta kunini string korinishda return qiling.
# Masalan: orderNumber = 4 Natija: Payshanba


# def findweekday(ordernumber):
#
#     weekday = ['dushanba', 'seshanba', 'chorshanba', 'payshanba', 'Juma', 'shanba', 'yakshanba']
#
#
#     week = weekday[ordernumber - 1]
#     return week
#
#
# print(findweekday(int(input('haftani nechanchi kuni kerak >>'))))



# Oson-6. funcNumber(myList) - myList da musbat va manfiy sonlar berilgan.
# qaysi turdagi sonlar soni ko'pligini print qiling.

# def funcnumber(mylist):
#     sikl = 0
#     sikl1 = 0
#     for n in mylist:
#         if n > 0:
#             sikl += 1
#         if n < 0:
#             sikl1 += 1
#         if sikl > sikl1:
#              natija = f'manfiy sonlar kop {sikl} > {sikl1} '
#         if sikl < sikl1:
#             natija = f'musbat sonlar kop {sikl} < {sikl1} '
#         if sikl == sikl1:
#             natija = f'musbat va manfiy sonlar soni teng {sikl} = {sikl1}'
#     return natija



# O'rta-1
# stringList(myList) - myList stringlar listini
# Masalan: ["Python", "Hello", "World", "Good"]
# Toq o'rindagi elementlarni toq va juft indexdagi harflarni o'rnini alishtiring.
# Masalan: "Python" -> "yPhtno"
# Juft o'rindagi elemetnlarni esa birinchi harifini oxirgisi bilan ikkinchisini oxirgisidan bitta oldingisi bilan alishtiring.
# Masalan: "Good" -> "dooG"



# def stringList(myList):
#     new_list = []
#     for i in range(len(myList)):
#         if i % 2 == 0:
#             new_list.append(myList[i][::-1])
#         else:
#             new_word = myList[i][0] + myList[i][-2::-1] + myList[i][-1]
#             new_list.append(new_word)
#     return new_list
#
#
# myList = "Python", "Hello", "World", "Good"
# print(stringList(myList)) # Output: 'yPhtno', 'oellH', 'drlWo', 'dooG'



# def stringList(myList):
#     new_list = []
#     for i in range(len(myList)):
#         if i % 2 == 0:
#             new_list.append(myList[i][::-1])
#         else:
#             new_word = myList[i][0] + myList[i][-2::-1] + myList[i][-1]
#             new_list.append(new_word)
#     return new_list


# Bu funksiya myList ro'yxatidagi har bir so'zni tekshiradi va toq o'rindagi so'zlarni toq va juft o'rindagi harflarni almashtiradi. Juft o'rindagi so'zlarni esa birinchi harifini oxirgisi bilan ikkinchisini oxirgisidan bitta oldingisi bilan almashtiradi.

# Misol uchun:

# myList = ["Python", "Hello", "World", "Good"]
# print(stringList(myList))


# Natija:

# ['yPhtno', 'olleH', 'dloW', 'dooG']


# Qiyin-1. [1, 2, 3, 4] -> [(1, 2, 3), (2, 3, 4), (1, 2, 4), (1, 3, 4))]
# findTriples(myList) - berilgan listdan bir biri bilan duch kelgan uchtalikni yangi listga append qilsin va listni return qilsin.
# (1, 2, 4) -> (2, 1, 4) mumkin emas.
# import random
# def findTriples(myList):
#     newlist = []
#     for n in range(4):
#         s = myList
#         m = random.sample(s,3 )
#         newlist.append(tuple(m))
#     return newlist
#
# print(findTriples([1, 2, 3, 4]))




# Qiyin-2. moveZero(myList) - bu funksiya berilgan listdan nollarni oxiriga surib
# qolgan sonlarni o'sish tartibida tartiblaydi va yangilangan listni return qiladi.
# Masal: [5, 0, 1, 4, 0, 7, 2, 0] -> [1, 2, 4, 5, 7, 0, 0, 0]


# def movezero(mylist):
#     newlist = []
#     newlist1 = []
#     for n in sorted(mylist):
#         if n == 0:
#             newlist1.append(n)
#         else:
#             newlist.append(n)
#     for n1 in newlist1:
#          newlist.append(n1)
#     print(newlist)
#
# print(movezero([5, 0, 1, 4, 0, 7, 2, 0]))



# Qiyin-3. pairCount(word) - word ni ichida hamma uchrashgan jufliklarni sonini
# aniqlang va return qiling.
# Masalan: "ababwertre" -> {"ab": 3, "bw": 1, "we": 1, "er": 2, "rt": 3}



# Tabriklayman, sizga yordam berishga tayyorman. Quyidagi funksiyani ishlatishingiz mumkin:

# def pairCount(word):
#     pairs = {}
#     for i in range(len(word)-1):
#         pair = word[i:i+2]
#         pair1 = word[i+2: i ]
#         if pair in pairs or  pair1 in pairs:
#             pairs[pair] += 1
#         else:
#             pairs[pair] = 1
#     return pairs
#
# print(pairCount("ababwertre"))


# Qiyin-4. Ikki o'lchovli list berilgan.
# Masalan: [
#   [4, 9, 3],
#   [5, 2, 6],
#   [8, 1, 7]
# ]
# Funksiya elon qiling diagonal(myList, is_reversed)
# myList - ikki o'lchovli list
# is_reversed - boolean
# Agar is_reversed = False bolsa
# Ikki o'lchovli listni to'gri diagonalini,
# is_reversed = True bo'lsa teskari diagonalini
# print qiling.
# Natija: To'gri diagonal = [4, 2, 7], Teskari diagonal = [3, 2, 8]


# def diagonal(myList, is_reversed):
#     diaganal = []
#     if is_reversed > 0:
#         diaganal.append(myList[0][2])
#         diaganal.append(myList[1][1])
#         diaganal.append(myList[2][0])
#     else:
#         diaganal.append(myList[0][0])
#         diaganal.append(myList[1][1])
#         diaganal.append(myList[2][2])
#     return diaganal
#
# lis = [
#   [4, 9, 3],
#   [5, 2, 6],
#   [8, 1, 7]
# ]
# print(diagonal(lis,-2))

# HM_Asadbek

# Keyingi darsga shuni string qb qabul qladigan va  % bo'yicha sort qladigan function yozib kelilar!



# natijalar = ["Farrux = 45.5%", "Rustam = 63.5%", "Ulug'bek = 62.9%", "Shohrux = 56.3%", "Botir = 56.5%", "Murod = 51.5%",
# "Asilbek = 83%",
# "Asadbek = 83%",
# "Behruz = 80%",
# "Farxod = 65%",
# "Abbos = 68%",
# "Abdullox = 61%"
# ]


#
# sonlar = {}
# nnn = []
# for natija in natijalar:
#         for index in range(len(natija)-1):
#             for i in range(1,100):
#                 juftlik = natija[index: index + 2]
#                 if juftlik == str(i) :
#                     sonlar = natija, int(juftlik)
#                     nnn.append(sonlar)
#                     print(sonlar)


#
# natijalar.sort(key=lambda x: float(x.split('=')[1].strip('%')))
#
#
# for natija in natijalar:
#     print(natija)



# def uzunlik(request):
#     context = {'uzunlik': 'assalomualaykumhelloworld'}
#     for uzun in range(len(context)):
#         if uzun >= 15 :
#             natija = context
#         else:
#             natija=lambda x: x.split('')[1].strip('a')
#             return (natija)


#
# if __name__ == '__main__':
#     n = int(input().strip())
#     if n % 2 != 0 or 6 < n <= 20:
#         print('Weird')
#     elif 2 < n < 5 or 20 < n:
#         print('Not Weird')

# a = int(input())
# b = int(input())
# print(f"{a//b}\n{a/b}")

# n = int(input())
# l = list(range(n))
# for n in l:
#     print(n ** 2)

#
# l = range(1,1)
# for n in l:
#     print(n, end='')
#
# from itertools import *
# A = list(map(int,input().split()))
# B = list(map(int,input().split()))
# print(*(product(A,B)))
#
# print("hello", sum(range(2, 4)), sep='\n')
#
#
#


# num1 = 5
# num2 = 6

# qiymat = num1 + num2

# print(qiymat)

# matin = str(input("matin> "))
# butun_son = int(input("int> "))
# qoldiqli = float(input("float> "))

# matn = '5'
# son = 5

# print(type(son))




# qiymat = matn + son
# print(qiymat)

# matin = str(input("matin> "))
# butun_son = int(input("int> "))




# ism = "Ali"
# familiya = "valiyev"


# print(' salom \n dunyo ')


# num1 = 5
# num2 = '6'

# natija = str(num1) + num2
# natija = num1 + int(num2)
# print(natija)
# print(type(num1))
# print(type(num2))







# name=input("name")
# print('name',name)

# ism=input('ismingiz???')
# familya=input('familyangiz???')
# print('ismingiz???',ism,'familyangiz???',familya)

# hazil=input('hazil')
# ism=input('ismi')
# print('hazil',hazil,'ismi',ism)

# a=int(input('a'))
# b=int(input('b'))
# print(a+b)

# a=int,input('5')
# b=int,input('5')
# d=int,input('5')
# print("a",int,5 +"b",int,5 *"d"int,5)

# Ism=input('ismingiz')
# yosh=int,input('yoshingiz')
# print('ismingiz',ism,'yoshingiz',yosh+1)

# narxi=input('narxi')
# b=input('soni')
# a=int(narxi%b)
# print("narxi",narxi%"soni",b)




# name= input ( " ismingiz nima ? " )
# yosh= int(input('yosh'))
# last=input ('familiya')
# a=int(10)
# print("Ismingiz->>", name,  "yoshingiz", yosh+a ,"da", "familiyangiz",last)

# ism =input("ismingizni kriting: ")
# yosh = int(input("yoshingizni kriting: "))
# print(f"sizning ismingiz {ism}, yoshingiz {yosh} da")


# name = input("ismizi kirtin ")
# familya = input("familyangizni kiritn")
# viloyatingiz = input("Shahringizni kiritin")
# age =int( input("Yoshingiz nechida "))
# password = str(("sining kodingiz"))
# print(f"sizning ismingiz {name} yoshingiz {age} da {viloyatingiz} {familya} {password} ")


# ism =input("ismingizni kriting: ")
# yosh = int(input("yoshingizni kriting: "))
# addres=input("manzilingizni kiriting")
# password= int(input("parolingizni kiriting;parol 8 ta raqamdan bolishi lozim: "))
# print(f"sizning ismingiz {ism}, yoshingiz  {yosh} da  manzilingiz {addres} parolingiz ********* " )


# sonlar_ismlar = [1, 2, 3, 'ali', 'vali' ]
# print(sonlar_ismlar[1: 4])

# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"] # mevalar ro'yxati (matnlar)
# narhlar = [12000, 18000, 10900, 22000] # narhlar ro'yxati (sonlar)
# sonlar = ['bir', 'ikki', 3, 4, 5] # sonlar va matnlar aralash ro'yxat
# ismlar = [] # bo'sh ro'yxat

# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"] # mevalar ro'yxati (matnlar)
#
#
# sonlar = [1, 2, 3, 4, 5]

# def bahola(ismlar):
#     baholar = {}
#     ism = ismlar[:]
#     for n in ism:
#             baho = input(f"Talaba {n.title()}ning bahosini kiriting: ")
#             baholar[n]=baho
#     return f"{baholar}\n{ismlar}"
#
# talabalar = ['ali', 'vali', 'hasan', 'husan']
# Baholar = bahola(talabalar)
# print(Baholar)

# ism = input("ismingizni kiriting")
# print(f"sizning ismingiz {ism} , da")



# quyidagi ichma ich massivdagi nollar sonini hisoblovchi dastur tuzing! [[0,1,0],[0,1,0],[1,0,1]]


# noll = [[0,1,0],[0,1,0],[1,0,1]]
# null2 = 20
# for i in list(range(null2)):
#     print(type(i))


# numbers = [0, 1, 2, 3, 4, 5, 6]
#
# for number in numbers:
#     print(f"sonlarni birga oshirib chiqilgan qiymat >>{number + 1}")
#

# mevalar=['olma', 'nok', 'banan', 'anor']
# for meva in mevalar:
#     print('holmeva', meva)
#     print('sabzavot emas', meva)
#
# sonlar=list(range(11))
# sonlar_kvadrati=[]
# for son in sonlar:
#     sonlar_kvadrati.append(son**2)
#
# print(sonlar)
# print(sonlar_kvadrati)

# mevani = []
# print("5 ta eng yoqtirgan meva?")
# for n in range(5):
#     mevani.append(input(f"{n+1}-mevani nomini kiriting: "))
# print(mevani)

# mashinalar=[]
# print('3 ta yoqtirgan mashinangiz???')
# for n in range(3):
#     mashinalar.append(input(f"{n+1}-mashina nomini kiriting:"))
# print(mashinalar)


# mevalar = []
# print ("3 ta yoqtirgan mevangiz qaysi?")
# for n in range (3):
#     mevalar.append(input(f"{n+1}-yoqtirgan mevalaringizni kiriting:"))
# print(mevalar)


# a =10
# b = 2
# s = 3
# d = 2
# c = 5
# n = 6
# max = a
#
# if max < b:
#   max = b
# if max < s:
#   max = s
# if max < s:
#   max = s
# if max < s:
#   max = s
#
#
# num = [55,2,3,4,-5,6,45,8,9,]
# for i in num:
#


# numbers = [-5, 2, 8, -3, 10, 6.2]
# max_number = numbers[0]
# min_number = numbers[0]
# count = 0
# for i in range(1, len(numbers)):
#     if numbers[i] > max_number:
#         max_number = numbers[i]
#     if numbers[i] < min_number:
#         min_number = numbers[i]
# for n in numbers:
#     count += n
# print(max_number,  min_number)
#




# import random

# from random import randint
#
# my_list = []
#
# list_len = 10


# for i in range(1, 10):
#     num = randint(1, 100)
#     for n in range(2, num):
#         if num % n != 0:
#             my_list.append(num)
# print(my_list)









#
#
# tup = []
# lis = [1,2,5,8,9,3,4,6,7]
# for n in lis:
#     print()
# for i in range(2,n):
#     print()
#     if n % i !=0:
#         # print(n)
#         lis.remove(n)
#         lis.append(n)
#
# print(tup)


# def tub_sonlarni_aniqlash(n):
#     tub_sonlar = []
#     for i in range(2, n+1):
#         is_tub = True
#         for j in range(2, int(i**0.5) + 1):
#             print(j)
#             if i % j == 0:
#                 print(i)
#                 is_tub = False
#                 break
#         if is_tub:
#             tub_sonlar.append(i)
#     return tub_sonlar

# n = int(input("Son kiriting: "))
# print(tub_sonlarni_aniqlash(n))







# name="HELLO MY NAME IS sARDOR "
# x = name.swapcase()
# print(x)

# informatsion = "it is cat"
# i= informatsion.capitalize()
# print(i)

#                                 2HM

# word=['Cola ', 'Fanta ', 'Pepsi']
# for wording in word:
#     print(wording)

# list=['olma', 'anor', 'banan']
# ol='olma'
# list.remove(ol)
# print(list)

# list = ['Malibu', 'Captiva', 'Merc']
# del list[0]
# print(list)


# list = ["samarqand","toshkent","jizzah"]
# a = input("o'chiradigan viloyat nomini kiriting : ").lower()
# print(f'siz {a.title()}ni o\'chirdingiz ')
# list.remove(a)
# print(list)


# ismlar=['Masrur', 'Sanjar', 'Iroda']
# del ismlar[2]
# i=input(f"do'stlaringiz ismi{ismlar}".lower())
# for i in ismlar:
#     print(i)


# son = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# for n in son:
#     if n %2 != 0:
#         print(n)

# son = ["muhammad", 1, 1.5]

# for n in son:
#     if type(n) == str:
#         print(f"{n} bu ism ")
#     if type(n) == int:
#         print(f"{n}  bu son ")
#     if type(n) == float:
#         print(f"{n} bu float ")
        

#         #uyga vazifa inputda  parolini kiritb parol tugri bulsa tugri deb chiqson+
  


# yulduz='*'
# k = ' '
# for i in range(5):
#     k += yulduz
#     print(k)

# shakl = ("*","* *","* * *","* * * *","* * * * *")
# for i in shakl:
#     print(i)


# a = ['*','**','***','****','*****']
# for i in a:
#     print(i)


# ism=input("ismingizni kiriting")
# for ismlar in ism:
#       for ismalrr in ismlar:
#         print (ismalrr)


# ism = ['islom', 'ali', 'shox']
# for n in ism:
#     print(n, end=' ')

# ism = 'Muhammad'
# yigindi = 0
# for n in ism:
#     if n == "a":
#         yigindi = yigindi + 1
# print(f'a soni {yigindi}ta')
#
# ismlar = ["islom", "sardor", "jasur", "muhammadyusuf", "malika"]
# jadval = {}
# fial = []
# pass_ = []
# for n in ismlar:
#     baho = input(f"{n}ning bahosini kiriting >")
#     jadval[n] = baho
# for ism, bahosi in jadval.items():
#
#     if int(bahosi) >= 4:
#         print(ism)
#     else:
#         print(ism)


# print("islom bahosi 5")

# mevalar = {"olma": "apple", "nok": "peach"}
# for i in mevalar.items():
#     print(i)

# star = input('toxtatish uchun stop yozing')
# while star != "stop":
#     star = input('toxtatish uchun stop yozing')

# mevalar={'olma':'apple', 'nok': 'peach' }
# for i in mevalar.values():
#     print(f'mevalar {i}')

# isim = input("ismingizni kiriting")
# familiya= input("familiyangizni kiriting")
# yosh=input("yoshingizni kiriting")
# print (f"isim {isim},'familiya {familiya}yosh{yosh }")

# ruyxat = [1, 3, 6, 5, 8, 4, 7, 5]
# a = ruyxat[1]
# b = ruyxat[3]
# c = ruyxat[5]
# s = (a*b/2)
# p = a + b + c
# print ("uchburchakning yuzasi:",s)
# print("uchburchakning perimetri",p)



# 1 misol rasm
# a = 4
# if a > 0:
#     print("musbat", a+1)
# elif a<0:
#     print("manfiy")
# else:
#     print("teng")
#
# # 2 misol rasm
# a = 6
# if a>=0:
#     print(a+1)
# else:
#     print(a-2)


# 3 rasm
# a = 0
# if a > 0:
#     print("musbat", a+1)
# elif a<0:
#     print("manfiy ", a - 2)
# elif a==0:
#     a = 10
#     print(a)
#
# else:
#     print("teng")
#
# start = int(input("Start sonini kiriting: "))
# end = int(input("End sonini kiriting: "))
# num = int(input("Num sonini kiriting: "))
#
# if num > start and num < end:
#     print(f"{num} soni {start} va {end} orasida joylashgan")
# else:
#     print(f"{num} soni {start} va {end} orasida yoki emas")


# start = int(input("Boshlang'ich sonni kiriting: "))
# end = int(input("Tugallanish sonni kiriting: "))
# num = int(input("Tekshirish uchun sonni kiriting: "))
#
# if start < num < end:
#     print(f"{num} soni {start} va {end} orasida joylashgan")
# else:
#     print(f"{num} soni {start} va {end} orasida yoki orasida emas")

#

# for i in range(21):
#     print(i)

# for num in range(3, 30, 2):
#     print(num)

#
# a = ['A', 'B', 'C', 'D', 'E', 'L']
# print(a[0] + a[2] + a[0] + a[5])

#
# n = int(input("Nechta Fibonachi sonini chiqarishni istaysiz? "))
# a = 0
# b = 1
# while a <= n:
#     print(a)
    # a, b = b, a + b

# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
#
# while True:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         break
#     else:
#         print(float(qiymat)**2)


# - [1] chi vazifa.
# Lug'at yaratish: Berilgan ismlar va ularning yoshlarini
# o'z ichiga olgan lug'at yaratishni talab qiluvchi dastur
# tuzing. Lug'atda biror ism bir marta faqat bitta yosh
# bilan biriktirilsin

# isimlar = {'anvar':20,'ali':15,'holbek':22,'saloh':17}
# for i in isimlar:
#     print(f"{isimlar}".title())
#     break


# [2] chi vazifa
# Lug'at ma'lumotini chiqarish: Berilgan lug'atdagi ma'lumotlarni
# ism: yosh formatida chiqaruvchi dastur tuzing.

# lugat = {"jasur ": 22,"salohiddin ": 17,"asat ": 29,"begzod ": 30}

# for isim, yosh in lugat.items():
#     print(f"{isim}: {yosh} yosh".title())

# [3] chi vazifa.
# Lug'atga element qo'shish: Berilgan lug'atga yangi ism va
# uning yoshini qo'shishni talab qiluvchi dastur tuzing.


# lugat = {"jasur ": 22,"salohiddin ": 17,"asat ": 29,"begzod ": 30}
# isim = input("Yangi ismni kiriting: ")
# yosh= int(input("Yangi yoshni kiriting: "))

# lugat[isim] = yosh

# for isim, yosh in lugat.items():
#     print(f"{isim}: {yosh} yosh")


# [4] chi vazifa. Lug'atdan element o'chirish: Berilgan
# lug'atdan istalgan ismni o'chirib tashlashni talab qiluvchi
# dastur tuzing.

# list = {"jasur":"sardor","abbos":"sulton"}
# a = input("o'chiradigan isimni kiriting : ").lower()
# print(f'siz {a.title()}ni o\'chirdingiz ')
# del list[a]
# print(list)


# (5) chi vazifa Lug'atdagi elementni yangilash:
# Berilgan lug'atda istalgan ismning yoshini
# yangilab, lug'atni yangilangan ma'lumot
# bilan chiqaruvchi dastur tuzing.
# #
# sikl = int(input("Nechta ism kiritishingizni kiriting: "))
# ruyhat = {'a': 4}
# for s in range(sikl):
#     ismi = input("Yangilanadigan ismni kiriting: ")
#     yosh = int(input("Yangi yoshni kiriting: "))
#     if ismi not in ruyhat.keys():
#         ruyhat[ismi] = yosh
#
#
# print("\nYangilangan lugat: ")
# for ism, yoshi in ruyhat.items():
#     print(f"{ism.title()}: {yoshi} yosh")
#

# try:
# list = []
# while True:
#     i = {}
#     ism = input("Ismni kiriting: ").title()
#     try:
#         yosh = int(input("Yoshni kiriting: "))
#         i["ismi"] = ism
#         i["yoshi"] = yosh
#         if i in list:
#             print(f"Kechirasiz {i}dagi foydalanuvchi oldinroq ro\'yxatdan o\'tgan.")
#             break
#         list.append(i)
#         print(list)
#     except:
#         print("siz son orniga harf kirgazdingiz")

#
# try:
#
#     a = 4
#     b = int(5)
#     c = a + b
#     print('to`g`ri javob')
# except:
#     print('sizning kodingizda xato bor')
#

nums = {1, 3, 4, 8, 8, 10, 1, 12, 3}
nums.isalpha()
