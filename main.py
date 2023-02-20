import time
from pandas._libs.hashtable import duplicated
from progress.bar import IncrementalBar
from get_version import InformationProcessor
from output_processor import OutputProcessor
from edit_csv import CSV_Editor
import pandas
import sys
import os


def main():
    art = '''
    ██╗   ██╗ █████╗ ██╗    ██╗███████╗
    ██║   ██║██╔══██╗██║    ██║██╔════╝
    ██║   ██║███████║██║ █╗ ██║█████╗  
    ██║   ██║██╔══██║██║███╗██║██╔══╝  
    ╚██████╔╝██║  ██║╚███╔███╔╝██║     
     ╚═════╝ ╚═╝  ╚═╝ ╚══╝╚══╝ ╚═╝     
    '''

    worker = InformationProcessor()

    editor = CSV_Editor()

    csv_path = "repo.csv"

    # determine if application is a script file or frozen exe
    if getattr(sys, 'frozen', False):
        application_path = os.path.dirname(sys.executable)
    elif __file__:
        application_path = os.path.dirname(__file__)
    
    REPO = os.path.join(application_path, csv_path)
    
    try:
        data = pandas.read_csv(REPO, index_col=[0])
    except FileNotFoundError:
        first_repo={"name":"UAWF", "version_link":"/Pixaler/UAWF", "path_to_exe": "C:\\PortableApps\\UAWF\\uawf.exe", "download_link": "https://github.com/Pixaler/UAWF/releases/latest", "source":"GitHub" }
        new_data = pandas.DataFrame(first_repo, index=[0])
        new_data.to_csv(csv_path)
    finally:
        data = pandas.read_csv(REPO, index_col=[0])
    want_edit = True
    while want_edit:
        os.system('cls')
        print(art)
        choice = input('''Version: 0.6.3\n
a - add new program
d - delete program
s - show list
l - launch program
e - exit program\n

Choose option: ''' )
        if choice == 'a':
            data = editor.edit_table(data)
            new_data = pandas.DataFrame(data)
            new_data = new_data.reset_index(drop=True)
            new_data.to_csv(REPO)
        elif choice == 'd':
            data = editor.delete_row(data)
            new_data = pandas.DataFrame(data)
            new_data = new_data.reset_index(drop=True)
            new_data.to_csv(REPO)
        elif choice == 's':
            editor.show_list(data)
        elif choice == 'e':
            exit()
        elif choice == 'l':
            want_edit = False
            break
        else:
            print("Wrong options!")
            pass
        go_on = input("\n\nYou want to edit again? (y/n): ")
        if go_on == 'n':
            want_edit = False

    amount = worker.amount_of_prog(data) # Amount of program
    os.system('cls')
    bar = IncrementalBar("Collecting data", max = amount)
 
    list_of_prog = worker.get_dict(data, bar) # Create a list of prog
    bar.finish() 
    time.sleep(1)
 
    gui_worker = OutputProcessor()
    gui_worker.create_table(list_of_prog) # Creation of table
     
     # Menu with download links
    while True:
        print(".\n.")
        menu_option = input(f"Type name of program. Type (exit) to stop: ")
        if menu_option == "exit":
            break
        # Search in dictionary name of program. Make name less sensitive to registry
        check = gui_worker.program_in_dict(list_of_prog, menu_option)
        if not check:
            print(".\n.")
            print(f"Program '{menu_option}' not in list. Please type correct name or add this program to repo.py")
if __name__ == "__main__":
    main()
