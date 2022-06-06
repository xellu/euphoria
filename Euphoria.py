#───────────────────────────────────────────────────────────────#
# ███████╗██╗   ██╗██████╗ ██╗  ██╗ ██████╗ ██████╗ ██╗ █████╗  #
# ██╔════╝██║   ██║██╔══██╗██║  ██║██╔═══██╗██╔══██╗██║██╔══██╗ #
# █████╗  ██║   ██║██████╔╝███████║██║   ██║██████╔╝██║███████║ #
# ██╔══╝  ██║   ██║██╔═══╝ ██╔══██║██║   ██║██╔══██╗██║██╔══██║ #
# ███████╗╚██████╔╝██║     ██║  ██║╚██████╔╝██║  ██║██║██║  ██║ #
# ╚══════╝ ╚═════╝ ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝ #
#───────────────────────────────────────────────────────────────#
# Coded & maintained by Xellu#1337 | github.com/xellu/euphoria  #
#───────────────────────────────────────────────────────────────# 


import os,json

importerror = 0

try:
    open(".install")
except:
    pass
else:
    os.system("start installer.py")
    os._exit(0)    

try:
    import colorama
except ModuleNotFoundError:
    importerror = 1
    os.system("pip install colorama")
try:
    import pyfiglet
except ModuleNotFoundError:
    importerror = 1
    os.system("pip install pyfiglet")
try:
    import mouse
except ModuleNotFoundError:
    importerror = 1
    os.system("pip install mouse")
try:
    import pyautogui
except ModuleNotFoundError:
    importerror = 1
    os.system("pip install pyautogui")
try:
    import urllib
except ModuleNotFoundError:
    importerror = 1
    os.system("pip install urllib")
try:
    import requests
except ModuleNotFoundError:
    importerror = 1
    os.system("pip install requests")
try:
    import discord
except ModuleNotFoundError:
    os.system('pip install discord.py')
    os.system('pip install discord.py-self')
try:
    import discord_webhook
except ModuleNotFoundError:
    os.system('pip install discord_webhook')
try:
    import zipfile
except ModuleNotFoundError:
    os.system('pip install zipfile')
try:
    import hashlib
except ModuleNotFoundError:
    os.system('pip intall hashlib')
try:
    import base64
except ModuleNotFoundError:
    os.system('pip install base64')
try:
    import discum
except:
    importerror = 1
    os.system("pip install discum")
try:
    import qrcode
except ModuleNotFoundError:
    importerror = 1
    os.system("pip install qrcode")
try:
    import pypresence
except ModuleNotFoundError:
    importerror = 1
    os.system("pip install pypresence")
try:
    import pystyle
except ModuleNotFoundError:
    importerror = 1
    os.system("pip install pystyle")
try:
    import translate
except ModuleNotFoundError:
    importerror = 1
    os.system("pip install translate")
try:
    import cursor
except ModuleNotFoundError:
    importerror = 1
    os.system("pip install cursor")
try:
    import http.client
except ModuleNotFoundError:
    importerror = 1
    os.system("pip install httpclient")
try:
    import psutil
except ModuleNotFoundError:
    importerror = 1
    os.system("pip install psutil")
try:
    import shutil
except ModuleNotFoundError:
    importerror = 1
    os.system("pip install shutil")
try:
    import better_profanity
except ModuleNotFoundError:
    os.system("pip install better_profanity")
try:
    if json.loads(open("settings/config.json").read())["toasts"] == "true":
        try:
            import win10toast
        except ModuleNotFoundError:
            importerror = 1
            os.system("pip install win10toast")
        try:
            from win10toast import ToastNotifier
        except:
            print("[ERROR] Can't import win10toast, if you're on linux please disable toasts in config.json")
except:
    pass
try:
    import PIL
except ModuleNotFoundError:
    os.system("pip install pillow")

if importerror != 0:
    print("[Euphoria] Successfully installed all the needed packages")
    print("[Euphoria] Loading the selfbot....")
    time.sleep(0.5)

import os
import re
import sys
import PIL
import time
import json
import mouse
import psutil
import urllib
import shutil
import string
import ctypes
import qrcode
import random
import cursor
import asyncio
import hashlib
import discord
import pyfiglet
import requests
import platform
import threading
import pyautogui
import subprocess
import http.client
import better_profanity
from zipfile import ZipFile
from colorama import *
from discord_webhook import *
from urllib.request import Request, urlopen
from discord.ext import *
from discord.ext import commands
from pypresence import Presence
from translate import Translator
from pystyle import Center

http.client._is_legal_header_name = re.compile(rb'[^\s][^:\r\n]*').fullmatch

#───────────────────────────────────────────────────────────────#
# Functions                                                     #
#───────────────────────────────────────────────────────────────# 

def startup():
    try:
        os.remove("settings/.restart")
    except:
        pass
    asset_whitelist = ["e.png", "icon.ico", "success.ico"]
    cls()
    ctypes.windll.kernel32.SetConsoleTitleW("Euphoria")
    log(f"AUTH: logged in")
    for file in os.listdir("settings/assets"):
        if file not in asset_whitelist:
            os.remove(f"settings/assets/{file}")
    title()
    if theme.lower() != "moon":
        separator()
    autoupdater()

class DevNull: 
        def write(self, msg): 
                pass
try:
    open("settings/experiments.json")
except:
    sys.stderr = DevNull()
else:
    if json.loads(open("settings/experiments.json", "r").read())["NullDev"]=="true":
        sys.stderr = DevNull()

def autoupdater():
    r = json.loads(requests.get("https://raw.githubusercontent.com/xellu/euphoria/main/latest_version.json").text)
    r_version = r["version"]
    r_build = r["build"]
    c = json.loads(open("settings/current.json", "r").read())
    c_version = c["version"]
    c_build = c["build"]
    if c_version != r_version or c_build != r_build:
        download = requests.get(f"https://raw.githubusercontent.com/xellu/euphoria/main/Euphoria.py")
        open("Euphoria.py", "wb").write(download.content)
        open("settings/current.json", "w").write(json.dumps({"version": r_version, "build": r_build}))
        successsay(f"Updated to {r_version}")
        successsay(f"Use '{prefix}r' to see changes")

def cmd_show():
    ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 0 )
    time.sleep(0.2)
    ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 1 )

def current_time():
    c_time = time.strftime("%H:%M:%S", time.localtime())
    return f" {Fore.LIGHTBLACK_EX}{c_time}"

