def main():
    try :
        fobj = open("Demo.txt","r")  #a = append
        print("File gets opened")
    
        Data =fobj.read()

        fobj.close()

        print(Data)

    except FileNotFoundError as fobj:
        print("File is not present in current directory")

if __name__ == "__main__":
    main()