import time
import webbrowser
from progress.bar import IncrementalBar
from win32com.client import Dispatch
from urllib.request import Request, urlopen
import re 
from bs4 import BeautifulSoup
from prettytable import PrettyTable
from array import *
import os


def get_version_number(app_location):
    """Obtain latest version of app that locate in provided location on Windows"""
    parser = Dispatch("Scripting.FileSystemObject")
    version = parser.GetFileVersion(app_location)
    return version

def soup_reader(url):
    """Make url ready for Soup"""
    request_site = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    page = urlopen(request_site)
    html = page.read().decode("ansi")
    soup = BeautifulSoup(html, 'lxml')
    return soup

def get_latest_version_portableapps(url):
    """Get latest version from link PortableApps.com on page with download button"""
    soup = soup_reader(url)
    latest=""
    for tag in soup.find_all("p",class_="download-info"):
        latest=re.sub(r"for.*Details$", "", tag.text)
        latest=re.sub(r"Version", "", latest)
        latest=re.sub(r" ", "", latest)
    return latest

def get_latest_version_github(repo):
    """Get latest version from latest version page on GitHub"""
    soup = soup_reader("https://github.com" + repo +"/releases/latest")
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
    """Get latest version from page of Techspot.com with download button"""
    soup = soup_reader(url)
    latest=""
    for tag in soup.find_all("span", itemprop=re.compile("softwareVersion")):
        latest=re.sub(r'\n', "", tag.text)
        latest=re.sub(r' ' , "", latest)
    return latest


dict_of_prog = {} # Create an empty list of prog


# Create/edit files

# How many programs I have 
count_prog = 0
amount_of_prog = 0

with open("C:\BATCH\!shit\App\Links.txt") as f:
    for lines in f:
        count_prog += 1
        if count_prog % 4 == 0:
            amount_of_prog += 1
    f.close()

amount_of_prog += 2


bar = IncrementalBar("Collecting data", max = amount_of_prog)
count = 1

source = ""

try:
    with open("Links.txt") as f:
        for lines in f:
            var = str(lines)
            var = re.sub(r'\n', "", var)

            if var == "GitHub" or var == "PortableApps" or var == "Techspot":
                source = var
            else:
                if count % 4 == 1:
                    name = var
            
                if count % 4 == 2:
                    url = var
                    if source == "GitHub":
                        latest = get_latest_version_github(url)
                    elif source == "PortableApps":
                        latest = get_latest_version_portableapps(url)
                    else:
                        latest = get_latest_version_techspot(url)

                if count % 4 == 3:
                    app_location = var
                    version = get_version_number(app_location)

                if count % 4 == 0:
                    link = var

                    dict_of_prog[name] = [version, latest, link]
                    bar.next()
                count += 1
    f.close()
except:
    print("\n")
    print("Links.txt are missing")


# Harcoded programs that not included in Links.txt

name = "Git"
url = "https://git-scm.com/downloads"
soup = soup_reader(url)

for tag in soup.find_all("span", class_="version"):
   latest=re.sub(r"\n", "", tag.text)
   latest=re.sub(r" ", "", latest)

app_location = r'C:\PortableApps\Git\git-bash.exe'
link = "https://git-scm.com/download/win"
version = get_version_number(app_location)

dict_of_prog[name] = [version, latest, link]

bar.next()
time.sleep(1)

name = "RivaTuner Statistics Server"
url="https://www.guru3d.com/files-details/rtss-rivatuner-statistics-server-download.html"
soup=soup_reader(url)
for tag in soup.find_all("span", itemprop="itemreviewed"):
   latest=re.sub(r"Guru3D.*Download ", "", tag.text)
   latest=re.sub(r" ", "", latest)
   latest=re.sub(r"build", ".", latest)

app_location = r'C:\PortableApps\RivaTuner Statistics Server\RTSS.exe'
version = get_version_number(app_location)
link = "https://www.guru3d.com/files-details/rtss-rivatuner-statistics-server-download.html"

dict_of_prog[name] = [version, latest, link]

bar.next()
time.sleep


bar.finish() 
time.sleep(1)

# Creation of table
os.system('cls')
th=['Name','Installed','Latest']
table = PrettyTable(th) 

for name_list in dict_of_prog:
    name_tb = name_list
    version_tb = dict_of_prog[name_list][0]
    latest_tb = dict_of_prog[name_list][1]
    table.add_row([name_tb, version_tb, latest_tb])  # Создаем строку с нашими данными

print(table)

# Menu with download links
while True:
    print(".\n.")
    menu_option = input(f"Type name of program. Type (exit) to stop: ")
    if menu_option == "exit":
        break
    try:
        # Search in dictionary name of program. Make name less sensitive to registry
        for name in dict_of_prog:
            if name.lower() == menu_option.lower():
                down_link = dict_of_prog[name][2]
        webbrowser.open(down_link, new = 0, autoraise = True)
        print(".\n.")
    except:
        print(".\n.")
        print(f"Program {menu_option} not in Links.txt. Please add this program or type program that printed in table.")