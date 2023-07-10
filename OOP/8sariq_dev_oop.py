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
# nums = [2, 2, 4, -4, -6, -5, -8, -9, 5, 2 ]
# print(funcnumber(nums))


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



natijalar = ["Farrux = 45.5%", "Rustam = 63.5%", "Ulug'bek = 62.9%", "Shohrux = 56.3%", "Botir = 56.5%", "Murod = 51.5%",
"Asilbek = 83%",
"Asadbek = 83%",
"Behruz = 80%",
"Farxod = 65%",
"Abbos = 68%",
"Abdullox = 61%"
]



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



def uzunlik(request):
    context = {'uzunlik': 'assalomualaykumhelloworld'}
    for uzun in range(len(context)):
        if uzun >= 15 :
            natija = context
        else:
            natija=lambda x: x.split('')[1].strip('a')
            return (natija)











