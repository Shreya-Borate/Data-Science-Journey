# python ProcessSurvillence.py 2 MarvellousLog
# python ProcessSurvillence.py  time_interval  FolderName
#             0                     1            2          


import psutil
import sys
import os


def main():
    Border = "-"*50
    print(Border)
    print("-----Marvellous Platform Survillence System -----")
    print(Border)

    # --h and --u handling
    if (len(sys.argv)==2):
        if (sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This Automation Script is used to perform :")
            print("1. It fetch the information of Running Processes")
            print("2. It fetch information about the Primary storage as Ram")
            print("3. It fetch information aboout Secondary Storage as Hdd")
            print("4. It fetch information about Microprocessor")
            print("5. It gets Auto schedule priodically")
            print("6. It maintians all reord into log file")
            print("7. It sends the log file through mail periodically")
            
        elif (sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the Automation Script as :")
            print(f"Python {sys.argv[0]} Time_interval FolderName")
            print("Time_interval : Time in minutes for periodic execution")
            print("folderName : Name of folder for log file creation")

        else:
            print("Unable to proceed as arguments are not matching")
            print("Please use --h or --u flag for getting more details")

    # Actual project code
    elif (len(sys.argv)==3):
        pass

    else:
        print("Invalid Number of Arguments")
        print("Unable to proceed as arguments are not matching")
        print("Please use --h or --u flag for getting more details")

    print(Border)
    print("---Thank You For Using our Automation System---")
    print(Border)

if __name__ == "__main__":
    main()