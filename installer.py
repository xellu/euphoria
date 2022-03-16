import os

try:
    import requests
except ModuleNotFoundError:
    os.system("pip install requests")
try:
    import urllib
except ModuleNotFoundError:
    os.system("pip install urllib")

import requests
from urllib.request import Request, urlopen
import os
import time
import json

database = "https://xello.blue/i/euphoria"

def run():
    print("\n     [Euphoria Installer]\n")

    #creating .install
    open(".install", "w")

    #downloading euphoria.py
    print("     TASK: downloading euphoria.py.. ", end="")
    try:
        download = requests.get(f"{database}/download/euphoria.py")
        open(f'euphoria.py', 'wb').write(download.content)
    except Exception as e:
        print(f"Failed, skipping [{e}]")
    else:
        time.sleep(0.25)
        print("Finished")

    #creating settings directory
    print("     TASK: creating settings directory.. ", end="")
    try:
        path = os.path.join("settings") 
        os.mkdir(path)
    except Exception as e:
        print(f"Failed, skipping [{e}]")
    else:
        print("Finished")

    #creating config.json
    print("     TASK: creating config.json ", end="")
    config = open("settings/config.json", "w")
    print("Finished")

    #creating current.json
    print("     TASK: creating current.json ", end="")
    current = open("settings/current.json", "w")
    print("Finished")

    #creating userdata.json
    print("     TASK: creating userdata.json ", end="")
    userdata = open("settings/userdata.json", "w")
    print("Finished")

    #download finished
    print("\n     TASK: download finished. DO NOT CLOSE!")
    time.sleep(1)
    os.system("cls")

    #selfbot setup
    print("\n     [Euphoria Installer]\n")
    print(">    [@] Loading", end="")

    #setup: current.json
    print(".", end="")
    latest = json.loads(urlopen(f"{database}/latest.json").read())
    version = latest["version"]
    release = latest["release"]
    current_content = {
        "version": version,
        "release": release
    }
    current_object = json.dumps(current_content, indent = 2)
    current.write(current_object)
    print(".", end="")

    #setup: userdata.json
    userdata_content = {
        "username": "none",
        "id": "none"
    }
    userdata_object = json.dumps(current_content, indent = 2)
    userdata.write(userdata_object)
    print(".")

    #setup: config.json
    token = input(">    Discord Token: ")
    prefix = input(">    Selfbot prefix: ")
    if prefix == "":
        prefix = "e."
        print(">    [ERROR] Invalid prefix, setting to 'e.'")

    config_content = {
        "token": f"{token}",
        "prefix": f"{prefix}",
        "autoupdate": "true",
        "notifications": "true",
        "consolemode": "false"
    }
    config_object = json.dumps(config_content, indent = 5)
    config.write(config_object)

    #finishing
    os.system("cls")
    print("\n     [Euphoria Installer]\n")
    print(">    [@] Finishing,.", end="")
    try:
        os.remove(".install")
    except:
        print(">    [@] Something went wrong... cannot remove .install")
    else:
        print(".",end="")
    print("")

    print(">    [@] Euphoria was successfully installed")
    input("Press enter to launch...")
    os.system("start \"\" https://discord.gg/kjh9bEytUH")
    time.sleep(3)
    os.system("start euphoria.py")

try:
    run()
except Exception as e:
    print(f"ERROR: {e}")
else:
    os._exit(0)