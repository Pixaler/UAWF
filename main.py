import time
from pandas._libs.hashtable import duplicated
from progress.bar import IncrementalBar
from get_version import InformationProcessor
from output_processor import OutputProcessor
from edit_csv import CSV_Editor
import pandas


def main():
    worker = InformationProcessor()

    editor = CSV_Editor()

    data = pandas.read_csv("repo.csv", index_col=[0])
    
    want_edit = True
    while want_edit:
        choice = input("a - add new program\nd - delete program\nn - skip\nChoose option: " )
        if choice == 'a':
            data = editor.edit_table(data)
            new_data = pandas.DataFrame(data)
            new_data = new_data.reset_index(drop=True)
            new_data.to_csv("repo.csv")
        elif choice == 'd':
            data = editor.delete_row(data)
            new_data = pandas.DataFrame(data)
            new_data = new_data.reset_index(drop=True)
            new_data.to_csv("repo.csv")
        go_on = input("You want to edit again? (y/n): ")
        if go_on == 'n':
            want_edit = False

    amount = worker.amount_of_prog(data) # Amount of program

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
        gui_worker.program_in_dict(list_of_prog, menu_option)
        if not gui_worker.program_in_dict(list_of_prog, menu_option):
            print(".\n.")
            print(f"Program '{menu_option}' not in list. Please type correct name or add this program to repo.py")

if __name__ == "__main__":
    main()
