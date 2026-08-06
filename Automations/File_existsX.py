import os

def main():
    if(os.path.exists("Demo.txt")):
        print("File present in current directory")
    
    else:
        print("File does not exists")


if __name__ == "__main__":
    main()