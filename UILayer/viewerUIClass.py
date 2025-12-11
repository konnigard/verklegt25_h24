from UILayer.playerUIClass import playerUI
from UILayer.teamUIClass import TeamUI
from UILayer.clubUIClass import ClubUI
from UILayer.tournamentUIClass import TournamentUI
from UILayer.eventUIClass import EventUI

class ViewerUI:
    def __init__(self):
        pass   

    def viewerMenu(self):
        uiTeam = TeamUI()
        uiClub = ClubUI()
        uiTournament = TournamentUI()
        uiEvent = EventUI()
        ui = playerUI

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
                print("Player Viewer not implamented yet")
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
