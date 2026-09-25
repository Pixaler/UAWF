from prettytable import PrettyTable
import os

class OutputProcessor:
    def __init__(self) -> None:
        pass

    def create_table(self, list_of_prog):
        """Create table based on list of dictionary"""
        os.system('cls')
        th=['n','Name','Installed','Latest']
        table = PrettyTable(th) 

        for dict_var in list_of_prog:
            index_tb = list_of_prog.index(dict_var)+1
            name_tb = dict_var.name
            version_tb = dict_var.current_version
            latest_tb = dict_var.latest_version
            table.add_row([index_tb, name_tb, version_tb, latest_tb])  # Создаем строку с нашими данными
        print(table)
