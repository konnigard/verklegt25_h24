from datetime import datetime
from LogicLayer.logicLayerAPI import LogicWrapper
from UILayer.sortingUtils import sort_by_name
import locale


class EventUI:
    """UI layer for events/matches within tournaments"""

    def __init__(self) -> None:
        self.logic = LogicWrapper()

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

    def _ask_for_valid_time(self, prompt: str) -> str:
        """Ask until user enters a valid time in HH:MM format or 'b' to cancel."""
        while True:
            value = input(prompt + " (or 'b' to cancel): ").strip()
            if value.lower() == 'b':
                return None
            try:
                datetime.strptime(value, "%H:%M")
                return value
            except ValueError:
                print("Invalid time. Please use format HH:MM (e.g., 14:30).")

    def event_menu(self) -> None:
        """Main event menu"""
        while True:
            print("\n===== EVENT MENU =====")
            print("1) Create new event")
            print("2) View all events")
            print("3) View events by tournament")
            print("4) Record event score")
            print()
            print("b) Back")
            print("q) Quit")

            choice = input("Choose action: ").strip().lower()

            if choice == "1":
                self.create_event()
            elif choice == "2":
                self.view_all_events()
            elif choice == "3":
                self.view_events_by_tournament()
            elif choice == "4":
                self.record_score()
            elif choice == "b":
                break
            elif choice == "q":
                quit()
            else:
                print("Invalid choice, try again.")

    def create_event(self) -> None:
        """Create a new event/match"""
        print("\nCreate New Event")
        print("(Enter 'b' at any prompt to cancel)\n")

        # Get list of tournaments
        tournaments = self.logic.get_all_tournaments()
        if not tournaments:
            print("No tournaments available. Please create a tournament first.")
            input("\nPress Enter to continue...")
            return

        # Sort tournaments by name using Icelandic sorting order
        tournaments = sort_by_name(tournaments, 'name')

        # Select tournament
        print("\nSelect tournament:")
        for idx, t in enumerate(tournaments, start=1):
            print(f"{idx}) {t.name}")

        while True:
            choice = input("Tournament (number or 'b' to cancel): ").strip()
            if choice.lower() == 'b':
                print("Event creation cancelled.")
                return
            if choice.isdigit():
                idx = int(choice)
                if 1 <= idx <= len(tournaments):
                    selected_tournament = tournaments[idx - 1]
                    break
            print("Invalid choice, try again.")

        # Get teams registered for this tournament
        registered_teams = self.logic.get_teams_for_tournament(selected_tournament.name)

        if not registered_teams:
            print(f"\n❌ NO TEAMS REGISTERED: No teams are registered for tournament '{selected_tournament.name}'")
            print("   Please register teams for this tournament first.")
            input("\nPress Enter to continue...")
            return

        if len(registered_teams) < 2:
            print(f"\n❌ INSUFFICIENT TEAMS: Only {len(registered_teams)} team(s) registered for '{selected_tournament.name}'")
            print("   At least 2 teams are required to create an event.")
            input("\nPress Enter to continue...")
            return

        # Get all teams and filter to only registered teams
        all_teams = self.logic.sendTeamInfoToUI()
        registered_team_objects = [t for t in all_teams if t.teamName in registered_teams]

        # Get unfinished events for THIS TOURNAMENT to check which teams are already scheduled
        # Teams can only be in one unfinished event at a time within the same tournament
        # Winners of completed events in this tournament should be available for next round
        tournament_events = self.logic.get_events_by_tournament(selected_tournament.name)
        teams_in_unfinished_events = set()
        for event in tournament_events:
            if event.status != "completed":  # scheduled or in_progress
                teams_in_unfinished_events.add(event.teamHome)
                teams_in_unfinished_events.add(event.teamAway)

        # Filter out eliminated teams and teams already in unfinished events
        available_teams = []
        for team in registered_team_objects:
            # Check if team is eliminated
            is_eliminated, elim_msg = self.logic.check_team_eliminated(team.teamName, selected_tournament.name)
            if is_eliminated:
                continue

            # Check if team is already in an unfinished event
            if team.teamName in teams_in_unfinished_events:
                continue

            available_teams.append(team)

        # Check if enough available teams remain
        if len(available_teams) < 2:
            print(f"\n❌ INSUFFICIENT TEAMS: Only {len(available_teams)} team(s) available for '{selected_tournament.name}'")
            print("   Teams are unavailable if they are:")
            print("   - Already eliminated from the tournament")
            print("   - Already scheduled for an unfinished event")
            print("   At least 2 available teams are required to create an event.")
            input("\nPress Enter to continue...")
            return

        # Sort available teams by name using Icelandic sorting order
        available_teams = sort_by_name(available_teams, 'teamName')

        # Select home team
        print("\nSelect HOME team:")
        for idx, team in enumerate(available_teams, start=1):
            print(f"{idx}) {team.teamName} (Club: {team.teamClub})")

        while True:
            choice = input("Home team (number or 'b' to cancel): ").strip()
            if choice.lower() == 'b':
                print("Event creation cancelled.")
                return
            if choice.isdigit():
                idx = int(choice)
                if 1 <= idx <= len(available_teams):
                    teamHome = available_teams[idx - 1].teamName
                    break
            print("Invalid choice, try again.")

        # Select away team (different from home team)
        print("\nSelect AWAY team:")
        away_team_options = [t for t in available_teams if t.teamName != teamHome]
        for idx, team in enumerate(away_team_options, start=1):
            print(f"{idx}) {team.teamName} (Club: {team.teamClub})")

        while True:
            choice = input("Away team (number or 'b' to cancel): ").strip()
            if choice.lower() == 'b':
                print("Event creation cancelled.")
                return
            if choice.isdigit():
                idx = int(choice)
                if 1 <= idx <= len(away_team_options):
                    teamAway = away_team_options[idx - 1].teamName
                    break
            print("Invalid choice, try again.")

        eventDate = self._ask_for_valid_date("Event date (YYYY-MM-DD)")
        if eventDate is None:
            print("Event creation cancelled.")
            return

        eventTime = self._ask_for_valid_time("Event time (HH:MM)")
        if eventTime is None:
            print("Event creation cancelled.")
            return

        location = input("Location: ").strip()
        if location.lower() == 'b':
            print("Event creation cancelled.")
            return

        # Show summary and confirm
        print("\nConfirm event creation:")
        print(f"  Tournament:   {selected_tournament.name}")
        print(f"  Match:        {teamHome} vs {teamAway}")
        print(f"  Date:         {eventDate}")
        print(f"  Time:         {eventTime}")
        print(f"  Location:     {location}")

        confirm = input("Confirm creation (y/n): ").strip().lower()
        if confirm != "y":
            print("Event creation cancelled.")
            return

        # Create event (EventID will be auto-generated)
        self.logic.create_event(
            tournamentName=selected_tournament.name,
            teamHome=teamHome,
            teamAway=teamAway,
            eventDate=eventDate,
            eventTime=eventTime,
            location=location,
            status="scheduled"
        )

        print("Event created successfully.")

    def view_all_events(self) -> None:
        """Display all events"""
        eventList = self.logic.get_all_events()

        # Sort by tournament name (Icelandic order), then date, then time
        eventList.sort(key=lambda e: (locale.strxfrm(e.tournamentName), e.eventDate, e.eventTime))

        while True:
            print("\n===== ALL EVENTS =====")
            if not eventList:
                print("No events registered yet.")
            else:
                for idx, event in enumerate(eventList, start=1):
                    status_symbol = "✓" if event.status == "completed" else "○"
                    print(f"{idx}. {status_symbol} {event.teamHome} vs {event.teamAway} - {event.eventDate} at {event.eventTime}")
                    print(f"   Tournament: {event.tournamentName}")
                    if event.status == "completed":
                        winner = event.teamHome if event.homeScore > event.awayScore else event.teamAway
                        print(f"   Score: {event.homeScore} - {event.awayScore} (Winner: {winner} 🏆)")

            print()
            print("b) Back")
            print("q) Quit")
            choice = input("Choose action: ").strip().upper()

            if choice == "B":
                break
            elif choice == "Q":
                quit()
            elif choice.isdigit():
                event_number = int(choice)
                if 1 <= event_number <= len(eventList):
                    self.show_event_details(eventList[event_number - 1])
                else:
                    print(f"Invalid event number. Please choose between 1 and {len(eventList)}.")
            else:
                print("Invalid choice, try again.")

    def view_events_by_tournament(self) -> None:
        """View events for a specific tournament"""
        tournaments = self.logic.get_all_tournaments()
        if not tournaments:
            print("No tournaments available.")
            input("\nPress Enter to continue...")
            return

        # Sort tournaments by name using Icelandic sorting order
        tournaments = sort_by_name(tournaments, 'name')

        # Select tournament
        print("\nSelect tournament:")
        for idx, t in enumerate(tournaments, start=1):
            print(f"{idx}) {t.name}")

        while True:
            choice = input("Tournament (number, or B to go back): ").strip()
            if choice.upper() == "B":
                return
            if choice.isdigit():
                idx = int(choice)
                if 1 <= idx <= len(tournaments):
                    selected_tournament = tournaments[idx - 1]
                    break
            print("Invalid choice, try again.")

        # Get events for tournament
        eventList = self.logic.get_events_by_tournament(selected_tournament.name)

        # Sort by date and time
        eventList.sort(key=lambda e: (e.eventDate, e.eventTime))

        while True:
            print(f"\n===== EVENTS FOR {selected_tournament.name.upper()} =====")
            if not eventList:
                print("No events for this tournament yet.")
            else:
                for idx, event in enumerate(eventList, start=1):
                    status_symbol = "✓" if event.status == "completed" else "○"
                    print(f"{idx}. {status_symbol} {event.teamHome} vs {event.teamAway} - {event.eventDate} at {event.eventTime}")
                    if event.status == "completed":
                        winner = event.teamHome if event.homeScore > event.awayScore else event.teamAway
                        print(f"   Score: {event.homeScore} - {event.awayScore} (Winner: {winner} 🏆)")

            print()
            print("b) Back")
            print("q) Quit")
            choice = input("Choose action: ").strip().upper()

            if choice == "B":
                break
            elif choice == "Q":
                quit()
            elif choice.isdigit():
                event_number = int(choice)
                if 1 <= event_number <= len(eventList):
                    self.show_event_details(eventList[event_number - 1])
                else:
                    print(f"Invalid event number. Please choose between 1 and {len(eventList)}.")
            else:
                print("Invalid choice, try again.")

    def show_event_details(self, event) -> None:
        """Display detailed information about an event"""
        print("\n===== EVENT DETAILS =====")
        print(f"Event ID:     {event.eventID}")
        print(f"Tournament:   {event.tournamentName}")
        print(f"Match:        {event.teamHome} vs {event.teamAway}")
        print(f"Date:         {event.eventDate}")
        print(f"Time:         {event.eventTime}")
        print(f"Location:     {event.location}")
        print(f"Status:       {event.status}")
        if event.status == "completed":
            winner = event.teamHome if event.homeScore > event.awayScore else event.teamAway
            loser = event.teamAway if event.homeScore > event.awayScore else event.teamHome
            print(f"Final Score:  {event.homeScore} - {event.awayScore}")
            print(f"Winner:       {winner} 🏆")
            print(f"Eliminated:   {loser} ❌")
        print()
        input("Press Enter to continue...")

    def record_score(self) -> None:
        """Record score for an event"""
        eventList = self.logic.get_all_events()

        # Filter for non-completed events
        scheduled_events = [e for e in eventList if e.status != "completed"]

        if not scheduled_events:
            print("\nNo scheduled events available to record scores.")
            input("\nPress Enter to continue...")
            return

        print("\n===== RECORD EVENT SCORE =====")
        print("Select event:")
        for idx, event in enumerate(scheduled_events, start=1):
            print(f"{idx}) {event.teamHome} vs {event.teamAway} - {event.eventDate}")
            print(f"   Tournament: {event.tournamentName}")

        while True:
            choice = input("Event (number, or B to go back): ").strip()
            if choice.upper() == "B":
                return
            if choice.isdigit():
                idx = int(choice)
                if 1 <= idx <= len(scheduled_events):
                    selected_event = scheduled_events[idx - 1]
                    break
            print("Invalid choice, try again.")

        # Get scores
        print(f"\nEnter scores for: {selected_event.teamHome} vs {selected_event.teamAway}")
        while True:
            try:
                home_score = int(input(f"{selected_event.teamHome} score: ").strip())
                away_score = int(input(f"{selected_event.teamAway} score: ").strip())
                break
            except ValueError:
                print("Please enter valid numbers.")

        # Confirm
        print(f"\nConfirm score: {selected_event.teamHome} {home_score} - {away_score} {selected_event.teamAway}")
        confirm = input("Confirm (y/n): ").strip().lower()

        if confirm != "y":
            print("Score recording cancelled.")
            return

        # Record score
        self.logic.record_event_score(selected_event.eventID, home_score, away_score)
        print("Score recorded successfully.")
