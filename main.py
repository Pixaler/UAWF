from win32com.client import Dispatch
from urllib.request import Request, urlopen
import re 
from bs4 import BeautifulSoup
from prettytable import PrettyTable

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
    page = urlopen(url)
    html = page.read().decode("ansi")
    soup = BeautifulSoup(html, 'lxml')
    latest=""
    for tag in soup.find_all("p",class_="download-info"):
        latest=re.sub(r"for.*Details$", "", tag.text)
        latest=re.sub(r"Version", "", latest)
        latest=re.sub(r" ", "", latest)
    return latest

def get_latest_version_github(url, repo):
    page = urlopen(url)
    html = page.read().decode("ansi")
    soup = BeautifulSoup(html, 'lxml')
    latest=""
    for tag in soup.find_all(href=re.compile(repo)):
        latest=re.sub("\n", "", tag.text)
        latest=re.sub(" ", "", latest)
    return latest



print("\tCollecting data...")
#AdobeAcrobatPro Portable rsload.net
url1 = "https://rsload.net/soft/big-programm/8875-adobe-acrobat-pro-v1010-rus-keygen.html"
soup=get_latest_version(url1)
for tag in soup.find_all(href=re.compile("x64 Portable")):
    latest_adobe=re.sub("x64", "", tag.text)
    latest_adobe=re.sub(r" ", "", latest_adobe)
  
app_location = r'C:\PortableApps\AcrobatPro\App\Acrobat\Acrobat.exe'
version_adobe = get_version_number(app_location)





#Autoruns
url2 = "https://docs.microsoft.com/en-us/sysinternals/downloads/autoruns"
soup=get_latest_version(url2)
for tag in soup.find_all(id=re.compile("autoruns-for-windows")):
    latest_autoruns=re.sub("Autoruns for Windows v", "", tag.text)
    latest_autoruns=re.sub(r" ", "", latest_autoruns)

app_location = r'C:\PortableApps\Autoruns\Autoruns64.exe'
version_autoruns = get_version_number(app_location)





#Discord portapps.io
url3 ="https://github.com/portapps/discord-portable/releases/latest"
repo="/portapps/discord-portable/releases/tag"

latest_discord=get_latest_version_github(url3, repo)

app_location = r'C:\PortableApps\discord-portable\app\app-1.0.9006\Discord.exe'
version_discord = get_version_number(app_location)





#Emacs
url4 ="https://www.gnu.org/savannah-checkouts/gnu/emacs/emacs.html"
soup=get_latest_version(url4)
for tag in soup.find_all('h2', id=re.compile("Releases")):
    latest_emacs=re.sub("\n", "", tag.text)
    latest_emacs=re.sub(" ", "", latest_emacs)
    latest_emacs=re.sub("Emacs", "", latest_emacs)

app_location = r'C:\PortableApps\emacs\bin\runemacs.exe'
version_emacs = get_version_number(app_location)




#Far Manager
url5 ="https://www.farmanager.com/download.php?l=en"
soup=get_latest_version(url5)

for tag in soup.find("b"):
    latest_far=re.sub("Far Manager ", "", tag.text)
    latest_far=re.sub("x86", "", latest_far)
    latest_far=re.sub(r" ", "", latest_far)
    latest_far=re.sub(r"build", ".", latest_far)
    latest_far=re.sub(r"v", "", latest_far)

app_location = r'C:\PortableApps\Far\Far.exe'
version_far = get_version_number(app_location)





#Foobar2000
url6 = "https://www.foobar2000.org/download"
soup=get_latest_version(url6)
for tag in soup.find_all("a",href=re.compile("getfile/foobar2000")):
    if tag.text == "64-bit" or tag.text == "32-bit":
        continue
    latest_foobar=re.sub("foobar2000 v", "", tag.text)
    latest_foobar=re.sub(r" ", "", latest_foobar)

app_location = r'C:\PortableApps\foobar2000\foobar2000.exe'
version_foobar = get_version_number(app_location)





