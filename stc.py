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
    print(pyfiglet.figlet_format('STCCheck'))
    sys.exit()
try:
	list = sys.argv[1]
except:
	help()
list=sys.argv[1]
try:
	import requests
except:
	import os
	os.system('pip3 install requests')
	os.system('clear')
import threading
import socket
fname = list
http = urllib3.PoolManager()
try:
	f=open(fname)
except:
	import os
	os.system('clear')
	print("\033[1;34;40m[+] File Not Found [+]")
	exit()
f = open(fname)
def full(i):
	i = i.replace('\n','')
	try:
		resp=requests.get(i)
		if resp.status_code==200:
			print(f'{i} 200 OK')
		elif resp.status_code==301:
			print(f'{i} Redirecting 301')
		elif resp.status_code==404:
			print(f'{i} 404 Not Found')
		elif resp.status_code==403:
			print(f"{i} 403 Forbidden")
		elif resp.status_code==400:
			print(f'{i} 400 Bad Request')
		else:
			print(f"{i} Status : {resp.status_code}")
	except requests.ConnectionError:
		pass
for i in f:
	thread = threading.Thread(target=full,args=(i,))
	thread.start()
