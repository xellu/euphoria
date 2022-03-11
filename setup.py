import os
try:
    import colorama
except ModuleNotFoundError:
    os.system("pip install colorama")
try:
    import urllib
except ModuleNotFoundError:
    os.system("pip install urllib")
try:
    import requests
except ModuleNotFoundError:
    os.system("pip install requests")

from itertools import cycle
import threading
import time
from colorama import Fore
import json
from urllib.request import Request, urlopen
import requests

prefix = f"{Fore.LIGHTBLUE_EX}[E] {Fore.LIGHTWHITE_EX}"
error = f"{Fore.LIGHTRED_EX}[!] {Fore.RED}"
warning = f"{Fore.YELLOW}[/] {Fore.LIGHTYELLOW_EX}"
success = f"{Fore.LIGHTGREEN_EX}[+] {Fore.GREEN}"
notif = f"{Fore.LIGHTBLUE_EX}[E] {Fore.LIGHTWHITE_EX}[Notification] {Fore.LIGHTBLUE_EX}"
broadcast = f"{Fore.LIGHTBLUE_EX}[E] {Fore.LIGHTWHITE_EX}[Broadcast] {Fore.LIGHTBLUE_EX}"

def load():
    

    database = "https://xello.blue/i/eph"

    
  
    os.system('cls')
    url = urlopen(f"{database}/latest.json")
    data = json.loads(url.read())    
    release = data["release"]  

    os.system('cls')
    time.sleep(5)
    print("\n")
    path = os.path.join("config") 
    os.mkdir(path)
    print("created config directory")
    open("config/current.json", 'w')
    open("config/config.json", 'w')
    version = data['version']
    name = data['name']
    current = {
        "name": name,
        "version": version,
        "release": release
    }
    json_object = json.dumps(current, indent = 3)
    with open("config/current.json", "w") as outfile:
        outfile.write(json_object)
    print("created current.json")
    config = {
        "token": "",
        "prefix": "e!"
    }
    json_object = json.dumps(config, indent = 3)
    with open("config/config.json", "w") as outfile:
        outfile.write(json_object)
    print("created config.json")
    download = requests.get(f"{database}/release/main.py")
    open(f'main.py', 'wb').write(download.content)
    print("created main.py")
    print("\nTASK: setup.py executed\n")

try:
    load()
except Exception as e:
    print(f"{error}{e}")
    input()
    exit(0)

print("launching in 5s")
time.sleep(4.5)
os.system("cls")
time.sleep(0.5)
os.system("start main.py")
exit(0)