import os, requests, pickle, html5lib
from bs4 import BeautifulSoup
import csv

url = "https://pokemondb.net/ability"
req =  requests.get(url)
soup = BeautifulSoup(req.content, 'html5lib')

file_name = 'abilities.csv'
open(file_name).close()
csv_writer = csv.writer(open(file_name,'w'))

header = True
for tr in soup.find_all('tr'):
    data = []

    if header:
        for th in tr.find_all('th'):
            line = th.text
            line = line.strip()
            #print(line)
            if 'é' in line:
                modified_line = line.replace('é', 'e')
                print("Adding this data" + modified_line)
                data.append(modified_line)
            else:
                print("Adding this data" + line)
                data.append(line)
            
        if data:
            csv_writer.writerow(data)
        data = []
        header = False

    for td in tr.find_all('td'):
        line = td.text
        line = line.strip()
        if 'é' in line:
            modified_line = line.replace('é', 'e')
            data.append(modified_line)
        else:
            data.append(line)
    
    if data:
        csv_writer.writerow(data)