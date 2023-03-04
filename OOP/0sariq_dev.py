class User:
    def __init__(self,ism,foydalanuvchi_ismi,email):
        self.ism = ism
        self.f_ismi = foydalanuvchi_ismi
        self.email = email

    def get_user(self):
        return f"ismi {self.ism} foydalanuvchi {self.f_ismi} emaili {self.email}"

    def get_name(self):
        return self.ism

    def get_foydalanuvchi(self):
        return  self.f_ismi
foydalanuvchi = User(ism='ali',foydalanuvchi_ismi='Asad2002',email='asad2002.gmail.com')
foydalanuvchi2 = User(ism='asad',foydalanuvchi_ismi='tuygunov2002',email='tuygunov002.gmail.com')

print(foydalanuvchi.get_user())
print(foydalanuvchi.get_name())
print(foydalanuvchi2.get_foydalanuvchi())
print(foydalanuvchi2.get_user())