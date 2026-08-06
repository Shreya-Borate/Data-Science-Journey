# two flags :
# --h -> help  
# --u -> usage

import sys

def main():
    print("-"*25)
    print("Marvellous Automation script")
    print("-"*25)
    if (len(sys.argv)== 2):
        if (sys.argv[1] == "--h" or sys.argv[1] == "--H" ):
            print("This automation scipt is used to travel the directory")
            print("For better usage please check --u flag")
        elif (sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("please exceute the script as ")
            print("python FileName.py DirectoryName")
            print("DirectoryName should be absolute path")
           
        else:
            DirectoryName = sys.argv[1]
            print("Directory Name is : ",DirectoryName)
    
    else:
        print("Invalid number of arguments")
        print("Please use --h or --u for more information")
    
    print("-"*25)
    print("Thank you for using Marvellous Automation script")
    print("-"*25)

    
if __name__ == "__main__":
    main()