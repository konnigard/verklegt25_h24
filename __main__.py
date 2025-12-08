from UILayer.playerUIClass import playerUI
from UILayer.teamUIClass import TeamUI


def show_see_menu(ui: playerUI) -> bool:
    """'See' menu – returns False if user wants to quit."""

    uiTeam = TeamUI()
    while True:
        print("\nSee")
        print("1) See Teams")
        print("2) See Clubs")
        print("3) See Players")
        print("4) See Events")
        print()
        print("b) Back")
        print("q) Quit")

        choice = input("Choose action: ").strip().lower()

        if choice == "1":
            uiTeam.teamMenu()
        elif choice == "2":
            print("[See Clubs] not implemented yet")
        elif choice == "3":
            ui.show_players()
        elif choice == "4":
            print("[See Events] not implemented yet")
        elif choice == "b":
            return True   # go back to main menu
        elif choice == "q":
            return False  # quit program
        else:
            print("Invalid choice, try again.")


def show_register_menu(ui: playerUI) -> bool:
    """'Register' menu returns False if user wants to quit."""
    while True:
        print("\nRegister")
        print("1) Register player")
        print("2) Register team")
        print("3) Register tournament")
        print("4) Register match result")
        print("5) Create schedule")
        print("6) Register club")
        print()
        print("b) Back")
        print("q) Quit")

        choice = input("Choose action: ").strip().lower()

        if choice == "1":
            ui.create_player_flow()
        elif choice == "2":
            print("[Register team] not implemented yet")
        elif choice == "3":
            print("[Register tournament] not implemented yet")
        elif choice == "4":
            print("[Register match result] not implemented yet")
        elif choice == "5":
            print("[Create schedule] not implemented yet")
        elif choice == "6":
            print("[Register club] not implemented yet")
        elif choice == "b":
            return True   # go back to main menu
        elif choice == "q":
            return False  # quit program
        else:
            print("Invalid choice, try again.")


def main() -> None:
    ui = playerUI()

    while True:
        print("************************")
        print("        MAIN MENU")
        print("************************")
        print("1 See details")
        print("2 Register")
        print("************************")
        print("Q Quit")
        print("************************")
        choice = input("Choose action: ").strip().upper()

        if choice == "1":
            keep_running = show_see_menu(ui)
            if not keep_running:
                break
        elif choice == "2":
            keep_running = show_register_menu(ui)
            if not keep_running:
                break
        elif choice == "Q":
            print("Bye!")
            break
        else:
            print("Invalid choice, try again.\n")


if __name__ == "__main__":
    main()