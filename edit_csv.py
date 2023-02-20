import pandas
import re
import os

class CSV_Editor():

    def __init__(self) -> None:
        pass

    def edit_table(self, data):
        """Add new program to csv table"""
        os.system('cls')
        user_choice = int(input("Source:\n\n1 - GitHub\n2 - PortableApps\n3 - Techspotn\n\nType (1, 2 or 3): "))
        name = input("\n\nType name of program: ")
        if user_choice == 1:
            source = "GitHub"
            version_link = input("\n\n\nType GitHub repo link\n\nYour input: ")
            version_link = re.sub(r'https://github.com', "", version_link)
            download_link = "https://github.com" + version_link + "/release/latest"
        elif user_choice == 2:
            source = "PortableApps"
            version_link = input("\n\n\nPaste link with download button from PortableApps\n\nYour input: ")
            download_link = version_link + "/releases/latest"
        else:
            source = "Techspot"
            version_link = input("\n\n\nPaste link with download button from TechSpot\n\nYour input: ")
            download_link = input("\n\n\nProgram just open link in browser.\n\nType download link: ")

        path_to_exe = input("\n\n\nFrom this path program try to find exe and read version.\n\nType path to exe files: ")
        new_row = pandas.DataFrame({"name": name,"version_link": version_link,"path_to_exe": path_to_exe,"download_link": download_link,"source": source}, index = [data.index[-1]+1])
        print("\n\n\nYour final data:")
        print("\n")
        print(new_row)
        confirmation = input("\n\n\nAre you cofirm addtion of new program?\ny - for yes\nn - for no\n\nYour choice: ")
        if confirmation == 'y':
            data = pandas.concat([data, new_row], axis = 0, ignore_index=True)
            return data
        else:
            return data
    def delete_row(self, data):
        """Delete program from csv table"""
        correct_name = False
        while correct_name == False:
            self.show_list(data)
            name = input("\n\nType name of program that you want to delete: ")
            for (index, row) in data.iterrows():
                if name == row["name"]:
                    print("\n\n")
                    print(row)
                    confirmation = input("\n\nAre you cofirm deletion of program?\ny - for yes\nn - for no\nYour choice: ")
                    if confirmation == 'y':
                        data = data.drop(index = [index])
                        print("Successfuly deleted")
                        return data
                    else:
                        return data

    def show_list(self, data):
        """Show name column value"""
        os.system('cls')
        return print(data.name)