def get_random_user_agent():
        userAgents = ["Mozilla/5.0 (Windows NT 6.2;en-US) AppleWebKit/537.32.36 (KHTML, live Gecko) Chrome/56.0.3075.83 Safari/537.32", "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/38.0.2125.101 Safari/537.1", "Mozilla/5.0 (Windows NT 8.0; WOW64) AppleWebKit/536.24 (KHTML, like Gecko) Chrome/32.0.2019.89 Safari/536.24", "Mozilla/5.0 (Windows NT 5.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.41 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3058.0 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3258.0 Safari/537.36", "Mozilla/5.0 (Windows NT 5.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36", "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2599.0 Safari/537.36", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.35 (KHTML, like Gecko) Chrome/27.0.1453.0 Safari/537.35", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.139 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/6.0 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.0.9757 Safari/537.36", "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/38.0.2125.101 Safari/537.1", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3258.0 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/6.0 Safari/537.36", "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/38.0.2125.101 Safari/537.1", "Mozilla/5.0 (Windows NT 5.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2151.2 Safari/537.36", "Mozilla/5.0 (Windows NT 5.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1204.0 Safari/537.1", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/67.0.3387.0 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.0.9757 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3359.181 Safari/537.36", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.81 Safari/537.36", "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3251.0 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/538 (KHTML, like Gecko) Chrome/36 Safari/538", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.18 Safari/535.1", "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.355.0 Safari/533.3", "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.4 Safari/532.0", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.35 (KHTML, like Gecko) Chrome/27.0.1453.0 Safari/537.35", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3359.181 Safari/537.36", "Mozilla/5.0 (Windows NT 10.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36", "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3057.0 Safari/537.36", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.14 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.14", "Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.111 Safari/537.36 TC2", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3058.0 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3258.0 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2531.0 Safari/537.36", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.81 Safari/537.36", "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.111 Safari/537.36,gzip(gfe)", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2264.0 Safari/537.36", "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.29 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.150 Safari/537.36", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.45 Safari/537.36", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.14 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.14", "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2714.0 Safari/537.36", "24.0.1284.0.0 (Windows NT 5.1) AppleWebKit/534.0 (KHTML, like Gecko) Chrome/24.0.1284.0.3.742.3 Safari/534.3", "Mozilla/5.0 (X11; Ubuntu; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1864.6 Safari/537.36", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Chrome/36.0.1985.125 CrossBrowser/36.0.1985.138 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Avast/70.0.917.102", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1615.0 Safari/537.36", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.14 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.14", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/6.0 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3608.0 Safari/537.36", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.81 Safari/537.36", "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3251.0 Safari/537.36", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/54.2.133 Chrome/48.2.2564.133 Safari/537.36", "24.0.1284.0.0 (Windows NT 5.1) AppleWebKit/534.0 (KHTML, like Gecko) Chrome/24.0.1284.0.3.742.3 Safari/534.3", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/54.2.133 Chrome/48.2.2564.133 Safari/537.36", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/54.2.133 Chrome/48.2.2564.133 Safari/537.36", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.18 Safari/535.1", "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2427.7 Safari/537.36", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.61 Safari/537.36", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Chrome/36.0.1985.125 CrossBrowser/36.0.1985.138 Safari/537.36", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.45 Safari/537.36", "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/530.6 (KHTML, like Gecko) Chrome/2.0.174.0 Safari/530.6", "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.29 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.104 Safari/537.36", "24.0.1284.0.0 (Windows NT 5.1) AppleWebKit/534.0 (KHTML, like Gecko) Chrome/24.0.1284.0.3.742.3 Safari/534.3", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko; Google Web Preview) Chrome/27.0.1453 Safari/537.36,gzip(gfe)", "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.29 Safari/537.36", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.45 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.45", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.150 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.102 Safari/537.36", "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2419.0 Safari/537.36", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Chrome/36.0.1985.125 CrossBrowser/36.0.1985.138 Safari/537.36", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1204.0 Safari/537.1", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2700.0 Safari/537.36#", "Mozilla/5.0 (Windows NT 10.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36", "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/533.16 (KHTML, like Gecko) Chrome/5.0.335.0 Safari/533.16", "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.68 Safari/537.36", "Mozilla/5.0 (Windows; U; Windows 95) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.43 Safari/535.1", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2700.0 Safari/537.36#", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.114 Safari/537.36", "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/530.6 (KHTML, like Gecko) Chrome/2.0.174.0 Safari/530.6", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/538 (KHTML, like Gecko) Chrome/36 Safari/538", "Mozilla/5.0 (Windows; U; Windows 95) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.43 Safari/535.1", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.18 Safari/535.1", "Mozilla/5.0 (X11; Linux x86_64; 6.1) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/17.0.1410.63 Safari/537.31", "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2583.0 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2151.2 Safari/537.36", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.18 Safari/535.1", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/536.36 (KHTML, like Gecko) Chrome/67.2.3.4 Safari/536.36", "Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/2.0.172.0 Safari/530.5", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.69 Safari/537.36", "Mozilla/5.0 (Windows NT 10.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.81 Safari/537.36", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Safari/537.36 EdgA/41.0.0.1662", "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/38.0.2125.101 Safari/537.1"]
        userAgent = random.choice(userAgents)
        return userAgent

def get_command(text):
    c = 0
    cmd = ""
    for letter in text:
        if letter == " ":
            c =1
        if c == 0:
            cmd += letter
    cmd = cmd.replace(prefix, "")
    return cmd

def nekobot_api(type, args):
    r = json.loads(requests.get(f"https://nekobot.xyz/api/imagegen?type={type}&{args}").content)
    return r["message"]

#Logging
def log(text):
    try:
        c_time = time.strftime("%H:%M:%S", time.localtime())
        try:
            content = open(f"settings/logs/{logfile}", "r", encoding="utf-8").read()
        except:
            open(f"settings/logs/{logfile}", "w", encoding="utf-8").write(text)
        else:
            open(f"settings/logs/{logfile}", "w", encoding="utf-8").write(content+f"\n[{c_time}]     {text}")
    except:
        settings_regenerate()

def logfile():
    datenow = time.strftime("%m_%d_20%y", time.localtime())
    filename = f"log_{datenow}_"
    count = 1
    while True:
        try:
            open(f"settings/logs/{filename}{count}.ep")
        except:
            return f"{filename}{count}.ep"
        else:
            count += 1

#Say commands
def errorsay(text):
    print(f"{Fore.WHITE}{current_time()} {Fore.RED}> {Fore.WHITE}{text}")
def consolesay(text, script=False):
    if script == False:
        print(f"{Fore.WHITE}{current_time()} {Fore.LIGHTBLUE_EX}> {Fore.WHITE}{text}")
    else:
        print(f"{Fore.WHITE}{current_time()} {Fore.CYAN}> {Fore.WHITE}{text}")
def warnsay(text):
    print(f"{Fore.WHITE}{current_time()} {Fore.YELLOW}> {Fore.WHITE}{text}")
def infosay(text):
    print(f"{Fore.WHITE}{current_time()} {Fore.LIGHTMAGENTA_EX}> {Fore.WHITE}{text}")
def successsay(text):
    print(f"{Fore.WHITE}{current_time()} {Fore.LIGHTGREEN_EX}> {Fore.WHITE}{text}")
#----

def hwid():
    return str(subprocess.check_output('wmic csproduct get uuid')).split('\\r\\n')[1].strip('\\r').strip()

def doublehash(text):
    text_hashed1 = \
            hashlib.sha256(text.encode()).hexdigest()
    text_hashed2 = \
        hashlib.sha256(text_hashed1.encode()).hexdigest()
    return text_hashed2

def selfbot_reboot():
    scriptname =  os.path.basename(sys.argv[0])
    if linux:
        os.system(f"./{scriptname}")
    else:
        os.system(f"""""{scriptname}""""")
    os._exit(0)

def config_edit(cfg_token=None, cfg_prefix=None, cfg_consolemode=None, cfg_toasts=None, cfg_embed_color=None, cfg_deletetimer=None, cfg_theme=None, cfg_ban_detections=None, cfg_giveaway_sniper=None, cfg_nitro_sniper=None, cfg_raid_detections=None):
    try:
        config_new = json.loads(open("settings/config.json").read())
        if cfg_token == None:
            cfg_token = config_new["token"]
        if cfg_prefix == None:
            cfg_prefix = config_new["prefix"]
        if cfg_consolemode == None:
            cfg_consolemode = config_new["consolemode"]
        if cfg_toasts == None:
            cfg_toasts = config_new["toasts"]
        if cfg_embed_color == None:
            cfg_embed_color = config_new["embed_color"]
        if cfg_deletetimer == None:
            cfg_deletetimer = config_new["deletetimer"]
        if cfg_theme == None:
            cfg_theme = config_new["theme"]
        if cfg_ban_detections == None:
            cfg_ban_detections = config_new["ban_detections"]
        if cfg_giveaway_sniper == None:
            cfg_giveaway_sniper = config_new["giveaway_sniper"]
        if cfg_nitro_sniper == None:
            cfg_nitro_sniper = config_new["nitro_sniper"]
        if cfg_raid_detections == None:
            cfg_raid_detections = config_new["raid_detections"]
    except:
        pass
    content = {
        "token": cfg_token,
        "prefix": cfg_prefix,
        "consolemode": cfg_consolemode,
        "toasts": cfg_toasts,
        "embed_color": cfg_embed_color,
        "deletetimer": cfg_deletetimer,
        "theme": cfg_theme,
        "ban_detections": cfg_ban_detections,
        "giveaway_sniper": cfg_giveaway_sniper,
        "nitro_sniper": cfg_nitro_sniper,
        "raid_detections": cfg_raid_detections
    }
    log("INFO: config edited")
    open("settings/config.json", "w").write(json.dumps(content, indent=6))

def title():
    themes = ["normal", "euphoria", "italic", "moon", "old", "fast", "czech", "rise", "nighty"]
    try:
        theme = json.loads(open("settings/config.json", "r").read())["theme"]
    except:
        theme = "normal"
    if theme == "normal" or theme == "euphoria" or theme not in themes:
        print(f"{Fore.LIGHTBLUE_EX}\n\n")
        print(f"███████╗██╗   ██╗██████╗ ██╗  ██╗ ██████╗ ██████╗ ██╗ █████╗ ".center(width))
        print(f"██╔════╝██║   ██║██╔══██╗██║  ██║██╔═══██╗██╔══██╗██║██╔══██╗".center(width))
        print(f"█████╗  ██║   ██║██████╔╝███████║██║   ██║██████╔╝██║███████║".center(width))
        print(f"██╔══╝  ██║   ██║██╔═══╝ ██╔══██║██║   ██║██╔══██╗██║██╔══██║".center(width))
        print(f"███████╗╚██████╔╝██║     ██║  ██║╚██████╔╝██║  ██║██║██║  ██║".center(width))
        print(f"╚══════╝ ╚═════╝ ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝".center(width))
    elif theme == "moon":
        broadcast = requests.get("https://euphoria.xellu1337.repl.co/broadcast").text
        broadcast = json.loads(broadcast)["message"]
        b = Fore.LIGHTBLUE_EX
        r = Fore.RESET
        y = Fore.YELLOW
        moon_ascii = f"""{b}
                                          {b}███{r}╗   {b}███{r}╗ {b}██████{r}╗  {b}██████{r}╗ {b}███{r}╗   {b}██{r}╗
                                          {b}████{r}╗ {b}████{r}║{b}██{r}╔═══{b}██{r}╗{b}██{r}╔═══{b}██{r}╗{b}████{r}╗  {b}██{r}║
                                          {b}██{r}╔{b}████{r}╔{b}██{r}║{b}██{r}║   {b}██{r}║{b}██{r}║   {b}██{r}║{b}██{r}╔{b}██{r}╗ {b}██{r}║
                                          {b}██{r}║╚{b}██{r}╔╝{b}██{r}║{b}██{r}║   {b}██{r}║{b}██{r}║   {b}██{r}║{b}██{r}║╚{b}██{r}╗{b}██{r}║
                                          {b}██{r}║ ╚═╝ {b}██{r}║╚{b}██████{r}╔╝╚{b}██████{r}╔╝{b}██{r}║ {r}╚{b}████{r}║
                                          {r}╚═╝     ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝"""
        print(Center.XCenter(moon_ascii))
        print(Fore.RESET + "─"*width)
        print(Center.XCenter(f"                      {b}[{r}+{b}]{r} {Euphoria.user}"))
        print(Center.XCenter(f"                       {b}[{r}+{b}]{r} {prefix}"))
        print(Fore.RESET + "─"*width)
        print(f"")
        print(f"{current_time()} {y}| {r}{broadcast}{r}")
    elif theme == "italic":
        print(f"{Fore.LIGHTBLUE_EX}\n\n")
        print("    ______            __               _      ".center(width))
        print("   / ____/_  ______  / /_  ____  _____(_)___ _".center(width))
        print("  / __/ / / / / __ \/ __ \/ __ \/ ___/ / __ `/".center(width))
        print(" / /___/ /_/ / /_/ / / / / /_/ / /  / / /_/ / ".center(width))
        print("/_____/\__,_/ .___/_/ /_/\____/_/  /_/\__,_/  ".center(width))
        print("           /_/                                ".center(width))
    elif theme == "old":
        print(Fore.LIGHTBLUE_EX)
        print("8888888888                  888                       d8b          ".center(width))
        print("888                         888                       Y8P          ".center(width))
        print("888                         888                                    ".center(width))
        print("8888888   888  888 88888b.  88888b.   .d88b.  888d888 888  8888b.  ".center(width))
        print("888       888  888 888 \"88b 888 \"88b d88\"\"88b 888P\"   888     \"88b ".center(width))
        print("888       888  888 888  888 888  888 888  888 888     888 .d888888 ".center(width))
        print("888       Y88b 888 888 d88P 888  888 Y88..88P 888     888 888  888 ".center(width))
        print("8888888888 \"Y88888 88888P\"  888  888  \"Y88P\"  888     888 \"Y888888 ".center(width))
        print("                   888                                             ".center(width))
        print("                   888                                             ".center(width))
        print("                   888                                             ".center(width))
    elif theme == "fast":
        print(Fore.LIGHTBLUE_EX)
        print("__________              ______              _____        ".center(width))
        print("___  ____/___  ____________  /_________________(_)_____ _".center(width))
        print("__  __/  _  / / /__  __ \_  __ \  __ \_  ___/_  /_  __ `/".center(width))
        print("_  /___  / /_/ /__  /_/ /  / / / /_/ /  /   _  / / /_/ / ".center(width))
        print("/_____/  \__,_/ _  .___//_/ /_/\____//_/    /_/  \__,_/  ".center(width))
        print("                /_/                                      ".center(width))
    elif theme == "czech":
        print(f"{Fore.LIGHTBLUE_EX}\n\n")
        print(f"███████╗██╗   ██╗███████╗ ██████╗ ██████╗ ██╗███████╗".center(width))
        print(f"██╔════╝██║   ██║██╔════╝██╔═══██╗██╔══██╗██║██╔════╝".center(width))
        print(f"█████╗  ██║   ██║█████╗  ██║   ██║██████╔╝██║█████╗  ".center(width))
        print(f"██╔══╝  ██║   ██║██╔══╝  ██║   ██║██╔══██╗██║██╔══╝  ".center(width))
        print(f"███████╗╚██████╔╝██║     ╚██████╔╝██║  ██║██║███████╗".center(width))
        print(f"╚══════╝ ╚═════╝ ╚═╝      ╚═════╝ ╚═╝  ╚═╝╚═╝╚══════╝".center(width))                                                     
    elif theme == "rise":
        r = Fore.CYAN
        b = Fore.RESET
        print("\n")
        print(f"   {b}██████{r}╗ {b}██{r}╗ {b}██████{r}╗{b}███████{r}╗")
        print(f"   {b}██{r}╔══{b}██{r}╗{b}██{r}║{b}██{r}╔════╝{b}██{r}╔════╝")
        print(f"   {b}██████{r}╔╝{b}██{r}║╚{b}█████{r}╗ {b}█████{r}╗")
        print(f"   {b}██{r}╔══{b}██{r}╗{b}██{r}║ ╚═══{b}██{r}╗{b}██{r}╔══╝")
        print(f"   {b}██{r}║  {b}██{r}║{b}██{r}║{b}██████{r}╔╝{b}███████{r}╗")
        print(f"   {r}╚═╝  ╚═╝╚═╝╚═════╝ ╚══════╝")    
    elif theme == "nighty":
        b = Fore.CYAN
        r = Fore.RESET
        print(f"""
                                {r}███{b}╗   {r}██{b}╗{r}██{b}╗ {r}██████{b}╗ {r}██{b}╗  {r}██{b}╗{r}████████{b}╗{r}██{b}╗   {r}██{b}╗
                                {r}████{b}╗  {r}██{b}║{r}██{b}║{r}██{b}╔════╝ {r}██{b}║  {r}██{b}║╚══{r}██{b}╔══╝╚{r}██{b}╗ {r}██{b}╔╝
                                {r}██{b}╔{r}██{b}╗ {r}██{b}║{r}██{b}║{r}██{b}║  {r}███{b}╗{r}███████{b}║   {r}██{b}║    ╚{r}████{b}╔╝
                                {r}██{b}║╚{r}██{b}╗{r}██{b}║{r}██{b}║{r}██{b}║   {r}██{b}║{r}██{b}╔══{r}██{b}║   {r}██{b}║     ╚{r}██{b}╔╝
                                {r}██{b}║ ╚{r}████{b}║{r}██{b}║╚{r}██████{b}╔╝{r}██{b}║  {r}██{b}║   {r}██{b}║      {r}██{b}║
                                {b}╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝      ╚═╝
        """)


def separator():
    if str(json.loads(open("settings/config.json", "r").read())["theme"]).lower() != "moon":
        friends = 0
        for friend in list(Euphoria.user.friends):
            friends += 1
        separator_size = width-4
        print(Fore.LIGHTBLUE_EX + " ┌" + "─"*separator_size + "┐ ")
        print(Fore.LIGHTWHITE_EX + f"Prefix: {prefix} | User: {Euphoria.user} | Servers: {len(Euphoria.guilds)} | Friends: {friends}".center(width))
        print(Fore.LIGHTBLUE_EX + " └" + "─"*separator_size + "┘ ")

def toast(text, icon=None):
    if icon == "success":
        iconpath = "settings/assets/success.ico"
    else:
        iconpath = "settings/assets/icon.ico"
    if toasts == "true":
        try:
            threaded = True
            if icon == "fix":
                threaded = False
            toaster = ToastNotifier()
            toaster.show_toast(
            "Euphoria",
            f"{text}",
            duration = 3,
            icon_path = iconpath,
            threaded = threaded,
            )
        except:
            pass

def emoji_gen():
    return random.choice(["🎮", "♻", "🐁", "🧱", "🧫", "🚅", "😇", "😂", "🙄", "😳", "🆔", "😡", "😠", "😱", "🥺", "♥", "🤫", "🥟", "🚌", "🧿", "🚎", "🤡", "👵", "🥭", "🥥", "🐱", "🐶", "😹", "👨", "🌾", "👱", "👩", "😶",  "💝"])

def owoify_text(text):
    whitelist = "rRlL"
    DICT = {
        "r": "w", "R": "W", "l": "w", "L": "W"
    }
    output = ""
    for letter in text:
        if letter in whitelist:
            output += DICT[letter]
        else:
            output += letter
    return output

def zalgo_text(text):
    output = ""
    for letter in text:
        zalgo_chars = random.choice(["̶̛̗̜̟͙͓̠͙̖̜̗͌̿͊̔͐́͌̽̿̈́̚͝", "̵̛̯̣̠̬̼͂̐", "̴̨̡̩̘̭̭̻̪̘̺͉̬͖̬͔̖̗̎̂́̉̌͂̚͝͝", "̷̛̛̛̛̯͙̻͕̯̱̺͙̖̙̪͖̰̻̹̟̳͉̺͇͕͆̌̊̿͂̔̆͐͊̌͛̎̾̔͛͋̎̏́̽͋̎̓̇͌̿̕͘̕̕͝͝ͅ", "̴̛̤̙̣̏̽̉̆̐͗͗͝", "̵̛̠̫̉̔̅̌̎", "̴̟͓̟̎͑͑", "̷̡̨̢̡̧̢̛̗͍̟̗̠̤̤̭̼͕̤̟͉͖͖̬̻̯̣͉̺͖̱̙̞͔̮̝̼̜̻̥̲̤͓͂͐̐͊͆̉͑̂̾̎̒͜͝ͅ"])
        output += f"{letter}{zalgo_chars}"
    return output

def emojify_text(text):
    output = ""
    for letter in text:
        if letter == " ":
            output += emoji_gen()
        else:
            output += letter
    return output

def leet_text(text):
    output = ""
    text = text.upper()
    DICT = {"L": "1", "I": "1", "E": "3", "A": "4", "S": "5", "T": "7", "O": "0"}
    for letter in text:
        if letter != " ":
            try:
                output += DICT[letter]
            except:
                output += letter
        else:
            output += " "
    return output

def embed_text(text):
    color = json.loads(open("settings/config.json","r").read())["embed_color"]
    return f"https://euphoria.xellu1337.repl.co/e?text={text}&title=&color={color}"

def modbypass_text(text):
    output = ""
    bypass = ""
    for letter in text:
        for i in range(random.randint(1,3)):
            bypass += empty_char2
        output += f"{letter}{bypass}"
        bypass = ""
    return output

def regional_text(text):
    regional_prefix = ":regional_indicator_"
    letter_whitelist = "abcdefghijklmnopqrstuvwxyz"
    number_whitelist = "0123456789"
    text = text.lower()
    output = ""
    for letter in text:
        if letter in letter_whitelist:
            output += f"{regional_prefix}{letter}:"
        elif letter in number_whitelist:
            if letter == "1":
                output += ":one:"
            elif letter == "2":
                output += ":two:"
            elif letter == "3":
                output += ":three:"
            elif letter == "4":
                output += ":four:"
            elif letter == "5":
                output += ":five:"
            elif letter == "6":
                output += ":six:"
            elif letter == "7":
                output += ":seven:"
            elif letter == "8":
                output += ":eight:"
            elif letter == "9":
                output += ":nine:"
        elif letter == " ":
            output += ":black_large_square:"
        else:
            output += ":asterisk:"
    return output

def china_text(text):
    translator= Translator(to_lang="Chinese")
    output = translator.translate(text)
    return output

def unchina_text(text):
    translator= Translator(to_lang="English")
    output = translator.translate(text)
    return output

def settings_regenerate():
    reinstall_needed = 0
    dirs = ["scripts", "settings"]
    for x in os.listdir():  
        if x in dirs:
            reinstall_needed += 1
    if reinstall_needed == 0:
        open("Installer.py", "wb").write(requests.get("https://raw.githubusercontent.com/xellu/euphoria/main/Installer.py").content)
    files = ["settings/misc/sharelist.txt", "settings/accounts.txt", "settings/current.json", "settings/misc/personalpins.ep"]
    # open("settings/assets/e.png", "wb").write(requests.get("https://raw.githubusercontent.com/xellu/euphoria/main/assets/e.png").content)
    # open("settings/assets/success.ico", "wb").write(requests.get("https://raw.githubusercontent.com/xellu/euphoria/main/assets/success.ico").content)
    # open("settings/assets/icon.ico", "wb").write(requests.get("https://raw.githubusercontent.com/xellu/euphoria/main/assets/icon.ico").content)
    for file in files:
        try:
            open(file)
        except:
            open(file, "w")
    try:
        open("settings/assets/e.png")
    except:
        open("settings/assets/e.png", "wb").write(requests.get("https://raw.githubusercontent.com/xellu/euphoria/main/assets/e.png").content)
    try:
        open("settings/assets/success.ico")
    except:
        open("settings/assets/success.ico", "wb").write(requests.get("https://raw.githubusercontent.com/xellu/euphoria/main/assets/success.ico").content)
    try:
        open("settings/assets/icon.ico")
    except:
        open("settings/assets/icon.ico", "wb").write(requests.get("https://raw.githubusercontent.com/xellu/euphoria/main/assets/icon.ico").content)
    
async def get_message(ctx, id):
        channelMsgHistory = await ctx.channel.history(limit=10000).flatten()
        for message in channelMsgHistory:
            if message.id == id:
                msg = message
                return msg

#raiding 

def _join_(invite, _token_):
    headers = {
        ":authority": "canary.discord.com",
        ":method": "POST",
        ":path": "/api/v9/invites/" + invite,
        ":scheme": "https",
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US",
        "authorization": _token_,
        "content-length": "0",
        "cookie": "__dcfduid=75af9050ff6211ebad731ffdee3c037e; __sdcfduid=75af9051ff6211ebad731ffdee3c037e933998e6356b1dffdf296486c9c67f3f52108589d44d26d29febc86909e52537; __stripe_mid=b1d29ec9-19c8-41d7-9ace-e35266d8e9d1725cd3; __cfruid=402026f51d740991320e719ec5b87763fb9f0b58-1630164866",
        "origin": "https://canary.discord.com",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": get_random_user_agent(),
        "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==      ",
        "x-debug-options": "bugReporterEnabled",
        "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
    }
    halftoken = _token_[:len(_token_)//2] + "******************************"
    try:
        a = requests.post("https://discordapp.com/api/v9/invites/" + invite, headers=headers)
    except Exception as e:
        pass

def _spam_(amountofmsgs, channel_id, text, _token_):
    request = requests.Session()
    headers = {
        'Authorization': _token_,
        'Content-Type': 'application/json',
        'User-Agent': get_random_user_agent()
    }
    payload = {"content": text, "tts": False}
    for i in range(amountofmsgs):
        src = request.post(f"https://canary.discordapp.com/api/v6/channels/{channel_id}/messages", headers=headers, json=payload, timeout=10)
        # print(src.content)
        if src.status_code == 429:
            ratelimit = json.loads(src.content)
            time.sleep(float(ratelimit['retry_after']/1000))
        elif src.status_code == 401:
            break
        elif src.status_code == 404:
            break
        elif src.status_code == 403:
            break

def _leave_(guild_id, _token_):
    data = {"lurking": False}
    headers = {
        ":authority": "canary.discord.com",
        ":method": "DELETE",
        ":path": "/api/v9/users/@me/guilds/" + guild_id,
        ":scheme": "https",
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-GB",
        "authorization": _token_,
        "content-length": "17",
        "content-type": "application/json",
        "cookie": "__dcfduid=4e2f9f3c60d6f01db50da724c5279b74; __sdcfduid=570cdd40f41a11eb93173bb26179babaaa7d5b774796751311e798934dfc5926a409695193927fd4a1663f2df990362a; __stripe_mid=22276a45-1261-4b07-9175-09de18fcaba7e3ea19; OptanonConsent=isIABGlobal=false&datestamp=Mon+Aug+30+2021+15%3A29%3A27+GMT%2B0200+(stredoeur%C3%B3psky+letn%C3%BD+%C4%8Das)&version=6.17.0&hosts=&landingPath=https%3A%2F%2Fcanary.discord.com%2F&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0; _fbp=fb.1.1630330188773.394704090; locale=en-GB",
        "origin": "https://canary.discord.com",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": get_random_user_agent(),
        "x-debug-options": "bugReporterEnabled",
        "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC40MCIsIm9zX3ZlcnNpb24iOiIxMC4wLjIyMDAwIiwib3NfYXJjaCI6Ing2NCIsInN5c3RlbV9sb2NhbGUiOiJzayIsImNsaWVudF9idWlsZF9udW1iZXIiOjk2MzU1LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==",
    }
    requests.delete("https://canary.discord.com/api/v9/users/@me/guilds/" + str(guild_id), json=data, headers=headers)

def _tokencheck_():
  tokens = open("settings/tokens.txt", "r").read().splitlines()
  working_tokens = ""
  for _token_ in tokens:
    headers = {
      ":authority": "canary.discord.com",
      ":method": "GET",
      ":path": "/api/v9/users/@me/library",
      ":scheme": "https",
      "accept": "*/*",
      "accept-encoding": "gzip, deflate, br",
      "accept-language": "en-US",
      "authorization": token,
      "cookie": "__dcfduid=75af9050ff6211ebad731ffdee3c037e; __sdcfduid=75af9051ff6211ebad731ffdee3c037e933998e6356b1dffdf296486c9c67f3f52108589d44d26d29febc86909e52537; __stripe_mid=b1d29ec9-19c8-41d7-9ace-e35266d8e9d1725cd3; __cfruid=c26830bd270657b40b36c5108fa12ba3bc18547c-1630302849",
      "referer": "https://canary.discord.com/channels/881577554409029683/881577554409029686",
      "sec-fetch-dest": "empty",
      "sec-fetch-mode": "cors",
      "sec-fetch-site": "same-origin",
      "user-agent": get_random_user_agent(),
      "x-debug-options": "bugReporterEnabled",
      "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTQwNSwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
    }
    url = "https://discordapp.com/api/v6/users/@me/library"
    halftoken = _token_[:len(_token_)//2] + "******************************"
    check = requests.get(url, headers=headers)
    if check.status_code == 200:
      working_tokens += _token_ + "\n"
      successsay(f"Valid: {halftoken}")
    else:
      errorsay(f"Invalid: {halftoken}")
  open("settings/tokens.txt", "w").write(working_tokens[:-1])

def downloadem(url, name, path="settings/scrape/emoji"):
    headers = {'User-Agent': get_random_user_agent()}
    extension = url[-3:]
    response = requests.get(url, stream=True, headers=headers)
    with open(f"{path}/{name}.{extension}", 'wb') as finalem:
        shutil.copyfileobj(response.raw, finalem)
    log(f"INFO: saved an emoji (url: {url})")
    return json.dumps({"path": f"{path}/{name}.{extension}", "label": str(name)})

def experiments_allow():
    try:
        open("settings/experiments.json")
    except:
        return False
    else:
        return True

def gettime():
    rawtime = str(time.time())
    c = 0
    newtime = ""
    for letter in rawtime:
        if letter == ".":
            c += 1
        if c == 0:
            newtime += letter
    return int(newtime)

def find_tokens(path):
    import os,re,json
    from urllib.request import Request, urlopen
    path += '\\Local Storage\\leveldb'

    tokens = []

    for file_name in os.listdir(path):
        if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
            continue

        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
            for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                for token in re.findall(regex, line):
                    tokens.append(token)
    return tokens

def gettokens():
    import os,re,json
    from urllib.request import Request, urlopen
    user_tokens = []
    local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')

    paths = {
        'Discord': roaming + '\\Discord',
        'Discord Canary': roaming + '\\discordcanary',
        'Discord PTB': roaming + '\\discordptb',
        'Google Chrome': local + '\\Google\\Chrome\\User Data\\Default',
        'Opera': roaming + '\\Opera Software\\Opera Stable',
        'Brave': local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
        'Yandex': local + '\\Yandex\\YandexBrowser\\User Data\\Default'
    }

    
    for platform, path in paths.items():
        if not os.path.exists(path):
            continue

        tokens = find_tokens(path)

        if len(tokens) > 0:
            for token in tokens:
                user_tokens.append(token)

    return user_tokens

def getheaders(token=None, content_type="application/json"):
	headers = {
		"Content-Type": content_type,
		"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
	}
	if token:
		headers.update({"Authorization": token})
	return headers

def getuserdata(token):
	try:
		return json.loads(urlopen(Request("https://discordapp.com/api/v6/users/@me", headers=getheaders(token))).read().decode())
	except:
		pass

def cls():
    if linux:
        os.system("clear")
    else:
        os.system("cls")

#───────────────────────────────────────────────────────────────#
# VARIABLES                                                     #
#───────────────────────────────────────────────────────────────# 

load_error = 0

#Files
try:
    database = "https://xello.blue/i/euphoria"
    width = os.get_terminal_size().columns
    config = json.loads(open("settings/config.json").read())
    current = json.loads(open("settings/current.json").read())
except:
    load_error = 1

#Settings
try: # CONFIG
    token = config["token"]
    prefix = config["prefix"]
    consolemode = config["consolemode"]
    toasts = config["toasts"]
    embed_color = config["embed_color"]
    deletetimer = config["deletetimer"]
    theme = config["theme"]
    ban_detections = config["ban_detections"]
    giveaway_sniper = config["giveaway_sniper"]
    nitro_sniper = config["nitro_sniper"]
    
except:
    prefix = "no-work!"
    load_error = 2

# try: # USERDATA
#     auth_username = userdata["auth_username"]
#     discord_password = userdata["password"]
# except:
#     load_error = 3

try: # CURRENT
    version = current["version"]
    release = current["release"]
except:
    load_error = 4

try:# EXPERIMENTS
    experiments = json.loads(open("settings/experiments.json", "r").read())
except:
    load_error = 11

    
#Codeblock Elements
codeblock = "```"
footer = f"\n\n[ Euphoria ]"
cb_prefix = "ini\n"
cb_error = "css\n"

#Unicode
empty_char = "⠀"
channel_space = "᲼"
empty_char2 = "​"
yellow = "\033[38;5;226m"
pink = "\033[38;5;200m"
text_hide = "||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||"

#Other
raid_log = []
latest_raid = 0
loaded_scripts = []
new_command = None
latest_command = None
logfile = logfile()
codeRegex = re.compile("(discord.com/gifts/|discordapp.com/gifts/|discord.gift/)([a-zA-Z0-9]+)")
module = None
module_value = None
module_value2 = None
customchat = None
afk_state = False
afk_blacklist = []
vc_regions = ["brazil", "hongkong", "india", 'japan', 'russia', 'singapore', 'sydney']
rainbow_role = False
bootup_time = int(time.time())
cycle_activity = False
cycle_status = False

#Utils
command_spoof = 0

#Help Page
#{prefix}command ─ description
c_help = f"""[ Categories ]

{prefix}fun
{prefix}text
{prefix}misc
{prefix}abuse
{prefix}admin
{prefix}scripts
{prefix}raiding
{prefix}account
{prefix}selfbot"""
#{prefix}─
c_fun = f"""[ Fun ]
<> = required | [] = optional

{prefix}gay [@user] ─ gay meter, very advanced
{prefix}penis [@user] ─ insane penis measuring system (doesn't lie)
{prefix}iqtest [@user] ─ iq testing service 
{prefix}ip ─ sends random ip
{prefix}dox [@user] ─ dox someone!
{prefix}ddos <@user> ─ boot someone off the internet 
{prefix}readrules <@user> ─ read the f-ing rules
{prefix}empty ─ nothing, just nothing 
{prefix}gif ─ random gif
{prefix}trash <@user> ─ throw @user outta ur house
{prefix}tweet <@user> <message> ─ fake tweet
{prefix}trump <message> ─ fake trump tweet
{prefix}changemymind <text> ─ change my mind meme
{prefix}clyde <text> ─ fake clyde message
{prefix}dice ─ rolls a dice
{prefix}8ball [question] ─ gives you a random answer
{prefix}alphabet ─ just read the name idk
{prefix}roast <@user> ─ roast the f- outta @target 
{prefix}rarefish [@user] ─ see how many rare fish user has
{prefix}uncleamount [@user] ─ have you ever wondered how many uncles the user has?
{prefix}zipbomb <file amount> ─ creates a zipbomb
{prefix}copy <@target> ─ send the same messages as your target!
{prefix}bomb <@role> ─ makes the role go *explosion*
{prefix}rainbow <@role> ─ makes the role 
{prefix}stoprainbow ─ stops the role from gay
{prefix}minesweeper ─ play the minesweeper game
{prefix}bao ─ watch the dumpling movie"""
#{prefix}─
c_text = f"""[ Text ]
<> = required | [] = optional

{prefix}ascii <text> ─ generates ascii text
{prefix}spoil <text> ─ marks every character of the 
{prefix}encode <encoding> <text> ─ encodes the text
{prefix}flag ─ sends a random flag (modile users wont be able to see it)
{prefix}decode <text> ─ decodes the text with base64
{prefix}owoify <text> ─ makes your message cute (and annoying)
{prefix}zalgo <text> ─ weird looking message
{prefix}emojify <text> ─ puts random emoji between each word
{prefix}1337 <text> ─ become a real 1337 h4x0r
{prefix}regional <text> ─ makes every letter of the message emoji 
{prefix}nitro [amount] ─ generates random nitro link
{prefix}embed <text> ─ sends an embedded message (working)
{prefix}embedcolor <hex color> ─ changes embed color
{prefix}say <text> ─ writes the text into the chat, doesnt trigger any commands
{prefix}customchat [mode] ─ modifies your messages sent in chat (use {prefix}customchat to disable)
{prefix}embedtalk ─ allows you to chat through embeds
{prefix}modbypass [text] ─ allows you to bypass automod
{prefix}china <text> ─ translates the text to chinese
{prefix}sing "<author_name>" "<song_name>" ─ sings the lyrics
{prefix}autoreply <text> ─ auto-replies to every message sent in the server
{prefix}bold <text> ─ makes your text thicc
{prefix}strike <text> ─ basicly {prefix}underline but with a twist
{prefix}underline <text> ─ puts a like under the text
{prefix}italic <text> ─ makes your text look like its falling (kinda)
{prefix}codeblock [type] <text> ─ puts the text into the codeblock 
{prefix}cowsay <text> ─ cowsay command from linux
{prefix}caption <text> ─ captions the latest image in the channel
{prefix}edit <new message> ─ edits your latest message"""
#{prefix}─
c_misc = f"""[ Misc ]
<> = required | [] = optional

{prefix}credits ─ credit page
{prefix}image ─ sends random image
{prefix}servericon ─ gets server icon
{prefix}invite <@bot> ─ sends the invite link for the bot
{prefix}download <filetype> <url> ─ downloads a file from url
{prefix}channelscrape ─ scrapes all channels in the discord server
{prefix}emojiscrape [server id] ─ scrapes all of the emojis from the server
{prefix}repeat ─ repeats latest command
{prefix}staffcheck ─ checks if discord staff is in a server you're in (takes a long time!)
{prefix}stealavatar <@user> ─ downloads @users avatar 
{prefix}chatsave [#channel] ─ saves 500 messages from that channel 
{prefix}share <@user> ─ adds/removes user from command sharing list
{prefix}sharelist ─ sends a list of users you're sharing your commands with
{prefix}timer [time(s)] ─ sets a timer in the channel
{prefix}date ─ gets current date
{prefix}queue ─ shows current 2b2 queue length
{prefix}serversave ─ saves the server you're in
{prefix}serverload <list/save id> ─ loads the saved server
{prefix}statuscycle [text] ─ cycles your status message
{prefix}activitycycle ─ cycles your activity status"""
#{prefix}─
c_abuse = f"""[ Abuse ]
<> = required | [] = optional | * = admin permissions required

{prefix}nuke [message] ─ destroy someones server*
{prefix}massreact [channel id] ─ reacts to every message sent with copious amounts of emojis
{prefix}massban ─ bans everyone from the server*
{prefix}massunban ─ unbans everyone from the server*
{prefix}masskick ─ kicks everyone from the server*
{prefix}massping [amount] ─ pings huge amounts of members in the server
{prefix}massghostping ─ pings huge amounts of members (secretly)
{prefix}masschannel <amount> <name> ─ creates channels*
{prefix}massspam <amount> <text> ─ spams messages in every channel that you can write in
{prefix}react [channel id] ─ adds random reactions under every message sent in the channel
{prefix}ghostping <@user> [amount] ─ pings @target secretly 
{prefix}spam <amount> <text> ─ spams messages
{prefix}spamtts <amount> <text> ─ spams messages using /tts
{prefix}nukechannels ─ deletes every channel in the server*
{prefix}silentlink <url> <text> ─ sends a message with hidden link (embeds will be shown) 
{prefix}cchat ─ clears the chat even if you dont have permissions to do so
{prefix}spoof ─ makes you go inviss
{prefix}vcspam <amount> ─ spams the vc with join sounds
{prefix}vcddos <duration(s)> ─ makes the makes the vc you're in quiet (only on servers, max 300s)*"""
#{prefix}─
c_admin = f"""[ Admin ]
<> = required | [] = optional
# Admin permissions are needed to execute these commands!

{prefix}ban <@user> [reason] ─ bans the user from the server
{prefix}kick <@user> [reason ]─ kicks the user from the server
{prefix}slowmode [delay] ─ sets the slowmode for the channel 
{prefix}mute <@user> [reason] ─ stops the user from talking ('Muted' role required)
{prefix}unmute <@user> ─ unmutes the user
{prefix}lock ─ locks the channel
{prefix}unlock ─ unlocks the channel
{prefix}purge <amount> [@user] ─ deletes a set amount of messages
{prefix}channelspace <name> ─ allows you to create text channel with spaces in the name
{prefix}addemoji <:custom emoji:> [name] ─ adds a emoji from another server (nitro required)"""
#{prefix}─
c_scripts = f"{prefix}scripts"
#{prefix}─
c_raiding = f"""[ Raiding ]
<> = required | [] = optional

{prefix}joinserver <invite> ─ joins the selected server
{prefix}spamserver <amount> <channel id> <text> ─ starts spamming in the channel
{prefix}massspamserver <amount> <server id> <text> ─ starts spamming in the whole server
{prefix}leaveserver <server id> ─ leaves the server
{prefix}singraid "<author_name>" "<song_name>" ─ sings the song with the tokens (accs must be in the server you're using it in)
{prefix}checktokens ─ checks if you have valid tokens
{prefix}tokens ─ see how many tokens do you have"""
#{prefix}─
c_account = f"""[ Account ]
<> = required | [] = optional

{prefix}purgeself <amount> ─ deletes messages sent by you
{prefix}whois [@user] ─ displays info about mentioned user/you
{prefix}status [text] ─ changes your status 
{prefix}aboutme [text] ─ changes your aboutme
{prefix}avatar [@user] ─ sends users/your avatar
{prefix}stealavatar <@user> ─ saves @users avatar"""
#{prefix}─
c_selfbot = f"""[ Selfbot ]
<> = required | [] = optional

{prefix}reboot/r/restart ─ restarts the console
{prefix}dr/disrestart [canary (true/false)] ─ restarts the discord
{prefix}clear/cls ─ clears the console
{prefix}prefix <new prefix> ─ changes the prefix
{prefix}switch [acc] ─ account switcher
{prefix}broadcast ─ allows you to see latest announcements
{prefix}token ─ sends your token into the console
{prefix}version ─ shows current version
{prefix}search ─ find the commands you need
{prefix}join ─ joins the support server
{prefix}afk ─ toggles afk mode
{prefix}logclear ─ clears unimportant logs 
{prefix}sniper [mode] ─ allows you to customize your sniper settings
{prefix}scripts [list/reload] ─ allows you to stuff with the scripts
{prefix}personalpin <message id> ─ pins a message to your personal pins
{prefix}remind <duration(min)> <message> ─ reminds you after (duration)min
{prefix}raidlog ─ toggles raid detections
{prefix}logout ─ disables the selfbot for your current discord account
{prefix}uptime ─ shows how long you've been using the selfbot"""
#{prefix}─
c_credits = f"""[ Credits ]
day1337 - made {prefix}search, {prefix}discord and helped alot with the selfbot development
popbobik - gave some ideas for commands etc.
<3"""

#───────────────────────────────────────────────────────────────#
# SELFBOT                                                       #
#───────────────────────────────────────────────────────────────# 

Euphoria = commands.Bot(command_prefix=prefix, self_bot=True)
Euphoria.remove_command('help') 

#───────────────────────────────────────────────────────────────#
# ON START                                                      #
#───────────────────────────────────────────────────────────────# 

linux = False
if "linux" in str(platform.system()).lower():
    linux = True

cls()
ctypes.windll.kernel32.SetConsoleTitleW("Euphoria")
log("INFO: Euphoria SB Launched")

#StartUp screen
def startscreen():
    title()
    separator_size = width-4
    print(Fore.LIGHTBLUE_EX + " ┌" + "─"*separator_size + "┐ ")
    print(Fore.LIGHTWHITE_EX + f"Connecting to discord".center(width))
    print(Fore.LIGHTBLUE_EX + " └" + "─"*separator_size + "┘ ")

startscreen()
app_id = '952121150832533564'
RPC = Presence(app_id)
#RPC
try:
    open("settings/.restart")
except:
    try:
        open("settings/.rpcoff")
    except:
        try:
            log("INFO: Connecting DISCORD RPC")
            RPC.connect()
            RPC.update(state="Euphoria Selfbot" ,details="https://euphoria.vip/", large_image='e', large_text=f'Euphoria VIP', start=time.time())
        except pypresence.exceptions.DiscordNotFound as error:
            pass
        else:
            log("INFO: DISCORD RPC Connected")
    else:
        log("INFO: DISCORD RPC disabled")
else:
    log("INFO: DISCORD RPC Already running")
#───────────────────────────────────────────────────────────────#
# EVENTS                                                        #
#───────────────────────────────────────────────────────────────# 

@Euphoria.event
async def on_ready(): #ON READY
    try:
        log(f"INFO: Logged into {Euphoria.user}")
        cursor.hide()
        startup()
        toast("Logged in", "fix")
        if linux:
            warnsay("Euphoria doesn't have linux support yet, you may experience some issues")
        
        #SCRIPT LOADING
        global loaded_scripts
        try:
            for file in os.listdir("scripts"):
                if file.endswith(".py"):
                    try:
                        script_code = open(f"scripts/{file}", "r", encoding="utf-8").read()
                        script_code = script_code.replace("@Euphoria.command", "@commands.command")
                        open(file, "w", encoding="utf-8").write(f"from discord.ext import commands\n{script_code}\ndef setup(Euphoria):\n    Euphoria.add_command({file[:len(str(file))-3]})")
                        Euphoria.load_extension(str(file[:len(str(file))-3]))
                        os.remove(file)
                        loaded_scripts.append(str(file[:len(str(file))-3]))
                    except Exception as error:
                        log(f"ERROR: Can't load a script (scripts/{file} | {error}) ")
                        try:
                            os.remove(file)
                        except:
                            pass
        except Exception as error:
            log(f"CRITICAL ERROR: Can't load scripts ({error})")

        #__PYCACHE__ REMOVER
        try:
            for file in os.listdir("__pycache__"):
                os.remove("__pycache__/"+file)
            os.rmdir("__pycache__")
        except Exception as error:
            log(f"ERROR: {error}")

    #FAIL
    except Exception as error:
        if experiments_allow():
            print(str(error))
        log(f"ERROR: {error}")

@Euphoria.event #ON COMMAND
async def on_command(ctx):
    global latest_command
    global new_command
    try:
        await ctx.message.delete()
    except:
        pass
    log(f"COMMAND: {ctx.command.name}")
    script = False
    if str(ctx.command.name) in loaded_scripts:
         script = True
    consolesay(ctx.command.name, script=script)
    if new_command.startswith(prefix+ctx.command.name):
        latest_command = new_command
    
@Euphoria.event #ON COMMAND ERROR
async def on_command_error(ctx, error):
    error_messages = ["A wild error appeared", "Unexpected error appeared", "There was an error while executing the command", "Oops! Something went wrong", "Well that was unexpected"]
    if isinstance(error, commands.CommandNotFound):
        pass
    else:
        if str(error) == "Command raised an exception: HTTPException: 400 Bad Request (error code: 50035): Invalid Form BodyIn content: Must be 4000 or fewer in length.":
            errorsay(f"{ctx.command.name}: output too long")
            if consolemode == "false":
                await ctx.send(f"{codeblock}{cb_error}[E] {random.choice(error_messages)}:\nOutput too long{footer}{codeblock}", delete_after=deletetimer)
        else:
            errorsay(f"{ctx.command.name}: {error}")
            if consolemode == "false":
                await ctx.send(f"{codeblock}{cb_error}[E] {random.choice(error_messages)}:\n{error}{footer}{codeblock}", delete_after=deletetimer)
        log(f"ERROR: ({ctx.command.name}) {error}")
    try:
        await ctx.message.delete()
    except:
        pass

@Euphoria.event #BAN DETECTIONS
async def on_member_ban(guild, user):
    try:
        if str(user) == str(Euphoria.user):
            log(f"BAN: You were banned from {guild.name}")
            errorsay(f"You were banned from {guild.name}")
        else:
            log(f"BAN: {user} ({guild.name})")
            if ban_detections == "true":
                infosay(f"{user} was banned from {guild.name}")
    except:
        pass

@Euphoria.event #ON MESSAGE & OMDS 
async def on_message(message):
    global new_command
    global afk_state
    global afk_blacklist
    global module
    global module_value
    global module_value2
    global customchat
    global raid_log
    global latest_raid

    #if messagelog == "true":
    #    async for message in message.channel.history(limit=1):
    #        if message.content != "":
    #            msg_log(f"[{message.guild.name} | #{message.channel.name}] {message.author}: {message.content}")

    async for message in message.channel.history(limit=1):
        message_content = message.content

    nitro_sniper = json.loads(open("settings/config.json", "r").read())["nitro_sniper"]
    giveaway_sniper = json.loads(open("settings/config.json", "r").read())["giveaway_sniper"]
    lograids = json.loads(open("settings/config.json", "r").read())["raid_detections"]


    #NITRO SNIPER-----------------

    if nitro_sniper == "true":
        snipe_start = time.time()
        try:
            if message.author.id != Euphoria.user.id:
                if codeRegex.search(message_content):
                    code = codeRegex.search(message_content).group(2)
                    if len(code) >= 16:
                        try:
                            result = requests.post(
                                'https://discordapp.com/api/v6/entitlements/gift-codes/' + code + '/redeem',
                                json={'channel_id': str(message.channel.id)},
                                headers={'authorization': token, 'user-agent': 'Mozilla/5.0'})
                            snipe_end = time.time()
                            snipe_time = snipe_start-snipe_end
                            if 'This gift has been redeemed already' in str(result.content):
                                errorsay(f"Nitro Sniper: used nitro code detected ({snipe_time}s)")
                                log(f"INFO: claimed nitro gift-code detected ({message.guild.name} | Sent by: {message.author} | Snipe Time: {snipe_time})")
                            elif 'nitro' in str(result.content):
                                successsay(f"Nitro Sniper: successfully redeemed a gift-code ({message.guild.name} | #{message.channel.name} | {message.author} | Snipe Time: {snipe_time})")
                                toast("Nitro Sniper: Redeemed a Nitro Gift-code", "success")
                                log(f"INFO: nitro gift-code redeemed ({message.guild.name} | Sent by: {message.author} | Snipe Time: {snipe_time})")
                            elif 'Unknown Gift Code' in str(result.content):
                                log(f"INFO: unknown nitro gift-code detected ({message.guild.name} | Sent by: {message.author} | Snipe Time: {snipe_time})")
                        except:
                            pass
        except:
            pass

    #GIVEAWAY SNIPER-----------------------------

    if giveaway_sniper == "true":
        if message.author.id == 294882584201003009:
            prize_bl = "ban kick mute timeout dox"
            prize_bl = prize_bl.split()
            if message_content == "<:yay:585696613507399692>   **GIVEAWAY**   <:yay:585696613507399692>":
                embeds = message.embeds # return list of embeds
                for embed in embeds:
                    gw_prize = embed.author.name
                    gw_desc = embed.description
                blcheck = False
                for word in prize_bl:
                    if word in gw_prize or Euphoria.user.mention in gw_desc: 
                        blcheck = True
                if blcheck:
                    log(f"INFO: Giveaway skipped (PRIZE: {gw_prize})")
                else:
                    try:
                        await message.add_reaction("🎉")
                    except Exception:
                        log(f"INFO: Can't join a giveaway (HOSTED IN: {message.guild.name}, #{message.channel.name} | PRIZE: {gw_prize}) (ERROR MSG: {Exception})")
                    else:
                        successsay(f"Giveaway Sniper: Joined a giveaway ({message.guild.name} | #{message.channel.name}) Prize: '{gw_prize}'")
                        log(f"INFO: Giveaway joined, prize: {gw_prize}")
                        toast(f"Giveaway Sniper: Joined a giveaway hosted in {message.guild.name}", True)

            elif f"Congratulations" in message_content:
                if Euphoria.user.mention in message_content:
                    gwp = 0
                    gw_prize = ""
                    for letter in message_content:
                        if letter == "*":
                            gwp += 1
                        if gwp == 2:
                            gw_prize += letter
                    gw_prize = re.sub(r'.', '', gw_prize, count = 1)
                    if gw_prize == "":
                        successsay(f"Giveaway Sniper: {Fore.LIGHTGREEN_EX}You won{Fore.RESET} a giveaway ({message.guild.name} | #{message.channel.name})")
                        toast(f"Giveaway Sniper: Giveaway won\n > Server: {message.guild.name}\n > Channel: #{message.channel.name}", "success")
                    else:
                        successsay(f"Giveaway Sniper: {Fore.LIGHTGREEN_EX}You won{Fore.RESET} a giveaway ({message.guild.name} | #{message.channel.name}) Prize: '{gw_prize}'")
                        toast(f"Giveaway Sniper: Giveaway won\n > Prize: {gw_prize} \n > Server: {message.guild.name}\n > Channel: #{message.channel.name}", "success")
                    log(f"INFO: Giveaway won, prize: {gw_prize}")


    #AFK MODE------------------------

    if afk_state:
        if message.author.id != Euphoria.user.id:
            if message.author.id not in afk_blacklist:
                if isinstance(message.channel, discord.channel.DMChannel):
                    await message.channel.send(f"{codeblock}{cb_prefix}[E] Hello! Im currently a{empty_char2}f{empty_char2}k, please dm me later{footer}{codeblock}")
                    afk_blacklist.append(message.author.id)
                elif Euphoria.user.mention in message_content:
                    await message.reply(f"{codeblock}{cb_prefix}[E] Hello! Im currently a{empty_char2}f{empty_char2}k, please dm me later{footer}{codeblock}")
                    afk_blacklist.append(message.author.id)
            
            if isinstance(message.channel, discord.channel.DMChannel) or Euphoria.user.mention in message.content:
                infosay(f"{message.author}: {message_content}")

        else:
            if f"a{empty_char2}f{empty_char2}k" not in message_content:
                afk_state = False
                afk_blacklist = []
                infosay("AFK Mode disabled")
                toast("Toggled off AFK Mode")
            
    #RAID LOGGING---------------------------
    if lograids == "true":
        if message.author.id != Euphoria.user.id:
            if message.author.bot == False:
                if message.attachments == False:
                    raid_id = f"{message_content}:{message.author.display_name}:{message.guild.id}"            
                    raid_log.append(raid_id)

                    raid_suspicion = 0


                    for i in raid_log:
                        if raid_id in i:
                            raid_suspicion += 1
                    
                    if raid_suspicion > 15:
                        if latest_raid != message.guild.id:
                            infosay(f"Raid logging: Possible raid detected at {message.guild.name}")
                        latest_raid = message.guild.id
                        try:
                            open(f"settings/misc/raids/{message.guild.id}.txt")
                        except:
                            open(f"settings/misc/raids/{message.guild.id}.txt", "w").write(str(message.jump_url)+"\n")
                        else:
                            content = open(f"settings/misc/raids/{message.guild.id}.txt", "r").read()
                            open(f"settings/misc/raids/{message.guild.id}.txt", "w").write(content+str(message.jump_url)+"\n")

    #MODULES & CUSTOMCHAT ----------------------------

    if module == "massreact":
        if message.channel.id == int(module_value):
            if message.author.id != Euphoria.user.id:
                for i in range(random.randint(5,10)):
                    try:
                        await message.add_reaction(emoji_gen())
                    except:
                        pass
    elif module == "react":
        if message.channel.id == int(module_value):
            try:
                await message.add_reaction(emoji_gen())
            except:
                pass
    elif module == "autoreply":
        if message.guild.id == module_value:
            if message.author.id != Euphoria.user.id:
                await message.reply(module_value2)
    elif module == "copy":
        if message.guild.id == module_value:
            if message.author.id == module_value2:
                copy_msg = better_profanity.profanity.censor(message_content, '\*')
                await message.channel.send(empty_char2+copy_msg)

    if message.author.id == Euphoria.user.id:
        if message.content.startswith(prefix) or message.content.startswith(empty_char2) or message.content.startswith("`"):
            pass
        else:
            try:
                if customchat == "1337":
                    await message.delete()
                    await message.channel.send(empty_char2+leet_text(message.content))
                elif customchat == "embed":
                    await message.delete()
                    await message.channel.send(empty_char2+text_hide+embed_text(message.content))
                elif customchat == "owoify":
                    await message.delete()
                    await message.channel.send(empty_char2+owoify_text(message.content))
                elif customchat == "zalgo":
                    await message.delete()
                    await message.channel.send(empty_char2+zalgo_text(message.content))
                elif customchat == "emojify":
                    await message.delete()
                    await message.channel.send(empty_char2+emojify_text(message.content))
                elif customchat == "regional":
                    await message.delete()
                    await message.channel.send(empty_char2+regional_text(message.content))
                elif customchat == "edit":
                    await message.edit(content=message.content)
                elif customchat == "color":
                    new_message = message_content
                    new_message = new_message.replace("&0", "\033[0;30m")
                    new_message = new_message.replace("&l", "\033[0m\033[1m")
                    new_message = new_message.replace("&n", "\033[0m\033[4m")
                    new_message = new_message.replace("&8", "\033[0;30m")
                    new_message = new_message.replace("&1", "\033[1;34m")
                    new_message = new_message.replace("&2", "\033[1;32m")
                    new_message = new_message.replace("&3", "\033[1;36m")
                    new_message = new_message.replace("&4", "\033[1;31m")
                    new_message = new_message.replace("&5", "\033[1;35m")
                    new_message = new_message.replace("&6", "\033[1;33m")
                    new_message = new_message.replace("&7", "\033[0;37m")
                    new_message = new_message.replace("&8", "\033[39m")
                    new_message = new_message.replace("&f", "\033[1;37m")
                    new_message = new_message.replace("&r", "\033[0m")
                    new_message = new_message.replace("&a", "\033[0;32m")
                    new_message = new_message.replace("&b", "\033[0;36m")
                    new_message = new_message.replace("&c", "\033[0;31m")
                    new_message = new_message.replace("&d", "\033[0;35m")
                    new_message = new_message.replace("&e", "\033[0;33m")

                    if new_message != message_content:
                        await message.edit(content=f"{codeblock}ansi\n{new_message}{codeblock}")
                    
            except:
                errorsay("Can't send a message")

    #COMMAND PROCESSING--------------
    
    if message.author.id == Euphoria.user.id:
        if message.content.startswith(f"{prefix}re") == False or message.content.startswith(f"{prefix}repeat") == False:
            new_command = message.content

    if str(message.author.id) in open("settings/misc/sharelist.txt", "r").read():
        if message_content.startswith(prefix):
            blacklisted_commands = ["logout", "ppin", "ppins", "personalpin", "personalpins", "logclear", "clearlog", "clearlogs", "raidlog", "lograid", "lograids", "remind", "switch", "login", "accountswitch", "switcher", "accswitch", "accountswitcher", "accswither", "rainbow", "stoprainbow", "bomb", "bombrole", "mimic", "copy", "share", "sharelist", "ban", "kick", "lock", "unlock", "purge", "purgeself", "channelspace", "addemoji", "nuke", "massban", "massreact", "massunban", "masskick", "massping", "massghostping", "masschannel", "massspam", "masspam", "react", "ghostping", "spamtts", "tssspam", "tsspam", "nukechannels", "silentlink", "cchat", "purgehack", "spoof", "download", "repeat", "re", "r", "reboot", "restart", "exit", "shutdown", "staff", "staffcheck", "token", "mytoken", "prefix", "sniper", "snipe", "afk", "join", "search", "clear", "cls", "joinserver", "spamserver", "masspamserver", "massspamserver", "leaveserver", "singraid", "tokencheck", "checktokens", "tokens", "mspamserver", "mspam", "status", "aboutme", "bio", "selfpurge", "purgeself", "spam"]
            blacklisted_commands_used = False
            for i in blacklisted_commands:
                if prefix+i in message_content:
                    blacklisted_commands_used = True
            if blacklisted_commands_used:
                await message.reply(f"{codeblock}{cb_error}[E] You're not allowed to execute harmful commands!{footer}{codeblock}", delete_after=deletetimer)
                return
            command = get_command(message_content)
            output = []
            for cmd in Euphoria.commands:
                output.append(cmd.name)
            if command in output:
                await message.reply(message_content)
            else:
                await message.reply(f"{codeblock}{cb_error}[E] Command not found!{footer}{codeblock}", delete_after=deletetimer)
    elif message.author == Euphoria.user:
        await Euphoria.process_commands(message)

#───────────────────────────────────────────────────────────────#
# COMMANDS                                                      #
#───────────────────────────────────────────────────────────────# 

    # if user == None:
    #     errorsay(f"{ctx.command.name}: missing arguments")
    #     if consolemode == "false":
    #         await ctx.send(f"{codeblock}{cb_error}[E] Usage: {prefix}{ctx.command.name} <@user>{footer}{codeblock}", delete_after=deletetimer)

    # output_len = 0
    # for letter in output:
    #     output_len += 1
    # if output_len > 2000:
    #     open("settings/assets/output.txt", "w").write(output)
    #     await ctx.send(f"{codeblock}{cb_error}[E] Output was over 2000 characters long!{footer}{codeblock}", file=discord.File(r"settings\assets\output.txt"))
    #     os.remove("settings/assets/output.txt")
    #     warnsay(f"{ctx.command.name}: output too long! sending txt file")
    # else:

#───────────────────────────────────────────────────────────────# 

#FUN-------------------------------------------------------

@Euphoria.command() #trash
async def trash(ctx, user: discord.User=None):
    if user == None:
        errorsay(f"{ctx.command.name}: text is missing")
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_error}[E] Usage: {prefix}{ctx.command.name} <@user> <message>{footer}{codeblock}", delete_after=deletetimer)
    else:
        ctx.send(nekobot_api("trash", f"url={user.avatar_url}"))

@Euphoria.command() #tweet
async def tweet(ctx, user: discord.User=None, *, message=None):
    if message == None or user == None:
        errorsay(f"{ctx.command.name}: text is missing")
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_error}[E] Usage: {prefix}{ctx.command.name} <@user> <message>{footer}{codeblock}", delete_after=deletetimer)
    else:
        ctx.send(nekobot_api("tweet", f"username={user.display_name}&text={message}"))

@Euphoria.command(aliases=["trumptweet"]) #trump
async def trump(ctx, *, text=None):
    if text == None:
        errorsay(f"{ctx.command.name}: text is missing")
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_error}[E] Usage: {prefix}{ctx.command.name} <text>{footer}{codeblock}", delete_after=deletetimer)
    else:
        ctx.send(nekobot_api("trumptweet", f"text={text}"))

@Euphoria.command(aliases=["cmm"]) #changemymind
async def changemymind(ctx, *, text=None):
    if text == None:
        errorsay(f"{ctx.command.name}: text is missing")
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_error}[E] Usage: {prefix}{ctx.command.name} <text>{footer}{codeblock}", delete_after=deletetimer)
    else:
        ctx.send(nekobot_api("changemymind", f"text={text}"))

