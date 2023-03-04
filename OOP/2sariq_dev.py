class Talaba:
    def __init__(self,ism,familiya,tyil):
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.bosqich = 1

    def set_bosqich(self,yangi_bosqich):
        self.bosqich = yangi_bosqich


    def update_bosqich(self):
        self.bosqich +=1


    def get_fullname(self):
      return f" {self.ism}  {self.familiya}"

    def get_info(self):
        return f"ismi {self.ism} familyasi {self.familiya} tugilgan yili {self.tyil}  basqochi {self.bosqich}"




class Fan:
    def __init__(self,nomi):
        self.nomi = nomi
        self.talabalar_soni = 0
        self.talabalar = []


    def add_student(self,talaba):
        self.talabalar.append(talaba)
        self.talabalar_soni += 1

    def get_students(self):
        # talabalar =[]
        # for talaba in self.talabalar:
        #     talabalar.append(talaba.get_fullname())
        return  [talaba.get_fullname() for talaba in self.talabalar]


matem = Fan(nomi='oliy matemetika')

talaba1 = Talaba('alijon','valiyev','2002')
talaba2 = Talaba('axrorjon','xoliqov','2003')
talaba3 = Talaba('xoja','xojaali','1989')
matem.add_student(talaba1)
matem.add_student(talaba2)
matem.add_student(talaba3)

print(matem.get_students())