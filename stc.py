import urllib3
import os
try:
	import requests
except:
	import os
	os.system('pip install requests')
	os.system('clear')
import threading
import socket
print('\033[1;33;40m------------[+] Status Code Checker By RC [+]----------\n')
fname = input('\033[1;37;40mEnter The File Name Which Contains The Subdomains \n\n\033[1;32;40mroot@rc #~ ')
http = urllib3.PoolManager()
try:
	f=open(fname)
	g=open(fname)
except:
	import os
	os.system('clear')
	print("\033[1;34;40m[+] File Not Found [+]")
	quit
	#f=open(fname)

def full(i):
	i = i.replace('\n','')
	try:
		resp=requests.get(i)
		if resp.status_code==200:
			print(f'\033[1;33;40m{i}  200 OK')
		elif resp.status_code==301:
			print(f'\033[1;32;40m;;{i} Redirected 301')
		elif resp.status_code==404:
			print(f'\033[1;31;40m{i} 404 Not Found')
		elif resp.status_code==403:
			print(f"\033[1;36;40m{i} 403 Forbidden/Redirecting")
		elif resp.status_code==400:
			print(f'\033[1;30;40m{i} 400 Bad Request')
		else:
			print(f"\033[1;34;40m{i} Status : {resp.status_code}")
	except requests.ConnectionError:
		print("\033[1;31;40m" + i + " 404 Not Found")
	
	
for i in f:
	thread = threading.Thread(target=full,args=(i,))
	thread.start()
