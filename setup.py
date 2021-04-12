import subprocess
import os
import time

try:
    file = open('api.txt')
except IOError as e:

	subprocess.call(['pip', 'install', 'telepot', '-y'])
	subprocess.call(['pip', 'install', 'request', '-y'])
        subprocess.call(['pip', 'install', 'pillow', '-y'])
	os.system('cls||clear')

	print(""" ____  _____ __  __  ___ _____ _____
|  _ \| ____|  \/  |/ _ \_   _| ____|_ __  _   _
| |_) |  _| | |\/| | | | || | |  _| | '_ \| | | |
|  _ <| |___| |  | | |_| || | | |___| |_) | |_| |
|_| \_\_____|_|  |_|\___/ |_| |_____| .__/ \__, |
                                    |_|    |___/""")

	s = input("Enter API key: ")
	l = input("Enter your telegram id: ")
	os.system('cls||clear')

	f = open('api.txt', 'w')
	for index in s:
			f.write(index)
	f.close()

	f = open('id.txt', 'w')
	for index in l:
    		f.write(index)
	f.close()

	subprocess.call(['python', 'remote.py'])  

else:
    with file:
    	text = "you have already installed!"
    	print(text.upper())
    	time.sleep(1.5)
    	os.system('cls||clear')
    	subprocess.call(['python', 'remote.py'])


	

 
