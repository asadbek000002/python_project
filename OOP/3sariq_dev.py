class Shaxs:
    def __init__(self,ism,familiya,passport,tyil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil

    def get_info(self):
       info = f"{self.ism} {self.familiya}  "
       info += f"passport: {self.passport}, {self.tyil} - yil"
       return info

    def get_age(self,yil):
       return yil - self.tyil

#inson = Shaxs(ism='axi',familiya='qodirov',passport='FB0011122',tyil=2002)

class Talaba(Shaxs):
    def __init__(self,ism,familiya,passport,tyil,idraqam,manzili):
        super().__init__(ism,familiya,passport,tyil)
        self.idraqam = idraqam
        self.bosqich = 1
        self.manzili  = manzili

    def get_id(self):
        return self.idraqam

    def get_bosqich(self):
        return self.bosqich

    def get_info(self):
       info = f"{self.ism} {self.familiya}  "
       info += f" {self.get_bosqich()}-bosqich, id raqami {self.idraqam} "
       return info

talaba1 = Talaba('alijon','valiyev','FD0011122',2002,'N00000011')
print(talaba1.get_id())
print(talaba1.get_age(2023))
print(talaba1.get_info())