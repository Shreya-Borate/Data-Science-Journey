no = 11   #Global variable

def Display():
    global no
    no = 21
    print("From Display : ", no)
  
print("before: ",no)
Display()
print("after: ",no)

