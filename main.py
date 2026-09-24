import time
from pandas._libs.hashtable import duplicated
from progress.bar import IncrementalBar
from get_version import InformationProcessor, RetriveInfo
from output_processor import OutputProcessor
from edit_csv import CSV_Editor
import pandas
import sys
import os


def save_data_to_csv(data, REPO):
    new_data = pandas.DataFrame(data)
    new_data = new_data.reset_index(drop=True)
    new_data.to_csv(REPO)
        

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
    VERSION_APP = RetriveInfo().get_version_number(sys.executable)
    
    try:
        data = pandas.read_csv(REPO, index_col=[0])
    except FileNotFoundError:
        first_repo={"name":"UAWF", "version_link":"/Pixaler/UAWF", "path_to_exe": "C:\\PortableApps\\UAWF\\uawf.exe", "download_link": "https://github.com/Pixaler/UAWF/releases/latest", "source":"GitHub" }
        new_data = pandas.DataFrame(first_repo, index=[0])
        new_data.to_csv(csv_path)
    finally:
        data = pandas.read_csv(REPO, index_col=[0])

    stay_in_menu = True
    while stay_in_menu:
        
        os.system('cls')

        print(art)
        print("Version: {}\n".format(VERSION_APP))
        editor.main_menu()
        
        choice = editor.check_answer(len(editor.main_menu_list), "\nChoose your option: ")
        selected_option = editor.main_menu_list[choice-1]

        if selected_option == 'add new program':
            data = editor.add_new_program(data)
            save_data_to_csv(data, REPO)
        elif selected_option == 'delete program':
            data = editor.delete_row(data)
            save_data_to_csv(data, REPO)
        elif selected_option == 'show list':
            editor.show_list(data)
        elif selected_option == 'edit table':
            data = editor.edit_program(data)
            save_data_to_csv(data, REPO)
        elif selected_option == 'start update':
            stay_in_menu = False
            break
        else:
            sys.exit()
        input("\n\nEnter any button to continue...")

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
        menu_option = input(f"Type number. Type 'exit' to stop: ")
        if menu_option == "exit":
            break
        # Change input to integer and check if it correct
        try:
            menu_option = int(menu_option)
            gui_worker.program_in_dict(list_of_prog, menu_option)
        except ValueError:
            print("Value are not in list. Please try again.")


if __name__ == "__main__":
    main()
