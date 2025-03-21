import requests
import asyncio
import aiohttp
import time
import threading
from bs4 import BeautifulSoup
from colorama import Fore, init

init(autoreset=True)

def banner():
    bnn = """
                                                  ______
                                               .-"      "-.       ▓█████ ▄████▄   ██░ ██  ██ ▄█▀    
                                              /            /      ▓█   ▀▒██▀ ▀█  ▓██░ ██▒ ██▄█▒            
                                             |              |     ▒███  ▒▓█    ▄ ▒██▀▀██░▓███▄░        
                                             |,  .-.  .-.  ,|     ▒▓█  ▄▒▓▓▄ ▄██▒░▓█ ░██ ▓██ █▄ 
                                             | )(_o/  \o_)( |     ░▒████▒ ▓███▀ ░░▓█▒░██▓▒██▒ █▄
                                             |/     /\     \|     ░░ ▒░ ░ ░▒ ▒  ░ ▒ ░░▒░▒▒ ▒▒ ▓▒  
                                   (@_       (_     ^^     _)      ░ ░  ░ ░  ▒    ▒ ░▒░ ░░ ░▒ ▒░
                              _     ) \_______\__|IIIIII|__/_____  ░  ░         ░  ░░ ░░ ░░ ░ 
                             (_)@8@8{}<________|-\IIIIII/-|___________________________>
                                    )_/        \          /
                                   (@           `--------`
                                        
                                     > Searchs Paths v1.0 - [No Brute-force] [Checker Activity]
                                     > Website Helper: https://web.archive.org/
                                     > G1thub: https://github.com/l44x
    """
    print(Fore.RED + f"{bnn}")


url = ''

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()

async def request_path():
    try:
        print(Fore.YELLOW + f"\n\t\t~ [M3nu 0PT10NS - By Ech0k]")
        url= input(str(f"{Fore.CYAN} \n\t\t\t[URL] Pass the website scanning > {Fore.WHITE}"))
        limit= input(str(f"{Fore.CYAN} \t\t\t[Limit 0-10000] Pass the rate limit > {Fore.WHITE}"))
        print("")
        s = requests.Session()
        # https://web.archive.org/web/*/https://github.com/admin/*
        # https://web.archive.org/web/timemap/json?url=${url}-&matchType=prefix&collapse=urlkey&output=json&fl=original,mimetype,timestamp,endtimestamp,groupcount,uniqcount&filter=!statuscode:[45]..&limit=10000&_=1742099529160
        url_website_org=f"https://web.archive.org/web/timemap/json?url={url}&matchType=prefix&collapse=urlkey&output=json&fl=original,mimetype,timestamp,endtimestamp,groupcount,uniqcount&filter=!statuscode:[45]..&limit={limit}&_=1742099529160"
        response_json = await fetch(url_website_org)
        #print(len(response_json))
        #print(response_json[1][0])

        for i in range(len(response_json)):
            #print(Fore.RED + f"\t\t\t\t[UNCHECKET STATUS URL] > " + Fore.GREEN + f"{response_json[i][0]}")
            url_target=response_json[i][0]
            checker_status_site(url_target)
            #t1 = threading.Thread(target=checker_status_site, args=(url_target))
            #t1.start()
            #t1.join()
    except:
        pass
                
def checker_status_site(url_checked):
    try:
        s = requests.Session()
        r = s.get(url_checked)
    
        if r.status_code == 200:
            print(Fore.BLUE + f"\t\t\t\t[ SUCCESSLY STATUS URL ] > " + Fore.GREEN + str(url_checked))
        else:
            print(Fore.RED + f"\t\t\t\t[ FAILED STATUS URL ] > " + Fore.YELLOW + str(url_checked))            
    except:
            print(Fore.RED + f"\t\t\t\t[ INVALID STATUS URL ] > " + Fore.RED + str(url_checked))
    

if __name__ == '__main__':
    banner()
    asyncio.run(request_path())
