import threading
import urllib3
import os
import sys
try:
	from colorama import Fore
except:
	os.system("pip3 install colorama")
try:
    import pyfiglet
except:
    os.system("pip3 install pyfiglet")
def help():
    print(Fore.RED + pyfiglet.figlet_format('STCCheck'))
	print("Example:\n\tpython3 stc.py <websitelist>")
    sys.exit()
try:
	list = sys.argv[1]
except:
	help()
list=sys.argv[1]
try:
	import requests
except:
	os.system('pip3 install requests')
	os.system('clear')
fname = list
http = urllib3.PoolManager()
try:
	f=open(fname)
except:
	import os
	print("[+] File Not Found [+]")
	exit()
f = open(fname)
def full(i):
	i = i.replace('\n','')
	try:
		resp=requests.get(i)
		if resp.status_code==200:
			print(f'{Fore.GREEN}{i} [ 200 OK ]')
		elif resp.status_code==301:
			print(f'{Fore.BLUE}{i} [ 301 Moved temperory ]')
		elif resp.status_code==404:
			print(f'{Fore.RED}{i} [ 404 Not Found ]')
		elif resp.status_code==403:
			print(f"{Fore.YELLOW}{i} [ 403 Forbidden ] ")
		elif resp.status_code==400:
			print(f'{Fore.LIGHTBLACK_EX}{i} [ 400 Bad Request ] ')
		else:
			print(f"{Fore.RED}{i} Status : {resp.status_code}")
	except requests.ConnectionError:
		pass
for i in f:
	thread = threading.Thread(target=full,args=(i,))
	thread.start()
