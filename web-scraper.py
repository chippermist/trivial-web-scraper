# import libraries
import urllib2
from bs4 import BeautifulSoup
# import csv library to export to excel
import csv
from datetime import datetime
import re

# specify the url
url_page = 'https://chinmaygarg.com'

# query the website and return the html code
page = urllib2.urlopen(url_page)

# parse the html code using beautiful soup
soup = BeautifulSoup(page, 'html.parser')

# find the <div> section in the html using soup
name_box = soup.find('span', attrs={'class': 'label'})

# strip the data by using the strip()
name = name_box.text.strip()
#print name

# make name a list
name = []

# doing the same thing in a loop to find all
for i in soup('span', 'label'):
	name.append(str(i.text.strip()))

print name

# open a csv file so it can be written
with open('parser.csv', 'a') as csv_file:
	writer = csv.writer(csv_file)
	writer.writerow([name])