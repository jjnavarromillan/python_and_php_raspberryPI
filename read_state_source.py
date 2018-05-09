#!/usr/python
import time
import sys
import os
print("Progress....")

while(True):
   
    print("State")
    try:
        file = open("file_value.txt","r")
        value = file.read();
        file.close();
        if value=="1":
            print("ON")
        elif value=="0":
            print("OFF")
        else :
            print("Finished!!!")
            sys.exit()

    except:
        print("File Not found!")
        sys.exit()
    time.sleep(0.5)

print("Good bye",a)