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

    Unique = 0
    Same = 0

    for FolderName,SubFolder,FileName in os.walk(DirectoryName):
        for FName in FileName:
            FName = os.path.join(FolderName,FName)

            CheckSum = calculateChecksum(FName)
            print(f"{FName}: {CheckSum}")

            if CheckSum in Duplicate:
                Same += 1
                Duplicate[CheckSum].append(FName)

            else:
                Unique += 1
                Duplicate[CheckSum] =[FName]

    print("Unique Files Found : ",Unique)
    print("Same Files Found : ",Same)

def main():
    FindDuplicate("Test")

if __name__ == "__main__":
    main()
