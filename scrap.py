from selenium import webdriver
import requests,time
from threading import Thread
from proxy_checker import ProxyChecker
uncheckedproxies = []
uncheckedproxytypes = []
checkedproxies = []
toplambulunan = 0
kacıncı = 0
print('\033[92m' + """\
___________            __                     ____  __.              .__.__                .__         
\_   _____/_ _________|  | _______    ____   |    |/ _|____    _____ |__|  |   ____   ____ |  |  __ __ 
 |    __)|  |  \_  __ \  |/ /\__  \  /    \  |      < \__  \  /     \|  |  |  /  _ \ / ___\|  | |  |  
 |     \ |  |  /|  | \/    <  / __ \|   |  \ |    |  \ / __ \|  Y Y  \  |  |_(  <_> ) /_/  >  |_|  |  /
 \___  / |____/ |__|  |__|_ \(____  /___|  / |____|__ (____  /__|_|  /__|____/\____/\___  /|____/____/ 
     \/                    \/     \/     \/          \/    \/      \/              /_____/             
""")
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
print( bcolors.OKBLUE + "Proxy Grabber For Selenium" + bcolors.ENDC)
BeklemeMs = input("Kaç Saniyede Bir Yeni Thread Açalım :")


def getallproxy():
    global toplambulunan,uncheckedproxies,uncheckedproxytypes
    maxdelay = input(bcolors.HEADER + "Proxylerin Yanıt Süresi Maksimum Kaç Milisaniye Olsun : " + bcolors.ENDC)
    types = ["socks4","socks5","http"]
    for ttype in types:
        for asd in requests.get("https://api.proxyscrape.com/?request=getproxies&proxytype=" + ttype +"&timeout=" + str(
                maxdelay) + "&country=all&ssl=all&anonymity=all", stream=True).iter_lines():
            toplambulunan += 1
            uncheckedproxies.append(str(asd)[2:-1])
            uncheckedproxytypes.append(ttype)
    print(bcolors.HEADER + str(toplambulunan) + " Proxy Bulundu" + bcolors.ENDC)


def proxydene(proxy,önek,kacinci):
    global bthread
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    options.add_argument("--headless")
    options.add_argument("--proxy-server="+ önek +"://" + proxy)
    options.add_argument("log-level=2")
    chrome = webdriver.Chrome(options=options)
    chrome.get("https://api.ipify.org")
    time.sleep(0.5)
    try:
        chrome.find_element_by_xpath("/html/body/pre").text
        print(bcolors.OKGREEN + "Çalışıyor " + proxy + " (" + str(kacinci + 1) + "/" + str(
            toplambulunan) + ")" + bcolors.ENDC)
        checkedproxies.append("--proxy-server=" + önek + "://" + proxy)
        open("çalışanproxyler.txt","a").write("--proxy-server=" + önek + "://" + proxy + "\n")
        print(str(len(checkedproxies)) + " Proxy Düzgün Çalışıyor.")
    except:
        print(bcolors.FAIL + "Bozuk " + proxy +" (" + str(kacinci + 1) + "/" + str(toplambulunan) + ")" + bcolors.ENDC)
    chrome.close()
    chrome.quit()
    return

getallproxy()
print(bcolors.WARNING + "Proxyler Deneniyor" + bcolors.ENDC)
for proxy in uncheckedproxies:
    if __name__ == "__main__":
        Thread(target=proxydene, args=(proxy, uncheckedproxytypes[kacıncı], kacıncı)).start()
        kacıncı += 1
        time.sleep(BeklemeMs)




