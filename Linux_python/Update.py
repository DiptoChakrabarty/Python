import subprocess as sp
import pyttsx3 as py
print("\t\t\t Gods Menu ")
speaker=py.init()
while True:
	print("Enter Choice")
	print(""" 
		  1) Date
		  2)Calendar
		  3)Yell	""")
	speaker.say("Enter Your Choice")
	speaker.runAndWait()
	ch=int(input())
	if(ch==1):
		speaker.say("The Date is")
		speaker.runAndWait()
		x= sp.getoutput("date")
		print(x)
	elif(ch==2):
		speaker.say("The Calendar is")
		speaker.runAndWait()
		x=sp.getoutput("cal")
		print(x)
	elif(ch==3):
		print("Yipeeee")
		speaker.say("yipeeeeeeeeeeeeeeee")
		speaker.runAndWait()
	else:
		break


