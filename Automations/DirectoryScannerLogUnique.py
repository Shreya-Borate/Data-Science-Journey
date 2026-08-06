import sys
import os
import time

def DirectoryScanner(DirectoryPath):

    timestamp = time.ctime()
    LogFilename = "Marvellous%s.log"%(timestamp)

    LogFilename = LogFilename.replace(" ","_")
    LogFilename = LogFilename.replace(":","_")

    print("Log file gets created with name  : ",LogFilename)
    
    fobj = open(LogFilename,"w")

    fobj.write("Marvellous Automation script \n")

    fobj.write("Files from the Directory are : \n ")

    for FolderName,SubFolder,FileName in os.walk(DirectoryPath):
        for fname in FileName :
            fobj.write(fname+"\n")
    
    fobj.close()


def main():
    Border = "-"*40
    print(Border)
    print("Marvellous Automation script")
    print(Border)
    if (len(sys.argv)== 2):
        if (sys.argv[1] == "--h" or sys.argv[1] == "--H" ):
            print("This automation scipt is used to travel the directory")
            print("For better usage please check --u flag")
        elif (sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("please exceute the script as ")
            print("python FileName.py DirectoryName")
            print("DirectoryName should be absolute path")
           
        else:
            DirectoryScanner(sys.argv[1])   #call
    
    else:
        print("Invalid number of arguments")
        print("Please use --h or --u for more information")
    
    print(Border)
    print("Thank you for using Marvellous Automation script")
    print(Border)

    
if __name__ == "__main__":
    main()