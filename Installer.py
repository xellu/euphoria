import requests,os,json

def run():
    print("[@] Downloading Euphoria.py")
    r = requests.get("https://raw.githubusercontent.com/xellu/euphoria/main/Euphoria.py")
    open("Euphoria.py", "wb").write(r.content)

    print("[@] Creating directories")
    dirs = """settings
settings/assets
settings/logs
settings/misc
settings/misc/raids
settings/scrape
settings/scrape/avatar
settings/scrape/emoji
settings/scrape/chat
settings/scrape/server"""
    for x in dirs.splitlines():
        try:
            os.mkdir(x)
        except:
            print(f"[@] Directory already '{x}' exists, skipping")

    print("[@] Creating accounts.txt")
    open("settings/accounts.txt", "w")

    print("[@] Creating current.json")
    r=json.loads(requests.get("https://raw.githubusercontent.com/xellu/euphoria/main/latest_version.json").text)
    open("settings/current.json", "w").write(json.dumps(r))



    print("[@] Creating tokens.txt")
    open("settings/tokens.txt", "w")

    print("[@] Creating misc/personalpins.ep")
    open("settings/misc/personalpins.ep", "w")

    print("[@] Creating misc/sharelist.txt")
    open("settings/misc/sharelist.txt", "w")

    print("[@] Downloading assets")
    open("settings/assets/e.png", "wb").write(requests.get("https://raw.githubusercontent.com/xellu/euphoria/main/assets/e.png").content)
    open("settings/assets/success.ico", "wb").write(requests.get("https://raw.githubusercontent.com/xellu/euphoria/main/assets/success.ico").content)
    open("settings/assets/icon.ico", "wb").write(requests.get("https://raw.githubusercontent.com/xellu/euphoria/main/assets/icon.ico").content)

    print("[@] Creating config.json")
    toasts = input("[@] Enable toasts? (disable them if you're using linux | y/n): ")
    rpc = input("[@] Disable RPC? (y/n): ")
    if toasts == "y":
        toasts = "true"
    else:
        toasts = "false"
    cfg = { 
        "token": "",
        "prefix": ".",
        "consolemode": "false",
        "toasts": toasts,
        "embed_color": "d37ffa",
        "deletetimer": 10,
        "theme": "euphoria",
        "ban_detections": "true",
        "giveaway_sniper": "true",
        "nitro_sniper": "true",
        "raid_detections": "false"

    }
    open("settings/config.json", "w").write(json.dumps(cfg, indent=5))

    if rpc == "y":
        print("[@] Creating .rpcoff")
        open("settings/.rpcoff", "w")

    print("[@] Installation finished")
    input("\n[@] Press enter to exit")
    os.system("start Euphoria.py")

try:
    run()
except Exception as error:
    print(error)
    input("[@] Installation failed, press enter to exit")    