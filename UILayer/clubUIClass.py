#from file import class
from Models.clubModel import Club
from LogicLayer.logicLayerAPI import LogicWrapper
from UILayer.sortingUtils import sort_by_name

class ClubUI:
    def __init__(self):
        self.LogicWrapper = LogicWrapper()

    def createClub(self):
        """ Creates a new club by collecting user input """
        print("\n===== REGISTER NEW CLUB =====")
        clubname = input("Please enter the Clubname: ").strip()
        teamlist = input("Please enter the Teamlist (comma-separated, or leave blank): ").strip()
        hometown = input("Please enter the Hometown: ").strip()
        country = input("Please enter the Country: ").strip()

        if not clubname or not hometown or not country:
            print("Error: Clubname, Hometown, and Country are required!")
            return

        newClub = Club(clubname, hometown, country, teamlist)
        self.LogicWrapper.saveClubFromUI(newClub)
        print(f"\nClub '{clubname}' has been successfully registered!")

    def showClubDetails(self, club: Club):
        """ Displays detailed information about a specific club """
        while True:
            print("\n===== CLUB DETAILS =====")
            print(f"Club name: {club.clubname}")
            print(f"Hometown:  {club.hometown}")
            print(f"Country:   {club.country}")

            # Get all teams belonging to this club
            all_teams = self.LogicWrapper.sendTeamInfoToUI()
            club_teams = [team for team in all_teams if team.teamClub == club.clubname]

            if club_teams:
                # Sort teams by name using Icelandic sorting order
                club_teams_sorted = sort_by_name(club_teams, 'teamName')
                teams_display = ", ".join([team.teamName for team in club_teams_sorted])
                print(f"Teams:     {teams_display}")
            else:
                print("Teams:     No teams registered")

            print()
            print("b) Back")
            print("q) Quit")
            choice = input("Choose action: ").strip().upper()

            if choice == "B":
                break
            elif choice == "Q":
                quit()
            else:
                print("Invalid choice, try again.")

    def showClubs(self):
        """ Displays all registered clubs """
        clubList = self.LogicWrapper.sendClubInfoToUI()

        # Sort clubs by name using Icelandic sorting order
        if clubList:
            clubList = sort_by_name(clubList, 'clubname')

        while True:
            print("\n===== REGISTERED CLUBS =====")
            if not clubList:
                print("No clubs registered yet.")
            else:
                for idx, club in enumerate(clubList, start=1):
                    print(f"{idx}. {club.clubname}")

            print()
            print("b) Back")
            print("q) Quit")
            choice = input("Choose action: ").strip().upper()

            if choice == "B":
                break
            elif choice == "Q":
                quit()
            elif choice.isdigit():
                club_number = int(choice)
                if 1 <= club_number <= len(clubList):
                    self.showClubDetails(clubList[club_number - 1])
                else:
                    print(f"Invalid club number. Please choose between 1 and {len(clubList)}.")
            else:
                print("Invalid choice, try again.")

    def clubMenu(self):
        """ Main menu for club operations """
        while True:
            print("\n===== CLUB MENU =====")
            print("1 Register new club")
            print("2 Show clubs")
            print()
            print("b) Back")
            print("q) Quit")
            choice = input("Choose action: ").strip().upper()

            if choice == "1":
                self.createClub()
            elif choice == "2":
                self.showClubs()
            elif choice == "B":
                break
            elif choice == "Q":
                quit()
            else:
                print("Invalid choice, try again.")