import requests
from bs4 import BeautifulSoup
r = requests.get('http://www.xcweather.co.uk/forecast/Kinkell_bridge')
soup = BeautifulSoup(r.content, 'html5lib')
print(soup.prettify())