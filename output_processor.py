from prettytable import PrettyTable
import os
import webbrowser

class OutputProcessor:
    def __init__(self) -> None:
        pass

    def create_table(self, list_of_prog):
        """Create table based on list of dictionary"""
        os.system('cls')
        th=['n','Name','Installed','Latest']
        table = PrettyTable(th) 

        for dict_var in list_of_prog:
            index_tb = dict_var["index"]+1
            name_tb = dict_var["name"]
            version_tb = dict_var["version"]
            latest_tb = dict_var["latest"]
            table.add_row([index_tb, name_tb, version_tb, latest_tb])  # Создаем строку с нашими данными
        print(table)
    
    def program_in_dict(self, list_of_prog, user_choice):
        """Check user input in list of dictionary"""

        down_link = list_of_prog[user_choice-1]["download_link"]
        webbrowser.open(down_link, new=0, autoraise = True)
        return True
