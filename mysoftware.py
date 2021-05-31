import pyttsx3
import os

print("enter your name:" ,end='')
p=input()
pyttsx3.speak("welcome {}".format(p))


print()
print('press 1 : to open chrome browser')
print('press 2 : to open notepad wmplayer')
print('press 3 : to open media player')
print()
print("Enter your choice : ",end='')


p=input()
print(p)

if int(p) == 1:
	os.system("chrome")
elif int(p) == 2:
	os.system("notepad")
elif int(p) == 3:
	os.system("wmplayer")
else:

	print('Invalid option')