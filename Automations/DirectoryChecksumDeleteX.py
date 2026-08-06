import sys
import os
import hashlib

def calculateChecksum(FileName):
    fobj = open(FileName,"rb")

    hobj = hashlib.md5()

    Buffer = fobj.read(1024)

    while (len(Buffer )>0):
        hobj.update(Buffer)
        Buffer = fobj.read(1024)

    fobj.close()

    return hobj.hexdigest()

def FindDuplicate(DirectoryName):
    Ret = False

    Ret = os.path.exists(DirectoryName)

    if Ret == False:
        print("Path is Invalid")
        return

    Ret = os.path.isdir(DirectoryName)

    if Ret == False:
        print("It is not a Directory")
        return

    Duplicate = {}

  
    for FolderName,SubFolder,FileName in os.walk(DirectoryName):
        for FName in FileName:
            FName = os.path.join(FolderName,FName)

            CheckSum = calculateChecksum(FName)
        

            if CheckSum in Duplicate:
                
                Duplicate[CheckSum].append(FName)

            else:
                
                Duplicate[CheckSum] =[FName]

    return Duplicate

def DeleteDuplicate(DirectoryName):
    MyDict = FindDuplicate(DirectoryName)

    
    Result = list(filter(lambda x : len(x) > 1, MyDict.values()))

    Count = 0
    TotalDeleted = 0

    for value in Result:
        for subvalue in value:
            
            Count +=1
            if (Count > 1):
                print("Duplicate found : ",subvalue)
                TotalDeleted += 1
        Count = 0

    print("Total Deleted Files : ",TotalDeleted)    
    

def main():
    DeleteDuplicate("Test")


if __name__ == "__main__":
    main()