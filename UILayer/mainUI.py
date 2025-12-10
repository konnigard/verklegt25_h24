import os
import sys

class MainUI:
    """Main menu interface"""
    
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
                    user_input = input(f"{prompt} (q) Quit: ").strip()
                    if user_input.lower() == "q":
                        return None
                else:
                    user_input = input(f"{prompt}: ").strip()
                if input_type == int:
                    return int(user_input)
                elif input_type == str:
                    if not user_input:
                        print("Error! input cannot be blank")
                        continue
                    return user_input
                else:
                    return input_type(user_input)
            except ValueError:
                print(f"Error invalid input. Expected input was {input_type.__name__}.")
    
    def show_home_menu(self):
        """Displays the main menu"""
        while True:
            self.display_header("Home Screen")
            print("1) see details")
            print("2) Register ")
            print("3) Admin acess")
            print()
            print("q) Quit")
            print()

            choice = self.get_input("Choose option", allow_back=False)

            if choice == "1":
                self.show_register_menu()
            elif choice == "2":
                self.show_view_menu()
            elif choice == "3":
                self.show_admin_menu()
            elif choice and choice.lower() == "q":
                print("\nThank you for the use!")
                sys.exit(0)
            else:
                print("Invalid choice, please press a number from 1-3 or q to quit!")
                input("Press Enter to continue")
