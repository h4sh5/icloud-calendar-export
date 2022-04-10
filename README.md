# icloud-calendar-export
a script to export all events from icloud (or any caldav server)

## usage

install requirements:

`pip3 install requirements.txt`

modify your caldav server url and email:

```py
url = 'https://caldav.icloud.com'
username = 'myaccount@icloud.com'
```

read your password in secret (no echo) in terminal:

`read -s CALDAV_PASS; export CALDAV_PASS`

run the script

`python3 calget.py`
