#!/usr/python
import time
import sys
import os

print("Progress....")

i=1;
max=10;
strPoints="."
while(True):
    os.system('cls')
    print("Progress")
    
    localtime = time.asctime( time.localtime(time.time()) )
    print(localtime)
    print("")
    print("State")
    print(strPoints)
    if(i>=10):
        i=1
        strPoints="."
    else:
        
        for x in range(i):
            strPoints=strPoints+"."
        
        
        
        i=i+1

    
    

    try:
        file = open("file_value.txt","r")
        value = file.read();
        file.close();
        if value=="1":
            print("")
            print("<<<<< ON >>>>>")
            
        elif value=="0":
            print("")
            print("<<<<< OFF >>>>>")
            
        else :
            i=1
            print("Finished!!!")
            sys.exit()

    except:
        print("File Not found!")
        sys.exit()

    time.sleep(1)

print("Good bye",a)