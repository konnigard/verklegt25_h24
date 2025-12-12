from datetime import datetime
from LogicLayer.logicLayerAPI import LogicWrapper
from UILayer.sortingUtils import sort_by_name


class TournamentUI:
    """UI layer for tournaments ONLY speak to LogicWrapper."""

    def __init__(self) -> None:
        self.logic = LogicWrapper()

    # Passa að það séu bara leyfðar alvöru dagsetningar og tölustafir.

    def _ask_for_valid_date(self, prompt: str) -> str:
        """Ask until user enters a valid date in YYYY-MM-DD format or 'b' to cancel."""
        while True:
            value = input(prompt + " (or 'b' to cancel): ").strip()
            if value.lower() == 'b':
                return None
            try:
                datetime.strptime(value, "%Y-%m-%d")
                return value
            except ValueError:
                print("Invalid date. Please use format YYYY-MM-DD.")

    def _ask_for_digits_only(self, prompt: str) -> str:
        """Ask until user enters digits only (for phone numbers etc.) or 'b' to cancel."""
        while True:
            value = input(prompt + " (or 'b' to cancel): ").strip()
            if value.lower() == 'b':
                return None
            if value.isdigit():
                return value
            print("This field must contain digits only. Please try again.")

    # main tournament menu 

    def tournament_menu(self) -> None:
        """Entry point from Main UI when user chooses tournament."""
        while True:
            print("\n===== TOURNAMENT MENU =====")
            print("1 Register new tournament")
            print("2 See tournaments")
            print("3 Record match result")
            print("B Back")

            choice = input("Choose action: ").strip().upper()

            if choice == "1":
                self.create_tournament()
            elif choice == "2":
                self.read_tournaments()
            elif choice == "3":
                self.tally_score()
            elif choice == "B":
                break
            else:
                print("Invalid choice, try again.")

    # create tournament

    def create_tournament(self) -> None:
        """Collect info and ask LogicLayerAPI to create a tournament."""

        print("\nRegister tournament")
        print("(Enter 'b' at any prompt to cancel)\n")

        name = input("Tournament name: ").strip()
        if name.lower() == 'b':
            print("Tournament registration cancelled.")
            return

        game = input("Game: ").strip()
        if game.lower() == 'b':
            print("Tournament registration cancelled.")
            return

        location = input("Location: ").strip()
        if location.lower() == 'b':
            print("Tournament registration cancelled.")
            return

        start_date = self._ask_for_valid_date("Start date (YYYY-MM-DD)")
        if start_date is None:
            print("Tournament registration cancelled.")
            return

        end_date = self._ask_for_valid_date("End date   (YYYY-MM-DD)")
        if end_date is None:
            print("Tournament registration cancelled.")
            return

        contact_name = input("Contact person name: ").strip()
        if contact_name.lower() == 'b':
            print("Tournament registration cancelled.")
            return

        contact_phone = self._ask_for_digits_only("Contact phone")
        if contact_phone is None:
            print("Tournament registration cancelled.")
            return

        contact_email = input("Contact email: ").strip()
        if contact_email.lower() == 'b':
            print("Tournament registration cancelled.")
            return

        # show summary and confirm
        print("\nConfirm tournament:")
        print(f"  Name:          {name}")
        print(f"  Game:          {game}")
        print(f"  Location:      {location}")
        print(f"  Start date:    {start_date}")
        print(f"  End date:      {end_date}")
        print(f"  Contact name:  {contact_name}")
        print(f"  Contact phone: {contact_phone}")
        print(f"  Contact email: {contact_email}")

        confirm = input("Confirm registration (y/n): ").strip().lower()
        if confirm != "y":
            print("Tournament registration cancelled.")
            return

        # UI sends only primitive data to LogicLayerAPI
        self.logic.create_tournament(
            name=name,
            game=game,
            location=location,
            start_date=start_date,
            end_date=end_date,
            contact_name=contact_name,
            contact_phone=contact_phone,
            contact_email=contact_email,
        )

        print("Tournament registered.")

    # See tournaments

    def read_tournaments(self) -> None:
        """Display all registered tournaments"""
        tournamentList = self.logic.get_all_tournaments()

        # Sort tournaments by name using Icelandic sorting order
        if tournamentList:
            tournamentList = sort_by_name(tournamentList, 'name')

        while True:
            print("\n===== REGISTERED TOURNAMENTS =====")
            if not tournamentList:
                print("No tournaments registered yet.")
            else:
                for idx, tournament in enumerate(tournamentList, start=1):
                    print(f"{idx}. {tournament.name} ({tournament.startDate} to {tournament.endDate})")

            print()
            print("b) Back")
            print("q) Quit")
            choice = input("Choose action: ").strip().upper()

            if choice == "B":
                break
            elif choice == "Q":
                quit()
            elif choice.isdigit():
                tournament_number = int(choice)
                if 1 <= tournament_number <= len(tournamentList):
                    self.show_tournament_details(tournamentList[tournament_number - 1])
                else:
                    print(f"Invalid tournament number. Please choose between 1 and {len(tournamentList)}.")
            else:
                print("Invalid choice, try again.")

    def show_tournament_details(self, tournament) -> None:
        """Display detailed information about a tournament"""
        while True:
            print("\n===== TOURNAMENT DETAILS =====")
            print(f"Name:          {tournament.name}")
            print(f"Game:          {tournament.game}")
            print(f"Location:      {tournament.location}")
            print(f"Start date:    {tournament.startDate}")
            print(f"End date:      {tournament.endDate}")
            print(f"Contact name:  {tournament.contact}")
            print(f"Contact phone: {tournament.contactPhone}")
            print(f"Contact email: {tournament.contactEmail}")

            # Get registered teams
            registered_teams = self.logic.get_teams_for_tournament(tournament.name)
            if registered_teams:
                # Sort teams by name using Icelandic sorting order
                registered_teams_sorted = sorted(registered_teams, key=lambda t: t)
                teams_display = ", ".join(registered_teams_sorted)
                print(f"Registered teams: {teams_display}")
            else:
                print("Registered teams: No teams registered yet")

            print()
            print("1) View events for this tournament")
            print("2) View registered teams")

            # Only show register/unregister options for Admin
            from UILayer.sessionManager import get_session
            session = get_session()
            if session.is_admin():
                print("3) Register team for tournament")
                print("4) Unregister team from tournament")

            print("b) Back")
            print("q) Quit")

            choice = input("Choose action: ").strip().lower()

            if choice == "1":
                self.show_tournament_events(tournament)
            elif choice == "2":
                self.view_registered_teams(tournament)
            elif choice == "3" and session.is_admin():
                self.register_team_for_tournament(tournament)
            elif choice == "4" and session.is_admin():
                self.unregister_team_from_tournament(tournament)
            elif (choice == "3" or choice == "4") and not session.is_admin():
                print("You do not have permission to register/unregister teams.")
            elif choice == "b":
                break
            elif choice == "q":
                quit()
            else:
                print("Invalid choice, try again.")

    def view_registered_teams(self, tournament) -> None:
        """Display detailed information about teams registered for this tournament"""
        print(f"\n===== TEAMS REGISTERED FOR {tournament.name.upper()} =====")

        # Get registered teams
        registered_team_names = self.logic.get_teams_for_tournament(tournament.name)

        if not registered_team_names:
            print("No teams registered for this tournament yet.")
            input("\nPress Enter to continue...")
            return

        # Get all team objects
        all_teams = self.logic.send_team_info_to_ui()

        # Filter to get only registered teams with full details
        registered_teams = [team for team in all_teams if team.teamName in registered_team_names]

        # Sort teams by name using Icelandic sorting order
        registered_teams_sorted = sort_by_name(registered_teams, 'teamName')

        # Display each team with details
        for idx, team in enumerate(registered_teams_sorted, start=1):
            print(f"\n{idx}. {team.teamName}")
            print(f"   Team ID:  {team.teamID}")
            print(f"   Club:     {team.teamClub}")

            # Get captain info
            if team.captain:
                players = self.logic.get_players_by_team(team.teamName)
                captain_player = next((p for p in players if p.username == team.captain), None)
                if captain_player:
                    print(f"   Captain:  {captain_player.name} (@{team.captain})")
                else:
                    print(f"   Captain:  @{team.captain}")
            else:
                print(f"   Captain:  No captain selected")

            # Get players
            players = self.logic.get_players_by_team(team.teamName)
            if players:
                players_sorted = sort_by_name(players, 'name')
                player_count = len(players_sorted)
                player_names = ", ".join([p.name for p in players_sorted])
                print(f"   Players:  {player_count} - {player_names}")
            else:
                print(f"   Players:  No players registered")

        print(f"\nTotal teams registered: {len(registered_teams_sorted)}")
        input("\nPress Enter to continue...")

    def register_team_for_tournament(self, tournament) -> None:
        """Interactive flow for registering teams for a tournament (supports comma-separated input)"""
        from UILayer.sessionManager import get_session
        session = get_session()

        # Permission check - only Admin can register teams
        if not session.is_admin():
            print("\nYou do not have permission to register teams for tournaments.")
            input("Press Enter to continue...")
            return

        print("\n===== REGISTER TEAM FOR TOURNAMENT =====")

        # Get all teams
        all_teams = self.logic.send_team_info_to_ui()
        if not all_teams:
            print("No teams available. Please create teams first.")
            input("\nPress Enter to continue...")
            return

        # Get already registered teams
        registered_teams = self.logic.get_teams_for_tournament(tournament.name)

        # Filter out already registered teams and teams with date conflicts
        available_teams = []
        for team in all_teams:
            # Skip if already registered
            if team.teamName in registered_teams:
                continue
            # Skip if team has date conflict with this tournament
            if self.logic.has_team_tournament_date_conflict(tournament.name, team.teamName):
                continue
            available_teams.append(team)

        if not available_teams:
            print("No teams available for this tournament.")
            print("(Teams may already be registered or have date conflicts with other tournaments)")
            input("\nPress Enter to continue...")
            return

        # Sort available teams by name using Icelandic sorting order
        available_teams_sorted = sort_by_name(available_teams, 'teamName')

        print(f"\nSelect team(s) to register for '{tournament.name}':")
        for idx, team in enumerate(available_teams_sorted, start=1):
            print(f"{idx}) {team.teamName} (Club: {team.teamClub})")

        print("\nYou can enter:")
        print("  - A single number (e.g., 3)")
        print("  - Multiple numbers separated by commas (e.g., 1,3,5)")
        print("  - 'b' to go back")

        while True:
            choice = input("\nTeam(s) (number or comma-separated): ").strip()
            if choice.lower() == "b":
                return

            # Parse input - could be single number or comma-separated
            try:
                # Split by comma and strip whitespace
                number_strings = [s.strip() for s in choice.split(',')]

                # Convert to integers
                indices = []
                for num_str in number_strings:
                    if not num_str.isdigit():
                        raise ValueError(f"'{num_str}' is not a valid number")
                    idx = int(num_str)
                    if idx < 1 or idx > len(available_teams_sorted):
                        raise ValueError(f"Number {idx} is out of range (1-{len(available_teams_sorted)})")
                    indices.append(idx)

                # Remove duplicates while preserving order
                seen = set()
                unique_indices = []
                for idx in indices:
                    if idx not in seen:
                        seen.add(idx)
                        unique_indices.append(idx)

                # Get selected teams
                selected_teams = [available_teams_sorted[idx - 1] for idx in unique_indices]

                # Show confirmation
                print(f"\nRegister the following team(s) for '{tournament.name}'?")
                for team in selected_teams:
                    print(f"  • {team.teamName} (Club: {team.teamClub})")

                confirm = input("\nConfirm registration (y/n): ").strip().lower()

                if confirm == "y":
                    # Register all selected teams
                    for team in selected_teams:
                        self.logic.register_team_for_tournament(tournament.name, team.teamName)

                    # Show success message
                    print(f"\n✓ Successfully registered {len(selected_teams)} team(s)!")
                    for team in selected_teams:
                        print(f"  ✓ {team.teamName}")
                    input("\nPress Enter to continue...")
                    return
                else:
                    print("Registration cancelled.")
                    return

            except ValueError as e:
                print(f"Invalid input: {e}")
                print("Please try again.")

    def unregister_team_from_tournament(self, tournament) -> None:
        """Interactive flow for unregistering a team from a tournament"""
        from UILayer.sessionManager import get_session
        session = get_session()

        # Permission check - only Admin can unregister teams
        if not session.is_admin():
            print("\nYou do not have permission to unregister teams from tournaments.")
            input("Press Enter to continue...")
            return

        print("\n===== UNREGISTER TEAM FROM TOURNAMENT =====")

        # Get registered teams
        registered_teams = self.logic.get_teams_for_tournament(tournament.name)

        if not registered_teams:
            print("No teams registered for this tournament.")
            input("\nPress Enter to continue...")
            return

        # Sort teams by name using Icelandic sorting order
        registered_teams_sorted = sorted(registered_teams, key=lambda t: t)

        print(f"\nSelect team to unregister from '{tournament.name}':")
        for idx, team_name in enumerate(registered_teams_sorted, start=1):
            print(f"{idx}) {team_name}")

        print("b) Back")

        while True:
            choice = input("\nTeam (number): ").strip()
            if choice.lower() == "b":
                return
            if choice.isdigit():
                idx = int(choice)
                if 1 <= idx <= len(registered_teams_sorted):
                    selected_team_name = registered_teams_sorted[idx - 1]

                    # Confirm unregistration
                    print(f"\nUnregister '{selected_team_name}' from '{tournament.name}'?")
                    confirm = input("Confirm (y/n): ").strip().lower()

                    if confirm == "y":
                        self.logic.unregister_team_from_tournament(tournament.name, selected_team_name)
                        print(f"\n✓ {selected_team_name} unregistered successfully!")
                        input("\nPress Enter to continue...")
                        return
                    else:
                        print("Unregistration cancelled.")
                        return
            print("Invalid choice, try again.")

    def show_tournament_events(self, tournament) -> None:
        """Display all events for a specific tournament sorted by date and time"""
        eventList = self.logic.get_events_by_tournament(tournament.name)

        # Sort by date and time
        eventList.sort(key=lambda e: (e.eventDate, e.eventTime))

        while True:
            print(f"\n===== EVENTS FOR {tournament.name.upper()} =====")
            if not eventList:
                print("No events scheduled for this tournament yet.")
            else:
                for idx, event in enumerate(eventList, start=1):
                    status_symbol = "✓" if event.status == "completed" else "○"
                    print(f"{idx}. {status_symbol} {event.teamHome} vs {event.teamAway}")
                    print(f"   Date: {event.eventDate} at {event.eventTime}")
                    print(f"   Location: {event.location}")
                    if event.status == "completed":
                        winner = event.teamHome if event.homeScore > event.awayScore else event.teamAway
                        print(f"   Score: {event.homeScore} - {event.awayScore} (Winner: {winner} 🏆)")
                    print()

            print("b) Back")
            print("q) Quit")
            choice = input("Choose action: ").strip().lower()

            if choice == "b":
                break
            elif choice == "q":
                quit()
            else:
                print("Invalid choice, try again.")

    # record match result / validateScore

    def tally_score(self) -> None:
        """
        UI for recording a match result in a tournament.
        Delegates validation to LogicLayerAPI / TournamentLogic.
        """

        print("\nRecord match result")

        # 1) choose tournament
        tournaments = self.logic.get_all_tournaments()
        if not tournaments:
            print("No tournaments available.")
            return

        # Sort tournaments by name using Icelandic sorting order
        tournaments = sort_by_name(tournaments, 'name')

        print("\nChoose tournament:")
        for idx, t in enumerate(tournaments, start=1):
            name = getattr(t, "name", None) or t.get("name", "")
            print(f"{idx}) {name}")

        while True:
            choice = input("Tournament (number, or B to go back): ").strip()
            if choice.upper() == "B":
                return
            if choice.isdigit():
                idx = int(choice)
                if 1 <= idx <= len(tournaments):
                    break
            print("Invalid choice, try again.")

        selected_tournament = tournaments[idx - 1]
        tournament_id = (
            getattr(selected_tournament, "id", None)
            or selected_tournament.get("id")
        )

        # 2) ask Logic for open matches in that tournament
        matches = self.logic.get_open_matches_for_tournament(tournament_id)
        if not matches:
            print("No open matches for this tournament.")
            return

        print("\nChoose match to record result for: ")
        for idx, m in enumerate(matches, start=1):
            home = getattr(m, "home_team", None) or m.get("home_team", "")
            away = getattr(m, "away_team", None) or m.get("away_team", "")
            print(f"{idx}) {home} vs {away}")

        while True:
            choice = input("Match (number, or B to go back): ").strip()
            if choice.upper() == "B":
                return
            if choice.isdigit():
                midx = int(choice)
                if 1 <= midx <= len(matches):
                    break
            print("Invalid choice, try again.")

        selected_match = matches[midx - 1]
        match_id = getattr(selected_match, "id", None) or selected_match.get("id")
        home_team = getattr(selected_match, "home_team", None) or selected_match.get(
            "home_team", ""
        )
        away_team = getattr(selected_match, "away_team", None) or selected_match.get(
            "away_team", ""
        )

        # 3) ask for scores (digits only)
        print(f"\nEnter scores for: {home_team} vs {away_team}")
        home_score = int(self._ask_for_digits_only(f"{home_team} score: "))
        away_score = int(self._ask_for_digits_only(f"{away_team} score: "))

        # 4) send to LogicLayerAPI – it will call validateScore etc.
        self.logic.record_match_result(
            match_id=match_id,
            tournament_id=tournament_id,
            home_score=home_score,
            away_score=away_score,
        )

        print("Result recorded.")