#Free Download Manager Portable
url7 = "https://rsload.net/soft/manager/8984-free-download-manager.html"
soup = get_latest_version(url7)
for tag in soup.find_all("a",href=re.compile("portable-RSLOAD.NET")):
    latest_fdm=re.sub("Portable", "", tag.text)
    latest_fdm=re.sub(r" ", "", latest_fdm)

app_location = r'C:\PortableApps\FreeDownloadManager\fdm.exe'
version_fdm = get_version_number(app_location)





#FastStone Viewer
url8 = "https://portableapps.com/apps/graphics_pictures/faststone-image-viewer-portable"
latest_fsv = get_latest_version_portableapps(url8)

app_location = r'C:\PortableApps\FSViewer\FSViewer.exe'
version_fsv = get_version_number(app_location)





#GIMP
url9 = "https://portableapps.com/apps/graphics_pictures/gimp_portable"
latest_gimp = get_latest_version_portableapps(url9)

app_location = r'C:\PortableApps\GIMPPortable\App\gimp\bin\gimp-2.10.exe'
version_gimp = get_version_number(app_location)





#Git
url10 = "https://git-scm.com/downloads"
soup = get_latest_version(url10)

for tag in soup.find_all("span", class_="version"):
   latest_git=re.sub(r"\n", "", tag.text)
   latest_git=re.sub(r" ", "", latest_git)

app_location = r'C:\PortableApps\Git\git-bash.exe'
version_git = get_version_number(app_location)





#Kodi
url11="https://kodi.tv/download/windows"
soup = get_latest_version(url11)
for tag in soup.find_all("h1", class_="text-xl font-bold"):
    latest_kodi=re.sub(r" ", "", tag.text)
    latest_kodi=re.sub(r"Kodiv", "", latest_kodi)
    latest_kodi=re.sub(r'[(]Matrix[)]', "", latest_kodi)

app_location = r'C:\PortableApps\Kodi\kodi.exe'
version_kodi = get_version_number(app_location)





#MSI Afterburner
url12="https://www.guru3d.com/files-details/msi-afterburner-beta-download.html"
soup = get_latest_version(url12)

for tag in soup.find_all("span", itemprop="itemreviewed"):
   latest_msia=re.sub(r"[(]Final[)] Download", "", tag.text)
   latest_msia=re.sub(r"MSI Afterburner ", "", latest_msia)
   latest_msia=re.sub(r" ", "", latest_msia)

app_location = r'C:\PortableApps\MSI Afterburner\MSIAfterburner.exe'
version_msia = get_version_number(app_location)





#Notepad++
url13="https://notepad-plus-plus.org/downloads/"
soup=get_latest_version(url13)
for tag in soup.find_all("a", href=re.compile("/downloads")):
   latest_npp=re.sub(r"Current Version ", "", tag.text)
   latest_npp=re.sub(r" ", "", latest_npp)
   break

app_location = r'C:\PortableApps\npp\notepad++.exe'
version_npp = get_version_number(app_location)





#OBS Studio
url14="https://github.com/obsproject/obs-studio/releases/latest"
repo="/obsproject/obs-studio/releases/tag"
latest_obs=get_latest_version_github(url14,repo)

app_location = r'C:\PortableApps\OBSStudio\bin\64bit\obs64.exe'
version_obs = get_version_number(app_location)





#PotPlayer PortableApps.com
url15="https://portableapps.com/apps/music_video/potplayer-portable"
latest_pot=get_latest_version_portableapps(url15)

app_location = r'C:\PortableApps\PotPlayerPortable\App\PotPlayer\PotPlayer.dll'
version_pot = get_version_number(app_location)





# Process Explorer
url16="https://docs.microsoft.com/en-us/sysinternals/downloads/process-explorer"
soup=get_latest_version(url16)

app_location = r'C:\PortableApps\ProcessExplorer\procexp64.exe'
version_pe = get_version_number(app_location)
for tag in soup.find_all("h1"):
   latest_pe=re.sub(r"Process Explorer v", "", tag.text)
   latest_pe=re.sub(r" ", "", latest_pe)
   latest_pe=re.sub(r'Build', ".", latest_pe)







