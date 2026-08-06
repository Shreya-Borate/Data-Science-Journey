import os

def main():
    ret = os.path.exists("Demo.txt")

    if(ret == True):
        print("File present in current directory")
    
    else:
        print("File does not exists")


if __name__ == "__main__":
    main()