import subprocess
import os

subprocess.call(['pip', 'install', 'telepot'])
subprocess.call(['pip', 'install', 'requests'])
os.system('cls||clear')

print(" ____  _____ __  __  ___ _____ _____\n|  _ \| ____|  \/  |/ _ \_   _| ____|_ __  _   _\n| |_) |  _| | |\/| | | | || | |  _| | '_ \| | | |\n|  _ <| |___| |  | | |_| || | | |___| |_) | |_| |\n|_| \_\_____|_|  |_|\___/ |_| |_____| .__/ \__, |\n                                    |_|    |___/\n")

s = input("Enter API key: ")
l = input("Enter your telegram id: ")

f = open('api.txt', 'w')
for index in s:
    f.write(index)
f.close()

f = open('id.txt', 'w')
for index in l:
    f.write(index)
f.close()

subprocess.call(['python', 'remote.py'])


