from datetime import datetime
from Models.playerModel import Player
from LogicLayer.logicLayerAPI import LogicWrapper
from UILayer.sortingUtils import sort_by_name


class playerUI:
    def __init__(self) -> None:
        self.logic = LogicWrapper()

    def player_menu(self) -> None:
        while True:
            print("\n===== PLAYER MENU =====")
            print("1 Register new player")
            print("2 Show players")
            print("B Back")
            choice = input("Choose action: ").strip().upper()

            if choice == "1":
                self.create_player_flow()
            elif choice == "2":
                self.show_players()
            elif choice == "B":
                break
            else:
                print("Invalid choice, try again.")

    # ---- Til að leyfa bara dagsetningar og tölustafi í simanúmer ----

    def ask_for_valid_date(self) -> str:
        """Ask until user enters a valid date in YYYY-MM-DD format or 'b' to cancel."""
        while True:
            dob = input("Date of birth (YYYY-MM-DD) (or 'b' to cancel): ").strip()
            if dob.lower() == 'b':
                return None
            try:
                datetime.strptime(dob, "%Y-%m-%d")
                return dob
            except ValueError:
                print("Invalid date. Please use format YYYY-MM-DD.")

    def ask_for_valid_phone(self) -> str:
        """Ask until user enters a phone number with digits only or 'b' to cancel."""
        while True:
            phone = input("Phone number (digits only) (or 'b' to cancel): ").strip()
            if phone.lower() == 'b':
                return None
            if phone.isdigit():
                return phone
            else:
                print("Phone number must contain digits only.")

    # ---- FLOW For register new player  ----

    def create_player_flow(self) -> None:
        """Ask user for player info, check username availability and confirm."""

        print("\nRegister player")
        print("(Enter 'b' at any prompt to cancel)\n")

        name = input("Player name: ").strip()
        if name.lower() == 'b':
            print("Registration cancelled.")
            return

        dob = self.ask_for_valid_date()
        if dob is None:
            print("Registration cancelled.")
            return

        address = input("Home address: ").strip()
        if address.lower() == 'b':
            print("Registration cancelled.")
            return

        phone_number = self.ask_for_valid_phone()
        if phone_number is None:
            print("Registration cancelled.")
            return

        email = input("Email: ").strip()
        if email.lower() == 'b':
            print("Registration cancelled.")
            return

        link = input("Link: ").strip()
        if link.lower() == 'b':
            print("Registration cancelled.")
            return

        # username: username available?
        while True:
            username = input("Username: ").strip()
            if username.lower() == 'b':
                print("Registration cancelled.")
                return
            if not username:
                print("Username cannot be empty.")
                continue

            if self.logic.is_username_available(username):
                break
            else:
                print(f"Username '{username}' is already taken. Please choose another one.")

        # Select team
        teams = self.logic.sendTeamInfoToUI()
        if not teams:
            print("\nNo teams available. Please register a team first before registering players.")
            input("Press Enter to continue...")
            return

        # Sort teams by name using Icelandic sorting order
        teams = sort_by_name(teams, 'teamName')

        print("\nSelect team:")
        for idx, team in enumerate(teams, start=1):
            print(f"{idx}) {team.teamName}")

        while True:
            choice = input("Team (number or 'b' to cancel): ").strip()
            if choice.lower() == 'b':
                print("Registration cancelled.")
                return
            if choice.isdigit():
                idx = int(choice)
                if 1 <= idx <= len(teams):
                    teamName = teams[idx - 1].teamName
                    break
            print("Invalid choice, try again.")

        # show summary and confirm
        print("\nConfirm registration:")
        print(f"  Name:         {name}")
        print(f"  Date of birth:{dob}")
        print(f"  Address:      {address}")
        print(f"  Phone:        {phone_number}")
        print(f"  Email:        {email}")
        print(f"  Link:         {link}")
        print(f"  Username:     {username}")
        print(f"  Team:         {teamName}")

        confirm = input("Confirm registration (y/n): ").strip().lower()

        if confirm != "y":
            print("Registration cancelled.")
            return

        # create Player and send to logic layer
        player = Player(
            name=name,
            dob=dob,
            address=address,
            phone_number=phone_number,
            email=email,
            link=link,
            username=username,
            teamName=teamName
        )

        self.logic.create_player(player)
        print("Player registered.")

    def show_players(self) -> None:
        """Displays all registered players"""
        playerList = self.logic.sendPlayerInfoToUI()

        # Sort players by name using Icelandic sorting order
        if playerList:
            playerList = sort_by_name(playerList, 'name')

        while True:
            print("\n===== REGISTERED PLAYERS =====")
            if not playerList:
                print("No players registered yet.")
            else:
                for idx, player in enumerate(playerList, start=1):
                    print(f"{idx}. {player.name} (@{player.username}) - Team: {player.teamName}")

            print()
            print("b) Back")
            print("q) Quit")
            choice = input("Choose action: ").strip().upper()

            if choice == "B":
                break
            elif choice == "Q":
                quit()
            elif choice.isdigit():
                player_number = int(choice)
                if 1 <= player_number <= len(playerList):
                    self.show_player_details(playerList[player_number - 1])
                else:
                    print(f"Invalid player number. Please choose between 1 and {len(playerList)}.")
            else:
                print("Invalid choice, try again.")

    def show_player_details(self, player) -> None:
        """Display detailed information about a player"""
        print("\n===== PLAYER DETAILS =====")
        print(f"Name:         {player.name}")
        print(f"Username:     {player.username}")
        print(f"Team:         {player.teamName}")
        print(f"Date of Birth:{player.dob}")
        print(f"Address:      {player.address}")
        print(f"Phone:        {player.phone_number}")
        print(f"Email:        {player.email}")
        print(f"Link:         {player.link}")

        # Get tournament history for this player's team
        tournament_names = self.logic.get_tournaments_for_team(player.teamName)
        if tournament_names:
            all_tournaments = self.logic.get_all_tournaments()
            # Get tournament objects for this player's team
            player_tournaments = [t for t in all_tournaments if t.name in tournament_names]
            # Sort by start date in reverse order (most recent first)
            player_tournaments_sorted = sorted(player_tournaments, key=lambda t: t.startDate, reverse=True)

            print("\nTournaments:")
            for tournament in player_tournaments_sorted:
                print(f"  • {tournament.name} - {tournament.startDate}")
        else:
            print("\nTournaments: No tournaments registered")

        print()
        input("Press Enter to continue...")
