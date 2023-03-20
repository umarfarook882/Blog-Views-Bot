import requests
import time
import sys
from torrequest import TorRequest

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36"
}

print("""\033[1m\033[37m
     _____ ___  ____            ____  _              __     ___                     ____        _                                                     
    |  ___/ _ \/ ___|          | __ )| | ___   __ _  \ \   / (_) _____      _____  | __ )  ___ | |_                                                   
    | |_ | | | \___ \   _____  |  _ \| |/ _ \ / _` |  \ \ / /| |/ _ \ \ /\ / / __| |  _ \ / _ \| __|                                                  
    |  _|| |_| |___) | |_____| | |_) | | (_) | (_| |   \ V / | |  __/\ V  V /\__ \ | |_) | (_) | |_                                                   
    |_|   \___/|____/          |____/|_|\___/ \__, |    \_/  |_|\___| \_/\_/ |___/ |____/ \___/ \__|                                                  
                                              |___/                                                                                                  
                                                                     \033[41m FOS- Fools of Security :)
\033[0m
""")

# Default Tor port configuration
proxy_port = 9050
ctrl_port = 9051
site = input("Enter your Blog Address: ")
blog = int(input("Enter The number of Viewers: "))


def run():
    response = tr.get(site, headers=headers, verify=False)
    # time.sleep(10)
    # print(response.text)
    print("[" + str(i) + "]" + " Blog View Added With IP:" + tr.get('http://ipecho.net/plain').content.decode())
    tr.reset_identity()


if __name__ == '__main__':
    if len(sys.argv) > 3:
        if sys.argv[1] and sys.argv[2]:
            proxy_port = int(sys.argv[1])
            ctrl_port = int(sys.argv[2])
    with TorRequest(proxy_port=proxy_port, ctrl_port=ctrl_port, password=None) as tr:
        for i in range(blog):
            run()
