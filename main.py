import time
import webbrowser
from progress.bar import IncrementalBar
from win32com.client import Dispatch
from urllib.request import Request, urlopen
import re 
from bs4 import BeautifulSoup
from prettytable import PrettyTable
from array import *


def get_version_number(app_location):
   parser = Dispatch("Scripting.FileSystemObject")
   version = parser.GetFileVersion(app_location)
   return version

def get_latest_version(url):
    request_site = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    page = urlopen(request_site)
    html = page.read().decode("ansi")
    soup = BeautifulSoup(html, 'lxml')
    return soup

def get_latest_version_portableapps(url):
    request_site = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    page = urlopen(request_site)
    html = page.read().decode("ansi")
    soup = BeautifulSoup(html, 'lxml')
    latest=""
    for tag in soup.find_all("p",class_="download-info"):
        latest=re.sub(r"for.*Details$", "", tag.text)
        latest=re.sub(r"Version", "", latest)
        latest=re.sub(r" ", "", latest)
    return latest

def get_latest_version_github(repo):
    url = "https://github.com" + repo +"/releases/latest"
    request_site = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    page = urlopen(request_site)
    html = page.read().decode("ansi")
    soup = BeautifulSoup(html, 'lxml')
    latest=""
    for tag in soup.find_all(href=re.compile(repo + "/releases/tag")):
        latest=re.sub(r'rel',"",tag.text)
        latest=re.sub(r'v', "", latest)
        latest=re.sub(r'\n', "", latest)
        latest=re.sub(r' ' , "", latest)
        latest=re.sub(r'ci/' , "", latest)
        latest=re.sub(r'-Matrix' , "", latest)
    return latest

def get_latest_version_techspot(url):
    request_site = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    page = urlopen(request_site)
    html = page.read().decode("ansi")
    soup = BeautifulSoup(html, 'lxml')
    latest=""
    for tag in soup.find_all("span", itemprop=re.compile("softwareVersion")):
        latest=re.sub(r'\n', "", tag.text)
        latest=re.sub(r' ' , "", latest)
    return latest

class Prog(object):
    def __init__(self, name, version, latest, link):
        self.name = name
        self.version = version
        self.latest = latest
        self.link = link

    def Output(self):
        return self.name + "\t Installed: " + self.version + " Latest: " + self.latest + " Link:" + self.link

    def GetName(self):
        return self.name

    def GetVersion(self):
        return self.version

    def GetLatest(self):
        return self.latest

    def GetLink(self): 
        return self.link


list_of_prog = [] # create an empty list of prog

amount_of_prog = 31 # how many programs I have 

bar = IncrementalBar("Collecting data", max = amount_of_prog)
count = 1

with open("Github.txt") as f:
    for lines in f:
        if count % 4 == 1:
            name = str(lines)
            name = re.sub(r'\n', "", name)
        
        if count % 4 == 2:
            repo = str(lines)
            repo = re.sub(r'\n', "", repo)
            latest = get_latest_version_github(repo)

        if count % 4 == 3:
            app_location = str(lines)
            app_location = re.sub(r'\n', "", app_location)
            version = get_version_number(app_location)

        if count % 4 == 0:
            link = str(lines)
            link = re.sub(r'\n', "", link)
            name_list = Prog(name, version, latest, link)
            list_of_prog.append(name_list)
            bar.next()
        count += 1
f.close()

with open("PortableApps.txt") as f:
    for lines in f:
        if count % 4 == 1:
            name = str(lines)
            name = re.sub(r'\n', "", name)
        
        if count % 4 == 2:
            url = str(lines)
            url = re.sub(r'\n', "", url)
            latest = get_latest_version_portableapps(url)

        if count % 4 == 3:
            app_location = str(lines)
            app_location = re.sub(r'\n', "", app_location)
            version = get_version_number(app_location)

        if count % 4 == 0:
            link = str(lines)
            link = re.sub(r'\n', "", link)
                
            name_list = Prog(name, version, latest, link)
            list_of_prog.append(name_list)
            bar.next()
        count += 1
f.close()

with open("Techspot.txt") as f:
    for lines in f:
        if count % 4 == 1:
            name = str(lines)
            name = re.sub(r'\n', "", name)
        
        if count % 4 == 2:
            url = str(lines)
            url = re.sub(r'\n', "", url)
            latest = get_latest_version_techspot(url)

        if count % 4 == 3:
            app_location = str(lines)
            app_location = re.sub(r'\n', "", app_location)
            version = get_version_number(app_location)

        if count % 4 == 0:
            link = str(lines)
            link = re.sub(r'\n', "", link)
            
            name_list = Prog(name, version, latest, link)
            list_of_prog.append(name_list)
            bar.next()
        count += 1
f.close()


#Git
name = "Git"
url = "https://git-scm.com/downloads"
soup = get_latest_version(url)

for tag in soup.find_all("span", class_="version"):
   latest=re.sub(r"\n", "", tag.text)
   latest=re.sub(r" ", "", latest)

app_location = r'C:\PortableApps\Git\git-bash.exe'
version = get_version_number(app_location)

link = "https://git-scm.com/download/win"

name_list = Prog(name, version, latest, link)
list_of_prog.append(name_list)

bar.next()
time.sleep(1)

#RivaTuner Statistics Server
name = "RivaTuner Statistics Server"
url="https://www.guru3d.com/files-details/rtss-rivatuner-statistics-server-download.html"
soup=get_latest_version(url)
for tag in soup.find_all("span", itemprop="itemreviewed"):
   latest=re.sub(r"Guru3D.*Download ", "", tag.text)
   latest=re.sub(r" ", "", latest)
   latest=re.sub(r"build", ".", latest)

link = "https://www.guru3d.com/files-details/rtss-rivatuner-statistics-server-download.html"

app_location = r'C:\PortableApps\RivaTuner Statistics Server\RTSS.exe'
version = get_version_number(app_location)

name_list = name
name_list = Prog(name, version, latest, link)
list_of_prog.append(name_list)

bar.next()
time.sleep

#Spotify
name = "Spotify"
url="https://rsload.net/soft/player/34998-spotify.html"
soup=get_latest_version(url)
for tag in soup.find("a", href=re.compile(r'spotify.*.rar')):
   latest=tag.text

app_location = r'C:\PortableApps\Spotify\App\Spotify.exe'
version = get_version_number(app_location)

link = "https://rsload.net/soft/player/34998-spotify.html"

name_list = Prog(name, version, latest, link)
list_of_prog.append(name_list)

bar.next()
bar.finish() 
time.sleep(1)


#Table
print('\n')
th=['Number', 'Name','Installed','Latest']
table = PrettyTable(th) 

columns = len(th) # Подсчитаем кол-во столбцов на будущее.
number_row = 1

for name_list in list_of_prog:
    name_tb = name_list.GetName()
    version_tb = name_list.GetVersion()
    latest_tb = name_list.GetLatest()
    table.add_row([number_row, name_tb, version_tb, latest_tb])  # Создаем строку с нашими данными
    number_row += 1

print(table)

#Menu


while True:
    menu_option = input("Type number of program (from 1 to 31). Type (exit) to stop: ")
    if menu_option == "exit":
        break
    menu_option = int(menu_option)
    url = list_of_prog[menu_option - 1].GetLink()
    webbrowser.open(url, new = 0, autoraise = True)
    print("\n")