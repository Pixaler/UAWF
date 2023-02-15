import pandas
import re

class CSV_Editor():

    def __init__(self) -> None:
        pass

    def edit_table(self, data):
        """Add new program to csv table"""
        user_choice = int(input("Source:\n1 - GitHub\n2 - PortableApps\n3 - Techspot\nType (1, 2 or 3): "))
        name = input("Type name of program: ")
        if user_choice == 1:
            source = "GitHub"
            version_link = input("Type username/repo_name from GitHub or just past repo link\nYour input: ")
            version_link = re.sub(r'https://github.com', "", version_link)
            download_link = "https://github.com" + version_link + "/releases/latest"
        elif user_choice == 2:
            source = "PortableApps"
            version_link = input("Paste link with download button from PortableApps\nYour input: ")
            download_link = version_link
        else:
            source = "Techspot"
            version_link = input("Paste link with download button from TechSpot\nYour input: ")
            download_link = input("Program just open link in browser.\nType download link: ")

        path_to_exe = input("From this path program try to find exe and read version.\nType path to exe files: ")
        new_row = pandas.DataFrame({"name": name,"version_link": version_link,"path_to_exe": path_to_exe,"download_link": download_link,"source": source}, index = [data.index[-1]+1])
        data = pandas.concat([data, new_row], axis = 0, ignore_index=True)
        return data

    def delete_row(self, data):
        """Delete program from csv table"""
        correct_name = False
        while correct_name == False:
            name = input("Type name of program that you want to delete: ")
            for (index, row) in data.iterrows():
                if name == row["name"]:
                    data = data.drop(index = [index])
                    print("Successfuly deleted")
                    return data



        
