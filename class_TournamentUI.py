from datetime import datetime
from LogicLayer.logicLayerAPI import LogicLayerAPI


class TournamentUI:
    """UI layer for tournaments ONLY speak to LogicLayerAPI."""

    def __init__(self) -> None:
        self.logic = LogicLayerAPI()

    # Passa að það séu bara leyfðar alvöru dagsetningar og tölustafir.

    def _ask_for_valid_date(self, prompt: str) -> str:
        """Ask until user enters a valid date in YYYY-MM-DD format."""
        while True:
            value = input(prompt).strip()
            try:
                datetime.strptime(value, "%Y-%m-%d")
                return value
            except ValueError:
                print("Invalid date. Please use format YYYY-MM-DD.")

    def _ask_for_digits_only(self, prompt: str) -> str:
        """Ask until user enters digits only (for phone numbers etc.)."""
        while True:
            value = input(prompt).strip()
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

        name = input("Tournament name: ").strip()
        game = input("Game: ").strip()
        location = input("Location: ").strip()

        start_date = self._ask_for_valid_date(
            "Start date (YYYY-MM-DD): "
        )
        end_date = self._ask_for_valid_date(
            "End date   (YYYY-MM-DD): "
        )

        contact_name = input("Contact person name: ").strip()
        contact_phone = self._ask_for_digits_only("Contact phone: ")
        contact_email = input("Contact email: ").strip()

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
        """ Ask LogicLayerAPI for tournaments and display them, exact structure of the returned data is up to Logic layer.
        Here we assume a list of dicts or objects with simple attributes."""
        tournaments = self.logic.get_all_tournaments()

        if not tournaments:
            print("\nNo tournaments found.")
            return

        print("\nTournaments:")
        for idx, t in enumerate(tournaments, start=1):
            # try to support both dict and object style
            name = getattr(t, "name", None) or t.get("name", "")
            start = getattr(t, "start_date", None) or t.get("start_date", "")
            end = getattr(t, "end_date", None) or t.get("end_date", "")
            print(f"{idx}) {name} ({start} – {end})")

        input("\nPress Enter to go back...")

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


## ATH VANTAR AÐ GETA VALIÐ LIÐ SEM KEPPA GETA GERT LEIKJADAGSKRÁNA OG SIÐAN 