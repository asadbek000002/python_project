names = ['asadbek', 'karimbek', 'samandar', 'temur']

print(f"salom {names[0].title()} bugun choyxona bormi")
print(f"{names[1].title()} senham kelasanmi")

numbers = [1, 3, 8, -4, 7, 3, 5, 14]
numbers[2]=5
print(numbers)
numbers[3]= numbers[3] +8
print(numbers)

t_shaxslar = ['amur temur', 'mirzo ulugbek', 'alisher navoi', 'ibn sino']
z_shaxslar = ['ranaldo', 'mbappe','neymar', 'marsello','ramos']

print(f"Assalomu alaykum men tarixiy shaxslardan {t_shaxslar.pop(1).title()}, zamonaviy shaxslardan \
{z_shaxslar.pop(0).title() } lar bilan suhbatlashishni hohlardin")
print(t_shaxslar)
print(z_shaxslar)
mehmonlar = []
frends = []
frends.append('samandar')
frends.append('karimbek')
frends.append('asadbek')
frends.append('temur')
frends.append('farrux')
m=0
print(frends)
for n in frends:
    print(n)
    print(m)
    dostlar = frends.pop(m)
    m += 1
    mehmonlar.append(dostlar)
print(mehmonlar , m)



while frends:
  a=frends.pop(0)
  mehmonlar.append(a)

print(mehmonlar)

country = ['uzbekiston', 'rassiya','amerika', 'kanada', 'yaponiya', 'xitoy']
a = len(country)
print(f'uzunligi {a}')
print(sorted(country , reverse=True))
country.reverse()
print(country)
country.sort(reverse=True)
print(country)

num_ = list(range(120,1200+2,2))
print(max(o))
print(min(o))
print(max(o) - min(o))

len = len(o)
print(len)
bosh = num_[0:20]
print(bosh)
num_.reverse()
oxir = num_[0:20]
oxir.reverse()
print(oxir)
n = num_[-20:]
print(n)
orta =num_[len(num_)//2-10 : len(num_)//2+10 ]
print(orta)
taomlar = ['osh', 'shashlik', 'manti', 'qovurdoq', 'barak']
nonushta = taomlar[:]

print(nonushta)
print(taomlar)
del nonushta[0]
del nonushta[2]

nonushta[0] = 'sut qaymoq'
print(nonushta)
nonushta= tuple(nonushta)
print(nonushta)

cars = ['toyota', 'mazda', 'hyunday', 'gm', 'kia']
for car in cars:
    n = car.upper()

    if car != 'gm':
        n = car.title()
    print(n)


login = input('login ism kriting>')
if login == 'admin':
    print('xush kelibsiz foydalanuvchilar royxatini korasizmi')
else:
    print(f'xish kelibsiz {login}')
print('ikkita son kriting')
a = input("brinchi son>>")
b = input("ikkinchi son>>")


if a == b :
    print("ikki son teng")

else:
    print("sonlar teng emas")


sikl = True
while sikl:
  num = int(input("son kriting>>"))
  if num % 2 == 0:
     print('raxmat javobingizz uchun')
     sikl = False
  else:
     print('juft son kriting')

user = int(input("yoshingizni kriting\n>>>"))

if 4 > user or user > 60:
     narh = 'bepul'
elif user < 18:
    narh = 10000
else:
    narh = 20000
print(f"chipta narhi {narh}")

mahsulotlar = ['banan', 'olma', 'shaftoli', 'anor', 'giloz', 'qulupnika', 'bexi', 'olcha']

savat = []
for  n in range(5):
    user = input(f"{n + 1}- mahsulotni kriting>>")
    savat.append(user)
print(f"Do'konimizda quidagi mahsulotlar yoq")
for mahsulot in savat:
    if mahsulot not in mahsulotlar:









