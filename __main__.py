from UILayer.playerUIClass import playerUI
from UILayer.teamUIClass import TeamUI
from UILayer.clubUIClass import ClubUI
from UILayer.clubUIClass import ClubUI


def show_see_menu(ui: playerUI) -> bool:
    """'See' menu - returns False if user wants to quit."""

    uiTeam = TeamUI()
    uiClub = ClubUI()
    while True:
        print("\nSee")
        print("1) Sjá Lið")
        print("2) Sjá Klubb")
        print("3) Sjá Leikmenn")
        print("4) Sjá Viðburði")
        print()
        print("b) Til baka")
        print("q) Hætta")

        choice = input("Choose action: ").strip().lower()

        if choice == "1":
            uiTeam.teamMenu()
        elif choice == "2":
            uiClub.showClubs()
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
    uiClub = ClubUI()
    while True:
        print("\nRegister")
        print("1) Skrá Leikmann")
        print("2) Skrá team")
        print("3) Skrá mót")
        print("4) Skrá niðurstöðu leiks")
        print("5) búa til dagskrá")
        print("6) Skrá Klúbb")
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
            uiClub.createClub()
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
        print("        Upphafsskjár")
        print("************************")
        print("1 Skoða ")
        print("2 Skrá")
        print("************************")
        print("q) Hætta")
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
            print("Rangt val, Vinsamlegast prufaðu annað \n")


if __name__ == "__main__":
    main()
