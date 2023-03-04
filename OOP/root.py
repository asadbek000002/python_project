class Root:
    def f(self):
         print("Root.f",self)

 class A(Root):
    def f(self):
         print("A,f",self)
         super().f()

 class B(Root):
     def f(self):
         print("B.f",self)
         super().f()


