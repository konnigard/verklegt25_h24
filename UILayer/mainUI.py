import os
import sys

class MainUI:
    """MainMenuUI"""
    
    def __init__(self, logic_layer):
        self.Logic_layer = logic_layer
        self.current_user_role = None #admin, captain or viewer
    
    def clear_screen(self):
        """clear the terminal screen"""
        os.system("cls" if os.name == "nt" else "clear")

    def display_header(self, title):
        """display the formatted header"""
        self.clear_screen()
        print("=" * 60)
        print(f" {title}")
        print("=" * 60)
        print()
    
    def get_input(self, prompt, input_type=str, allow_back=True):
        """get valid input from the user"""
        while True:
            try:
                if allow_back:
                    user_input = input(f"{prompt} (q) Hætta: ").strip()
                    if user_input.lower() == "q":
                        return None
                else:
                    user_input = input(f"{prompt}: ").strip()
                if input_type == int:
                    return int(user_input)
                elif input_type == str:
                    if not user_input:
                        print("Villa! intak má ekki vera tómt.")
                        continue
                    return user_input
                else:
                    return input_type(user_input)
            except ValueError:
                print(f"Villa ógilt inntak tegund. Búist var við {input_type.__name__}.")
    
    def show_home_menu(self):
        """Displays the main menu"""
        while True:
            self.display_header("Heimaskjár")
            print("1) skrá")
            print("2) sjá")
            print("3) stjórnandaðgangur")
            print()
            print("q) hætta")
            print()

            choice = self.get_input("veldu valkost", allow_back=False)

            #TODO change the switchboard to relevent Menus
            if choice == "1":
                self.show_register_menu()
            elif choice == "2":
                self.show_view_menu()
            elif choice == "3":
                self.show_admin_menu()
            elif choice and choice.lower() == "q":
                print("\nÞakka þér fyrir notkun!")
                sys.exit(0)
            else:
                print("ógildur Valkostur. Vinsamlega sláðu inn 1-3 eða q til að hætta")
                input("Ýttu á Enter til að halda áfram...")
