class Base :
    def fun(self):
        print("Inside Base Fun")

class Derived(Base): 
    def fun(self):
        print("Inside Derived Fun")

Dobj = Derived()
Dobj.fun()