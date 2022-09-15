# UAWF
Program, that update my portable apps on Windows (Update Apps Without F@#k)

## Feature
- Grab apps version from sites, check version apps on your PC and output this data
- Now program can open sites. Personal I put in this files web page with download link

## How create .txt files 
Program can grub latest version from 3 sources: Github, PortableApps, Techspot. Structure of contets in Github.txt slightly diffrent from PortableApps.txt and Techspot.txt.

Example for Github.txt
```
Discord # 1 line: Name of program, choose what you want
/portapps/discord-portable # 2 line: Repository of Github. Example: for https://github.com/Pixaler/UAWF repo will be /Pixaler/UAWF.
C:\PortableApps\discord-portable\app\app-1.0.9006\Discord.exe # 3 line: Path to .exe that conatin a file version
https://github.com/portapps/discord-portable/releases/latest # 4 line: web page with download link
# And continue fill your file line by line. Importatnt: don't leave empty lines, that lead to wrong output.
```

Example for PortableApps.txt
```
PDF-XChange Editor # 1 line: Name of program, choose what you want
https://portableapps.com/apps/office/pdf-xchange-editor-portable # 2 line: Url on website. If you put link from PortableApp.com, check if this looks like that.
C:\PortableApps\PDFXChangeEditor\PDFXEdit.exe # 3 line: Path to .exe that conatin a file version
https://www.tracker-software.com/product/pdf-xchange-editor # 4 line: web page with download link
# And continue fill your file line by line. Importatnt: don't leave empty lines, that lead to wrong output.
```

Example for Techspot.txt
```
Autoruns # 1 line: Name of program, choose what you want
https://www.techspot.com/downloads/2879-autoruns.html # 2 line: Url on website. If you put link from Techspot.com, check if this looks like that.
C:\PortableApps\Autoruns\Autoruns64.exe # 3 line: Path to .exe that conatin a file version
https://docs.microsoft.com/en-us/sysinternals/downloads/autoruns # 4 line: web page with download link
# And continue fill your file line by line. Importatnt: don't leave empty lines, that lead to wrong output.
```

## Using
1. Unzip archive
2. Edit .txt files for your prefrences
3. Run program
