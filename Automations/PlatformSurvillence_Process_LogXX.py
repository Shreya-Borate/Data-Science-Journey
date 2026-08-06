import psutil
import sys
import os
import time
import schedule

def ProcessScan():
    listprocess =[]


    for proc in psutil.process_iter():
        info = proc.as_dict(attrs=["pid","name","username","status"])
        info["cpu_percent"] = proc.cpu_percent(None)
        info["memory_percent"] =proc.memory_percent()

        listprocess.append(info)

    return listprocess
        
def PlatformSurvillence(FolderName):
    Border = "-"*50

    Ret = False

    Ret = os.path.exists(FolderName)

    if Ret == True:
        Ret = os.path.isdir(FolderName)
        if Ret == False:
            print("Unable to procced as Directory Name exists but it is not a Directory")
            return   

    else:
        os.mkdir(FolderName)
        print("Directory for Logfile gets created sucessfully.")

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")

    FileName = os.path.join(FolderName, "Marvellous_%s.log" %timestamp)  #this %s will replace with timestamp  
    fobj = open(FileName,"w")

    print(f"Log File gets sucessfully created with name {FileName}")

    fobj.write(Border+"\n")
    fobj.write("-----Marvellous Platform Survillence System -----\n")
    fobj.write("Log file gets created at "+timestamp+"\n")
    fobj.write(Border+"\n\n")
    fobj.write("-----------------------System Report-----------------------\n")

    #CPU Information
    fobj.write("Number of active cores : %s\n" %psutil.cpu_count())
    fobj.write("CPU Usage : %s %%\n" %psutil.cpu_percent())
    fobj.write(Border+"\n")

    #RAM Information
    memory = psutil.virtual_memory()

    fobj.write("RAM Usage : %s %%\n" %memory.percent)
    fobj.write("Total RAM avaliable : %s \n" %memory.total)

    fobj.write(Border+"\n")

    #Network Uasage
    netobj = psutil.net_io_counters()
    fobj.write("Network Usage report \n")
    fobj.write("Sent : %.2f MB\n"%(netobj.bytes_sent/ (1024 * 1024)))
    fobj.write("Recieve : %.2f MB\n" %(netobj.bytes_recv / (1024 * 1024)))

    #process log
    Data = ProcessScan()

    for info in Data:
        #fobj.write(f"{info}\n")
        fobj.write("PID : %s \n" %info.get("pid"))
        fobj.write("Name : %s \n" %info.get("name"))
        fobj.write("User Name : %s \n" %info.get("username"))
        fobj.write("Status : %s \n" %info.get("status"))
        fobj.write("CPU Usage : %.2f \n" %info.get("cpu_percent"))
        fobj.write("RAM Usage : %.2f \n" %info.get("memory_percent"))

        fobj.write(Border+"\n")
    
    

    fobj.write(Border+"\n")
    fobj.write("-----------End of Log File-----------\n")
    fobj.write(Border+"\n")

    fobj.close()

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

        #print("CPU Usage : ",psutil.cpu_percent())
        print("Scheduler started Succesfully")
        print("Press ctrl + C to abort the automation Script")
        schedule.every(int(sys.argv[1])).minutes.do(PlatformSurvillence, sys.argv[2])

        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid Number of Arguments")
        print("Unable to proceed as arguments are not matching")
        print("Please use --h or --u flag for getting more details")

    print(Border)
    print("---Thank You For Using our Automation System---")
    print(Border)

if __name__ == "__main__":
    main()