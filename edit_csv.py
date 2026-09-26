import pandas
import os

class CSV_Editor():
    
    main_menu_list = ['show list','start update' ,'add new program', 'delete program', 'edit table', 'exit']  


    def __init__(self) -> None:
        pass

    def save_data_to_csv(self, data, REPO):
        new_data = pandas.DataFrame(data)
        new_data = new_data.reset_index(drop=True)
        new_data.to_csv(REPO)
        updated_data = pandas.read_csv(REPO, index_col=[0])
        return updated_data

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

    def edit_program(self, data, REPO):
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
                    self.save_data_to_csv(data, REPO)
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

        updated_data = self.save_data_to_csv(data, REPO)
        return updated_data

            
    def add_new_program(self, data, REPO):
        """Add new program to csv table"""
        os.system('cls')
        name = input("\n\nType name of program: ")

        # User choice of source of app
        print("""Type link for latest version 
                GitHub - Type link of repository. Example: https://github.com/Pixaler/UAWF\n
                PortableApps - Type link with download button. Example: https://portableapps.com/apps/development/gvim_portable\n
                Techspot - Type link with donwload button. Example: https://www.techspot.com/downloads/2879-autoruns.html\n\n""")
        version_link_not_correct = True
        while version_link_not_correct:
            version_link = input("Type your link: ")
            if  version_link.strip().find("https://github.com") == 0:
                version_link = version_link + "/releases/latest"
                download_link = version_link
                version_link_not_correct = False
            elif version_link.strip().find("https://portableapps") == 0:
                download_link = version_link
                version_link_not_correct = False
            elif version_link.find("https://www.techspot/downloads") == 0:
                download_link = input("\n\nType download link: ")
                version_link_not_correct = False
            else: 
                print("\n\nPlease check that link in right form")
                

        path_to_exe = input("\n\n\nFrom this path program try to find exe and read version.\n\nType path to exe files: ")

        new_row = pandas.DataFrame({"name": name,"version_link": version_link,"path_to_exe": path_to_exe,"download_link": download_link}, index = [data.index[-1]+1])

        print("\n\n\nYour final data:")
        print("\n")
        print(new_row)
        confirmation = self.question_yn("\n\n\nAre you cofirm addtion of new program?\ny - for yes\nn - for no\n\nYour choice: ")

        if confirmation == 'y':
            data = pandas.concat([data, new_row], axis = 0, ignore_index=True)

        updated_data = self.save_data_to_csv(data, REPO)
        return updated_data   

    def delete_row(self, data, REPO):
        """Delete program from csv table"""
        correct_name = False
        while correct_name == False:
            self.show_list(data)
            program_to_delete = self.check_answer(data.index[-1], "\n\nType name of program that you want to delete: ")
            print(data.iloc[program_to_delete])
            confirmation = input("\n\nAre you cofirm deletion of program?\ny - for yes\nn - for no\nYour choice: ")
            if confirmation == 'y':
                data = data.drop(index = program_to_delete)
                print("Successfuly deleted")
            updated_data = self.save_data_to_csv(data, REPO)
            return updated_data

    def show_list(self, data):
        """Show DataFrame value"""
        os.system('cls')
        return print(data)
