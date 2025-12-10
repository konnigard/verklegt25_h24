from datetime import datetime
from LogicLayer.logicLayerAPI import LogicWrapper
from UILayer.sortingUtils import sort_by_name
import locale


class EventUI:
    """UI layer for events/matches within tournaments"""

    def __init__(self) -> None:
        self.logic = LogicWrapper()

    def _ask_for_valid_date(self, prompt: str) -> str:
        """Ask until user enters a valid date in YYYY-MM-DD format."""
        while True:
            value = input(prompt).strip()
            try:
                datetime.strptime(value, "%Y-%m-%d")
                return value
            except ValueError:
                print("Invalid date. Please use format YYYY-MM-DD.")

    def _ask_for_valid_time(self, prompt: str) -> str:
        """Ask until user enters a valid time in HH:MM format."""
        while True:
            value = input(prompt).strip()
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
            choice = input("Tournament (number): ").strip()
            if choice.isdigit():
                idx = int(choice)
                if 1 <= idx <= len(tournaments):
                    selected_tournament = tournaments[idx - 1]
                    break
            print("Invalid choice, try again.")

        # Get event details
        eventID = input("Event ID: ").strip()
        teamHome = input("Home team: ").strip()
        teamAway = input("Away team: ").strip()

        # Check if teams are registered for this tournament
        if not self.logic.is_team_registered_for_tournament(selected_tournament.name, teamHome):
            print(f"\n❌ NOT REGISTERED: Team '{teamHome}' is not registered for tournament '{selected_tournament.name}'")
            print("   Please register the team for this tournament first.")
            input("\nPress Enter to continue...")
            return

        if not self.logic.is_team_registered_for_tournament(selected_tournament.name, teamAway):
            print(f"\n❌ NOT REGISTERED: Team '{teamAway}' is not registered for tournament '{selected_tournament.name}'")
            print("   Please register the team for this tournament first.")
            input("\nPress Enter to continue...")
            return

        eventDate = self._ask_for_valid_date("Event date (YYYY-MM-DD): ")
        eventTime = self._ask_for_valid_time("Event time (HH:MM): ")
        location = input("Location: ").strip()

        # Check for team conflicts
        home_conflict, home_msg = self.logic.check_team_availability(teamHome, eventDate, eventTime)
        if home_conflict:
            print(f"\n❌ CONFLICT: {home_msg}")
            input("\nPress Enter to continue...")
            return

        away_conflict, away_msg = self.logic.check_team_availability(teamAway, eventDate, eventTime)
        if away_conflict:
            print(f"\n❌ CONFLICT: {away_msg}")
            input("\nPress Enter to continue...")
            return

        # Check for team elimination (knockout tournament)
        home_eliminated, home_elim_msg = self.logic.check_team_eliminated(teamHome, selected_tournament.name)
        if home_eliminated:
            print(f"\n❌ ELIMINATED: {home_elim_msg}")
            print("   In knockout tournaments, only winning teams can advance.")
            input("\nPress Enter to continue...")
            return

        away_eliminated, away_elim_msg = self.logic.check_team_eliminated(teamAway, selected_tournament.name)
        if away_eliminated:
            print(f"\n❌ ELIMINATED: {away_elim_msg}")
            print("   In knockout tournaments, only winning teams can advance.")
            input("\nPress Enter to continue...")
            return

        # Show summary and confirm
        print("\nConfirm event creation:")
        print(f"  Event ID:     {eventID}")
        print(f"  Tournament:   {selected_tournament.name}")
        print(f"  Match:        {teamHome} vs {teamAway}")
        print(f"  Date:         {eventDate}")
        print(f"  Time:         {eventTime}")
        print(f"  Location:     {location}")

        confirm = input("Confirm creation (y/n): ").strip().lower()
        if confirm != "y":
            print("Event creation cancelled.")
            return

        # Create event
        self.logic.create_event(
            eventID=eventID,
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
