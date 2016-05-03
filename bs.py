import requests
import datetime
import dateutil.relativedelta as reldate
import time
from bs4 import BeautifulSoup
from dateutil.relativedelta import relativedelta
r = requests.get('https://www.windfinder.com/forecast/strathallen_airfield')
soup = BeautifulSoup(r.content, 'html5lib')

#Now we extract the individual parameters to separate files
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
from itertools import islice
def yield_alt(f, option='odd'):
        if option == 'odd':
            return islice(f, 0, None, 2)
        return islice(f, 1, None, 2)
with open('windspeeds.txt') as f:
    for line in yield_alt(f):      
        print (line)

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
        print("Date and time of next Saturday 8 am is: %s" % following_saturday(dt))

#Lets calculate the date of the coming Sunday at 8am

def following_sunday(dt):   
    rd=reldate.relativedelta(weekday=reldate.SU(+1),hours=+8)
    rd2=reldate.relativedelta(hour=8,minute=0,second=0,microsecond=0)
    return dt+rd+rd2

if __name__=='__main__':
    for dt in [today+datetime.timedelta(days=0)]:
        print("Date and time of next Sunday 8 am is: %s" % following_sunday(dt))
        
        
#Lets subtract the dates to get two offsets

saturday_offset = following_saturday(dt) - today
print("Number of seconds until 8am next Saturday is: %s" % saturday_offset.total_seconds())
sunday_offset = following_sunday(dt) - today
print("Number of seconds until 8am next Sunday is: %s" % sunday_offset.total_seconds())

#how many slots to ignore

saturday_ignore_slots = saturday_offset.total_seconds() / 10800
int_saturday_ignore_slots = int(round(saturday_ignore_slots) + (time.localtime().tm_hour/3))
print("Number of timeslots to ignore until 8am next Saturday is: %s" % int_saturday_ignore_slots)

sunday_ignore_slots = sunday_offset.total_seconds()/10800
int_sunday_ignore_slots = int(round(sunday_ignore_slots) + (time.localtime().tm_hour/3))
print("Number of timeslots to ignore until 8am next Sunday is: %s" % int_sunday_ignore_slots)

fp = open("sat_temperatures.txt","w")
for i,line in enumerate(open("temperatures.txt")):
    if i >= (int_saturday_ignore_slots - 1) and i < (int_saturday_ignore_slots + 4) :
        fp.write(line)
file.close()

fp = open("sun_temperatures.txt","w")
for i,line in enumerate(open("temperatures.txt")):
    if i >= (int_sunday_ignore_slots - 1) and i < (int_sunday_ignore_slots + 4) :
        fp.write(line)
file.close()