# Psiphon 
url17 = "https://rsload.net/soft/traffic/33341-psiphon.html"
soup=get_latest_version(url17)
for tag in soup.find_all("a", href=re.compile("/psiphon_3")):
   latest_psiphon=re.sub(r" Build ", ".", tag.text)

app_location = r'C:\PortableApps\Psiphon\App\AppInfo\AppInfo.ini'
pattern="PackageVersion="
with open(app_location, "r") as file:
    for line in file:
      if pattern not in line:
        continue
      else:
        version_psiphon=re.sub(r"PackageVersion=", "", line)
        version_psiphon=re.sub(r"\n", "", version_psiphon)








#qBittorrent
url18="https://github.com/portapps/qbittorrent-portable/releases/latest"
repo="/portapps/qbittorrent-portable/releases/tag"
latest_qbt=get_latest_version_github(url18,repo)

app_location = r'C:\PortableApps\qbittorrent-portable\app\qbittorrent.exe'
version_qbt = get_version_number(app_location)





#Reaper
url19="https://www.reaper.fm/download.php"
soup=get_latest_version(url19)
for tag in soup.find("div", class_=re.compile("downloadinfo")):
   if "REAPER" not in tag:
      continue
   latest_reaper=re.sub(r'-.*MB',"",tag.text)
   latest_reaper=re.sub(r'R.*v',"",latest_reaper)
   latest_reaper=re.sub(r'\n',"",latest_reaper)

app_location = r'C:\PortableApps\REAPER\reaper.exe'
version_reaper = get_version_number(app_location)




#RivaTuner Statistics Server
url20="https://www.guru3d.com/files-details/rtss-rivatuner-statistics-server-download.html"
soup=get_latest_version(url20)
for tag in soup.find_all("span", itemprop="itemreviewed"):
   latest_rtss=re.sub(r"Guru3D.*Download ", "", tag.text)
   latest_rtss=re.sub(r" ", "", latest_rtss)
   latest_rtss=re.sub(r"build", ".", latest_rtss)

app_location = r'C:\PortableApps\RivaTuner Statistics Server\RTSS.exe'
version_rtss = get_version_number(app_location)




#Rufus
url21="https://github.com/pbatard/rufus/releases/latest"
repo="/pbatard/rufus/releases/tag"
latest_rufus=get_latest_version_github(url21, repo)

app_location = r'C:\PortableApps\Rufus\rufus.exe'
version_rufus = get_version_number(app_location)





#Shotcut PortableApps.com
url22="https://portableapps.com/apps/music_video/shotcut-portable"
latest_shotcut=get_latest_version_portableapps(url22)

app_location = r'C:\PortableApps\ShotcutPortable\App\Shotcut64\shotcut.exe'
version_shotcut = get_version_number(app_location)




#SoftmakerOffice
url23="https://rsload.net/soft/document/16292-softmaker-office-professional.html"
soup=get_latest_version(url23)
for tag in soup.find("a", href=re.compile(r'x32.*Portable RSLOAD.NET')):
   latest_office=tag.text

app_location = r'C:\PortableApps\SoftMakerOffice\App\SoftMaker Office 2021\TextMaker.exe'
version_office = get_version_number(app_location)





#Spotify
url24="https://rsload.net/soft/player/34998-spotify.html"
soup=get_latest_version(url24)
for tag in soup.find("a", href=re.compile(r'spotify.*.rar')):
   latest_spotify=tag.text

app_location = r'C:\PortableApps\Spotify\App\Spotify.exe'
version_spotify = get_version_number(app_location)





#Sumatra
url25="https://github.com/sumatrapdfreader/sumatrapdf/releases/latest"
repo="sumatrapdfreader/sumatrapdf/releases/tag"
latest_sumatra=get_latest_version_github(url25, repo)
latest_sumatra=re.sub(r'rel',"",latest_sumatra)

app_location = r'C:\PortableApps\SumatraPDF\SumatraPDF.exe'
version_sumatra = get_version_number(app_location)




#TeamViewer
url26="https://portableapps.com/apps/utilities/teamviewer_portable"
latest_teamviewer=get_latest_version_portableapps(url26)

