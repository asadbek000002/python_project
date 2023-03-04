class Avto:
    def __init__(self,model,rang,karobka,narh):
        self.model = model
        self.rang = rang
        self.karobka = karobka
        self.narh = narh
        self.kilometr = 0

    def get_info(self):
        return f"mashinamizning modeli {self.model}  rangi {self.rang}  karobka {self.karobka} narhi {self.narh}  kilometri {self.kilometr}"

    def set_kilom(self,kilometr):
        self.kilometr=kilometr
        

    def get_model(self):
       return  self.model

    def get_rang(self):
        return self.rang

    def get_kilometr(self):
        return self.kilometr



avto1 = Avto(model='malibu',rang='qora',narh='500000',karobka='mexanik',)

print(avto1.get_info())
avto1.set_kilom(200)
print(avto1.get_info())


