#from file import class
from Models.teamModel import Team
from LogicLayer.logicLayerAPI import LogicWrapper
from UILayer.sortingUtils import sort_by_name

class TeamUI:
    def __init__(self):
        self.LogicWrapper = LogicWrapper()

    def createTeam(self):
        """ Creates new team through input from user """

        print("\nRegister New Team")

        # Check if clubs exist
        clubs = self.LogicWrapper.sendClubInfoToUI()
        if not clubs:
            print("\nCreate the CLUB first!")
            input("Press Enter to continue...")
            return

        #Input from user
        teamID = input("Team ID: ").strip()
        teamName = input("Team Name: ").strip()

        # Sort clubs by name using Icelandic sorting order
        clubs_sorted = sort_by_name(clubs, 'clubname')

        # Select club from existing clubs
        print("\nSelect club:")
        for idx, club in enumerate(clubs_sorted, start=1):
            print(f"{idx}) {club.clubname}")

        while True:
            choice = input("Club (number): ").strip()
            if choice.isdigit():
                idx = int(choice)
                if 1 <= idx <= len(clubs_sorted):
                    clubName = clubs_sorted[idx - 1].clubname
                    break
            print("Invalid choice, try again.")

        # Show summary and confirm
        print("\nConfirm registration:")
        print(f"  Team ID:   {teamID}")
        print(f"  Team Name: {teamName}")
        print(f"  Club:      {clubName}")

        confirm = input("Confirm registration (y/n): ").strip().lower()

        if confirm != "y":
            print("Registration cancelled.")
            return

        # Create Team and send to logic layer
        newTeam: Team = Team(teamID, teamName, clubName)
        self.LogicWrapper.addNewTeam(newTeam)
        print("Team registered successfully.") 
    
    def showTeam(self):
        """ Shows a list of teams """
        teamList = self.LogicWrapper.sendTeamInfoToUI()

        # Sort teams by name using Icelandic sorting order
        if teamList:
            teamList = sort_by_name(teamList, 'teamName')

        while True:
            print("\n===== REGISTERED TEAMS =====")
            if not teamList:
                print("No teams registered yet.")
            else:
                for idx, team in enumerate(teamList, start=1):
                    print(f"{idx}. {team.teamName} (Club: {team.teamClub})")

            print()
            print("b) Back")
            print("q) Quit")

            #User input
            choice = input("Choose action: ").strip().upper()

            #Goes back to the previous screen
            if choice == "B":
                break
            #Quits the program
            elif choice == "Q":
                quit()
            else:
                # Try to parse as team selection number
                try:
                    teamIndex = int(choice) - 1
                    if 0 <= teamIndex < len(teamList):
                        self.showTeamDetails(teamList[teamIndex])
                    else:
                        print("Invalid team number, try again.")
                except ValueError:
                    print("Invalid choice, try again.")

    def showTeamDetails(self, team: Team):
        """ Shows detailed information about a team including its players and captain """
        while True:
            print("\n===== TEAM DETAILS =====")
            print(f"Team ID:   {team.teamID}")
            print(f"Team Name: {team.teamName}")
            print(f"Club:      {team.teamClub}")

            # Get players for this team
            players = self.LogicWrapper.get_players_by_team(team.teamName)

            # Display captain
            if team.captain:
                # Find captain's full name
                captain_player = next((p for p in players if p.username == team.captain), None)
                if captain_player:
                    print(f"Captain:   {captain_player.name} (@{team.captain})")
                else:
                    print(f"Captain:   @{team.captain}")
            else:
                print(f"Captain:   No captain selected")

            if players:
                # Sort players by name using Icelandic sorting order
                players_sorted = sort_by_name(players, 'name')
                # Format as comma-separated list: Name (@handle), Name (@handle)
                player_list = ", ".join([f"{player.name} (@{player.username})" for player in players_sorted])
                print(f"Players:   {player_list}")
            else:
                print("Players:   No players registered")

            print("\n===========================")
            print("1) Select/Change captain")
            print("b) Back")
            print("q) Quit")

            choice = input("Choose action: ").strip().lower()

            if choice == "1":
                self.selectCaptain(team, players)
                # Reload team to get updated captain
                teamList = self.LogicWrapper.sendTeamInfoToUI()
                team = next((t for t in teamList if t.teamID == team.teamID), team)
            elif choice == "b":
                break
            elif choice == "q":
                quit()
            else:
                print("Invalid choice, try again.")

    def selectCaptain(self, team: Team, players: list):
        """ Allows selecting a captain for the team """
        print("\n===== SELECT CAPTAIN =====")

        if not players:
            print("No players in this team. Add players first before selecting a captain.")
            input("\nPress Enter to continue...")
            return

        # Sort players by name using Icelandic sorting order
        players_sorted = sort_by_name(players, 'name')

        print("\nSelect captain:")
        for idx, player in enumerate(players_sorted, start=1):
            captain_mark = " (Current Captain)" if player.username == team.captain else ""
            print(f"{idx}) {player.name} (@{player.username}){captain_mark}")

        print("0) Remove captain (no captain)")
        print("b) Back")

        while True:
            choice = input("\nCaptain (number): ").strip()
            if choice.lower() == "b":
                return
            if choice.isdigit():
                idx = int(choice)
                if idx == 0:
                    # Remove captain
                    team.captain = ""
                    self.LogicWrapper.updateTeam(team)
                    print("Captain removed.")
                    input("\nPress Enter to continue...")
                    return
                elif 1 <= idx <= len(players_sorted):
                    selected_player = players_sorted[idx - 1]
                    team.captain = selected_player.username
                    self.LogicWrapper.updateTeam(team)
                    print(f"\n{selected_player.name} (@{selected_player.username}) is now the captain!")
                    input("\nPress Enter to continue...")
                    return
            print("Invalid choice, try again.")
 
    
    def teamMenu(self):
        """ Team Menu """

        while True:
            print("\n===== TEAM MENU =====")
            #Following options the user can make to use the program
            print("1 Register new team")
            print("2 Show teams")
            print()
            print("b) Back")
            print("q) Quit")

            #Input from use
            choice = input("Choose action: ").strip().upper()

            #Goes to Create Team Menu
            if choice == "1": 
                self.createTeam()
            #Goes to See Team menu
            elif choice == "2": 
                self.showTeam()
            #Returns to the preivious screen
            elif choice == "B": 
                break
            #Quits the program
            elif choice =="Q": 
                quit()
            #Lovely error messsage
            else:
                print("Invalid choice, try again.")