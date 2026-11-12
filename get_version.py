from urllib.error import HTTPError
import win32api
from urllib.request import Request, urlopen, urlretrieve
import urllib.parse
from bs4 import BeautifulSoup
import os
import re
import ssl
import certifi


class ProgramData:
    def __init__(self, name, download_link, current_version, latest_version):
        self.name = name
        self.download_link = download_link
        self.current_version = current_version
        self.latest_version = latest_version


class RetriveInfo:
    def __init__(self) -> None:
        pass

    def download_from_portableapps(self, download_link, app_location):

        soup = self.soup_reader(download_link)
        tag = soup.find('a', style="display:block;width:313px;height:66px;border-radius:4px;padding:15px 17px 17px;color:white;font-family:Arimo;font-size:14px;text-decoration:none;box-sizing: border-box;text-align: left;background-color: #197f19;") 
        link_to_parse = urllib.parse.quote("https://portableapps.com" + str(tag.get('href')), safe='')
        print(link_to_parse)

        soup = self.soup_reader(link_to_parse)
        tag = soup.find('a', rel="nofollow")
        link_to_download = "https://portableapps.com" + str(tag.get('href'))

        filename = re.search(r"f=([^&]+)", link_to_download).group(1)
        urlretrieve(link_to_download, app_location + filename)
        print(f"Download {filename}")

        

    def get_current_version(self, app_location):
        """Obtain latest version of app that locate in provided location on Windows"""
        if os.path.exists(app_location):
            info = win32api.GetFileVersionInfo(app_location,"\\")

            ms=info['FileVersionMS']
            ls=info['FileVersionLS']

            major = win32api.HIWORD(ms)
            minor = win32api.LOWORD(ms)
            build = win32api.HIWORD(ls)
            revision = win32api.LOWORD(ls)

            current_version = f"{major}.{minor}.{build}.{revision}"
        else:
            print("\nApp location is incorrect or not exist:", app_location)
            current_version = "Not found"
        
        return current_version 

    def soup_reader(self, url): 
        """Make url ready for Soup"""
        os.environ['SSL_CERT_FILE'] = certifi.where()
        request_site = Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'})
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
        
    def compare_versions(self, current_version, latest_version):
        latest_version_list = list(int(y) for y in latest_version.split('.')) 
        latest_version_str = ''.join(map(str,latest_version_list))

        current_version_str = current_version.replace('.','')[:len(latest_version_str)]        

        current_version_hash = int(current_version_str)
        latest_version_hash = int(latest_version_str)

        if latest_version_hash > current_version_hash:
            return True
        else: 
            return False
        
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
            if current_version != "Not found":
                latest_version = RetriveInfo().get_latest_version(row["version_link"])
                if RetriveInfo().compare_versions(current_version, latest_version):
                    program = ProgramData(row["name"], row["download_link"], current_version, latest_version)            
                    list_of_prog.append(program) 
            bar.next()

        return list_of_prog 
