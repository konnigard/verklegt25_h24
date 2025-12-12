from UILayer.playerUIClass import playerUI
from UILayer.teamUIClass import TeamUI
from UILayer.clubUIClass import ClubUI
from UILayer.tournamentUIClass import TournamentUI
from UILayer.eventUIClass import EventUI
from UILayer.authUIClass import AuthUI
from UILayer.sessionManager import get_session


def show_see_menu(ui: playerUI) -> str:
    """'See' menu - returns 'BACK', 'LOGOUT', or 'QUIT'."""

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
        print("l) Logout")
        print("q) Quit")

        choice = input("Choose action: ").strip().lower()

        if choice == "1":
            uiTeam.show_team()
        elif choice == "2":
            uiClub.show_clubs()
        elif choice == "3":
            ui.show_players()
        elif choice == "4":
            uiTournament.read_tournaments()
        elif choice == "5":
            uiEvent.view_all_events()
        elif choice == "b":
            return "BACK"
        elif choice == "l":
            get_session().logout()
            return "LOGOUT"
        elif choice == "q":
            return "QUIT"
        else:
            print("Invalid choice, try again.")


def show_register_menu(ui: playerUI) -> str:
    """'Register' menu returns 'BACK', 'LOGOUT', or 'QUIT'."""
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
        print("l) Logout")
        print("q) Quit")

        choice = input("Choose action: ").strip().lower()

        if choice == "1":
            ui.create_player_flow()
        elif choice == "2":
            uiTeam.create_team()
        elif choice == "3":
            uiTournament.create_tournament()
        elif choice == "4":
            uiClub.create_club()
        elif choice == "5":
            uiEvent.create_event()
        elif choice == "6":
            uiEvent.record_score()
        elif choice == "b":
            return "BACK"
        elif choice == "l":
            get_session().logout()
            return "LOGOUT"
        elif choice == "q":
            return "QUIT"
        else:
            print("Invalid choice, try again.")


def main() -> None:
    auth_ui = AuthUI()

    while True:
        # Login screen (returns False if user quits during login)
        if not auth_ui.login():
            print("Bye!")
            break

        # Main menu loop (only accessible when authenticated)
        session = get_session()
        ui = playerUI()

        while session.is_authenticated:
            print("************************")
            print("        MAIN MENU")
            print("************************")
            print("1 See details")

            # Only show Register option for Admin (not Captain or User)
            if session.is_admin():
                print("2 Register")

            print("************************")
            print("l) Logout")
            print("q) Quit")
            print("************************")
            choice = input("Choose action: ").strip().lower()

            if choice == "1":
                result = show_see_menu(ui)
                if result == "LOGOUT":
                    break  # Exit to login screen
                elif result == "QUIT":
                    print("Bye!")
                    session.logout()
                    return  # Exit program
            elif choice == "2" and session.is_admin():
                result = show_register_menu(ui)
                if result == "LOGOUT":
                    break  # Exit to login screen
                elif result == "QUIT":
                    print("Bye!")
                    session.logout()
                    return  # Exit program
            elif choice == "2" and not session.is_admin():
                print("You do not have permission to register items.")
            elif choice == "l":
                session.logout()
                print("Logged out successfully.")
                break  # Return to login screen
            elif choice == "q":
                print("Bye!")
                session.logout()
                return  # Exit program
            else:
                print("Invalid choice, try again.\n")


if __name__ == "__main__":
    main()