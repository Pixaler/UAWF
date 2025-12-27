from win32com.client import Dispatch
from urllib.request import Request, urlopen
from playwright.sync_api import sync_playwright
import re 
from bs4 import BeautifulSoup
import pandas
import time

class RetriveInfo:
    def __init__(self) -> None:
        pass

    def soup_reader(self, url): 
        """Make url ready for Soup"""
        request_site = Request(url, headers={"User-Agent": "Mozilla/5.0"})
        page = urlopen(request_site)
        html = page.read().decode("ansi")
        soup = BeautifulSoup(html, 'lxml')
        return soup

    def get_version_number(self, app_location):
            """Obtain latest version of app that locate in provided location on Windows"""
            parser = Dispatch("Scripting.FileSystemObject")
            version = parser.GetFileVersion(app_location)
            return version

    def get_latest_version_portableapps(self, url):
        """Get latest version from link PortableApps.com on page with download button"""
        soup = self.soup_reader(url)
        latest=""
        for tag in soup.find_all("p",class_="download-info"):
            latest=re.sub(r"for.*Details$", "", tag.text)
            latest=re.sub(r"Version", "", latest)
            latest=re.sub(r" ", "", latest)
        return latest

    def get_latest_version_github(self, repo):
        """Get latest version from latest version page on GitHub"""
        soup = self.soup_reader("https://github.com" + repo + "/releases/latest")
        latest=""
        for tag in soup.find_all(href=re.compile(repo + "/releases/tag")):
            latest=re.sub(r'rel',"",tag.text)
            latest=re.sub(r'v', "", latest)
            latest=re.sub(r'\n', "", latest)
            latest=re.sub(r' ' , "", latest)
        return latest

    def get_latest_version_techspot(self, url):
        """Get latest version from page of Techspot.com with download button"""
        with sync_playwright() as p:
        # Launch browser 
            browser = p.chromium.launch(headless=True)
        
        # Create context and User-Agent
            context = browser.new_context(
                viewport={'width': 1920, 'height': 1080},
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
            )
        
            page = context.new_page()
        
            try:
            # Got to page and wait
                page.goto(url, wait_until="networkidle")
                time.sleep(2) 
            
            # Gethtml HTML
                content = page.content()
                soup = BeautifulSoup(content, 'lxml')
            
                tag = soup.find("div", class_="subver")
                if tag:
                    latest = tag.get_text(strip=True).replace("Version", "").strip()
                else:
                    print(0)
                
            except Exception as e:
                print(f"Error: {e}")
            finally:
                browser.close()
            return latest

class InformationProcessor:
    def __init__(self) -> None:
        pass

    def amount_of_prog(self, data):
        """Return amount of prog in repo.py files"""
        amount_of_prog = len(data.index)
        return amount_of_prog 

    def get_dict(self, data, bar):
        """Create dictionary with version and latetst version"""
        list_of_prog = []
        for (index, row) in data.iterrows():
            source = row["source"]
            name = row["name"]
            url = row["version_link"]
            if source == "GitHub":
                latest = RetriveInfo().get_latest_version_github(url)
            elif source == "PortableApps":
                latest = RetriveInfo().get_latest_version_portableapps(url)
            else:
                latest = RetriveInfo().get_latest_version_techspot(url)
            app_location = row["path_to_exe"]
            version = RetriveInfo().get_version_number(app_location)
            link = row["download_link"]

            list_of_prog.append(
                {
                    "name":name,
                    "version":version,
                    "latest":latest,
                    "download_link":link
                }
            ) 
            bar.next()
        return list_of_prog 
