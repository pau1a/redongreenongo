import requests
import datetime
import dateutil.relativedelta as reldate
from bs4 import BeautifulSoup
from dateutil.relativedelta import relativedelta
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

#Lets calculate the date of the coming Saturday at 8am

def following_saturday(dt):   
    rd=reldate.relativedelta(weekday=reldate.SA(+1),hours=+8)
    rd2=reldate.relativedelta(hour=8,minute=0,second=0,microsecond=0)
    return dt+rd+rd2

if __name__=='__main__':
    today=datetime.datetime.now()
    for dt in [today+datetime.timedelta(days=0)]:
        print(following_saturday(dt))

#Lets calculate the date of the coming Sunday at 8am

def following_sunday(dt):   
    rd=reldate.relativedelta(weekday=reldate.SU(+1),hours=+8)
    rd2=reldate.relativedelta(hour=8,minute=0,second=0,microsecond=0)
    return dt+rd+rd2

if __name__=='__main__':
    for dt in [today+datetime.timedelta(days=0)]:
        print(following_sunday(dt))
        
        
#Lets subtract the dates to get two offsets

saturday_offset = following_saturday(dt) - today
print(saturday_offset)
sunday_offset = following_sunday(dt) - today
print(saturday_offset)
print(datetime.datetime.now())

#Lets divide the offsets into a number of 3hr chunks


