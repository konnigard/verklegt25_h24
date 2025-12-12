#from file import class
from Models.teamModel import Team
from LogicLayer.logicLayerAPI import LogicWrapper
from UILayer.sortingUtils import sort_by_name

class TeamUI:
    def __init__(self):
        self.LogicWrapper = LogicWrapper()

    def create_team(self):
        """ Creates new team through input from user """

        print("\nRegister New Team")
        print("(Enter 'b' at any prompt to cancel)\n")

        # Check if clubs exist
        clubs = self.LogicWrapper.send_club_info_to_ui()
        if not clubs:
            print("\nCreate the CLUB first!")
            input("Press Enter to continue...")
            return

        # Check team name uniqueness
        while True:
            teamName = input("Team Name: ").strip()
            if teamName.lower() == 'b':
                print("Registration cancelled.")
                return
            if not teamName:
                print("Team name cannot be empty.")
                continue

            if self.LogicWrapper.is_team_name_available(teamName):
                break
            else:
                print(f"Team name '{teamName}' is already taken. Please choose another name.")

        # Sort clubs by name using Icelandic sorting order
        clubs_sorted = sort_by_name(clubs, 'clubname')

        # Select club from existing clubs
        print("\nSelect club:")
        for idx, club in enumerate(clubs_sorted, start=1):
            print(f"{idx}) {club.clubname}")

        while True:
            choice = input("Club (number or 'b' to cancel): ").strip()
            if choice.lower() == 'b':
                print("Registration cancelled.")
                return
            if choice.isdigit():
                idx = int(choice)
                if 1 <= idx <= len(clubs_sorted):
                    clubName = clubs_sorted[idx - 1].clubname
                    break
            print("Invalid choice, try again.")

        # Show summary and confirm
        print("\nConfirm registration:")
        print(f"  Team Name: {teamName}")
        print(f"  Club:      {clubName}")

        confirm = input("Confirm registration (y/n): ").strip().lower()

        if confirm != "y":
            print("Registration cancelled.")
            return

        # Create Team and send to logic layer (TeamID will be auto-generated)
        newTeam: Team = Team(teamID="", teamName=teamName, teamClub=clubName)
        self.LogicWrapper.add_new_team(newTeam)
        print("Team registered successfully.") 
    
    def show_team(self):
        """ Shows a list of teams """
        teamList = self.LogicWrapper.send_team_info_to_ui()

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

    def show_team_details(self, team: Team):
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

            # Get tournament history for this team
            tournament_names = self.LogicWrapper.get_tournaments_for_team(team.teamName)
            if tournament_names:
                all_tournaments = self.LogicWrapper.get_all_tournaments()
                # Get tournament objects for this team
                team_tournaments = [t for t in all_tournaments if t.name in tournament_names]
                # Sort by start date in reverse order (most recent first)
                team_tournaments_sorted = sorted(team_tournaments, key=lambda t: t.startDate, reverse=True)

                print("\nTournaments:")
                for tournament in team_tournaments_sorted:
                    print(f"  • {tournament.name} - {tournament.startDate}")
            else:
                print("\nTournaments: No tournaments registered")

            print("\n===========================")

            # Get session for permission checks
            from UILayer.sessionManager import get_session
            session = get_session()

            # Show options based on permissions
            if session.can_edit_player(team.teamName):
                print("1) Select/Change captain")
                print("2) Edit player")

            print("b) Back")
            print("q) Quit")

            choice = input("Choose action: ").strip().lower()

            if choice == "1" and session.can_edit_player(team.teamName):
                self.selectCaptain(team, players)
                # Reload team from database to get updated captain information
                teamList = self.LogicWrapper.send_team_info_to_ui()
                team = next((t for t in teamList if t.teamID == team.teamID), team)
                # Reload players as well to ensure captain marking is correct
                players = self.LogicWrapper.get_players_by_team(team.teamName)
            elif choice == "1" and not session.can_edit_player(team.teamName):
                print("You do not have permission to select captain.")
            elif choice == "2" and session.can_edit_player(team.teamName):
                self.edit_player_in_team(team, players)
                # Reload players to reflect any changes
                players = self.LogicWrapper.get_players_by_team(team.teamName)
            elif choice == "2" and not session.can_edit_player(team.teamName):
                print("You do not have permission to edit players.")
            elif choice == "b":
                break
            elif choice == "q":
                quit()
            else:
                print("Invalid choice, try again.")

    def select_captain(self, team: Team, players: list):
        """ Allows selecting a captain for the team """
        from UILayer.sessionManager import get_session
        session = get_session()

        # Permission check
        if not session.can_edit_player(team.teamName):
            print("\nYou do not have permission to select captain for this team.")
            input("Press Enter to continue...")
            return

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
                    self.LogicWrapper.update_team(team)
                    print("\n✓ Captain removed successfully!")
                    print("✓ Changes saved to database.")
                    input("\nPress Enter to continue...")
                    return
                elif 1 <= idx <= len(players_sorted):
                    selected_player = players_sorted[idx - 1]
                    team.captain = selected_player.username
                    self.LogicWrapper.update_team(team)
                    print(f"\n✓ {selected_player.name} (@{selected_player.username}) is now the captain!")
                    print("✓ Changes saved to database.")
                    input("\nPress Enter to continue...")
                    return
            print("Invalid choice, try again.")
 
    
    def team_menu(self):
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

    def edit_player_in_team(self, team: Team, players: list):
        """Select and edit a player from the team"""
        from UILayer.playerUIClass import playerUI

        print("\n===== SELECT PLAYER TO EDIT =====")

        if not players:
            print("No players in this team.")
            input("\nPress Enter to continue...")
            return

        players_sorted = sort_by_name(players, 'name')

        print("\nSelect player to edit:")
        for idx, player in enumerate(players_sorted, start=1):
            print(f"{idx}) {player.name} (@{player.username})")
        print("b) Back")

        while True:
            choice = input("\nPlayer (number): ").strip()
            if choice.lower() == "b":
                return
            if choice.isdigit():
                idx = int(choice)
                if 1 <= idx <= len(players_sorted):
                    selected_player = players_sorted[idx - 1]
                    # Use playerUI's edit flow
                    player_ui = playerUI()
                    player_ui.edit_player_flow(selected_player)
                    return
            print("Invalid choice, try again.")