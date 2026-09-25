import pandas
import re
import os

class CSV_Editor():
    
    main_menu_list = ['show list','start update' ,'add new program', 'delete program', 'edit table', 'exit']  


    def __init__(self) -> None:
        pass

    def main_menu(self):
        for option in self.main_menu_list:
            print(self.main_menu_list.index(option)+1, '-', option)

    def question_yn (self, message):
        while True:
            answer = input(message)
            if answer == 'y' or answer == 'n':
                return answer
            else:
                print("Please type 'y' or 'n'")
        
    def check_answer(self, max_input, message):
        # Methods check user choice with its range. If user type exit it return 'exit'
        while True:
            user_choice = input(message)
            if user_choice == 'exit':
                return 0
            try: 
                user_choice = int(user_choice)
                if user_choice > max_input or user_choice < 0:
                    print("Your choice is out of range.")
                else:
                    return user_choice
            except:
                print("Choose number from 1 to {} .".format(max_input))

    def edit_program(self, data):
        program_not_chosed = True
        while program_not_chosed:
            self.show_list(data)
            max_input = data.index[-1]
            message = "\n\nChoose number of program you want to edit: "
            user_choice = self.check_answer(max_input, message)

            os.system("cls")
            print(data.iloc[user_choice])

            confirmation = self.question_yn("\n\nIs it right?(y/n): ")
            if confirmation == 'y':
                program_not_chosed = False
            else:
                back = self.question_yn("Return to menu?(y/n): ") 
                if back == 'y':
                    return data
                else:
                    continue

        os.system("cls")
        column_list = list(data.columns.values)
        for title in column_list:
            print(column_list.index(title)+1,"- ", title)

        message = "\n\nChoose which column you want to edit:"
        max_input = len(column_list)+1
        chosed_column = self.check_answer(max_input, message)

        os.system("cls")
        print("Selected column: ", column_list[chosed_column - 1], "\nValues stored: ", data.iloc[user_choice][column_list[chosed_column-1]])
        value_to_add = input("Type new value: ")

        
        backup_value = data.iloc[user_choice][column_list[chosed_column-1]]
        data.at[user_choice, column_list[chosed_column - 1]] = value_to_add
        print(data.iloc[user_choice])

        store_value = self.question_yn("\n\nIs it right?(y/n): ")

        if store_value == 'y':
            return data
        else:
            data.at[user_choice, column_list[chosed_column - 1]] = backup_value
            return data

            
    def add_new_program(self, data):
        """Add new program to csv table"""
        os.system('cls')
        name = input("\n\nType name of program: ")

        # User choice of source of app
        user_choice = int(input("Source:\n\n1 - GitHub\n2 - PortableApps\n3 - Techspotn\n\nType (1, 2 or 3): "))
        if user_choice == 1:
            source = "GitHub"
            version_link = input("\n\n\nType GitHub repo link\n\nYour input: ") + "/releases/latest"
            download_link = version_link
        elif user_choice == 2:
            source = "PortableApps"
            version_link = input("\n\n\nPaste link with download button from PortableApps\n\nYour input: ")
            download_link = version_link
        else:
            source = "TechSpot"
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
        """Show DataFrame value"""
        os.system('cls')
        return print(data)