@Euphoria.command() #clyde
async def clyde(ctx, *, text=f"Usage: {prefix}clyde <text>"):
    await ctx.send(nekobot_api("clyde", f"text={text}"))

@Euphoria.command() #dice
async def dice(ctx):
    await ctx.send(":"+random.choice(["one", "two", "three", "four", "five", "six"])+":")

@Euphoria.command(name="8ball") #8ball
async def ztuhfrjklg(ctx, q="How do I use this command?"):
    answers = ["Yes", "Totally!", "Nope", "I don't think so", "Maybe", "Ye i like that"]
    answer = random.choice(answers)
    if q == "How do I use this command?":
        answer = f"{prefix}8ball <question>"
    await ctx.send(f"{codeblock}{cb_prefix}[E] 8Ball replied!\n\n[Question] {q}\n[Answer] {answer}{footer}{codeblock}", delete_after=deletetimer)


@Euphoria.command() #gif
async def gif(ctx):
    giflist = ['https://tenor.com/view/car-tiny-gif-25285525', 'https://tenor.com/view/goofy-quantavious-quandale-dingle-gif-25174774', 'https://tenor.com/view/mercedes-benz-mercedes-amg-meme-funny-gif-24923771', 'https://tenor.com/view/install-cat-install-cat-gif-21711026', 'https://media.discordapp.net/attachments/741400495091875873/958394277111677018/huh.gif', 'https://media.discordapp.net/attachments/735026304763691071/827752409069387796/image0.gif', 'https://media.discordapp.net/attachments/941393792425152512/944615612406169680/tenor.gif', 'https://cdn.discordapp.com/attachments/981423215471636490/981474225170812958/07d_1.jpg', 'https://cdn.discordapp.com/attachments/981423215471636490/981432214006956032/40EAE2CF-2728-4C2F-BF9B-0617602CB8E3.jpg', 'https://cdn.discordapp.com/attachments/942538452057071670/960627254004678737/IMG_0814.gif', 'https://tenor.com/view/minor-inconvenience-gif-23795670', 'https://media.discordapp.net/attachments/941393792425152512/964595974586662912/caption-12.gif', 'https://tenor.com/view/yroue-youre-your-you-our-gif-23886497', 'https://tenor.com/view/cooper-jinx-bigfootjinx-im-still-amazed-by-it-cat-gif-23555036', 'https://cdn.discordapp.com/attachments/913816677278429304/971823097063833630/7A975301-412C-4FAA-B521-241262AE9A1F.gif', 'https://cdn.discordapp.com/attachments/879864923172261938/973716751806242816/No-Bitches-Meme-Template-on-Megamind.jpg', 'https://cdn.discordapp.com/attachments/660513126990741506/970439696033398884/2020-06-14_20.47.11.png', 'https://tenor.com/view/nigga-gif-18674554', 'https://cdn.discordapp.com/attachments/905513416721047562/970010054227009576/image0-1.gif', 'https://media.discordapp.net/attachments/964577111950106644/976930620716503090/yYsschlw.gif', 'https://media.discordapp.net/attachments/976730805906841613/976734695591145562/GLfmEcyd.gif', 'https://tenor.com/view/cat-cute-burger-burger-cat-cat-burger-gif-25078813', 'https://tenor.com/view/burger-delicious-yummy-mouth-watering-gif-16353143', 'https://tenor.com/view/burger-delicious-yummy-mouth-watering-gif-16353143', 'https://cdn.discordapp.com/attachments/973246398696914995/982001733670694912/unknown.png']
    await ctx.send(random.choice(giflist))

