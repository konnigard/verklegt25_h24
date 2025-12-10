from LogicLayer.logicLayerAPI import LogicLayerAPI


class ClubUI:
    def __init__(self) -> None:
        # UI only talks to the logic wrapper
        self.logic = LogicLayerAPI()

    def createClub(self) -> None:
        """Create a new club and assign teams to it."""

        print("\nCreate club")

        name = input("Club name: ").strip()
        contact_name = input("Contact person name: ").strip()
        phone = input("Contact phone: ").strip()
        email = input("Contact email: ").strip()

        # Ask logic layer for all teams so user can choose from the list
        teams = self.logic.get_all_teams()

        if not teams:
            print("No teams available. You must create teams before creating a club.")
            return

        print("\nAvailable teams:")
        for index, team in enumerate(teams, start=1):
            # assumes each team has a 'name' attribute
            print(f"{index}) {team.name}")

        print()
        print("Select teams that belong to this club.")
        print("Enter numbers separated by commas, e.g. 1,3,4.")
        print("Leave empty if you do not want to assign any teams now.")

        selected_team_indices: list[int] = []

        while True:
            raw = input("Your choice: ").strip()
            if raw == "":
                break

            parts = [p.strip() for p in raw.split(",") if p.strip() != ""]
            try:
                indices = [int(p) for p in parts]
            except ValueError:
                print("Invalid input. Please enter only numbers separated by commas.")
                continue

            # check range
            if any(i < 1 or i > len(teams) for i in indices):
                print("One or more numbers are out of range. Try again.")
                continue

            # everything ok
            selected_team_indices = indices
            break

        selected_teams = [teams[i - 1] for i in selected_team_indices]

        # Show summary and confirm
        print("\nConfirm club creation:")
        print(f"  Club name:      {name}")
        print(f"  Contact person: {contact_name}")
        print(f"  Phone:          {phone}")
        print(f"  Email:          {email}")
        print("  Teams:")

        if selected_teams:
            for t in selected_teams:
                print(f"    - {t.name}")
        else:
            print("    (no teams selected)")

        confirm = input("Confirm creation (y/n): ").strip().lower()
        if confirm != "y":
            print("Club creation cancelled.")
            return

        # For LogicLayerAPI we only send the data it needs.
        # Common pattern: send name, contact info, and a list of team IDs.
        team_ids = [t.id for t in selected_teams]

        self.logic.create_club(
            name=name,
            contact_name=contact_name,
            phone=phone,
            email=email,
            team_ids=team_ids,
        )

        print("Club created.")

    def readClub(self) -> None:
        """Let the user choose a club and show its details including team list."""

        clubs = self.logic.get_all_clubs()

        if not clubs:
            print("\nNo clubs have been created yet.")
            return

        print("\nClubs:")
        for index, club in enumerate(clubs, start=1):
            # assumes each club has a 'name' attribute
            print(f"{index}) {club.name}")

        while True:
            choice = input("Select a club by number (or 'b' to go back): ").strip().lower()

            if choice == "b":
                return

            try:
                idx = int(choice)
            except ValueError:
                print("Invalid input. Please enter a number or 'b' to go back.")
                continue

            if idx < 1 or idx > len(clubs):
                print("Number out of range. Try again.")
                continue

            selected_club = clubs[idx - 1]
            break

        # Show club details
        print("\nClub details:")
        print(f"  Name:          {selected_club.name}")
        if hasattr(selected_club, "contact_name"):
            print(f"  Contact name:  {selected_club.contact_name}")
        if hasattr(selected_club, "phone"):
            print(f"  Phone:         {selected_club.phone}")
        if hasattr(selected_club, "email"):
            print(f"  Email:         {selected_club.email}")

        print("  Teams:")

        # We expect the club to provide a team list in some form.
        # Adjust this part to match your Club/Team models.
        teams = getattr(selected_club, "teams", None)
        team_names = getattr(selected_club, "team_names", None)

        if teams is not None:
            # list of Team objects
            for t in teams:
                name = getattr(t, "name", str(t))
                print(f"    - {name}")
        elif team_names is not None:
            # list of plain strings
            for name in team_names:
                print(f"    - {name}")
        else:
            print("    (no teams registered for this club)")
