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


class Spinner:
    __default_spinner_symbols_list = ['[|]', '[/]', '[-]', '[\]']

    def __init__(self, spinner_symbols_list: [str] = None):
        spinner_symbols_list = spinner_symbols_list if spinner_symbols_list else Spinner.__default_spinner_symbols_list
        self.__screen_lock = threading.Event()
        self.__spinner = cycle(spinner_symbols_list)
        self.__stop_event = False
        self.__thread = None

    def get_spin(self):
        return self.__spinner

    def start(self, spinner_message: str):
        self.__stop_event = False
        time.sleep(0.3)

        def run_spinner(message):
            while not self.__stop_event:
                print("\r{spinner} {message}".format(message=message, spinner=next(self.__spinner)), end="")
                time.sleep(0.2)

            self.__screen_lock.set()

        self.__thread = threading.Thread(target=run_spinner, args=(spinner_message,), daemon=True)
        self.__thread.start()

    def stop(self):
        self.__stop_event = True
        if self.__screen_lock.is_set():
            self.__screen_lock.wait()
            self.__screen_lock.clear()
            print("\r", end="")

        print("\r", end="")

if __name__ == '__main__':
    import time
    
    prefix = f"{Fore.LIGHTBLUE_EX}[E] {Fore.LIGHTWHITE_EX}"
    error = f"{Fore.LIGHTRED_EX}[!] {Fore.RED}"
    warning = f"{Fore.YELLOW}[/] {Fore.LIGHTYELLOW_EX}"
    success = f"{Fore.LIGHTGREEN_EX}[+] {Fore.GREEN}"
    notif = f"{Fore.LIGHTBLUE_EX}[E] {Fore.LIGHTWHITE_EX}[Notification] {Fore.LIGHTBLUE_EX}"
    broadcast = f"{Fore.LIGHTBLUE_EX}[E] {Fore.LIGHTWHITE_EX}[Broadcast] {Fore.LIGHTBLUE_EX}"

    database = "https://xello.blue/i/eph"

    spinner = Spinner()
    try: 
        os.system('cls')
        url = urlopen(f"{database}/latest.json")
        data = json.loads(url.read())    
        release = data["release"]  
        spinner.start(f"Downloading Euphoria {release}")

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
            "token": ""
        }
        json_object = json.dumps(config, indent = 3)
        with open("config/current.json", "w") as outfile:
            outfile.write(json_object)
        print("created config.json")
        download = requests.get(f"{database}/release/main.py")
        open(f'main.py', 'wb').write(download.content)
        print("created main.py")
        print("\nTASK: setup.py executed\n")
        print("quitting in 5s")
    except Exception as e:
        print(f"{error}Download failed: {e}")
    spinner.stop()
    time.sleep(4.5)
    os.system("cls")
    time.sleep(0.5)
    exit(0)