# @Euphoria.command(name="dame party", aliases=["dame"]) #dame party?
# async def feuhjueigj(ctx):
#     lyrics = """Ptáš se, jak se mám? Já se mám nejlíp.
# Ležím s drinkem u bazénu ve slunečních brejlích.
# Nejmíň milion stupňů na mě teď paří,
# voda už je horká tak, že se skoro vaří."""
#     for i in lyrics.splitlines():
#         await ctx.send(i)

# @Euphoria.command(name="zijeme len raz", aliases=["zijeme"]) #zijeme len raz
# async def zufhesuifgj(ctx):
#     lyrics = """Žijeme len raz, práve tu a práve teraz
# Slnko svieti rovnako na všetkých z nás
# Tak sa nemrač, ale zabudni na stres
# Zabudni, čo tu bolo včera, dneska je tu ďalší deň
# Voda, slnko, party, klub, relax"""
#     for i in lyrics.splitlines():
#         await ctx.send(i)

@Euphoria.command() #bao
async def bao(ctx):
    os.system("start \"\" https://youtu.be/f5CcgFTO274")

@Euphoria.command() #stoprainbow
async def stoprainbow(ctx):
    global rainbow_role
    if rainbow_role:
        rainbow_role = False
        await ctx.send(f"{codeblock}{cb_prefix}[E] Rainbow role was disabled{footer}{codeblock}")
    else:
        rainbow_role = False
        await ctx.send(f"{codeblock}{cb_error}[E] You dont have '{prefix}rainbow <@role>' command activated")

@Euphoria.command() #rainbow
async def rainbow(ctx, role: discord.Role=None):
    global rainbow_role
    if role == None:
        errorsay(f"{ctx.command.name}: @role is missing")
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_error}[E] Usage: {prefix}{ctx.command.name} <@role>{footer}{codeblock}", delete_after=deletetimer)
    else:
        rainbow_role = True
        await ctx.message.delete()
        while rainbow_role:
            await role.edit(reason = None, colour = 0xff0000)
            await asyncio.sleep(10)
            await role.edit(reason = None, colour = 0xff7600)
            await asyncio.sleep(10)
            await role.edit(reason = None, colour = 0xffd100)
            await asyncio.sleep(10)
            await role.edit(reason = None, colour = 0x00ff0c)
            await asyncio.sleep(10)
            await role.edit(reason = None, colour = 0x00ffb9)
            await asyncio.sleep(10)
            await role.edit(reason = None, colour = 0x00c0ff)
            await asyncio.sleep(10)
            await role.edit(reason = None, colour = 0x8d00ff)
            await asyncio.sleep(10)
            await role.edit(reason = None, colour = 0xe100ff)
            await asyncio.sleep(10)
            await role.edit(reason = None, colour = 0xff0092)
            await asyncio.sleep(10)

@Euphoria.command(aliases=["mine"]) #minesweeper
async def minesweeper(ctx):
    m_offets= [ 
    (-1,-1), 
    (0,-1), 
    (1,-1), 
    (-1,0), 
    (1,0), 
    (-1,1), 
    (0,1), 
    (1,1) 
] 

    m_numbers= [ 
   "1️⃣", 
   "2️⃣",  
   "3️⃣",  
   "4️⃣",  
   "5️⃣",  
   "6️⃣" 
]
    size = 8
    size = max(min(size, 8), 2) 
    bombs = [[random.randint(0, size - 1), random.randint(0, size - 1)] for x in range(int(size - 1))] 
    is_on_board = lambda x, y: 0 <= x < size and 0 <= y < size 
    has_bomb = lambda x, y: [i for i in bombs if i[0] == x and i[1] == y] 
    message = "\n" 
    for y in range(size): 
        for x in range(size): 
            tile = "||{}||".format(chr(11036)) 
            if has_bomb(x, y): 
                tile = "||{}||".format(chr(128163)) 
            else: 
                count = 0 
                for xmod, ymod in m_offets: 
                    if is_on_board(x + xmod, y + ymod) and has_bomb(x + xmod, y + ymod): 
                        count += 1 
            message += tile 
        message += "\n" 
    await ctx.send(message)


@Euphoria.command(aliases=["bombrole"]) #bomb
async def bomb(ctx, role: discord.Role=None):
    if role == None:
        errorsay(f"{ctx.command.name}: @role is missing")
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_error}[E] Usage: {prefix}{ctx.command.name} <@role>{footer}{codeblock}", delete_after=deletetimer)
    else:
        await ctx.message.delete()
        for i in range(random.randint(5,10)):
            await role.edit(reason = None, colour = discord.Colour.red(), name="Allahu")
            await asyncio.sleep(3)
            await role.edit(reason = None, colour = 0xffffff, name="Akbar")
            await asyncio.sleep(3)
        await role.edit(reason=None, colour=discord.Colour.red(), name="Allahu Akbar!")
        for i in range(3):
            await role.edit(reason = None, colour = discord.Colour.red())
            await asyncio.sleep(0.25)
            await role.edit(reason = None, colour = 0xffffff)
            await asyncio.sleep(0.25)

        await asyncio.sleep(5)
        await role.delete()

@Euphoria.command(aliases=["mimic"]) #copy
async def copy(ctx, target: discord.User=None):
    global module
    global module_value
    global module_value2
    server_id = ctx.guild.id
    if target == None:
        if module != "copy":
            errorsay(f"{ctx.command.name}: @target is missing")
            if consolemode == "false":
                await ctx.send(f"{codeblock}{cb_error}[E] Usage: {prefix}{ctx.command.name} <@target>{footer}{codeblock}", delete_after=deletetimer)
        else:
            module = None
            module_value = None
            module_value2 = None
            if consolemode == "false":
                await ctx.send(f"{codeblock}{cb_prefix}[E] Turned off copy{footer}{codeblock}", delete_after=deletetimer)
    else:
        module = "copy"
        module_value = server_id
        module_value2 = target.id
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_prefix}[E] Turned on copy{footer}{codeblock}", delete_after=deletetimer)

@Euphoria.command(aliases=["uncles"]) #uncleamount
async def uncleamount(ctx, user: discord.User=None):
    if user == None:
        user = Euphoria.user
    uncle_amount = random.randint(0,100)
    await ctx.send(f"{codeblock}{cb_prefix}[E] {user.name} has mined {uncle_amount} uncles{footer}{codeblock}")

@Euphoria.command() #rarefish
async def rarefish(ctx, user: discord.User=None):
    if user == None:
        user = Euphoria.user
    fish_amount = random.randint(0,69420)
    await ctx.send(f"{codeblock}{cb_prefix}[E] {user.name} has {fish_amount} rare fish{footer}{codeblock}")

@Euphoria.command(aliases=["rekt"]) #roast
async def roast(ctx, user: discord.User=None):
    if user == None:
        errorsay(f"{ctx.command.name}: @user is missing")
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_error}[E] Usage: {prefix}{ctx.command.name} <@user>{footer}{codeblock}", delete_after=deletetimer)
    else:
        roast = random.choice(["HERE'S 20 CENTS, CALL ALL YOUR FRIENDS AND GIVE ME BACK THE CHANGE.", "SOME CAUSE HAPPINESS WHEREVER THEY GO; OTHERS, WHENEVER THEY GO.", "YOUR MAMMA SO FAT SHE HAS TO WEAR 2 WATCHES BECAUSE SHE COVERS TWO TIME ZONES.", "YO MAMA SO FAT WEN SHE JUMPED IN THE OCEAN THE WHALES STARTED SINGING WE ARE FAMILY.", "WHY DON'T YOU CHECK UP ON EBAY AND SEE IF THEY HAVE A LIFE FOR SALE.", "YOU SIR ARE AN INSULT UPON INSULTS OF A BOOBLE ON AN ASSORTMENT.", "DO YOUR KEEPERS A HUGE FAVOR: DO A TRIPLE SUMMERSAULT THROUGH THE AIR, AND DISAPPEAR UP YOUR OWN ASSHOLE.", "YOU'RE SO UGLY YOU MADE AN ONION CRY.", "GO AND HIDE UNDER SOMETHING OLD!", "HEY, YOU HAVE SOMETHING ON YOUR CHIN...3RD ONE DOWN.", "YOUR VALUE DOESN'T EVEN AMOUNT TO THE JUICE SQUEEZED FROM AN OLD WHORE'S SOILED TAMPON.", "DO YOUR KEEPERS A HUGE FAVOR: DO A TRIPLE SUMMERSAULT THROUGH THE AIR, AND DISAPPEAR UP YOUR OWN ASSHOLE.", "MAY YOUR WIFE GIVE BIRTH TO A CENTIPEDE SO YOU HAVE TO WORK FOR SHOES ALL YOUR LIFE.", "YOU'RE SO UGLY HELLO KITTY SAID GOODBYE TO YOU.", "YOU'RE AS UGLY AS A SALAD!", "WHEN YOU WERE BORN, THE POLICE ARRESTED YOUR DAD, THE DOCTOR SLAPPED YOUR MOM, ANIMAL CONTROL EUTHANIZED YOUR BROTHER, AND A&E MADE A DOCUMENTARY THAT SAVED YOUR LIFE.", "YOU'RE SO STUPID YOU GOT FIRED FROM THE M&M FACTORY FOR THROWING OUT ALL THE WS.", "I HEAR WHEN YOU WERE A CHILD YOUR MOTHER WANTED TO HIRE SOMEBODY TO TAKE CARE OF YOU, BUT THE MAFIA WANTED TOO MUCH.", "DO YOU HAVE TO LEAVE SO SOON? I WAS JUST ABOUT TO POISON THE TEA.", "IS THAT YOUR FACE? OR DID YOUR NECK JUST THROW UP", "WITH A FACE LIKE YOURS, I WISH I WAS BLIND.", "IT'S NOT PRETTY WATCHING A JACKASS TRYING TO EAT A POMEGRANATE.", "THE ONLY POSITIVE THING ABOUT YOU IS YOUR HIV STATUS."]).lower()
        await ctx.send(user.mention + " " + roast)

@Euphoria.command(aliases=["abc"]) #alphabet
async def alphabet(ctx):
    messages = ["Bro so dumb that he cant remember the abcs", "Ur so lazy that you use selfbot to see the alphabet", "Imagine searching up abcs in discord"]
    await ctx.send(f"{codeblock}{cb_prefix}[E] ABCDEFGHIJKLMNOPQRSTUVWXYZ\n{random.choice(messages)}{emoji_gen()}{footer}{codeblock}")

@Euphoria.command(aliases=["gayometer", "howgay"]) #gay
async def gay(ctx, user: discord.User=None):
    if user == None:
        user = Euphoria.user
    await ctx.send(f"{codeblock}{cb_prefix}[E] {user.name} is {random.randint(0,100)}% gay{footer}{codeblock}")

@Euphoria.command(aliases=["pp", "dick", "benis"]) #penis
async def penis(ctx, user: discord.User=None):
    if user == None:
        user = Euphoria.user
    benis = "8"+"="*random.randint(0,50)+"D"
    await ctx.send(f"{codeblock}{cb_prefix}[E] {user.name}'s penis:\n{benis}{footer}{codeblock}")
   

@Euphoria.command(aliases=["iq"]) #iqtest
async def iqtest(ctx, user: discord.User=None):
    if user == None:
        user = Euphoria.user
    iq = random.randint(0,200)
    if iq < 80:
        await ctx.send(f"{codeblock}{cb_error}[E] {user.name} failed the iq test{footer}{codeblock}")
    else:
        await ctx.send(f"{codeblock}{cb_prefix}[E] {user.name} passed the iq test with {iq} IQ{footer}{codeblock}")

@Euphoria.command() #ip
async def ip(ctx):
    await ctx.send(f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}:{random.randint(1,25555)}")

@Euphoria.command() #dox
async def dox(ctx, user: discord.User=None):
    content = f"{codeblock}{cb_prefix}[ DOX ]\n\n"
    if user == None:
        content += f"[ General Info ]\nDiscord: {Euphoria.user}"
    else:
        content += f"[ General Info ]\nDiscord: {user}"

    first_name = random.choice(["David", "Julia", "Ethan", "Ayden"])
    last_name = random.choice(["Smith", "Newell", "Sinclair", "Bullard", "Romijnsen"])
    full_name = f"{first_name} {last_name}"
    facebook_name = f"{first_name}_{last_name}"
    company = random.choice(["Visa", "Mastercard"])
    card_num = "".join(random.choice(string.digits) for i in range(16))
    card_cvc = "".join(random.choice(string.digits) for i in range(3))
    card_pin = "".join(random.choice(string.digits) for i in range(4))
    exp = f"{random.randint(1,12)}/{random.randint(23,27)}"
    content += f"""
Age: {random.randint(18,50)}
Facebook: @{facebook_name}
IP: {random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}
[ Card Info ]
Card holder: {full_name}
Card number: {card_num}
CVC: {card_cvc}
PIN: {card_pin}
Expiration date: {exp}
Issued by: {company}"""

    content += f"{footer}{codeblock}"
    await ctx.send(content)

@Euphoria.command(aliases=["boot", "dos"]) #ddos
async def ddos(ctx, user: discord.User=None):
    if user == None:
        errorsay(f"{ctx.command.name}: @user is missing")
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_error}[E] Usage: {prefix}{ctx.command.name} <@user>{footer}{codeblock}", delete_after=deletetimer)
    else:
        await ctx.send(f"<@{user.id}>{codeblock}{cb_prefix}[E] Sending {random.randint(50000, 1000000)} requests/1s to {user.name}{footer}{codeblock}")

@Euphoria.command() #readrules
async def readrules(ctx, user: discord.User=None):
    if user == None:
        errorsay(f"{ctx.command.name}: @user is missing")
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_error}[E] Usage: {prefix}{ctx.command.name} <@user>{footer}{codeblock}", delete_after=deletetimer)
    else:
        msg = await ctx.send(f"Read{text_hide}<@{user.id}>")
        await asyncio.sleep(1)
        await msg.edit(content=f"Read the{text_hide}<@{user.id}>")
        await asyncio.sleep(1)
        await msg.edit(content=f"Read the fucking{text_hide}<@{user.id}>")
        await asyncio.sleep(1)
        await msg.edit(content=f"Read the fucking rules{text_hide}<@{user.id}>")
        await asyncio.sleep(1)
        await msg.edit(content=f"Read the fucking rules <@{user.id}>")
        await asyncio.sleep(5)
        await msg.edit(content=f"Read the rules <@{user.id}>")

@Euphoria.command(aliases=["none"]) #empty
async def empty(ctx):
    await ctx.send("** **")

@Euphoria.command(aliases=["zip"]) #zipbomb
async def zipbomb(ctx, amount: int=None):
    if amount == None or amount < 2:
        errorsay(f"{ctx.command.name}: amount is missing")
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_error}[E] Usage: {prefix}{ctx.command.name} <file amount>{footer}{codeblock}", delete_after=deletetimer)
    else:
        await ctx.message.delete()
        toast("Please wait...", True)
        zipname = "".join(random.choice(string.ascii_lowercase + string.digits) for i in range(5))
        zip = ZipFile(f'{zipname}.zip', 'w')
        for i in range(amount):
            filecontent = "".join(random.choice(string.printable) for i in range(random.randint(5000, 10000)))
            filename = ''.join(random.choice(string.ascii_lowercase) for i in range(50)) + '.' + ''.join(random.choice(string.ascii_lowercase) for i in range(20))
            open(filename, "w").write(filecontent)
            zip.write(filename)
            os.remove(filename) 
        zip.close()
        await ctx.send(file=discord.File(zipname+".zip"))
        os.remove(zipname+".zip")


#TEXT-------------------------------------------------------------

@Euphoria.command() #edit
async def edit(ctx, *,new_message=None):
    if new_message == None:
        errorsay(f"{ctx.command.name}: text is missing")
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_error}[E] Usage: {prefix}{ctx.command.name} <text>{footer}{codeblock}", delete_after=deletetimer)
    else:
        await ctx.message.delete()
        history = await ctx.channel.history(limit=100).flatten()
        for message in history:
            if message.author.id == Euphoria.user.id:
                await message.edit(content=new_message)
                break

@Euphoria.command() #caption
async def caption(ctx, text=None):
    if text == None:
        errorsay(f"{ctx.command.name}: text is missing")
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_error}[E] Usage: {prefix}{ctx.command.name} <text>{footer}{codeblock}", delete_after=deletetimer)
    else:
        errorsay(f"'{prefix}caption {text}' no work :(")
        try:
            supportchannel = Euphoria.get_channel(951503906540761151)
            await supportchannel.send(codeblock+"caption no work :^("+codeblock)
        except:
            pass

@Euphoria.command(aliases=["kravarict"]) #cowsay
async def cowsay(ctx, *, text=f"Usage: {prefix}cowsay <text>"):
    def cowsay_text(msg):
        msg_len = int(len(msg))
        output = ""
        output += " " + "_"*int(msg_len+2)
        output += "\n"+f"< {msg} >"
        output += "\n " + "-"*int(msg_len+2)
        output += """
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\\
                ||----w |
                ||     ||"""
        return output

    newtext = ""
    for letter in text:
        if letter == "\n":
            newtext += " "
        else:
            newtext += letter
    
    await ctx.send(codeblock+cowsay_text(newtext)+codeblock)

@Euphoria.command(name="codeblock", aliases=["cb", "cblock"]) #codeblock
async def huifherjui(ctx, cb_type=None, *, text=None):
    if cb_type == None:
        errorsay(f"{ctx.command.name}: text or type is missing")
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_error}[E] Usage: {prefix}{ctx.command.name} [type] <text>{footer}{codeblock}", delete_after=deletetimer)
    else:
        cb_typelist = ["c", "cpp", "cs", "css", "java", "py", "js", "html", "lua", "ini", "yaml", "diff", "ansi", "md", "json"]
        if cb_type.lower() in cb_typelist:
            await ctx.send(f"{codeblock}{cb_type.lower()}\n{text}{codeblock}")
        else:
            if text == None:
                text = ""
            cb_type = cb_type.replace("`", "\\`")
            text = text.replace("`", "\\`")
            await ctx.send(f"{codeblock}{cb_type} {text}{codeblock}")

@Euphoria.command() #italic
async def italic(ctx, *, text=None):
    if text == None:
        errorsay(f"{ctx.command.name}: text is missing")
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_error}[E] Usage: {prefix}{ctx.command.name} <text>{footer}{codeblock}", delete_after=deletetimer)
    else:
        await ctx.send(f"*{text}*")

@Euphoria.command(aliases=["underlined"]) #underline
async def underline(ctx, *, text=None):
    if text == None:
        errorsay(f"{ctx.command.name}: text is missing")
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_error}[E] Usage: {prefix}{ctx.command.name} <text>{footer}{codeblock}", delete_after=deletetimer)
    else:
        await ctx.send(f"__{text}__")

@Euphoria.command() #strike
async def strike(ctx, *, text=None):
    if text == None:
        errorsay(f"{ctx.command.name}: text is missing")
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_error}[E] Usage: {prefix}{ctx.command.name} <text>{footer}{codeblock}", delete_after=deletetimer)
    else:
        await ctx.send(f"~~{text}~~")

@Euphoria.command() #bold
async def bold(ctx, *, text=None):
    if text == None:
        errorsay(f"{ctx.command.name}: text is missing")
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_error}[E] Usage: {prefix}{ctx.command.name} <text>{footer}{codeblock}", delete_after=deletetimer)
    else:
        await ctx.send(f"**{text}**")

@Euphoria.command() #flag
async def flag(ctx):
    flags = ["""
[0m[0;34m█████████████████████████████████████
█████████████████████████████████████
█████████████████████████████████████
█████████████████████████████████████
[0m[0;33m█████████████████████████████████████
█████████████████████████████████████
█████████████████████████████████████
█████████████████████████████████████""",
"""
[0m[0;34m█████████████████████████████████████
█████████████████████████████████████
[0m[0;30m█████████████████████████████████████
█████████████████████████████████████
[0m[0;37m█████████████████████████████████████
█████████████████████████████████████
""",
"""
[0m[0;34m███[0m[0;37m██████████████████████████████████
[0m[0;34m██████[0m[0;37m███████████████████████████████
[0m[0;34m█████████[0m[0;37m████████████████████████████
[0m[0;34m████████████[0m[0;37m█████████████████████████
[0m[0;34m████████████[0m[0;31m█████████████████████████
[0m[0;34m█████████[0m[0;31m████████████████████████████
[0m[0;34m██████[0m[0;31m███████████████████████████████
[0m[0;34m███[0m[0;31m██████████████████████████████████
""",
"""
[0m[0;30m█████████████████████████████████████
█████████████████████████████████████
[0m[0;31m█████████████████████████████████████
█████████████████████████████████████
[0m[0;33m█████████████████████████████████████
█████████████████████████████████████
""",
"""
[0m[0;32m█████████[0m[0;37m█████████[0m[0;31m█████████
[0m[0;32m█████████[0m[0;37m█████████[0m[0;31m█████████
[0m[0;32m█████████[0m[0;37m█████████[0m[0;31m█████████
[0m[0;32m█████████[0m[0;37m█████████[0m[0;31m█████████
[0m[0;32m█████████[0m[0;37m█████████[0m[0;31m█████████
[0m[0;32m█████████[0m[0;37m█████████[0m[0;31m█████████
[0m[0;32m█████████[0m[0;37m█████████[0m[0;31m█████████
[0m[0;32m█████████[0m[0;37m█████████[0m[0;31m█████████
""",
"""
[0m[0;32m█████████[0m[0;37m█████████[0m[0;33m█████████
[0m[0;32m█████████[0m[0;37m█████████[0m[0;33m█████████
[0m[0;32m█████████[0m[0;37m█████████[0m[0;33m█████████
[0m[0;32m█████████[0m[0;37m█████████[0m[0;33m█████████
[0m[0;32m█████████[0m[0;37m█████████[0m[0;33m█████████
[0m[0;32m█████████[0m[0;37m█████████[0m[0;33m█████████
[0m[0;32m█████████[0m[0;37m█████████[0m[0;33m█████████
[0m[0;32m█████████[0m[0;37m█████████[0m[0;33m█████████
""",
"""
[0m[0;31m█████████████████████████████████████
█████████████████████████████████████
[0m[0;37m█████████████████████████████████████
█████████████████████████████████████
[0m[0;31m█████████████████████████████████████
█████████████████████████████████████
""",
"""
[0m[0;37m█████████████████████████████████████
█████████████████████████████████████
█████████████████████████████████████
█████████████████████████████████████
[0m[0;31m█████████████████████████████████████
█████████████████████████████████████
█████████████████████████████████████
█████████████████████████████████████
""",
"""
[0m[0;37m█████████████████████████████████████
█████████████████████████████████████
[0m[0;34m█████████████████████████████████████
█████████████████████████████████████
[0m[0;31m█████████████████████████████████████
█████████████████████████████████████
""",
"""
[0m[0;31m█████████████████████████████████████
█████████████████████████████████████
[0m[0;37m█████████████████████████████████████
█████████████████████████████████████
[0m[0;34m█████████████████████████████████████
█████████████████████████████████████
""",
"""
[0m[0;31m█████████████████████████████████████
█████████████████████████████████████
[0m[0;37m█████████████████████████████████████
[0m[0;31m█████████████████████████████████████
█████████████████████████████████████
""",
"""
[0m[0;31m█████████[0m[0;37m█████████[0m[0;34m█████████
[0m[0;31m█████████[0m[0;37m█████████[0m[0;34m█████████
[0m[0;31m█████████[0m[0;37m█████████[0m[0;34m█████████
[0m[0;31m█████████[0m[0;37m█████████[0m[0;34m█████████
[0m[0;31m█████████[0m[0;37m█████████[0m[0;34m█████████
[0m[0;31m█████████[0m[0;37m█████████[0m[0;34m█████████
[0m[0;31m█████████[0m[0;37m█████████[0m[0;34m█████████
[0m[0;31m█████████[0m[0;37m█████████[0m[0;34m█████████
"""]
    await ctx.send(f"""{codeblock}ansi{random.choice(flags)}{codeblock}""")

