import requests
import datetime
from bs4 import BeautifulSoup
r = requests.get('https://www.windfinder.com/forecast/strathallen_airfield')
soup = BeautifulSoup(r.content, 'html5lib')
smidge = soup.find_all("div", {"class": "weathertable forecast-day forecast forecast-day-8"})

file = open("temperatures.txt", "wt")
for hit in soup.findAll(attrs={'class' : 'units-at'}):
    file.write(hit.text+"\n")
file.flush()
file.close()

file = open("windspeeds.txt", "wt")
for hit in soup.findAll(attrs={'class' : 'units-ws'}):
    file.write(hit.text+"\n")
file.flush()
file.close()

file = open("cloud-percent.txt", "wt")
for hit in soup.findAll(attrs={'class' : 'units-cl-perc'}):
    file.write(hit.text+"\n")
file.flush()
file.close()

_3AM = datetime.time(hour=3)
_FRI = 4 # Monday=0 for weekday()

def _next_weekday(day_of_week=4, time_of_day=datetime.time(hour=3), dt=None):
    if dt is None: dt = datetime.datetime.now()
    dt += datetime.timedelta(days=7)
    if dt.time() < time_of_day: dt = dt.combine(dt.date(), time_of_day)
    else: dt = dt.combine(dt.date(), time_of_day) + datetime.timedelta(days=1)
    return dt + datetime.timedelta((day_of_week - dt.weekday()) % 7)
