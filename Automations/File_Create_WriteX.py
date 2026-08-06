def main():
    try :
        fobj = open("Demo.txt","w")  #it will create also nd open also 
        print("File gets opened")
    
        fobj.write("Marvellous Infosystem")

        fobj.close()

    except FileNotFoundError as fobj:
        print("File is not present in current directory")

if __name__ == "__main__":
    main()