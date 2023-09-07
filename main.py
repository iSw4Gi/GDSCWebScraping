# Author : @iSw4Gi = Nader Alharbi
# GDSC Web Scraping 
# Analys & Web Grapping 



# Importing Libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd

# Getting The WebSite Source
source = requests.get('https://gdsc.community.dev/tabuk-university/').text

# Soup The Page as lxml
soup = BeautifulSoup(source, 'lxml')

# Creating Data Rows 
titles = []
infos = []
dates = []


# Getting All data Attribute As a list
title_elements = soup.find_all('p', class_='event-page vertical-box--event-title')
for title in title_elements:
    titles.append(title.text.strip())

info_elements = soup.find_all('p', class_='event-page vertical-box--event-type')
for info in info_elements:
    infos.append(info.text.strip())

date_elements = soup.find_all('p', class_='vertical-box--event-date')
for date in date_elements:
    dates.append(date.text.strip())

# Ensure all lists have the same length
min_length = min(len(titles), len(infos), len(dates))
titles = titles[:min_length]
infos = infos[:min_length]
dates = dates[:min_length]

# Creating Data Frame
df = pd.DataFrame({'title': titles, 'info': infos, 'date': dates})

# Export Data to Excel file
df.to_csv('data.csv')