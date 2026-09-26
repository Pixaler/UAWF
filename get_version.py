from ssl import get_default_verify_paths
from urllib.error import HTTPError

from win32com.client import Dispatch
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import os
import re


class ProgramData:
    def __init__(self, name, download_link, current_version, latest_version):
        self.name = name
        self.download_link = download_link
        self.current_version = current_version
        self.latest_version = latest_version


class RetriveInfo:
    def __init__(self) -> None:
        pass

    def get_current_version(self, app_location):
        """Obtain latest version of app that locate in provided location on Windows"""
        if os.path.exists(app_location):
            parser = Dispatch("Scripting.FileSystemObject")
            current_version = parser.GetFileVersion(app_location)
        else:
            print("\nApp location is incorrect or not exist:", app_location)
            current_version = "Not found"
        
        return current_version 

    def soup_reader(self, url): 
        """Make url ready for Soup"""
        request_site = Request(url, headers={"User-Agent": "Mozilla/5.0"})
        try:
            page = urlopen(request_site)
            html = page.read().decode("ansi")
            soup = BeautifulSoup(html, 'lxml')
            return soup
        except HTTPError:
            print(HTTPError)

    def get_latest_version(self, version_link):
        soup = self.soup_reader(version_link)
        if version_link.find("portableapps") > 0:
            tag = soup.find('p', class_="download-info") 
        elif version_link.find("techspot") > 0:
            tag = soup.find('div', class_="subver")
        else:
            new_version_link = version_link.removeprefix("https://github.com")
            new_version_link = new_version_link.replace("/latest", "/tag")
            tag = soup.find('a',href=re.compile(new_version_link))
        text = tag.get_text()
        latest = re.search(r'\d+(?:\.\d+)+', text).group(0)
        
        return latest


        
class InformationProcessor:
    def __init__(self) -> None:
        pass

    def amount_of_prog(self, data):
        """Return amount of prog in repo.csv files"""
        amount_of_prog = len(data.index)
        return amount_of_prog 

    def get_dict(self, data, bar):
        """Create dictionary with version and latest version"""
        list_of_prog = []
        for (index, row) in data.iterrows():
            current_version = RetriveInfo().get_current_version(row["path_to_exe"])
            latest_version = RetriveInfo().get_latest_version(row["version_link"])
            program = ProgramData(row["name"], row["download_link"], current_version, latest_version)            

            list_of_prog.append(program) 
            bar.next()

        return list_of_prog 
