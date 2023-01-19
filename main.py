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

PATH_TO_TXT = "Links.txt"

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

def amount_of_prog():
    """Return amount of prog in txt files"""
    count_prog = 0
    amount_of_prog = 0
    with open(PATH_TO_TXT) as f:
        for lines in f:
            count_prog += 1
            if count_prog % 4 == 0:
                amount_of_prog += 1
        f.close()
    return amount_of_prog

def get_dict(bar):
    try:
        dict_of_prog = {}
        count = 1
        with open(PATH_TO_TXT) as f:
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
        return dict_of_prog
    except:
        print("\n")
        print("Links.txt are missing")

def create_table(dict_of_prog):
    os.system('cls')
    th=['Name','Installed','Latest']
    table = PrettyTable(th) 

    for name_list in dict_of_prog:
        name_tb = name_list
        version_tb = dict_of_prog[name_list][0]
        latest_tb = dict_of_prog[name_list][1]
        table.add_row([name_tb, version_tb, latest_tb])  # Создаем строку с нашими данными

    print(table)

def main():
    # Create/edit files

    amount = amount_of_prog() # Amount of program

    bar = IncrementalBar("Collecting data", max = amount)

    dict_of_prog = get_dict(bar)# Create a list of prog

    bar.finish() 
    time.sleep(1)

    create_table(dict_of_prog) # Creation of table

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

if __name__ == "__main__":
    main()