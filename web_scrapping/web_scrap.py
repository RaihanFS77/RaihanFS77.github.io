# list imported package
import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

# request to website
page = requests.get("https://www.republika.co.id/")

# define variabel
obj = BeautifulSoup(page.text, 'html.parser')
divtag = obj.find_all('div', class_='conten1')
data = []
now = datetime.now()

print('Menampilkan objek html')
print('======================')
print(obj)
print('\nMenampilkan title browser dengan tag')
print('================================')
print(obj.title)
print(obj.title.text)
print(obj.find_all('h2'))
for headline in obj.find_all('h2'):
    print(headline.text)
print(obj.find_all('div', class_='conten1'))

for headline in divtag:
    print(headline.find('h2').text)
createnote = open(
    'E:\Mahastudent\Semester 2\Tugas\Proyek 1 Pengembangan Perangkat Lunak Desktop\Minggu 6\web scrapping\headline.txt', 'w')
for headline in divtag:
    createnote.write(headline.find('h2').text)
    createnote.write(' (')
    datetag = headline.find('div', class_='date')
    createnote.write(datetag.text)
    createnote.write(')\n')
createnote.close()
createJson = open(
    'E:\Mahastudent\Semester 2\Tugas\Proyek 1 Pengembangan Perangkat Lunak Desktop\Minggu 6\web scrapping\headline.json', 'w')
for headline in divtag:
    kategori = headline.find('div', class_='teaser_conten1_center')
    data.append({"Judul": headline.find('h2').text,
                 "Kategori": kategori.find('a').text,
                 "Waktu_publish": headline.find('div', class_='date').text,
                 "Waktu_scrapping": now.strftime("%d/%m/%Y %H:%M:%S")})
jdumps = json.dumps(data, indent=2)
createJson.writelines(jdumps)
createJson.close()
