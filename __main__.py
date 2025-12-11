from UILayer.playerUIClass import playerUI
from UILayer.teamUIClass import TeamUI
from UILayer.clubUIClass import ClubUI
from UILayer.tournamentUIClass import TournamentUI
from UILayer.eventUIClass import EventUI
from UILayer.captainUIClass import Captain


def show_see_menu(ui: playerUI) -> bool:
    """'See' menu - returns False if user wants to quit."""

    uiTeam = TeamUI()
    uiClub = ClubUI()
    uiTournament = TournamentUI()
    uiEvent = EventUI()
    
    while True:
        print("\nSee")
        print("1) See Teams")
        print("2) See Clubs")
        print("3) See Players")
        print("4) See Tournaments")
        print("5) See Events")
        print()
        print("b) Back")
        print("q) Quit")

        choice = input("Choose action: ").strip().lower()

        if choice == "1":
            uiTeam.showTeam()
        elif choice == "2":
            uiClub.showClubs()
        elif choice == "3":
            ui.show_players()
        elif choice == "4":
            uiTournament.read_tournaments()
        elif choice == "5":
            uiEvent.view_all_events()
        elif choice == "b":
            return True   # go back to main menu
        elif choice == "q":
            return False  # quit program
        else:
            print("Invalid choice, try again.")


def show_register_menu(ui: playerUI) -> bool:
    """'Register' menu returns False if user wants to quit."""
    uiClub = ClubUI()
    uiTeam = TeamUI()
    uiTournament = TournamentUI()
    uiEvent = EventUI()
    while True:
        print("\nRegister")
        print("1) Register player")
        print("2) Register team")
        print("3) Register tournament")
        print("4) Register club")
        print("5) Create event (schedule match)")
        print("6) Record event score")
        print()
        print("b) Back")
        print("q) Quit")

        choice = input("Choose action: ").strip().lower()

        if choice == "1":
            ui.create_player_flow()
        elif choice == "2":
            uiTeam.createTeam()
        elif choice == "3":
            uiTournament.create_tournament()
        elif choice == "4":
            uiClub.createClub()
        elif choice == "5":
            uiEvent.create_event()
        elif choice == "6":
            uiEvent.record_score()
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
        print("q) Quit")
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

def loginMenu():
    while True:
        uiCaptain = Captain()
        print("************************")
        print("      LOGIN MENU")
        print("************************")
        print("1 Admin")
        print("2 Captain")
        print("3 User")
        print("************************")
        print("q) Quit")
        print("************************")

        choice = input("Choose a Login: ")

        if choice == "1":
            main()
        elif choice == "2":
            uiCaptain.CaptainMenu()
        elif choice == "3":
            print("User Menu Not Implemented")
        elif choice.upper() == "Q":
            quit()
        else: 
            print("In valid choice please try again")

if __name__ == "__main__":
    loginMenu()