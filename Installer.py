import requests,os,json

def run():
    print("[@] Downloading Euphoria.py")
    r = requests.get("https://raw.githubusercontent.com/xellu/euphoria/main/Euphoria.py")
    open("Euphoria.py", "wb").write(r.content)

    print("[@] Creating directories")
    dirs = """settings
scripts
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

    print("[@] Installation finished")
    input("\n[@] Press enter to exit")
    os.system("start Euphoria.py")

try:
    run()
except Exception as error:
    print(error)
    input("[@] Installation failed, press enter to exit")    