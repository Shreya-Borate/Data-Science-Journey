import matplotlib.pyplot as plt

def main():
   language = ["C","C++","Java","Python"]
   students = [30,40,35,55]

   plt.bar(
       language,                #Values of x axis
       students,                #Values of y axis
       width=0.6,               #width of bars
       edgecolor= "black",      #border color of bar
       linewidth =1,            #wifth of bar border
       alpha = 0.8,             #transparence 0.0 to 1.0
       label = "students"       #legend text
   )

   plt.title("Marvellous Bar Plot")
   plt.xlabel = ("Languages")
   plt.ylabel = ("Number of students")
   plt.legend()
   plt.show()


if __name__ == "__main__":
    main()