@Euphoria.command(aliases=["reply"]) #autoreply
async def autoreply(ctx, *, message=None):
    global module
    global module_value
    global module_value2    
    server_id = ctx.guild.id
    if message == None:
        if module != "autoreply":
            errorsay(f"{ctx.command.name}: message is missing")
            if consolemode == "false":
                await ctx.send(f"{codeblock}{cb_error}[E] Usage: {prefix}{ctx.command.name} <message>{footer}{codeblock}", delete_after=deletetimer)
        else:
            module = None
            module_value = None
            module_value2 = None
            if consolemode == "false":
                await ctx.send(f"{codeblock}{cb_prefix}[E] Turned off autoreply{footer}{codeblock}", delete_after=deletetimer)
    else:
        module = "autoreply"
        module_value = server_id
        module_value2 = message
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_prefix}[E] Turned on autoreply{footer}{codeblock}", delete_after=deletetimer)
            


@Euphoria.command(aliases=["lyrics", "lyric"]) #sing
async def sing(ctx, *, song=None):
    def spellcheck(text):
        q = 0
        for letter in text:
            if letter == "\"":
                q += 1
        return q
    if song == None or spellcheck(song) != 4:
        errorsay(f"{ctx.command.name}: \"author name\" or \"song name\" is missing")
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_error}[E] Usage: {prefix}{ctx.command.name} \"<author name>\" \"<song name>\"{footer}{codeblock}", delete_after=deletetimer)
    else:
        author = ""
        songname = ""
        q = 0
        for letter in song:
            if letter == "\"":
                q += 1
            if q == 1:
                author += letter
            if q == 3:
                songname += letter
        songname = songname.replace("\"", "")
        author = author.replace("\"", "")
        r = requests.get(f"https://api.lyrics.ovh/v1/{author}/{songname}")
        try:
            lyrics_raw = json.loads(r.text)["lyrics"]
        except:
            await ctx.send(f"{codeblock}{cb_error}[E] This song isnt in the database{footer}{codeblock}")
        else:
            lyrics = ""
            maxlines = 0
            for letter in lyrics_raw:
                if letter != "\n":
                    lyrics += letter
                elif maxlines <= 4:
                    maxlines += 1
                    lyrics += letter
                else:
                    try:
                        await ctx.send(lyrics)
                        await asyncio.sleep(3)
                    except:
                        pass
                    lyrics = ""
                    maxlines = 0
            if lyrics != "":
                await ctx.send(lyrics)
            successsay("Finished singing the song")
    #https://api.lyrics.ovh/v1/jmeno+autora/jmeno+pisnicky
    

@Euphoria.command(aliases=["chong"]) #china
async def china(ctx, *, text=None):
    if text == None:
        errorsay(f"{ctx.command.name}: text is missing")
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_error}[E] Usage: {prefix}{ctx.command.name} <text>{footer}{codeblock}", delete_after=deletetimer)
    else:
        try:
            await ctx.send(china_text(text))
        except:
            await ctx.send(text)

@Euphoria.command(aliases=["unchong"]) #unchina
async def unchina(ctx,*, text=None):
    if text == None:
        errorsay(f"{ctx.command.name}: text is missing")
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_error}[E] Usage: {prefix}{ctx.command.name} <text>{footer}{codeblock}", delete_after=deletetimer)
    else:
        try:
            await ctx.send(unchina_text(text))
        except:
            await ctx.send(text)

@Euphoria.command() #say
async def say(ctx, *, text):
    await ctx.send(empty_char2+text)

@Euphoria.command(aliases=["chatmode", "chat"]) #customchat
async def customchat(ctx, mode=None):
    global customchat
    if mode == None:
        if customchat == "":
            errorsay(f"{ctx.command.name}: text is missing")
            if consolemode == "false":
                await ctx.send(f"""{codeblock}{cb_prefix}[E] Custom Chat modes:\n
Mode  -  Command  -  Application
1337 - {prefix}1337 - {prefix}customchat 1337
embed - {prefix}embed - {prefix}customchat embed
owoify - {prefix}owoify - {prefix}customchat owoify
zalgo - {prefix}zalgo - {prefix}customchat zalgo
emojify - {prefix}emojify - {prefix}customchat emojify
regional - {prefix}regional - {prefix}customchat regional
color - / - {prefix}customchat color
edit - / - {prefix}customchat edit
off - / - {prefix}customchat off or {prefix}customchat{footer}{codeblock}""", delete_after=deletetimer)
        else:
            await ctx.send(f"{codeblock}{cb_prefix}[E] Turned off customchat{footer}{codeblock}", delete_after=deletetimer)
            customchat = ""
    else:
        allowed_modes = ["1337", "embed", "owoify", "zalgo", "emojify", "regional", "edit", "color"]
        success = True
        if mode == "modes":
            await ctx.send(f"""{codeblock}{cb_prefix}[E] Custom Chat modes:\n
Mode  -  Command  -  Application
1337 - {prefix}1337 - {prefix}customchat 1337
embed - {prefix}embed - {prefix}customchat embed
owoify - {prefix}owoify - {prefix}customchat owoify
zalgo - {prefix}zalgo - {prefix}customchat zalgo
emojify - {prefix}emojify - {prefix}customchat emojify
regional - {prefix}regional - {prefix}customchat regional
color - / - {prefix}customchat color
edit - / - {prefix}customchat edit
off - / - {prefix}customchat off or {prefix}customchat{footer}{codeblock}""", delete_after=deletetimer)
            success = False
        elif mode.lower() in allowed_modes:
            customchat = str(mode.lower())
        elif mode == "off":
            await ctx.send(f"{codeblock}{cb_prefix}[E] Turned off customchat{footer}{codeblock}", delete_after=deletetimer)
            customchat = ""
            success = None
        else:
            await ctx.send(f"{codeblock}{cb_error}[E] Usage: {prefix}{ctx.command.name} <mode>\n[i] Use '{prefix}customchat' to see all modes available{footer}{codeblock}", delete_after=deletetimer)
            success = False

        if success == True:
            await ctx.send(f"{codeblock}{cb_prefix}[E] Toggled on customchat using {mode}-mode{footer}{codeblock}", delete_after=deletetimer)

@Euphoria.command(aliases=["encrypt"]) #encode
async def encode(ctx, mode=None, *, text=None):
    if text == None or mode == None:
        errorsay(f"{ctx.command.name}: text is missing")
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_error}[E] Usage: {prefix}{ctx.command.name} <base64/sha256/sha512> <text>{footer}{codeblock}", delete_after=deletetimer)
    else:
        if mode.lower() == "base64":
            string_bytes = text.encode('ascii')
            base64_bytes = base64.b64encode(string_bytes)
            output = base64_bytes.decode('ascii')
            await ctx.send(f"{codeblock}{cb_prefix}[E] Encoded string:\n{output}{footer}{codeblock}")
        elif mode.lower() == "sha256":
            output = \
                hashlib.sha256(text.encode()).hexdigest()
            await ctx.send(f"{codeblock}{cb_prefix}[E] Encrypted string:\n{output}{footer}{codeblock}")
        elif mode.lower() == "sha512":
            output = \
                hashlib.sha512(text.encode()).hexdigest()
            await ctx.send(f"{codeblock}{cb_prefix}[E] Encrypted string:\n{output}{footer}{codeblock}")
        else:
            await ctx.send(f"{codeblock}{cb_error}[E] Invalid encryption type\nYou can choose from: Sha256, Sha512 or Base64{footer}{codeblock}",detele_after=deletetimer)

@Euphoria.command(aliases=["decrypt"]) #decode
async def decode(ctx, *, text=None):
    if text == None:
        errorsay(f"{ctx.command.name}: text is missing")
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_error}[E] Usage: {prefix}{ctx.command.name} <text>{footer}{codeblock}", delete_after=deletetimer)
    else:
        output = base64.b64decode(text)
        await ctx.send(f"{codeblock}{cb_prefix}[E] Decoded text:\n{output}{footer}{codeblock}")

@Euphoria.command(aliases=["uwu", "owo"]) #owoify
async def owoify(ctx, *, text=None):
    if text == None:
        errorsay(f"{ctx.command.name}: text is missing")
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_error}[E] Usage: {prefix}{ctx.command.name} <text>{footer}{codeblock}", delete_after=deletetimer)
    else:
        output = owoify_text(text)
        await ctx.send(output)

@Euphoria.command() #zalgo
async def zalgo(ctx, *, text=None):
    if text == None:
        errorsay(f"{ctx.command.name}: text is missing")
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_error}[E] Usage: {prefix}{ctx.command.name} <text>{footer}{codeblock}", delete_after=deletetimer)
    else:
        output_len = 0
        output = zalgo_text(text)
        for letter in output:
            output_len += 1

        if output_len > 2000:
            open("settings/assets/output.txt", "w").write(output)
            await ctx.send(f"{codeblock}{cb_error}[E] Output was over 2000 characters long!{footer}{codeblock}", file=discord.File(r"settings\assets\output.txt"))
            os.remove("settings/assets/output.txt")
            warnsay(f"{ctx.command.name}: output too long! sending txt file")
        else:
            await ctx.send(output)

@Euphoria.command() #emojify
async def emojify(ctx, *, text=None):
    if text == None:
        errorsay(f"{ctx.command.name}: text is missing")
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_error}[E] Usage: {prefix}{ctx.command.name} <text>{footer}{codeblock}", delete_after=deletetimer)
    else:
        output_len = 0
        output = emojify_text(text)
        for letter in output:
            output_len += 1
        try:
            await ctx.send(output)
        except:
            open("settings/assets/output.txt", "w").write(output)
            await ctx.send(f"{codeblock}{cb_error}[E] Output was over 2000 characters long!{footer}{codeblock}", file=discord.File(r"settings\assets\output.txt"))
            os.remove("settings/assets/output.txt")
            warnsay(f"{ctx.command.name}: output too long! sending txt file")

@Euphoria.command(aliases=["1337"]) #1337
async def leet(ctx, *, text=None):
    if text == None:
        errorsay(f"{ctx.command.name}: text is missing")
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_error}[E] Usage: {prefix}{ctx.command.name} <text>{footer}{codeblock}", delete_after=deletetimer)
    else:
        output = leet_text(text)
        await ctx.send(output)

@Euphoria.command(aliases=["emojitext"]) #regional
async def regional(ctx, *, text=None):
    if text == None:
        errorsay(f"{ctx.command.name}: text is missing")
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_error}[E] Usage: {prefix}{ctx.command.name} <text>{footer}{codeblock}", delete_after=deletetimer)
    else:
        await ctx.send(regional_text(text))

@Euphoria.command() #nitro
async def nitro(ctx):
    code = "https://discord.gift/" + "".join(random.choice(string.ascii_letters) for i in range(16))
    await ctx.send(code)

@Euphoria.command() #embedcolor
async def embedcolor(ctx, hexcolor):
    config_edit(None, None, None, None, hexcolor, None, None)
    await ctx.send(f"{codeblock}{cb_prefix}[E] Embed color was set to #{hexcolor}{footer}{codeblock}")

@Euphoria.command() #embed 
async def embed(ctx, *, text=None):
    if text == None:
        errorsay(f"{ctx.command.name}: text is missing")
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_error}[E] Usage: {prefix}{ctx.command.name} <text>{footer}{codeblock}", delete_after=deletetimer)
    else:
        await ctx.send(text_hide+embed_text(text))
             

@Euphoria.command(aliases=["spoiler"]) #spoil
async def spoil(ctx, *, text=None):
    if text == None:
        errorsay(f"{ctx.command.name}: text is missing")
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_error}[E] Usage: {prefix}{ctx.command.name} <text>{footer}{codeblock}", delete_after=deletetimer)
    else:
        output = ""
        for letter in text:
            output += f"||{letter}||"
        output_len = 0
        for letter in output:
            output_len += 1
        if output_len > 2000:
            open("settings/assets/output.txt", "w").write(output)
            await ctx.send(f"{codeblock}{cb_error}[E] Output was over 2000 characters long!{footer}{codeblock}", file=discord.File(r"settings\assets\output.txt"))
            os.remove("settings/assets/output.txt")
            warnsay(f"{ctx.command.name}: output too long! sending txt file")
        else:
            await ctx.send(output)

@Euphoria.command() #ascii
async def ascii(ctx, *, text=None):
    if text == None:
        errorsay(f"{ctx.command.name}: text is missing")
        await ctx.send(f"""{codeblock}⠀⠀⠀⠀⠀⠀⢠⣤⣴⣶⣿⣿⣿⣿⣿⣶⣤⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡧⠀⠀⠀⡀⠀
⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⣿⠀
⠀⢰⣾⣿⣿⣿⣿⣿⡿⠋⠁⠀⠀⠀⠀⠈⠉⠀⠀⢀⣾⣿⡇
⢀⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣴⣿⣿⣿⡇
⢸⣿⣿⣿⣿⣿⣧⣤⣤⣤⣤⣤⣤⣶⣶⣾⣿⣿⣿⣿⣿⣿⠃
⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁  Usage: {prefix}ascii <text>
⠸⣿⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠋⠁⠀⠀⠀ 
⠀⢟⣾⣻⣞⡿⣯⣏⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⡀⠀⠀⠀
⠀⠈⣳⣻⣼⣻⡽⣯⢷⣦⣄⣀⣀⣀⣀⣠⣤⣶⣿⣿⣦⡀⠀
⠀⠀⠀⠑⢯⡷⣻⣭⣟⡾⣽⣻⣟⡿⣿⣿⣿⣿⣿⣿⣿⣿⡄
⠀⠀⠀⠀⠀⠉⢷⡿⣾⣹⢷⣷⣾⣹⢷⡿⣾⢿⣹⣿⠿⠉⠀
⠀⠀⠀⠀⠀⠀⠀⠉⠁⠋⠻⠶⠏⠷⠯⠟⠝⠛⠁⠁⠀⠀⠀{codeblock}""",delete_after=deletetimer)
    else:
        output = pyfiglet.figlet_format(text)
        output_len = 0
        for letter in output:
            output_len += 1
        if output_len > 2000:
            open("settings/assets/output.txt", "w").write(output)
            await ctx.send(f"{codeblock}{cb_error}[E] Output was over 2000 characters long!{footer}{codeblock}", file=discord.File(r"settings\assets\output.txt"))
            os.remove("settings/assets/output.txt")
            warnsay(f"{ctx.command.name}: output too long! sending txt file")
        else:
            await ctx.send(codeblock+output+codeblock)


#MISC-------------------------------------------------------------

@Euphoria.command(aliases=["q", "que", "2b", "2bq", "2bqueue"]) #queue
async def queue(ctx):
    r = json.loads(requests.get("https://2bqueue.info/queue").text)
    prio = r["prio"]
    regular = r["regular"]
    await ctx.send(f"{codeblock}{cb_prefix}[E] 2b2t's current queue:\nPriority: {prio}\nRegular: {regular}{footer}{codeblock}", delete_after=deletetimer)

@Euphoria.command(name="bots", aliases=["bot"]) #bots
async def bots(ctx):
    await ctx.message.delete()
    bot = discum.Client(token=token, log=False, user_agent=get_random_user_agent())
    def close_after_fetching(resp, guild_id):          
        if bot.gateway.finishedMemberFetching(guild_id):
            members = bot.gateway.session.guild(guild_id).members
            bot.gateway.removeCommand({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
            bot.gateway.close()
            return members

    def get_members(guild_id, channel_id):
        bot.gateway.fetchMembers(guild_id, channel_id, keep="all", wait=0)
        bot.gateway.command({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
        bot.gateway.run()
        bot.gateway.resetSession()
        return bot.gateway.session.guild(guild_id).members

    members = get_members(str(ctx.guild.id), str(ctx.channel.id))
    botcount = 0
    botlist = ""
    for member_id in members:
        member = await Euphoria.fetch_user(int(member_id))
        if member.bot:
            botcount += 1
            botlist += f"\n{member}"
    
    if botcount != 0:
        await ctx.send(f"{codeblock}{cb_prefix}[E] Found [{botcount}] bots\n{botlist}{footer}{codeblock}", delete_after=deletetimer)
    else:
        await ctx.send(f"{codeblock}{cb_prefix}[E] There aren't any bots here!{footer}{codeblock}", delete_after=deletetimer)

@Euphoria.command(name="invite", aliases=["inv"]) #invite
async def feafguzrewhg(ctx, target: discord.User=None):
    if target == None:
        errorsay(f"{ctx.command.name}: target is missing")
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_error}[E] Usage: {prefix}{ctx.command.name} <@target>{footer}{codeblock}", delete_after=deletetimer)
    else:
        target = target
        if target.bot:
            await ctx.send(f"https://discord.com/oauth2/authorize?permissions=8&scope=bot+applications.commands&client_id={target.id}")
        else:
            await ctx.send(f"{codeblock}{cb_error}[E] That the user is bot at games doesnt mean he/she's a discord bot dum{empty_char2}ba{empty_char2}ss{footer}{codeblock}",delete_after=deletetimer)


@Euphoria.command(aliases=["loadserver", "loadguild", "guildload"]) #serverload
async def serverload(ctx, save=None):
    def getsaves():
        output = []
        for file in os.listdir("settings/scrape/server"):
            output.append(file)
        return output

    if save == None:
        errorsay(f"{ctx.command.name}: save_id is missing")
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_error}[E] Usage: {prefix}{ctx.command.name} <save id>\n[i] Use '{prefix}serverload list' to see available presets{footer}{codeblock}", delete_after=deletetimer)
    else:
        if save == "list":
            guild_list = ""
            for file in os.listdir("settings/scrape/server"):
                guild_list += f"\n{file}"
        
            await ctx.send(f"{codeblock}{cb_prefix}[E] Server presets:{guild_list}{footer}{codeblock}", delete_after=deletetimer)
        elif save in getsaves():
            for channel in list(ctx.guild.channels):
                await channel.delete()
            
            folder = f"settings/scrape/server/{save}"
            
            #Text Channels
           
            for file in os.listdir(folder):
                if file.endswith(".txt"):
                    perms = json.loads(open(folder+"/"+file).read())
                    view_channel = perms["view_channel"]
                    manage_permissions = perms["manage_permissions"]
                    manage_webhooks = perms["manage_webhooks"]
                    send_messages = perms["send_messages"]
                    embed_links = perms["embed_links"]
                    attach_files = perms["attach_files"]
                    manage_messages = perms["manage_messages"]
                    read_message_history = perms["read_message_history"]
                    add_reactions = perms["add_reactions"]
                    use_external_emojis = perms["use_external_emojis"]
                    mention_everyone = perms["mention_everyone"]
                    send_tts_messages = perms["send_tts_messages"]

                    channelname = file.replace(".txt", "")

                    channel = await ctx.guild.create_text_channel(name=channelname)
                    await channel.set_permissions(ctx.guild.default_role, use_external_emojis=use_external_emojis, add_reactions=add_reactions, view_channel=view_channel, manage_permissions=manage_permissions, manage_webhooks=manage_webhooks, send_messages=send_messages, embed_links=embed_links, attach_files=attach_files, manage_messages=manage_messages,read_message_history=read_message_history, mention_everyone=mention_everyone, send_tts_messages=send_tts_messages)
                
                #Voice Channels
            for file in os.listdir(folder):
                if file.endswith(".vc"):
                    perms = json.loads(open(folder+"/"+file).read())
                    view_channel = perms["view_channel"]
                    manage_permissions = perms["manage_permissions"]
                    connect = perms["connect"]
                    speak = perms["speak"]
                    mute_members = perms["mute_members"]
                    move_members = perms["move_members"]

                    channelname = file.replace(".vc", "")
                    channel = await ctx.guild.create_voice_channel(name=channelname)
    
                    await channel.set_permissions(ctx.guild.default_role, view_channel=view_channel, manage_permissions=manage_permissions, connect=connect, speak=speak, move_members=move_members, mute_members=mute_members)

                #Categories
            for file in os.listdir(folder):
                if file.endswith(".ctg"):
                    channelname = file.replace(".ctg", "")
                    await ctx.guild.create_category(name=channelname)

                #Roles
            for file in os.listdir(folder):
                if file.endswith(".rl"):
                    desc = json.loads(open(folder+"/"+file).read())
                    color = desc["color"]
                    
                    rolename = file.replace(".rl", "")
                    await ctx.guild.create_role(name=rolename)
        
                #Server Properties
                if file.endswith(".gld"):
                    desc = json.loads(open(folder+"/"+file).read())
                    server_name = desc["name"]
                    icon = desc["icon"]
                    if icon != "":
                        r_icon = requests.get(icon).content
                    await ctx.guild.edit(name=server_name, icon=r_icon)
            #Emojis
            for file in os.listdir(f"{folder}/emojis"):
                with open(folder+"/emojis/"+file, "rb") as img:
                    img_bytes = img.read()
                    emojiname = file.replace(".png", "")
                    emojiname = file.replace(".gif", "")
                    await ctx.guild.create_custom_emoji(name = (emojiname), image = img_bytes)
            toast("Server copied")
        else:
            guild_list = ""
            for file in os.listdir("settings/scrape/server"):
                guild_list += f"\n{file}"
        
            await ctx.send(f"{codeblock}{cb_prefix}[E] Save not found\n[i] Server presets:{guild_list}{footer}{codeblock}", delete_after=deletetimer)


@Euphoria.command(aliases=["copyserver", "saveserver", "saveguild", "guildsave", "servercopy", "copyguild", "guildcopy"]) #serversave
async def serversave(ctx):
    foldername = f"{ctx.guild.id}" + "".join(random.choice(string.ascii_lowercase) for i in range(5))
    folderpath = f"settings/scrape/server/{foldername}"
    try:
        os.mkdir(folderpath)
    except:
        pass
    #SERVER PROPERTIES
    try:
        guild_icon = str(ctx.guild.icon_url)
    except:
        guild_icon = None
    guild_properties  = {
        "name": ctx.guild.name,
        "icon": guild_icon
    }
    open(f"{folderpath}/properties.gld", "w").write(json.dumps(guild_properties))

    #EMOJIS
    os.mkdir(f"{folderpath}/emojis")
    for emoji in list(ctx.guild.emojis):
        if emoji.animated:
            downloadem(f"https://cdn.discordapp.com/emojis/{emoji.id}.gif", emoji.name, path=f"{folderpath}/emojis")
        else:
            downloadem(f"https://cdn.discordapp.com/emojis/{emoji.id}.png", emoji.name, path=f"{folderpath}/emojis")

    #ROLES
    for role in list(ctx.guild.roles):
        if str(role.name) != "@everyone":
            open(f"{folderpath}/{role.name}.rl", "w").write(json.dumps({"color": f"{role.color}"}))

    #CHANNELS
    for channel in list(ctx.guild.channels):
        if str(channel.type) == "text":
            view_channel = None
            manage_permissions = False
            manage_webhooks = False
            send_messages = False
            embed_links = None
            attach_files = None
            add_reactions = None
            manage_messages = False
            read_message_history = False
            use_external_emojis = None
            mention_everyone = False
            send_tts_messages = None
            overwrite = channel.overwrites_for(ctx.guild.default_role)
            if overwrite.view_channel:
                view_channel = True
            if overwrite.manage_permissions:
                manage_permissions = True
            if overwrite.manage_webhooks:
                manage_webhooks = True
            if overwrite.send_messages:
                send_messages = True
            if overwrite.embed_links:
                embed_links = True
            if overwrite.attach_files:
                attach_files = True
            if overwrite.add_reactions:
                add_reactions = True
            if overwrite.manage_messages:
                manage_messages = True
            if overwrite.read_message_history:
                read_message_history = True
            if overwrite.use_external_emojis:
                use_external_emojis = True
            if overwrite.mention_everyone:
                mention_everyone = True
            if overwrite.send_tts_messages:
                send_tts_messages = True
            
            perms = {
                "view_channel": view_channel,
                "manage_permissions": manage_permissions,
                "manage_webhooks": manage_webhooks,
                "send_messages": send_messages,
                "embed_links": embed_links,
                "attach_files": attach_files,
                "add_reactions": add_reactions,
                "manage_messages": manage_messages,
                "read_message_history": read_message_history,
                "use_external_emojis": use_external_emojis,
                "mention_everyone": mention_everyone,
                "send_tts_messages": send_tts_messages
            }
            open(f"{folderpath}/{channel.name}.txt", "w", encoding="utf-8").write(json.dumps(perms))
            
        elif str(channel.type) == "voice":
            view_channel = None
            manage_permissions = None
            connect = None
            speak = None
            mute_members = None
            move_members = None

            overwrite = channel.overwrites_for(ctx.guild.default_role)
            if overwrite.view_channel:
                view_channel = True
            if overwrite.manage_permissions:
                manage_permissions = True
            if overwrite.connect:
                connect = True
            if overwrite.speak:
                speak = True
            if overwrite.mute_members:
                mute_members = True
            if overwrite.move_members:
                move_members = True
            
            perms = {
                "view_channel": view_channel,
                "manage_permissions": manage_permissions,
                "connect": connect,
                "speak": speak,
                "mute_members": mute_members,
                "move_members": move_members
            }
            open(f"{folderpath}/{channel.name}.vc", "w", encoding="utf-8").write(json.dumps(perms))
        elif str(channel.type) == "category":
            open(f"{folderpath}/{channel.name}.ctg", "w")
    await ctx.send(f"{codeblock}{cb_prefix}[E] Saved the server as '{foldername}'\n[i] You can load the preset using '{prefix}serverload {foldername}'{footer}{codeblock}", delete_after=deletetimer)

@Euphoria.command(aliases=["shlist", "slist"]) #sharelist
async def sharelist(ctx):
    output = ""
    for userid in open("settings/misc/sharelist.txt", "r").read().splitlines():
        try:
            user = await Euphoria.fetch_user(int(userid))
            output += f"\n{user.name}#{user.discriminator}"
        except:
            pass
    if output != "":
        await ctx.send(f"{codeblock}{cb_prefix}[E] Share list:{output}{footer}{codeblock}", delete_after=deletetimer)
    else:
        await ctx.send(f"{codeblock}{cb_error}[E] Wow such empty{footer}{codeblock}", delete_after=deletetimer)

@Euphoria.command(aliases=["sh", "commandshare"]) #share
async def share(ctx, user: discord.User=None):
    if user == None:
        errorsay(f"{ctx.command.name}: @user is missing")
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_error}[E] Usage: {prefix}{ctx.command.name} <@user>{footer}{codeblock}", delete_after=deletetimer)
    else:
        if user != Euphoria.user:
            share_user = str(user.id)
            share_list = open("settings/misc/sharelist.txt", "r").read()
            share_new = ""
            if share_user in share_list:
                for line in share_list.splitlines():
                    if line != share_user:
                        share_new += line+"\n"
                
                open("settings/misc/sharelist.txt", "w").write(share_new)
                await ctx.send(f"{codeblock}{cb_prefix}[E] Disabled command sharing for {user.name}{footer}{codeblock}", delete_after=deletetimer)
                log(f"INFO: Removed {user} from sharelist")
            else:
                open("settings/misc/sharelist.txt", "w").write(share_list+share_user+"\n")
                await ctx.send(f"{codeblock}{cb_prefix}[E] Enabled command sharing for {user.name}{footer}{codeblock}", delete_after=deletetimer)
                log(f"INFO: Added {user} to sharelist")
        else:
            await ctx.send(f"{codeblock}{cb_error}[E] You can't add yourself to command sharing{footer}{codeblock}", delete_after=deletetimer)

@Euphoria.command(aliases=["savechannel", "messagescrape", "scrapemessages", "channelsave"]) #chatsave
async def chatsave(ctx, channel_id: int=None):
    if channel_id == None:
        channel = ctx.channel
    else:
        channel = Euphoria.get_channel(channel_id)

    history = await channel.history(limit=2500).flatten()
    saved_messages = 0

    filename = f"{channel.name}-{channel.id}.txt"

    open(f"settings/scrape/chat/{filename}", "w", encoding="utf-8")

    for message in history:
        content = open(f"settings/scrape/chat/{filename}", "r", encoding="utf-8").read()
        open(f"settings/scrape/chat/{filename}", "w", encoding="utf-8").write(content+f"{message.author.name}#{message.author.discriminator}: {message.content}\n")
        saved_messages += 1

    if saved_messages > 0:
        path = os.path.abspath(f"{filename}")
        path = f"{path}\\{filename}"
        successsay(f"Saved {saved_messages} messages from #{channel.name} (path: {path})")
        await ctx.send(f"{codeblock}{cb_prefix}[E] Saved {saved_messages} messages from #{channel.name}!{footer}{codeblock}", delete_after=deletetimer)
    else:
        errorsay(f"No messages were found in #{channel.name}")
        await ctx.send(f"{codeblock}{cb_error}[E] No messages were found :^({footer}{codeblock}", delete_after=deletetimer)

    

@Euphoria.command(aliases=["stealav", "stealpfp", "avsteal", "pfpsteal"]) #stealavatar
async def stealavatar(ctx, user: discord.User):
    if user == None:
        errorsay(f"{ctx.command.name}: user is missing")
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_error}[E] Usage: {prefix}{ctx.command.name} <user>{footer}{codeblock}", delete_after=deletetimer)
    else:
        img = requests.get(user.avatar_url)
        if ".png" in str(user.avatar_url):
            filetype = "png"
        else:
            filetype = "gif"
        open(f"settings/scrape/avatar/{user.name}-{user.id}.{filetype}", "wb").write(img.content)
        
        path = os.path.abspath(f"{user.name}-{user.id}.{filetype}")
        path = f"{path}\\{user.name}-{user.id}.{filetype}"
        successsay(f"Saved {user}'s avatar (path: {path})")
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_prefix}[E] Saved {user.name}'s avatar{footer}{codeblock}")
        log(f"INFO: Saved profile picture from '{user}' (path: {path})")

