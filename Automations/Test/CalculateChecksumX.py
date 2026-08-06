import sys
import os
import hashlib

def calculateChecksum(FileName):
    fobj = open(FileName,"rb")

    hobj = hashlib.md5()

    Buffer = fobj.read(1000)

    while (len(Buffer )>0):
        hobj.update(Buffer)
        Buffer = fobj.read(1000)

    fobj.close()

    return hobj.hexdigest()


def main():
    Ret =calculateChecksum("DemoX.txt")
    print("Checksum of file is : ",Ret)

if __name__ == "__main__":
    main()