import requests
import time
import sys
from torrequest import TorRequest

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36"
}

def print_banner():
    print("\033[1m\033[37m")
    print("     _____ ___  ____            ____  _              __     ___                     ____        _            ")
    print("    |  ___/ _ \/ ___|          | __ )| | ___   __ _  \ \   / (_) _____      _____  | __ )  ___ | |_          ")
    print("    | |_ | | | \___ \   _____  |  _ \| |/ _ \ / _` |  \ \ / /| |/ _ \ \ /\ / / __| |  _ \ / _ \| __|         ")
    print("    |  _|| |_| |___) | |_____| | |_) | | (_) | (_| |   \ V / | |  __/\ V  V /\__ \ | |_) | (_) | |_          ")
    print("    |_|   \___/|____/          |____/|_|\___/ \__, |    \_/  |_|\___| \_/\_/ |___/ |____/ \___/ \__|         ")
    print("                                              |___/                                                         ")
    print("                                                                     \033[41m FOS- Fools of Security :) \033[0m")
    print()

def add_blog_views(site_url: str, num_views: int, proxy_port: int = 9050, ctrl_port: int = 9051):
    print_banner()

    with TorRequest(proxy_port=proxy_port, ctrl_port=ctrl_port, password=None) as tr:
        for i in range(num_views):
            response = tr.get(site_url, headers=HEADERS, verify=False)
            print(f"[{i+1}] Blog View Added with IP: {tr.get('http://ipecho.net/plain').content}")
            tr.reset_identity()

if __name__ == '__main__':
    site_url = input("Enter your Blog Address: ")
    num_views = int(input("Enter the number of viewers: "))
    add_blog_views(site_url, num_views)
