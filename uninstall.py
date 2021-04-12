import subprocess 
import time
import os

text = input("continue? (y/n): ")

cont = text.lower()
 
if cont == 'y':
	print("Thank you for using my bot.")
	time.sleep(1.5)
    subprocess.call(["pip", "uninstall", "telepot", "-y"])
    subprocess.call(["pip uninstall requests", "-y"])
    subprocess.call(["pip", "uninstall", "pillow", "-y"])
    subprocess.call(["DEL", "remote.py"])
    subprocess.call(["DEL", "README.md"])
    subprocess.call(["DEL", "api.txt"])
    subprocess.call(["DEL", "id.txt"])
    subprocess.call(["DEL", "uninstall.py"])
 
elif cont == 'n':
    quit()