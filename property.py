import requests
import pandas as pd
from bs4 import BeautifulSoup


property = []

url = 'https://bdproperty.com/properties-row-template/page/2/'
pages = requests.get(url)
soup = BeautifulSoup(pages.content, 'html.parser')
lists = soup.find_all('div', class_= 'property-row-content')
for list in lists:
    name =list.find('a').text
    location=list.find('div', class_='property-row-location').text
    type =list.find_all('div', class_='property-row-meta-item')[0].text
    price =list.find_all('div', class_='property-row-meta-item')[1].text
    area =list.find_all('div', class_='property-row-meta-item')[2].text
    bed =list.find_all('div', class_='property-row-meta-item')[3].text
    bath =list.find_all('div', class_='property-row-meta-item')[4].text
    toLet =list.find_all('div', class_='property-row-meta-item')[5].text
    property.append([name, location, type, price, area, bed, bath, toLet])
    
    
print(property)
