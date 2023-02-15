# UAWF
Program, that update my portable apps on Windows (Update Apps Without F@#k)

## Feature
- Grab apps version from sites, check version apps on your PC and output this data
- Now program can open sites. Personal I put in this files web page with download link

## Using
1. Unzip archive
2. Run program

## Edit repo.csv file
You can it do with program, but faster do it manualy. Open in spreadsheet viewer and edit column in that way. 
  ---|name| version_link | path_to_exe | download_link | source
  ---|---|---|---|---|---
  0  |Far Manager | /FarGroup/FarManager | C:\PortableApps\Far\Far.exe | https://github.com/FarGroup/FarManager/releases/latest | GitHub

first column - number of string, starting with 0
- name - name of program
- version_link: 
  - For GitHub.   */<'user_name'>/<'repo'>*   format: /Pixaler/UAWF
  - For PortableApps. Webpage with download button: https://portableapps.com/apps/development/gvim_portable
  - For TechSpot. Webpage with download button: https://www.techspot.com/downloads/7142-visual-studio-code.html
- path_to_exe - path to your exe file that contain FileVersion
- download_link - that link will be open in your browser
- source - Which source you use: GitHub, PortableApps or TechSpot. Registry sensitive.
