class Base:
    def __init__(self):
        print("Inside Base Contructor")

class Derived(Base):
    def __init__(self):
        super().__init__()
        print("Inside Derived Constructor")

dobj = Derived()