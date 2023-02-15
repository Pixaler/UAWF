from prettytable import PrettyTable
import os
import webbrowser

class OutputProcessor:
    def __init__(self) -> None:
        pass

    def create_table(self, list_of_prog):
        """Create table based on list of dictionary"""
        os.system('cls')
        th=['Name','Installed','Latest']
        table = PrettyTable(th) 

        for dict_var in list_of_prog:
            name_tb = dict_var["name"]
            version_tb = dict_var["version"]
            latest_tb = dict_var["latest"]
            table.add_row([name_tb, version_tb, latest_tb])  # Создаем строку с нашими данными
        print(table)
    
    def program_in_dict(self, list_of_prog, user_choice):
        """Check user input in list of dictionary"""
        for prog in list_of_prog:
            if prog["name"].lower() == user_choice.lower():
                down_link = prog["download_link"]
                webbrowser.open(down_link, new = 0, autoraise = True)
                return True
        return False
