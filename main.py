import time
from progress.bar import IncrementalBar
from get_version import InformationProcessor
from output_processor import OutputProcessor
from repo import repo

def main():
    worker = InformationProcessor()

    amount = worker.amount_of_prog(repo) # Amount of program

    bar = IncrementalBar("Collecting data", max = amount)

    list_of_prog = worker.get_dict(repo, bar) # Create a list of prog

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
