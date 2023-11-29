import os, requests, pickle, html5lib
from bs4 import BeautifulSoup
import csv


url = "https://pokemondb.net/move/generation/"
# req = requests.get(url)
# print(req)

# soup = BeautifulSoup(req.content, 'html5lib')
generation = [1,2,3,4,5,6,7,8,9]
filename = ['Generation1.csv', 'Generation2.csv', 'Generation3.csv', 'Generation4.csv', 'Generation5.csv', 'Generation6.csv',
             'Generation7.csv', 'Generation8.csv', 'Generation9.csv']

new_filename = 'Moves.csv'
csv_writer = csv.writer(open(new_filename,'w'))
#csv.writer(open(new_filename, 'w'))
# heading = soup.find('h1')
# print(heading.text)
header = True
for gen in generation:
    # print(filename[gen-1])

    # csv_writer = csv.writer(open(filename[gen-1],'w'))
    new_url = url + str(gen)
    req =  requests.get(new_url)
    soup = BeautifulSoup(req.content, 'html5lib')

    for tr in soup.find_all('tr'):
        data = []
        
        if header:
            # Getting each header for the table
            for th in tr.find_all('th'):
                data.append(th.text)
            data.append('Gen')
            header = False
            # Add it to the csv file
            if data:
                print("Inserting headers to" + new_filename + " : {}".format(','.join(data)))
                csv_writer.writerow(data)
                continue
        
        for td in tr.find_all('td'):
            # Check what type of cell it is, if its an image of special, physical or status attack
            if "cell-icon" in td['class'] and "text-center" in td['class']:
                # Add the value of either special, pysical or status to the csv
                if td['data-sort-value']:
                    data.append(td['data-sort-value'].strip())
            
            # We check if there's an infinity symbol, if yes
            # then replace it with 101
            elif "cell-num" in td['class'] and "num-infinity" in td['class']:
                data.append("101")
            # Check if there is none or dash symbol, if yes
            # then change it to a zero
            elif  td.text == "—" :
                data.append("0")
            else: # Add everything normally as it is
                line = td.text.replace('"', '')
                line = line.strip()
                modified_line = line.replace('é', 'e')
                data.append(modified_line)

        if data:
            data.append(str(gen))
            csv_writer.writerow(data)
    print("File written to : " + filename[gen-1])