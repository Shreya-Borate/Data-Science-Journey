class Base:
    def __init__(self):
        print("Inside Base Contructor")

class Derived(Base):
    def __init__(self):
        print("Inside Derived Constructor")

bobj = Base()