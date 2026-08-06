def main():
    try :
        fobj = open("Demo.txt","r")  #a = append
        print("File gets opened")

        print("File Offset is :",fobj.tell())

        Data =fobj.read(10)

        print(Data)

        print("File Offset is :",fobj.tell())

        Data =fobj.read(10)

        print(Data)

        print("File Offset is :",fobj.tell())

    except FileNotFoundError as fobj:
        print("File is not present in current directory")

if __name__ == "__main__":
    main()