@Euphoria.command(name="date") #date
async def AAAdate123(ctx):
    await ctx.send(f"<t:{gettime()}:F>")

@Euphoria.command(name="timer") #timer
async def AAAtimer123(ctx, count: int=0):
    await ctx.send(f"<t:{gettime()+count}:R>")

@Euphoria.command(aliases=["staffscan"]) #staffcheck
async def staffcheck(ctx, confirm=""):
    await ctx.message.delete()
    if confirm.lower() != "confirm":
        await ctx.send(f"{codeblock}{cb_prefix}[E] Are you sure? this action will take a long time! use '{prefix}staffcheck confirm' to continue{footer}{codeblock}", delete_after=deletetimer)
        return
    bot = discum.Client(token=token, log=False, user_agent=get_random_user_agent())
    # badges = user.public_flags.all()
    # badges = str(badges)
    # if "UserFlags.hypesquad" in badges:
    #     hypesquad = True
    # else:
    #     hypesquad = False
    # if "<UserFlags.staff: 1>" in badges:
    #     staff = True
    # else:
    try:
        totalstaff = 0
        staffguilds = ""
        guilds = 0
        toast("Please wait... this action takes a long time!")
        for guild in list(Euphoria.guilds):
            guildstaff = 0
            successsay(f"Scanning {guild.name}")

            def close_after_fetching(resp, guild_id):          
                if bot.gateway.finishedMemberFetching(guild_id):
                    members = bot.gateway.session.guild(guild_id).members
                    bot.gateway.removeCommand({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
                    bot.gateway.close()
                    return members

            def get_members(guild_id, channel_id):
                bot.gateway.fetchMembers(guild_id, channel_id, keep="all", wait=0)
                bot.gateway.command({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
                bot.gateway.run()
                bot.gateway.resetSession()
                return bot.gateway.session.guild(guild_id).members

            members = get_members(str(guild.id), str(random.choice(guild.channels)))

            for member in members:
                user = await Euphoria.fetch_user(int(member))
                badges = user.public_flags.all()
                badges = str(badges)
                if "<UserFlags.staff: 1>" in badges:
                    guildstaff += 1
                    totalstaff += 1

            if guildstaff != 0:
                warnsay(f"Staff Detection: staff member found in {guild.name}")
                staffguilds += f"{guild.name}\n"
            guilds += 1
        successsay(f"Found {totalstaff} in {guilds}")
        if totalstaff == None:
            await ctx.send(f"{codeblock}{cb_prefix}[E] No discord staff found in your server list!{footer}{codeblock}")
    except Exception as error:
        await ctx.send(f"{codeblock}{cb_error}[E] An error occured while scanning the servers\n{error}{footer}{codeblock}")


@Euphoria.command(aliases=["re"]) #repeat
async def repeat(ctx):
    global latest_command
    if latest_command != None:
        await ctx.send(latest_command)
    else:
        await ctx.send(f"{codeblock}{cb_error}[E] Can't repeat any commands as you didnt use any!{footer}{codeblock}", delete_after=deletetimer)

@Euphoria.command(aliases=["stealemoji", "emojiscrape"]) #emojisteal
async def emojisteal(ctx, guild_id: int=None):
    if guild_id != None:
        guild = Euphoria.get_guild(guild_id)
    else:
        guild = ctx.guild.id
    emojis = guild.emojis
    emojicount = 0
    for emoji in emojis:
        if emoji.animated:
            emojicount += 1
            downloadem(f"https://cdn.discordapp.com/emojis/{emoji.id}.gif", emoji.name+"-"+str(guild.id))
        else:
            emojicount += 1
            downloadem(f"https://cdn.discordapp.com/emojis/{emoji.id}.png", emoji.name+"-"+str(guild.id))
    await ctx.send(f"{codeblock}{cb_prefix}[E] Scraped {emojicount} emojis from {guild.name}{footer}{codeblock}", delete_after=deletetimer)

@Euphoria.command(aliases=["install"]) #download
async def download(ctx, filetype=None, url=None):
    if url == None or filetype == None:
        errorsay(f"{ctx.command.name}: url or filetype is missing")
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_error}[E] Usage: {prefix}{ctx.command.name} <url>{footer}{codeblock}", delete_after=deletetimer)
    else:
        r = requests.get(url, allow_redirects=True)
        randomvalue = "".join(random.choice(string.ascii_lowercase) for i in range(5))
        open(f'{randomvalue}.{filetype}', 'wb').write(r.content)
        await ctx.send(f"{codeblock}{cb_prefix}[E] Downloaded the file as {randomvalue}.{filetype}{footer}{codeblock}")


@Euphoria.command(aliases=["serveravatar", "serverlogo", "sav"]) #serveravatar
async def servericon(ctx):
    try:
        await ctx.send(ctx.guild.icon_url)
    except:
        errorsay(f"{ctx.guild.name} doesnt have any server icon")
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_error}[E] This server doesnt have any server icon{footer}{codeblock}", delete_after=deletetimer)
        

@Euphoria.command(aliases=["scrapechannels"]) #channelscrape
async def channelscrape(ctx, open_file=None):
    def cs_scrape(guild_id):
        try:
            guild = Euphoria.get_guild(int(guild_id))
            output = ""
            raw = ""
            for channel in list(guild.channels):
                output += f"\n{channel.name}: {channel.id}"
                raw += f"\n{channel.id}"
            return json.dumps({"output": output, "raw": raw})
        except Exception as error:
            return f"An error occured: {error}"
    try:
        if open_file != "open":
            scraped_channels = json.loads(cs_scrape(ctx.guild.id))["output"]
            scraped_ids = json.loads(cs_scrape(ctx.guild.id))["raw"]
            await ctx.send(f"{codeblock}{cb_prefix}[E] Scraped channels:{scraped_channels}\n\n[i] Use '{prefix}channelscrape open' to open the file{footer}{codeblock}", delete_after=deletetimer)
            open("settings/assets/channelscrape.txt", "w").write("Output:" + scraped_channels + "\n\n\nRaw:" + scraped_ids)
        else:
            try:
                open("settings/assets/channelscrape.txt")
            except:
                scraped_channels = json.loads(cs_scrape(ctx.guild.id))["output"]
                scraped_ids = json.loads(cs_scrape(ctx.guild.id))["raw"]
                open("settings/assets/channelscrape.txt", "w").write("Output:" + scraped_channels + "\n\n\nRaw:" + scraped_ids)
                os.system("start settings/assets/channelscrape.txt")
            else:
                os.system("start settings/assets/channelscrape.txt")
    except Exception as error:
        await ctx.send(f"{codeblock}{cb_error}[E] Something went wrong:\n{error}{footer}{codeblock}", delete_after=deletetimer)

@Euphoria.command() #image
async def image(ctx):
    messages = ["Searching", "Trying to find the right image", "Sending copious amounts of requests", "Scanning ctrlv.cz"]
    milestones = [10,20,30,40,50,60,70,80,90,100]
    msg = await ctx.send(f"{codeblock}{cb_prefix}[E] {random.choice(messages)} {footer}{codeblock}")
    retries = 0
    while True:
        link = f"https://ctrlv.cz/"+"".join(random.choice(string.ascii_letters) for i in range(4))

        if retries in milestones:
            await msg.edit(content=f"{codeblock}{cb_prefix}[E] {random.choice(messages)} {footer}{codeblock}")

        r = requests.get(f"{link}")
        if "/images/notexists.png" not in r.text: 
            open("settings/assets/image.txt", "w").write(r.text)
            with open("settings/assets/image.txt", encoding="ansi") as f:
                urls = f.read()
                links = re.findall('"((http)s?://ctrlv.cz/shots.*?)"', urls)

            for url in links:
                download = requests.get(url[0])
                successsay(f"Found an image (URL: {url[0]})")
                open(f'settings/assets/image.png', 'wb').write(download.content)
            await ctx.send(file=discord.File(r"settings\assets\image.png"))
            os.remove("settings/assets/image.png")
            os.remove("settings/assets/image.txt")
            break
        retries += 1

    await asyncio.sleep(3)
    await msg.delete()

@Euphoria.command(aliases=["selfpurge"]) #purgeself
async def purgeself(ctx, amount: int=1):    
    amount += 1
    history = await ctx.channel.history(limit=amount).flatten()
    deletedamount = 0
    for message in history:
        if message.author.id == Euphoria.user.id:
            try:
                deletedamount+=1
                await message.delete()
            except:
                pass
    await ctx.send(f"{codeblock}{cb_prefix}[E] Purged {deletedamount} messages{footer}{codeblock}", delete_after=deletetimer)

#ABUSE------------------------------------------------------------
 
@Euphoria.command(aliases=["hookspam", "wbspam", "spamwebhook", "webhookspammer", "wbspammer", "hookspammer"]) #webhookspam
async def webhookspam(ctx, amount: int=None, url=None, *,message=None):
    if url == None or message == None or amount == None or "https://discord.com/api/webhooks/" not in url:
        errorsay(f"{ctx.command.name}: url, amount or message is missing")
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_error}[E] Usage: {prefix}{ctx.command.name} <amount> <url> <message>{footer}{codeblock}", delete_after=deletetimer)
    else:
        def sendrequest():
            r = requests.post(url, json={"content": message})
            if "204" not in str(r):
                errorsay("Failed to post webhook message")
        for i in range(amount):
            threading.Thread(target=sendrequest).start()


@Euphoria.command(aliases=["vcboot", "vcdos", "ddosvc", "bootvc", "dosvc"]) #vcddos
async def vcddos(ctx, duration: int=None):
    if duration == None:
        errorsay(f"{ctx.command.name}: duration is missing")
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_error}[E] Usage: {prefix}{ctx.command.name} <duration(s) max: 300s>{footer}{codeblock}", delete_after=deletetimer)
    else:
        channel = ctx.author.voice.channel
        amount = int(duration/2)
        current_region = random.choice(vc_regions)
        await ctx.send(f"{codeblock}{cb_prefix}[E] Booting the voice chat{footer}{codeblock}", delete_after=deletetimer)
        for i in range(amount):
            while True:
                new_region = random.choice(vc_regions)
                if new_region != current_region:
                    current_region = new_region
                    break
            await channel.edit(rtc_region=current_region)
            await asyncio.sleep(2)

@Euphoria.command(aliases=["spamvc"]) #vcspam
async def vcspam(ctx, amount: int=None):
    if amount == None:
        errorsay(f"{ctx.command.name}: amount is missing")
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_error}[E] Usage: {prefix}{ctx.command.name} <amount>{footer}{codeblock}", delete_after=deletetimer)
    else:
        channel = ctx.author.voice.channel
        for i in range(amount):
            await asyncio.sleep(2)
            await channel.connect()
            await asyncio.sleep(2)
            await ctx.voice_client.disconnect()
        await ctx.send(f"{codeblock}{cb_prefix}[E] Successfully joined & leaved {amount} times{footer}{codeblock}", delete_after=deletetimer)

@Euphoria.command() #spoof
async def spoof(ctx):
    member = Euphoria.user
    await member.edit(nick="ㅤ"*random.randint(4,8), password="undefined")

