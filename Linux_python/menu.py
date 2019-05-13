import os
import pyttsx3 as py
import subprocess as sp
os.system("tput setaf 1")
print("\t\t\t Welcome To The God menu ")
os.system("tput setaf 0")

speaker=py.init()
print("\t\t\t ----------------------- ")
speaker.say("Enter Your Choice")
speaker.runAndWait()
print(""" 
	  Press 1 : Check Date 
	  Press 2 : Check Calendar
	  Press 3 : Create file
	  Press 4 : Create User
	  Press 5 : Exit """)

print("Enter your Choice ",end='' )
ch=int(input())
print(ch)

if(ch==1):
	speaker.say("The date is")
	speaker.runAndWait()
	x=sp.getoutput("date")
	print(x)
	
elif(ch==2):
	speaker.say("Calendar is")
	speaker.runAndWait()
	x=sp.getoutput("cal")
	print(x)
elif(ch==3):
	f=input("Provide File Name ")
	x=sp.getoutput("mkdir {}".format(f))
elif(ch==4):
	print("user")

elif(ch==5):
	print("exit")
	
