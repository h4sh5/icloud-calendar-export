#!/usr/bin/env python3
import caldav 
import os
import time

start = time.time()

url = 'https://caldav.icloud.com'
username='EXAMPLE@EXAMPLE.com'
password = os.getenv('CALDAV_PASS')

if password == None:
	print("pls set CALDAV_PASS")
	print("read -s CALDAV_PASS; export CALDAV_PASS")
	exit(1)


client = caldav.DAVClient(url=url, username=username, password=password)
my_principal = client.principal()
calendars = my_principal.calendars()
print("Calendars:")
count = 0

allevents = []

for i in calendars:
	# print(type(i),i)
	print(f'[{count}]',i.name, i)
	count += 1
	# allevents.append(i.events())
	with open(f'icloud-{i.name}.cal.txt','w+') as f:
		for e in i.events():
			f.write(e.data)
	print('elapsed:', time.time() - start)


print('elapsed:', time.time() - start)

# import code
# code.interact(local=locals())