@Euphoria.command(aliases=["servernuke"]) #nuke
async def nuke(ctx, *, text=f"@everyone Euphoria on top! {text_hide}https://discord.gg/kjh9bEytUH"):
    await ctx.message.delete()
    infosay("Please wait...")
    bot = discum.Client(token=token, log=False, user_agent=get_random_user_agent())

    def close_after_fetching(resp, guild_id):          
        if bot.gateway.finishedMemberFetching(guild_id):
            members = bot.gateway.session.guild(guild_id).members
            bot.gateway.removeCommand({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
            bot.gateway.close()
            return members

    def get_members(guild_id, channel_id):
        bot.gateway.fetchMembers(guild_id, channel_id, keep="all", wait=0)
        bot.gateway.command({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
        bot.gateway.run()
        bot.gateway.resetSession()
        return bot.gateway.session.guild(guild_id).members

    members = get_members(str(ctx.guild.id), str(ctx.channel.id))
    try:

        role = discord.utils.get(ctx.guild.roles, name = "@everyone")
        await role.edit(permissions = discord.Permissions.all())
    except:
        errorsay("Can't give @everyone admin permissions")
    else:
        successsay("Gave @everyone admin permissions")
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
            successsay(f"Deleted #{channel.name}")
        except:
            errorsay(f"Can't delete #{channel.name}")

    for member in members:
        try:
            member = await ctx.guild.fetch_member(int(member))
            await member.ban(reason="")
            successsay(f"Banned {member.name}")
        except:
            errorsay(f"Can't ban {member.name}")
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
            successsay(f"Deleted {role}")
        except:
            errorsay(f"Can't delete {role}")
    for i in range(15):
        try:
            await ctx.guild.create_text_channel(f"Euphoria{channel_space}owns{channel_space}all")
        except:
            errorsay("Can't create text channel")
    for i in range(2):
        for channel in list(ctx.guild.channels):
            await channel.send(text)
            successsay("Message sent")

    toast("Nuked the server 🔥")

@Euphoria.command(aliases=["ghostlink", "ghosturl", "silenturl"]) #silentlink
async def silentlink(ctx, url=None, *, text=None):
    if text == None or url == None:
        errorsay(f"{ctx.command.name}: text is missing")
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_error}[E] Usage: {prefix}{ctx.command.name}<url> <text>{footer}{codeblock}", delete_after=deletetimer)
    else:
        if "https://" in url:
            await ctx.send(text+text_hide+url)
        else:
            await ctx.send(f"{codeblock}{cb_error}[E] Invalid url{footer}{codeblock}")

@Euphoria.command(aliases=["chatbypass"]) #modbypass
async def modbypass(ctx, *, text=None):
    await ctx.message.delete()
    if text == None:
        cmd_show()
        toast("Input the text into the console", True)
        text = input(f"{Fore.WHITE}{current_time()} {yellow}> {Fore.WHITE}Input: ")
    output = modbypass_text(text)
    if len(output) > 2000:
        warnsay(f"{ctx.command.name}: output too long")
    else:
        await ctx.send(output)

@Euphoria.command(aliases=["purgehack", "clearchat"]) #cchat
async def cchat(ctx):
    await ctx.send(f"{empty_char}\n"*1000)

@Euphoria.command(aliases=["reaction"]) #react
async def react(ctx, channel_id=None):
    global module
    global module_value
    global module_value2
    if channel_id == None:
        if module != "react":
            if channel_id == None:
                channel_id = ctx.channel.id
            module = "react"
            module_value = channel_id
            await ctx.send(f"{codeblock}{cb_prefix}[E] Turned on react{footer}{codeblock}", delete_after=deletetimer)
        else:
            module = None
            module_value = None
            module_value2 = None
            await ctx.send(f"{codeblock}{cb_prefix}[E] Turned off react{footer}{codeblock}", delete_after=deletetimer)
    else:
        if channel_id == None:
            channel_id = ctx.channel.id
        module = "react"
        module_value = channel_id
        await ctx.send(f"{codeblock}{cb_prefix}[E] Turned on react for #{Euphoria.get_channel(int(channel_id)).name}{footer}{codeblock}")

@Euphoria.command(aliases=["massreaction"]) #massreact
async def massreact(ctx, channel_id=None):
    global module
    global module_value
    global module_value2
    if channel_id == None:
        if module != "massreact":
            if channel_id == None:
                channel_id = ctx.channel.id
            module = "massreact"
            module_value = channel_id
            await ctx.send(f"{codeblock}{cb_prefix}[E] Turned on massreact{footer}{codeblock}", delete_after=deletetimer)
        else:
            module = None
            module_value = None
            module_value2 = None
            await ctx.send(f"{codeblock}{cb_prefix}[E] Turned off massreact{footer}{codeblock}", delete_after=deletetimer)
    else:
        if channel_id == None:
            channel_id = ctx.channel.id
        module = "massreact"
        module_value = channel_id
        await ctx.send(f"{codeblock}{cb_prefix}[E] Turned on massreact for #{Euphoria.get_channel(int(channel_id)).name}{footer}{codeblock}")

@Euphoria.command() #massunban
@commands.guild_only()
@commands.has_permissions(administrator=True)
async def massunban(ctx):    
    banlist = await ctx.guild.bans()
    for users in banlist:
        try:
            await asyncio.sleep(0.5)
            await ctx.guild.unban(user=users.user)
        except:
            pass

@Euphoria.command() #massban
@commands.has_permissions(ban_members=True)
async def massban(ctx):
    await ctx.message.delete()
    bot = discum.Client(token=token, log=False, user_agent=get_random_user_agent())

    def close_after_fetching(resp, guild_id):          
        if bot.gateway.finishedMemberFetching(guild_id):
            members = bot.gateway.session.guild(guild_id).members
            bot.gateway.removeCommand({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
            bot.gateway.close()
            return members

    def get_members(guild_id, channel_id):
        bot.gateway.fetchMembers(guild_id, channel_id, keep="all", wait=0)
        bot.gateway.command({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
        bot.gateway.run()
        bot.gateway.resetSession()
        return bot.gateway.session.guild(guild_id).members

    members = get_members(str(ctx.guild.id), str(ctx.channel.id))
    kicked_members = 0
    for member in members:
        try:
            member = await ctx.guild.fetch_member(int(member))
            await member.ban(reason="")
        except:
            errorsay(f"Can't ban {member.name}")
        else:
            kicked_members += 1
    await ctx.send(f"{codeblock}{cb_prefix}[E] Banned {kicked_members} members{footer}{codeblock}", delete_after=deletetimer)

@Euphoria.command() #masskick
@commands.has_permissions(kick_members=True)
async def masskick(ctx):
    await ctx.message.delete()
    bot = discum.Client(token=token, log=False, user_agent=get_random_user_agent())

    def close_after_fetching(resp, guild_id):          
        if bot.gateway.finishedMemberFetching(guild_id):
            members = bot.gateway.session.guild(guild_id).members
            bot.gateway.removeCommand({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
            bot.gateway.close()
            return members

    def get_members(guild_id, channel_id):
        bot.gateway.fetchMembers(guild_id, channel_id, keep="all", wait=0)
        bot.gateway.command({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
        bot.gateway.run()
        bot.gateway.resetSession()
        return bot.gateway.session.guild(guild_id).members

    members = get_members(str(ctx.guild.id), str(ctx.channel.id))
    kicked_members = 0
    for member in members:
        try:
            member = await ctx.guild.fetch_member(int(member))
            await member.kick(reason="")
        except:
            errorsay(f"Can't kick {member.name}")
        else:
            kicked_members += 1
    await ctx.send(f"{codeblock}{cb_prefix}[E] Kicked {kicked_members} members{footer}{codeblock}", delete_after=deletetimer)

@Euphoria.command() #massping
async def massping(ctx, amount: int=1):
    await ctx.message.delete()
    bot = discum.Client(token=token, log=False, user_agent=get_random_user_agent())

    def close_after_fetching(resp, guild_id):          
        if bot.gateway.finishedMemberFetching(guild_id):
            #print(f" {Fore.RED}[{getCurrentTime()}] [INFO] {Fore.RESET}Fetching complete.")
            members = bot.gateway.session.guild(guild_id).members
            bot.gateway.removeCommand({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
            bot.gateway.close()
            return members

    def get_members(guild_id, channel_id):
        bot.gateway.fetchMembers(guild_id, channel_id, keep="all", wait=0)
        bot.gateway.command({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
        bot.gateway.run()
        bot.gateway.resetSession()
        return bot.gateway.session.guild(guild_id).members

    members = get_members(str(ctx.guild.id), str(ctx.channel.id))
    messages = []
    message = ""

    for member in members:
        if len(message) < 1950:
            message += f"<@{member}> "
        else:
            messages.append(message)
            message = ""

    messages.append(message)

    for _ in range(amount):
        for message in messages:
            try:
                await ctx.send(message)
                await asyncio.sleep(0.25)
            except:
                break

@Euphoria.command() #ghostping
async def ghostping(ctx, user: discord.User=None, amount: int=None):
    if user == None:
        errorsay(f"{ctx.command.name}: user-id is missing")
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_error}[E] Usage: {prefix}{ctx.command.name} <user id> [amount]{footer}{codeblock}", delete_after=deletetimer)
    else:
        if amount == None or amount < 2:
            await ctx.send(user.mention, delete_after=0.1)
        else:
            for i in range(amount):
                await ctx.send(user.mention, delete_after=0.1)
                await asyncio.sleep(0.25)

@Euphoria.command() #massghostping
async def massghostping(ctx, amount: int=1):
    await ctx.message.delete()
    bot = discum.Client(token=token, log=False, user_agent=get_random_user_agent())

    def close_after_fetching(resp, guild_id):          
        if bot.gateway.finishedMemberFetching(guild_id):
            #print(f" {Fore.RED}[{getCurrentTime()}] [INFO] {Fore.RESET}Fetching complete.")
            members = bot.gateway.session.guild(guild_id).members
            bot.gateway.removeCommand({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
            bot.gateway.close()
            return members

    def get_members(guild_id, channel_id):
        bot.gateway.fetchMembers(guild_id, channel_id, keep="all", wait=0)
        bot.gateway.command({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
        bot.gateway.run()
        bot.gateway.resetSession()
        return bot.gateway.session.guild(guild_id).members

    members = get_members(str(ctx.guild.id), str(ctx.channel.id))
    messages = []
    message = ""

    for member in members:
        if len(message) < 1950:
            message += f"<@{member}> "
        else:
            messages.append(message)
            message = ""

    messages.append(message)

    for _ in range(amount):
        for message in messages:
            try:
                msg = await ctx.send(message)
                await msg.delete()
                await asyncio.sleep(0.25)
            except:
                break

@Euphoria.command() #spam
async def spam(ctx, amount: int=None, *, text=None):
    if amount == None or text == None:
        errorsay(f"{ctx.command.name}: amount or text is missing")
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_error}[E] Usage: {prefix}{ctx.command.name} <amount> <text>{footer}{codeblock}", delete_after=deletetimer)
    else:
        for i in range(amount):
            await ctx.send(text)
            await asyncio.sleep(0.25)

@Euphoria.command(aliases=["ttsspam"]) #spamtts
async def spamtts(ctx, amount: int=None, *, text=None):
    if amount == None or text == None:
        errorsay(f"{ctx.command.name}: amount or text is missing")
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_error}[E] Usage: {prefix}{ctx.command.name} <amount> <text>{footer}{codeblock}", delete_after=deletetimer)
    else:
        for i in range(amount):
            await ctx.send(text, tts=True)
            await asyncio.sleep(0.25)

@Euphoria.command(aliases=["mspam", "masspam"]) #massspam
async def massspam(ctx, amount: int=None, *, text=None):
    if amount == None or text == None:
        errorsay(f"{ctx.command.name}: amount or text is missing")
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_error}[E] Usage: {prefix}{ctx.command.name} <amount> <text>{footer}{codeblock}", delete_after=deletetimer)
    else:
        for i in range(amount):
            for channel in list(ctx.guild.channels):
                try:
                    await channel.send(text)
                    await asyncio.sleep(0.2)
                except:
                    pass
        toast("Finished")

@Euphoria.command(aliases=["masschannels"]) #masschannel
@commands.guild_only()
@commands.has_permissions(manage_channels=True)
async def masschannel(ctx, amount: int=None,  *, name=None):
    if amount == None or name == None:
        errorsay(f"{ctx.command.name}: amount or name is missing")
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_error}[E] Usage: {prefix}{ctx.command.name} <amount> <name>{footer}{codeblock}", delete_after=deletetimer)
    else:
        for _i in range(amount):
            try:
                await ctx.guild.create_text_channel(name=name)
            except:
                errorsay("Can't create any channels")
                break
        toast("Finished")

@Euphoria.command(aliases=["channelnuke", "nukechannel"]) #nukechannels
@commands.guild_only()
@commands.has_permissions(manage_channels=True)
async def nukechannels(ctx):
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
        except:
            errorsay("Can't delete any channels")
            break
    toast("Finished")

#ADMIN------------------------------------------------------------

@Euphoria.command(aliases=["emojiadd"]) #addemoji
@commands.has_permissions(manage_emojis=True)
async def addemoji(ctx, emoji: discord.Emoji=None, *, emojiname=None):
    if emoji == None:
        errorsay(f"{ctx.command.name}: emoji is missing")
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_error}[E] Usage: {prefix}{ctx.command.name} <emoji> [name]{footer}{codeblock}", delete_after=deletetimer)
    else:
        emoji = emoji
        if emojiname == None:
            emojiname = emoji.name
        if emoji.animated:
            filetype = "gif"
        else:
            filetype = "png"
        r = json.loads(downloadem(f"https://cdn.discordapp.com/emojis/{emoji.id}.{filetype}", emojiname))
        with open(r["path"], "rb") as img:
            img_bytes = img.read()
            await ctx.guild.create_custom_emoji(name = (emojiname), image = img_bytes)
        os.remove(r["path"])
        log(f"INFO: added emoji ({emoji.name}) to {ctx.guild.name}")
        await ctx.send(f"{codeblock}{cb_prefix}[E] Added :{emojiname}: to the server{footer}{codeblock}", delete_after=deletetimer)
            

@Euphoria.command(aliases=["spacechannel"]) #channelspace
@commands.has_permissions(manage_channels=True)
async def channelspace(ctx, *, channelname=None):
    if channelname == None:
        errorsay(f"{ctx.command.name}: channel name is missing")
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_error}[E] Usage: {prefix}{ctx.command.name} <channel name>{footer}{codeblock}", delete_after=deletetimer)
    else:
        channelname_new = ""
        for letter in channelname:
            if letter == " ":
                channelname += channel_space
            else:
                channelname_new += letter
        await ctx.guild.create_text_channel(channelname_new)

@Euphoria.command() #purge
@commands.has_permissions(manage_messages=True)
async def purge(ctx, amount: int=None, user: discord.User=None):
    if user == None:
        errorsay(f"{ctx.command.name}: @user is missing")
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_error}[E] Usage: {prefix}{ctx.command.name} <@user>{footer}{codeblock}", delete_after=deletetimer)
    else:
        if user == None:
            await ctx.channel.purge(limit=amount)
            if consolemode == "false":
                await ctx.send(f"{codeblock}{cb_prefix}[E] {amount} messages were deleted{footer}{codeblock}", delete_after=deletetimer)
        else:
            amount += 1
            history = await ctx.channel.history(limit=amount).flatten()
            deletedamount = 0
            for message in history:
                if message.author.id == user.id:
                    try:
                        deletedamount+=1
                        await message.delete()
                    except:
                        pass
            await ctx.send(f"{codeblock}{cb_prefix}[E] Purged {deletedamount} messages{footer}{codeblock}", delete_after=deletetimer)
            toast(f"Purged {deletedamount} messages")

@Euphoria.command() #unlock
@commands.has_permissions(manage_channels=True)
async def unlock(ctx):
    overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = True
    await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.send(f"{codeblock}{cb_prefix}[E] 🔓 Channel was unlocked {footer}{codeblock}", delete_after=deletetimer)  

@Euphoria.command() #lock
@commands.has_permissions(manage_channels=True)
async def lock(ctx):
    overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = False
    await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.send(f"{codeblock}{cb_prefix}[E] 🔒 Channel was locked {footer}{codeblock}", delete_after=deletetimer)  

@Euphoria.command() #slowmode
@commands.has_permissions(manage_channels=True)
async def slowmode(ctx, delay: int=0):
    await ctx.channel.edit(slowmode_delay=delay)

@Euphoria.command() #unmute
@commands.has_permissions(manage_channels=True, manage_roles=True)
async def unmute(ctx, member: discord.Member=None):
    if member == None:
        errorsay(f"{ctx.command.name}: @user is missing")
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_error}[E] Usage: {prefix}{ctx.command.name} <@user>{footer}{codeblock}", delete_after=deletetimer)
    else:
        try:
            mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")
        except:
            await ctx.send(f"{codeblock}{cb_error}[E] Error: no muted role was found{footer}{codeblock}")
        else:
            await member.remove_roles(mutedRole)
            await member.send(f"{codeblock}{cb_prefix}[E] You were unmuted from {ctx.guild.name}{footer}{codeblock}")
            await ctx.send(f"{codeblock}{cb_prefix}[E] {member} was unmuted{footer}{codeblock}", delete_after=deletetimer)
            toast(f"{member} was unmuted")

@Euphoria.command() #mute
@commands.has_permissions(manage_channels=True, manage_roles=True)
async def mute(ctx, member: discord.Member=None, *, reason=None):
    if member == None:
        errorsay(f"{ctx.command.name}: @user is missing")
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_error}[E] Usage: {prefix}{ctx.command.name} <@user> [reason]{footer}{codeblock}", delete_after=deletetimer)
    else:
        try:
            mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")
        except:
            await ctx.send(f"{codeblock}{cb_error}[E] Error: no muted role was found{footer}{codeblock}")
        else:
            await member.add_roles(mutedRole)
            if reason == None:
                await member.send(f"{codeblock}{cb_error}[E] You were muted from {ctx.guild.name}{footer}{codeblock}")
            else:
                await member.send(f"{codeblock}{cb_error}[E] You were muted from {ctx.guild.name} for '{reason}'{footer}{codeblock}")
            await ctx.send(f"{codeblock}{cb_prefix}[E] {member} was muted{footer}{codeblock}", delete_after=deletetimer)
            toast(f"{member} was muted")

@Euphoria.command() #ban
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.User=None, *, reason="Unspecified"):
    if user == None:
        errorsay(f"{ctx.command.name}: @user is missing")
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_error}[E] Usage: {prefix}{ctx.command.name} <@user> [reason]{footer}{codeblock}", delete_after=deletetimer)
    else:
        try:
            await user.send(f"{codeblock}{cb_error}[E] You were banned in {ctx.guild.name} for '{reason}'{footer}{codeblock}")
        except:
            pass
        await user.ban(reason=reason)
        await ctx.send(f"{codeblock}{cb_prefix}[E] {user.name} was banned{footer}{codeblock}", delete_after=deletetimer)

@Euphoria.command() #kick
@commands.has_permissions(ban_members=True)
async def kick(ctx, user: discord.User=None, *, reason="Unspecified"):
    if user == None:
        errorsay(f"{ctx.command.name}: @user is missing")
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_error}[E] Usage: {prefix}{ctx.command.name} <@user> [reason]{footer}{codeblock}", delete_after=deletetimer)
    else:
        try:
            await user.send(f"{codeblock}{cb_error}[E] You were kicked from {ctx.guild.name} for '{reason}'{footer}{codeblock}")
        except:
            pass
        await user.kick(reason=reason)
        await ctx.send(f"{codeblock}{cb_prefix}[E] {user.name} was kicked{footer}{codeblock}", delete_after=deletetimer)

#SCRIPTS----------------------------------------------------------


@Euphoria.command(aliases=["script"]) #scripts
async def scripts(ctx, selection="", arg=None):
    global loaded_scripts
    if selection.lower() == "reload":
        for script in loaded_scripts:
            try:
                Euphoria.reload_extension(script)
            except:
                loaded_scripts.remove(script)
        successsay("Reloaded the scripts")
        log("INFO: Scripts reloaded")
        await ctx.send(f"{codeblock}{cb_prefix}[E] Scripts reloaded!{footer}{codeblock}", delete_after=deletetimer)
    elif selection.lower() == "list":
        #unloaded scripts
        o_unloaded_scripts = ""
        unloaded_amount = 0
        for file in os.listdir("scripts"):
            if str(file[:len(file)-3]) not in loaded_scripts:
                o_unloaded_scripts += f"\n{file[:len(file)-3]}"
                unloaded_amount += 1 
        #loaded scripts
        o_loaded_scripts = ""
        loaded_amount = 0
        for script in loaded_scripts:
            o_loaded_scripts += f"\n{script}"
            loaded_amount += 1
        #output
        infosay(f"Script list: {loaded_amount} loaded | {unloaded_amount} unloaded")
        if unloaded_amount == 0:
            await ctx.send(f"""{codeblock}{cb_prefix}[E] Script list:
[Total: {loaded_amount+unloaded_amount}] [Loaded: {loaded_amount}] [Unloaded: {unloaded_amount}]

[Loaded scripts]{o_loaded_scripts}{footer}{codeblock}""", delete_after=deletetimer)
        else:
            await ctx.send(f"""{codeblock}{cb_prefix}[E] Script list:
[Total: {loaded_amount+unloaded_amount}] [Loaded: {loaded_amount}] [Unloaded: {unloaded_amount}]

[Loaded scripts]{o_loaded_scripts}

[Unloaded scripts]{o_unloaded_scripts}{footer}{codeblock}""", delete_after=deletetimer)
    else:
        scriptlist = ""
        for script in loaded_scripts:
            scriptlist += f"\n{prefix}{script}"
        await ctx.send(f"""{codeblock}{cb_prefix}[ Scripts ]
{scriptlist}
 
[ Commands ]

{prefix}scripts list ─ shows all loaded & unloaded scripts
{prefix}scripts reload ─ reloads all of the scripts{footer}{codeblock}""", delete_after=deletetimer)
#{prefix}─

#RAIDING----------------------------------------------------------

@Euphoria.command(name="tokens") #tokens
async def tokenamount(ctx):
    token_amount = 0
    tokens = open("settings/tokens.txt", "r").read().splitlines()
    for token in tokens:
        token_amount += 1
    await ctx.send(f"{codeblock}{cb_prefix}[E] You have {token_amount} tokens{footer}{codeblock}", delete_after=deletetimer)

@Euphoria.command() #joinserver
async def joinserver(Euphoria, invite=None):
    if invite == None:
        errorsay(f"{Euphoria.command.name}: invite is missing")
        if consolemode == "false":
            await Euphoria.send(f"{codeblock}{cb_error}[E] Usage: {prefix}{Euphoria.command.name} <invite code>{footer}{codeblock}", delete_after=deletetimer)
    else:
        tokens = open("settings/tokens.txt", "r").read().splitlines()

        invite = invite.replace('https://discord.gg/', '')
        invite = invite.replace('discord.gg/', '')
        invite = invite.replace('https://discord.com/invite/', '')
        await Euphoria.message.delete()
        for _token_ in tokens:
            threading.Thread(target=_join_, args=(invite, _token_)).start()

@Euphoria.command(aliases=["mspamserver"]) #massspamserver
async def massspamserver(ctx, amount: int=None, guild_id: int=None,*, text=None):
    if amount == None or text == None or guild_id == None:
        errorsay(f"{ctx.command.name}: invite, amount, channel id or text is missing")
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_error}[E] Usage: {prefix}{ctx.command.name} <amount> <guild id> <text>{footer}{codeblock}", delete_after=deletetimer)
    else:
        try:
            guild = Euphoria.get_guild(guild_id)
            await ctx.message.delete()
            tokens = open("settings/tokens.txt", "r").read().splitlines()
            for _token_ in tokens:
                for channel in list(guild.channels):
                    threading.Thread(target=_spam_, args=(amount, channel.id, text, _token_)).start()

        except Exception as error:
            errorsay(error)

@Euphoria.command() #spamserver
async def spamserver(Euphoria, amountofmsgs=None, channel_id=None, *, text=None):
    if amountofmsgs == None or channel_id == None or text == None:
        errorsay(f"{Euphoria.command.name}: invite, amount, channel id or text is missing")
        if consolemode == "false":
            await Euphoria.send(f"{codeblock}{cb_error}[E] Usage: {prefix}{Euphoria.command.name} <amount> <channel id> <text>{footer}{codeblock}", delete_after=deletetimer)
    else:
        try:
            await Euphoria.message.delete()
            tokens = open("settings/tokens.txt", "r").read().splitlines()

            amountofmsgs = int(amountofmsgs)
            for _token_ in tokens:
                threading.Thread(target=_spam_, args=(amountofmsgs, channel_id, text, _token_)).start()
        except Exception as error:
            errorsay(error)

@Euphoria.command() #singraid
async def singraid(ctx, song=None):
    def spellcheck(text):
        q = 0
        for letter in text:
            if letter == "\"":
                q += 1
        return q
    if song == None or spellcheck(song) != 4:
        errorsay(f"{ctx.command.name}: \"author name\" or \"song name\" is missing")
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_error}[E] Usage: {prefix}{ctx.command.name} \"<author name>\" \"<song name>\"{footer}{codeblock}", delete_after=deletetimer)
    else:
        tokens = open("settings/tokens.txt")
        author = ""
        songname = ""
        q = 0
        for letter in song:
            if letter == "\"":
                q += 1
            if q == 1:
                author += letter
            if q == 3:
                songname += letter
        songname = songname.replace("\"", "")
        author = author.replace("\"", "")
        r = requests.get(f"https://api.lyrics.ovh/v1/{author}/{songname}")
        try:
            lyrics_raw = json.loads(r.text)["lyrics"]
        except:
            await ctx.send(f"{codeblock}{cb_error}[E] This song isnt in the database{footer}{codeblock}")
        else:
            lyrics = ""
            for letter in lyrics_raw:
                if letter != "\n":
                    lyrics += letter
                else:
                    try:
                        threading.Thread(target=_spam_, args=(1, ctx.channel.id, lyrics, random.choice(tokens))).start()
                    except:
                        pass
                    lyrics = ""

@Euphoria.command() #leaveserver
async def leaveserver(ctx, guild_id=None):
    if guild_id == None:
        errorsay(f"{ctx.command.name}: server id is missing")
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_error}[E] Usage: {prefix}{ctx.command.name} <server id>{footer}{codeblock}", delete_after=deletetimer)
    else:
        tokens = open("settings/tokens.txt", "r").read().splitlines()

        await ctx.message.delete()
        for _token_ in tokens:
            threading.Thread(target=_leave_, args=(guild_id, _token_)).start()

@Euphoria.command(aliases=["tokenscheck"])
async def checktokens(Euphoria):
    await Euphoria.message.delete()
    _tokencheck_()

#ACCOUNT----------------------------------------------------------

@Euphoria.command(aliases=["bio"]) #aboutme
async def aboutme(ctx, *, bio=None):
    await ctx.message.delete()
    try:
        requests.patch(url="https://discord.com/api/v9/users/@me", headers= {"authorization": token}, json = {"bio": bio})
    except:
        await ctx.send(f"{codeblock}{cb_error}[E] Failed to update About-Me{footer}{codeblock}", delete_after=deletetimer)
    else:
        if bio == None:
            await ctx.send(f"{codeblock}{cb_prefix}[E] Removed About-Me{footer}{codeblock}", delete_after=deletetimer)
        else:
            await ctx.send(f"{codeblock}{cb_prefix}[E] About-Me was changed{footer}{codeblock}", delete_after=deletetimer)

@Euphoria.command(aliases=["av"]) #avatar
async def avatar(ctx, user: discord.User=None):
    if user == None:
        user = Euphoria.user
    await ctx.send(user.avatar_url)

@Euphoria.command(aliases=["cycleactivity", "ac"]) #activitycycle
async def activitycycle(ctx):
    global cycle_activity
    if cycle_activity:
        cycle_activity = False
        await ctx.send(f"{codeblock}{cb_prefix}[E] Turned off activty cycle{footer}{codeblock}", delete_after=deletetimer)
        return

    cycle_activity = True
    await ctx.send(f"{codeblock}{cb_prefix}[E] Turned on activty cycle{footer}{codeblock}", delete_after=deletetimer)
    while cycle_activity:
        await Euphoria.change_presence(status=discord.Status.online)
        await asyncio.sleep(5)
        await Euphoria.change_presence(status=discord.Status.idle)
        await asyncio.sleep(5)
        await Euphoria.change_presence(status=discord.Status.dnd)
        await asyncio.sleep(5)
        

@Euphoria.command(name="status") #status
async def statuschanger(ctx, *, text=""):
    url = "https://discordapp.com/api/v8/users/@me/settings"

    payload="{\r\n    \"custom_status\": {\r\n        \"text\": \"" + text + "\"\r\n    }\r\n}"
    headers = {
    'Authorization': token,
    'Content-Type': 'application/json',
    'Cookie': '__cfduid=d7e8d2784592da39fb3f621664b9aede51620414171; __dcfduid=24a543339247480f9b0bb95c710ce1e6'
    }

    requests.request("PATCH", url, headers=headers, data=payload)
    await ctx.send(f"{codeblock}{cb_prefix}[E] Updated your status{footer}{codeblock}", delete_after=deletetimer)

@Euphoria.command(aliases=["cyclestatus"]) #statuscycle
async def statuscycle(ctx, *, text=None):
    global cycle_status
    if text == None:
        if cycle_status:
            cycle_status = False
            url = "https://discordapp.com/api/v8/users/@me/settings"
            payload="{\r\n    \"custom_status\": {\r\n        \"text\": \"" + "" + "\"\r\n    }\r\n}"
            headers = {
            'Authorization': token,
            'Content-Type': 'application/json',
            'Cookie': '__cfduid=d7e8d2784592da39fb3f621664b9aede51620414171; __dcfduid=24a543339247480f9b0bb95c710ce1e6'
            }

            requests.request("PATCH", url, headers=headers, data=payload)
            await ctx.send(f"{codeblock}{cb_prefix}[E] Statuscycle was disabled{footer}{codeblock}", delete_after=deletetimer)
            return
        else:
            errorsay(f"{ctx.command.name}: text is missing")
            if consolemode == "false":
                await ctx.send(f"{codeblock}{cb_error}[E] Usage: {prefix}{ctx.command.name} <text>{footer}{codeblock}", delete_after=deletetimer)
    else:  
        status_text = []
        temp = ""
        for x in text:
            temp += x
            status_text.append(temp)
        
        cycle_status = True
        while cycle_status:
            for x in status_text:
                url = "https://discordapp.com/api/v8/users/@me/settings"

                payload="{\r\n    \"custom_status\": {\r\n        \"text\": \"" + x + "\"\r\n    }\r\n}"
                headers = {
                'Authorization': token,
                'Content-Type': 'application/json',
                'Cookie': '__cfduid=d7e8d2784592da39fb3f621664b9aede51620414171; __dcfduid=24a543339247480f9b0bb95c710ce1e6'
                }

                requests.request("PATCH", url, headers=headers, data=payload)
                await asyncio.sleep(10)

@Euphoria.command(aliases=["who", "whos"]) #whois
async def whois(ctx, user: discord.User=None):
    if user == None:
        user = Euphoria.user
    badges = user.public_flags.all()
    badges = str(badges)
    hypesquad = False
    if "UserFlags.hypesquad" in badges:
        hypesquad = True
    if "<UserFlags.staff: 1>" in badges:
        staff = True
    else:
        staff = False
    if "UserFlags.partner" in badges:
        partner = True
    else:
        partner = False
    output = f"""[ Account ]
Username: {user.name}
Discriminator: {user.discriminator}
Creation date: {user.created_at}
HypeSquad: {hypesquad}
Discord Partner: {partner}
Discord Support: {staff}"""
    await ctx.send(f"{codeblock}{cb_prefix}{output}{footer}{codeblock}")


#SELFBOT----------------------------------------------------------

@Euphoria.command(aliases=["online"]) #uptime
async def uptime(ctx):
    commandexc_time = int(time.time())
    await ctx.send(f"{codeblock}{cb_prefix}[E] The selfbot is running for {int(commandexc_time-bootup_time)}sec{footer}{codeblock}", delete_after=deletetimer)

@Euphoria.command(aliases=["raidsave", "lograids", "lograid"]) #raidlog
async def raidlog(ctx):
    if json.loads(open("settings/config.json", "r").read())["raid_detections"] == "true":
        config_edit(cfg_raid_detections="false")
        await ctx.send(f"{codeblock}{cb_prefix}[E] Raid Logging disabled{footer}{codeblock}", delete_after=deletetimer)

    else:
        config_edit(cfg_ban_detections="true")
        await ctx.send(f"{codeblock}{cb_prefix}[E] Raid Logging enabled{footer}{codeblock}", delete_after=deletetimer)

@Euphoria.command(aliases=["clearlog", "purgelogs", "clearlogs", "purgelog"]) #logclear
async def logclear(ctx):
    clearedlogs = 0
    for file in os.listdir("settings/logs"):
        if file != logfile:
            content = open(f"settings/logs/{file}", "r", encoding="utf-8").read()
            logsize = 0
            for line in content.splitlines():
                logsize += 1
            if logsize < 15:
                clearedlogs += 1
                try:
                    os.remove(f"settings/logs/{file}")
                except Exception as error:
                    errorsay(error)
    await ctx.send(f"{codeblock}{cb_prefix}[E] Cleared {clearedlogs} logs{footer}{codeblock}", delete_after=deletetimer)

@Euphoria.command(aliases=["login", "accountswitch", "switcher", "accswitch", "accountswitcher", "accswither"]) #switch
async def switch(ctx, selection: int=None):
    await ctx.message.delete()
    def getusers(jsonlist=False):
        i = 0
        users = ""
        user_list = []
        for Atoken in gettokens():
            if getuserdata(Atoken) != None:
                i += 1
                userdata = getuserdata(Atoken)
                name = userdata["username"]
                if str(userdata["id"]) == str(Euphoria.user.id):
                    name += " - Current"
                users += f"\n[{i}] {name}"
                user_list.append(Atoken)
        for line in open("settings/accounts.txt", "r",encoding="utf-8").read().splitlines():
            if line not in user_list:
                if getuserdata(line) != None:
                    i += 1
                    userdata = getuserdata(line)
                    name = userdata["username"]
                    if str(userdata["id"]) == str(Euphoria.user.id):
                        name += " - Current"
                    users += f"\n[{i}] {name}"
                    user_list.append(line)
        users += f"\n\n[{i+1}] Other..."

        if jsonlist:
            return json.dumps({"tokens": user_list, "amount": i})
        else:
            return users
            
    
    if selection == None:
        userlist = getusers()
        await ctx.send(f"{codeblock}{cb_prefix}[E] Account switcher:\n{userlist}{footer}{codeblock}", delete_after=deletetimer)
    else:
        jsonlist = json.loads(getusers(jsonlist=True))
        i = jsonlist["amount"]
        tokens = jsonlist["tokens"]
        if selection == i+1:
            await ctx.send(f"{codeblock}{cb_prefix}[E] Please input user token into the console{footer}{codeblock}",delete_after=deletetimer)
            newtoken = str(input(f"{Fore.WHITE}{current_time()} {yellow}[Token] {Fore.LIGHTBLACK_EX} "+Fore.LIGHTBLACK_EX))
            if newtoken == "" or len(newtoken) < 5:
                successsay("Action cancelled")
                await ctx.send(f"{codeblock}{cb_error}[E] Action cancelled{footer}{codeblock}",delete_after=deletetimer)
                return
            else:
                if newtoken not in open("settings/accounts.txt", "r", encoding="utf-8").read():
                    content = open("settings/accounts.txt", "r", encoding="utf-8").read()
                    open("settings/accounts.txt", "w", encoding="utf-8").write(content+"\n"+newtoken)
        elif selection <= i:
            newtoken = tokens[int(selection-1)]
        else:
            await ctx.send(f"{codeblock}{cb_error}[E] Invalid selection{footer}{codeblock}",delete_after=deletetimer)
            return

        username = getuserdata(newtoken)["username"]

        await ctx.send(f"{codeblock}{cb_prefix}[E] Account switched to '{username}', restart to apply changes{footer}{codeblock}",delete_after=deletetimer)
        config_edit(cfg_token=newtoken)
        
@Euphoria.command() #logout
async def logout(ctx):
    config_edit(cfg_token="logged out")
    log("INFO: Logged out of {}".format(Euphoria.user))
    await ctx.send(f"{codeblock}{cb_prefix}[E] Logged out{footer}{codeblock}")
    selfbot_reboot()

@Euphoria.command(aliases=["reminder"]) #remind
async def remind(ctx, delay: int=None, *, message=None):
    if delay == None or message == None:
        errorsay(f"{ctx.command.name}: delay is missing")
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_error}[E] Usage: {prefix}{ctx.command.name} <delay (min)> <message>{footer}{codeblock}", delete_after=deletetimer)
    else:
        await ctx.message.delete()
        toast(f"Reminder set to {delay}min")
        await asyncio.sleep(int(delay*60))
        open("reminder.vbs", "w").write(f"x=Msgbox(\"Reminder: {message}\",vbOK+vbInformation, \"Euphoria\")")
        os.system("start reminder.vbs")
        await asyncio.sleep(1)
        os.remove("reminder.vbs")

@Euphoria.command(aliases=["ppin", "ppins", "personalpins"]) #personalpin
async def personalpin(ctx, method=None, message_id: int=None):
    if method == None:
        output = ""
        for line in open("settings/misc/personalpins.ep", "r", encoding="utf-8").read().splitlines():
            c = 0
            msg_id = ""
            msg_cont = ""
            for letter in line:
                if letter == " ":
                    c = 1
                if c == 0:
                    msg_id += letter
                if c == 1:
                    if letter == empty_char2:
                        msg_cont += "\n"
                    else:
                        msg_cont += letter
            output += f"\n[{msg_id}] {msg_cont}"
        await ctx.send(f"{codeblock}{cb_prefix}[E] Personal Pins:{codeblock}{codeblock}{output}{codeblock}{codeblock}{cb_prefix}{footer}{codeblock}", delete_after=deletetimer)
            
    else:
        if method.lower() == "add":
            await ctx.message.delete()
            message = await get_message(ctx, message_id)

            if message == None:
                await ctx.send(f"{codeblock}{cb_error}[E] Message not found{footer}{codeblock}", delete_after=deletetimer)
                return

            content = open("settings/misc/personalpins.ep", "r", encoding="utf-8").read()
            ppin_msg = message.content.replace("\n", empty_char2)
            open(f"settings/misc/personalpins.ep", "w", encoding="utf-8").write(f"{content}{message.id} {message.author.name}#{message.author.discriminator}: {ppin_msg}\n")
            await ctx.send(f"{codeblock}{cb_prefix}[E] Pinned the message{footer}{codeblock}", delete_after=deletetimer)
        elif method.lower() == "del" or method.lower() == "delete" or method.lower() == "remove":
            output = ""
            for line in open("settings/misc/personalpins.ep", "r", encoding="utf-8").read().splitlines():
                if line.startswith(str(message_id)) == False:
                    output += line
            open("settings/misc/personalpins.ep", "w", encoding="utf-8").write(output)
            await ctx.send(f"{codeblock}{cb_prefix}[E] Message removed{footer}{codeblock}", delete_after=deletetimer)
        else:
            await ctx.send(f"{codeblock}{cb_error}[E] Usage: {prefix}{ctx.command.name} <add/del> <message id>{footer}{codeblock}", delete_after=deletetimer)

@Euphoria.command(aliases=["dr", "discordrestart", "drestart", "discordreboot", "dreboot"]) #disrestart
async def disrestart(ctx, mode="false"):
    if mode.lower() == "true":
        msg = await ctx.send(f"{codeblock}{cb_prefix}[E] Rebooting the discord canary...{footer}{codeblock}")
        taskstatus = os.popen("taskkill /F /IM discordcanary.exe").read()
        try:
            if "SUCCESS" not in str(taskstatus):
                await msg.edit(content=f"{codeblock}{cb_error}[E] Restarting failed. Are you sure you're using canary?{footer}{codeblock}")
            else:
                path = f"C:/Users/{os.getlogin()}/AppData/Local/DiscordCanary"
                for file in os.listdir(path):
                    if "app-1" in str(file):
                        path += f"/{file}/DiscordCanary.exe"
                        break
                os.popen("start "+path)
        except:
            errorsay("Failed to restart discord canary")
        await asyncio.sleep(5)
        await msg.delete()
    else:
        msg = await ctx.send(f"{codeblock}{cb_prefix}[E] Rebooting the discord...{footer}{codeblock}")
        taskstatus = os.popen("taskkill /F /IM discord.exe").read()
        try:
            if "SUCCESS" not in str(taskstatus):
                await msg.edit(content=f"{codeblock}{cb_error}[E] Restarting failed. Are you sure you're not using canary?{footer}{codeblock}")
            else:
                path = f"C:/Users/{os.getlogin()}/AppData/Local/Discord"
                for file in os.listdir(path):
                    if "app-1" in str(file):
                        path += f"/{file}/Discord.exe"
                        break
                os.popen(path)
        except:
            errorsay("Failed to restart discord")
        await asyncio.sleep(5)
        await msg.delete()

@Euphoria.command(name="showtoast") #showtoast
async def ntoast(ctx, *, text="Hello!"):
    toast(text)

@Euphoria.command(aliases=["snipe"]) #sniper
async def sniper(ctx, *, arg=None):
    snipelist = f"""
{prefix}sniper giveaways ─ toggles giveaway sniper
{prefix}sniper nitro ─ toggles nitro sniper
"""
    if arg == None:
        await ctx.send(f"{codeblock}{cb_prefix}[E] Sniper modes:{snipelist}{footer}{codeblock}")

    elif arg.lower() == "giveaways":
        state = json.loads(open("settings/config.json", "r").read())["giveaway_sniper"]
        if state == "true":
            togglemode = "false"
            await ctx.send(f"{codeblock}{cb_prefix}[E] Giveaway sniper was disabled{footer}{codeblock}", delete_after=deletetimer)
        else:
            togglemode = "true"
            await ctx.send(f"{codeblock}{cb_prefix}[E] Giveaway sniper was enabled{footer}{codeblock}", delete_after=deletetimer)
        config_edit(None, None, None, None, None, None, None, None, togglemode)

    elif arg.lower() == "nitro":
        state = json.loads(open("settings/config.json", "r").read())["nitro_sniper"]
        if state == "true":
            togglemode = "false"
            await ctx.send(f"{codeblock}{cb_prefix}[E] Nitro sniper was disabled{footer}{codeblock}", delete_after=deletetimer)
        else:
            togglemode = "true"
            await ctx.send(f"{codeblock}{cb_prefix}[E] Nitro sniper was enabled{footer}{codeblock}", delete_after=deletetimer)
        config_edit(None, None, None, None, None, None, None, None, None, togglemode)

    else:
        await ctx.send(f"{codeblock}{cb_prefix}[E] Sniper modes:{snipelist}{footer}{codeblock}")

@Euphoria.command(name="afk", aliases=["afkmode"]) #afk
async def afk1(ctx):
    global afk_state
    afk_state = True
    toast("Toggled on AFK Mode")

@Euphoria.command(name='toasts', aliases=["toast", "notifications", "alerts"]) #toasts
async def toastdisabler(ctx):
    state = json.loads(open("settings/config.json", "r").read())["toasts"]
    if state == "true":
        config_edit(None, None, None, "false")
        await ctx.send(f"{codeblock}{cb_prefix}[E] Toast notifications were disabled{footer}{codeblock}", delete_after=deletetimer)
    else:
        config_edit(None, None, None, "true")
        toast("Toasts Enabled", True)
        await ctx.send(f"{codeblock}{cb_prefix}[E] Toast notifications were enabled{footer}{codeblock}", delete_after=deletetimer)

@Euphoria.command(aliases=["deletetimer"]) #deletetimeout
async def deletetimeout(ctx, delay: int=None):
    if delay == None or delay < 1:
        errorsay(f"{ctx.command.name}: delay is missing")
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_error}[E] Usage: {prefix}{ctx.command.name} <delay (s)>{footer}{codeblock}", delete_after=deletetimer)
    else:
        config_edit(None, None, None, None, None, delay)
        await ctx.send(f"{codeblock}{cb_prefix}[E] Delete Timer was set to {delay}s{footer}{codeblock}", delete_after=delay)

