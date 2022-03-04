import datetime as dt
import time

#This IP address will serve as redirecting path for all websites to block
ip_localmachine = "127.0.0.1"

#location of host file 
host_file_path = "C:\Windows\System32\drivers\etc\hosts"

#getting list of websites names to block from websites.txt
websites = open("websites.txt","r").read().strip().split(",")

#getting starting time (Hour:Minute:Second) and ending time (Hour:Minute:Second) during which access to websites should be blocked
start_time,end_time = open("time.txt","r").read().split("\n")

#getting current time (Hour:Minute:Second)
current_time = dt.datetime.now().strftime("%H:%M:%S")

while True:

    if start_time<=current_time and current_time<=end_time:#if current time is within working hours

        print("Working Hours")

        with open(host_file_path,"r+") as host_file:#open the host file in read write mode

            file_content = host_file.read()

            #for every website needed to be blocked, it is checked if it is mapped to local IP address ih host file
            for site in websites:

                if site not in file_content:
                    host_file.write(ip_localmachine+" "+site+"\n")
                else:
                    pass

    else:
        
        print("Non Working Hours")

        with open(host_file_path,"r+") as host_file:#open the host file in read write mode

            file_content = host_file.readlines()

            #File handle is pointed to the starting point in the file
            host_file.seek(0)

            #for every line read, it is checked if it contains any of the websites to be blocked. 
            #If it contains, the line is skipped otherwise it is written back to the original host file
            for line in file_content:

                if any(site in line for site in websites):
                    pass
                else:
                    host_file.write(line)

            host_file.truncate()        

    time.sleep(3)