app_location = r'C:\PortableApps\TeamViewerPortable\App\teamviewer\TeamViewer.exe'
version_teamviewer = get_version_number(app_location)




#VSCode
url27="https://code.visualstudio.com/"
soup=get_latest_version(url27)
for tag in soup.find("a", id=re.compile("banner-link-updates")):
   latest_vscode=tag.text
   latest_vscode=re.sub(r'Version ',"",latest_vscode)

app_location = r'C:\PortableApps\VSCode\Code.exe'
version_vscode = get_version_number(app_location)






#WinCDEmu PortableApps.com
url28="https://portableapps.com/apps/utilities/wincdemu-portable"
latest_cd=get_latest_version_portableapps(url28)

app_location = r'C:\PortableApps\WinCDEmuPortable\App\WinCDEmu\PortableWinCDEmu-x.x.exe'
version_cd = get_version_number(app_location)





#WinRAR
url29="https://www.win-rar.com/download.html?&L=0"
soup=get_latest_version(url29)
for tag in soup.find("span", class_=re.compile("dwn-btn")):
      latest_winrar=tag.text
      latest_winrar=re.sub(r'WinRAR ',"",latest_winrar)
      latest_winrar=re.sub(r' English 64 bit',"",latest_winrar)

app_location = r'C:\PortableApps\WinRAR\WinRAR.exe'
version_winrar = get_version_number(app_location)





#WizTree
url30="https://www.majorgeeks.com/files/details/wiztree.html"
soup=get_latest_version(url30)
for tag in soup.find("a", href=re.compile("files/details/wiztree.html")):
      latest_wiztree=tag.text
      latest_wiztree=re.sub(r' ',"",tag.text)
      latest_wiztree=re.sub(r'WizTree',"",latest_wiztree)

app_location = r'C:\PortableApps\WizTree\WizTree64.exe'
version_wiztree = get_version_number(app_location)


#Table
th=['Name','Installed','Latest']
td=['AdobeAcrobatPro', version_adobe, latest_adobe,
    'Autoruns', version_autoruns, latest_autoruns,
    'Discord', version_discord, latest_discord,
    'Emacs', version_emacs, latest_emacs,
    'Far Manager', version_far, latest_far,
    'foobar2000', version_foobar, latest_foobar,
    'Free Download Manager', version_fdm, latest_fdm,
    'FastStone', version_fsv, latest_fsv,
    'GIMP', version_gimp, latest_gimp,
    'Git', version_git, latest_git,
    'Kodi', version_kodi, latest_kodi,
    'MSI Afterburner', version_msia, latest_msia,
    'Notepad+++', version_npp, latest_npp,
    'OBS Studio', version_obs, latest_obs,
    'PotPlayer', version_pot, latest_pot,
    'Process Explorer', version_pe, latest_pe,
    'Psiphon', version_psiphon, latest_psiphon,
    'qBitttorent', version_qbt, latest_qbt,
    'Reaper', version_reaper, latest_reaper,
    'RivaTuner Statistics Server', version_rtss, latest_rtss,
    'Rufus', version_rufus, latest_rufus,
    'ShotCut', version_shotcut, latest_shotcut,
    'SoftmakerOffice', version_office, latest_office,
    'Spotify', version_spotify, latest_spotify,
    'Sumatra', version_sumatra, latest_sumatra,
    'TeamViewer', version_teamviewer, latest_teamviewer,
    'VSCode', version_vscode, latest_vscode,
    'WinCDEmu', version_cd, latest_cd,
    'WinRAR', version_winrar, latest_winrar,
    'WizTree', version_wiztree, latest_wiztree]


columns = len(th) # Подсчитаем кол-во столбцов на будущее.

table = PrettyTable(th)  # Определяем таблицу

td_data = td[:] # Cкопируем список td, на случай если он будет использоваться в коде дальше.

while td_data:
    table.add_row(td_data[:columns])  # Используя срез добавляем первые пять элементов в строку.
    td_data = td_data[columns:] # Используя срез переопределяем td_data так, чтобы он больше не содержал первых 5 элементов.

print(table)