@Euphoria.command(name='theme') #theme
async def themechanger(ctx, *, newtheme=None):
    themes = ["normal", "euphoria", "moon", "old", "fast", "italic", "czech", "rise", "nighty"]
    if newtheme == None:
        theme_list = """
Normal/Euphoria - The basic one
Moon - Main theme on Moon Selfbot
Old - The old Euphoria theme
Fast - Speedy lookin' theme
Italic - 𝘪𝘵𝘢𝘭𝘪𝘤 𝘴𝘵𝘺𝘭𝘦 𝘵𝘩𝘦𝘮𝘦
Czech - Euforie
Rise - Rise selfbot looking theme
Nighty - b real niggty user"""
        await ctx.send(f"{codeblock}{cb_prefix}[E] Available themes:{theme_list}{footer}{codeblock}",delete_after=deletetimer)
    elif newtheme.lower() in themes:
        config_edit(None, None, None, None, None, None, newtheme.lower())
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_prefix}[E] Theme was changed to {newtheme.lower()}{footer}{codeblock}",delete_after=deletetimer)
        cls()
        title()
        separator()
        successsay(f"Theme was changed to '{newtheme.lower()}'")

@Euphoria.command() #reload
async def reload(ctx):
    await ctx.message.delete()
    msg = await ctx.send(f"{codeblock}{cb_prefix}[E] Reloading... Please wait.{footer}{codeblock}")
    toast("Reloading...", True)
    scriptname =  os.path.basename(sys.argv[0])
    await msg.delete()
    os.system(f"""""start {scriptname}""""")
    os._exit(0)
    

@Euphoria.command(aliases=["discord"]) #join
async def join(ctx):
    try:
        requests.post("https://discordapp.com/api/v6/invites/kjh9bEytUH", headers={'authorization': token})
    except:
        os.system("start \"\" https://discord.gg/kjh9bEytUH")
    await ctx.send(f"{codeblock}{cb_prefix}[E] Joined the support server{footer}{codeblock}", delete_after=deletetimer)

@Euphoria.command() #search
async def search(ctx, * ,command=""):
    output = ""
    searched_commands = 0+command_spoof
    for cmd in Euphoria.commands:
        if command in cmd.name or command in cmd.description or command in cmd.aliases:
            if str(cmd.name) not in loaded_scripts:
                searched_commands += 1
                output += f"{prefix}{cmd.name}\n"
    if command == "":
        await ctx.send(f"{codeblock}{cb_prefix}[E] Search: found {searched_commands} commands{footer}{codeblock}")
    else:
        await ctx.send(f"{codeblock}{cb_prefix}[E] Search: Found {searched_commands} commands\n{output}{footer}{codeblock}", delete_after=deletetimer)

@Euphoria.command(name="version",aliases=["ver", "release"]) #version
async def versionviewer(ctx):
    build = current["build"]
    current_version = f"Euphoria {version}--{build}"
    await ctx.send(f"{codeblock}{cb_prefix}[E] Version: {current_version}{footer}{codeblock}")

@Euphoria.command(aliases=["br", "announcements"]) #broadcast
async def broadcast(ctx):
    r = requests.get("https://euphoria.xellu1337.repl.co/broadcast")
    message = json.loads(r.text)["message"]
    await ctx.send(f"{codeblock}{cb_prefix}[ Broadcast ]\n{message}{footer}{codeblock}")

@Euphoria.command(name="token") #token
async def tokenviewer(ctx):
    consolesay(f"tokenviewer: {token}")
    warnsay("[!] Warning: DO NOT SHARE YOUR TOKEN TO ANYONE!")
    toast("Check the console")

@Euphoria.command(name="prefix") #prefix
async def prefixchanger(ctx, new_prefix):
    config_edit(None, new_prefix, None, None, None, None, None)
    successsay("Prefix changed to '{}'".format(new_prefix))
    toast("Prefix was changed", True)
    if consolemode == "false":
        await ctx.send(f"{codeblock}{cb_prefix}[E] Prefix was changed to '{new_prefix}'{footer}{codeblock}", delete_after=deletetimer)
    selfbot_reboot()
    
@Euphoria.command(aliases=["r", "reboot"]) #restart
async def restart(ctx):
    await ctx.message.delete()
    open("settings/.restart", "w")
    infosay("Rebooting...")
    selfbot_reboot()

@Euphoria.command(name="cls", aliases=["clear", "consoleclear"]) #cls
async def clearcmd(ctx):
    cls()
    title()
    separator()
    if consolemode == "false":
        await ctx.send(f"{codeblock}{cb_prefix}[E] The console was cleared{footer}{codeblock}", delete_after=deletetimer)

@Euphoria.command(aliases=["shutdown"]) #exit
async def exit(ctx):
    await ctx.message.delete()
    os._exit(0)

#Scripts----------------------------------------------------------

# @Euphoria.command(aliases=["customcmd", "customcommands", "scripts"]) #script
# async def script(ctx, *, script_name):
#     success = False
#     for file in os.listdir("scripts"):
#         if file == script_name:
            
#             success == True
#     if success == False:
#         await ctx.send(f"{codeblock}{cb_error}[E] Can't find any script named '{script_name}'{footer}{codeblock}")
# for file in os.listdir("scripts"):
#     try:
#         Euphoria.load_extension(f'scripts/{file}')
#     except Exception as error:
#         print(error)


#HELP-------------------------------------------------------------

@Euphoria.command(aliases=["credit", "creds"]) #credits
async def credits(ctx):
    await ctx.send(f"{codeblock}{cb_prefix}{c_credits}{footer}{codeblock}", delete_after=deletetimer)

@Euphoria.command(aliases=["categories"]) #help
async def help(ctx):
    await ctx.send(f"{codeblock}{cb_prefix}{c_help}{footer}{codeblock}", delete_after=deletetimer)

@Euphoria.command() #fun
async def fun(ctx):
    await ctx.send(f"{codeblock}{cb_prefix}{c_fun}{footer}{codeblock}", delete_after=deletetimer)

@Euphoria.command() #text
async def text(ctx):
    await ctx.send(f"{codeblock}{cb_prefix}{c_text}{footer}{codeblock}", delete_after=deletetimer)

@Euphoria.command(aliases=["miscellaneous"]) #misc
async def misc(ctx):
    await ctx.send(f"{codeblock}{cb_prefix}{c_misc}{footer}{codeblock}", delete_after=deletetimer)

@Euphoria.command() #abuse
async def abuse(ctx):
    await ctx.send(f"{codeblock}{cb_prefix}{c_abuse}{footer}{codeblock}", delete_after=deletetimer)

@Euphoria.command(aliases=["administration"]) #admin
async def admin(ctx):
    await ctx.send(f"{codeblock}{cb_prefix}{c_admin}{footer}{codeblock}", delete_after=deletetimer)

@Euphoria.command(aliases=["raid"]) #raiding
async def raiding(ctx):
    await ctx.send(f"{codeblock}{cb_prefix}{c_raiding}{footer}{codeblock}", delete_after=deletetimer)

@Euphoria.command(aliases=["acc"]) #account
async def account(ctx):
    await ctx.send(f"{codeblock}{cb_prefix}{c_account}{footer}{codeblock}", delete_after=deletetimer)

@Euphoria.command() #selfbot
async def selfbot(ctx):
    await ctx.send(f"{codeblock}{cb_prefix}{c_selfbot}{footer}{codeblock}", delete_after=deletetimer)


#───────────────────────────────────────────────────────────────#
# RUNNING                                                       #
#───────────────────────────────────────────────────────────────# 

try:
    Euphoria.run(token, bot=False)
except:
    settings_regenerate()
    try:
        token = json.loads(open("settings/config.json", "r").read())["token"]
    except:
        token = ""
    if token == "logged out":
        cls()
        ctypes.windll.kernel32.SetConsoleTitleW("Euphoria")
        title()
        print("[You're logged out]".center(width))
        newtoken = input(f"{Fore.WHITE}{current_time()} {yellow}[Auth] {Fore.WHITE}Token: "+Fore.LIGHTBLACK_EX)
        config_edit(cfg_token=newtoken)
        selfbot_reboot()
    else:
        ctypes.windll.kernel32.SetConsoleTitleW("Euphoria")
        cls()
        title()
        print("[Authentication]".center(width))
        consolesay("Welcome to euphoria! To use the selfbot, you'll need to authenticate first\n")
        set_token = input(f"{Fore.WHITE}{current_time()} {yellow}[Auth] {Fore.WHITE}Token: "+Fore.LIGHTBLACK_EX)
        set_prefix = input(f"{Fore.WHITE}{current_time()} {yellow}[Auth] {Fore.WHITE}Prefix: "+Fore.LIGHTBLACK_EX)
        # content = {
        #     "token": cfg_token,
        #     "prefix": cfg_prefix,
        #     "consolemode": cfg_consolemode,
        #     "toasts": cfg_toasts,
        #     "embed_color": cfg_embed_color,
        #     "deletetimer": cfg_deletetimer,
        #     "theme": cfg_theme,
        #     "ban_detections": cfg_ban_detections,
        #     "giveaway_sniper": cfg_giveaway_sniper,
        #     "nitro_sniper": cfg_nitro_sniper
        # }
        config_edit(set_token, set_prefix, "false", "true", "d37ffa", 10, "normal", "true", "true", "true")
        selfbot_reboot()
# Made by Xellu with <3