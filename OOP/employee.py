class Eployee:

    def __init__(self, fname , lname,):
        self.fname = fname
        self.lname = lname
        self.fullname = self.fname + ' ' + self.lname
        self.gmail = self.fullname + '@gmail'

    def get_info(self):
        return f"name; {self.fname} last name; {self.lname} fullname; {self.fullname}  gmail; {self.gmail}"

    def salary(self):
        return f"dear {self.fullname}"


class dailyemployee:
    def __init__(self,fname,lname,pay):
        super().__init__(fname,lname)
        self.pay = pay

    def salary(self):
        return super().salary() + f"{self.pay} dollors"


eployee1 = Eployee(fname='ali',lname='valiyev')

print(eployee1.get_info())

de = dailyemployee('jon','doe',5)
print(de.salary())