from LogicLayer.logicLayerAPI import LogicWrapper
from UILayer.sessionManager import get_session
from UILayer.sortingUtils import sort_by_name


class AuthUI:
    """Handles user authentication and login flow"""

    def __init__(self):
        self.logic = LogicWrapper()

    def login(self):
        """
        Display login screen and authenticate user

        Returns:
            True if user successfully logged in, False if user quit
        """
        session = get_session()

        while True:
            print("\n" + "=" * 40)
            print("        AUTHENTICATION")
            print("=" * 40)
            print("1 Admin")
            print("2 Captain")
            print("3 User")
            print("=" * 40)
            print("q Quit")
            print("=" * 40)

            choice = input("Select user type: ").strip().lower()

            if choice == "1":
                session.set_admin()
                print("\nLogged in as Admin")
                return True

            elif choice == "2":
                # Captain login requires team selection
                if self._captain_login():
                    return True
                # If captain login fails, loop back to user type selection

            elif choice == "3":
                session.set_user()
                print("\nLogged in as User")
                return True

            elif choice == "q":
                return False

            else:
                print("Invalid choice, please try again.")

    def _captain_login(self):
        """
        Handle captain login with username input, team selection and validation

        Returns:
            True if captain successfully authenticated, False if cancelled
        """
        session = get_session()

        # Step 1: Ask for captain username
        print("\n===== CAPTAIN LOGIN =====")
        captain_username = input("Enter your username (or 'b' to cancel): ").strip()

        if captain_username.lower() == 'b':
            return False

        if not captain_username:
            print("Username cannot be empty.")
            input("Press Enter to continue...")
            return False

        # Step 2: Get all teams
        teams = self.logic.send_team_info_to_ui()

        if not teams:
            print("\nNo teams available. Cannot login as Captain.")
            input("Press Enter to continue...")
            return False

        # Sort teams by name
        teams_sorted = sort_by_name(teams, 'teamName')

        # Step 3: Show team selection WITHOUT captain usernames
        print("\n===== SELECT YOUR TEAM =====")
        print("Select the team you are captain of:")
        for idx, team in enumerate(teams_sorted, start=1):
            print(f"{idx}) {team.teamName}")
        print("\nb) Back")

        while True:
            choice = input("\nTeam (number or 'b' to cancel): ").strip().lower()

            if choice == 'b':
                return False

            if choice.isdigit():
                idx = int(choice)
                if 1 <= idx <= len(teams_sorted):
                    selected_team = teams_sorted[idx - 1]

                    # Validate captain assignment
                    if not selected_team.captain:
                        print(f"\nError: Team '{selected_team.teamName}' has no captain assigned.")
                        print("Please select a different team or choose a different role.")
                        input("Press Enter to continue...")
                        return False

                    # Validate entered username matches team's captain
                    if captain_username != selected_team.captain:
                        print(f"\nError: You are not the captain of team '{selected_team.teamName}'.")
                        print("Username does not match the assigned captain for this team.")
                        input("Press Enter to continue...")
                        return False

                    # Validate captain is actually a player on the team
                    players = self.logic.get_players_by_team(selected_team.teamName)

                    if not players:
                        print(f"\nError: Team '{selected_team.teamName}' has no players.")
                        print("Cannot login as captain of a team with no players.")
                        input("Press Enter to continue...")
                        return False

                    player_usernames = [p.username for p in players]

                    if captain_username not in player_usernames:
                        print(f"\nError: Captain '@{captain_username}' is not a player on this team.")
                        print("Please contact an administrator to fix this issue.")
                        input("Press Enter to continue...")
                        return False

                    # Success - set captain session
                    session.set_captain(captain_username, selected_team.teamName)
                    print(f"\nLogged in as Captain of {selected_team.teamName}")
                    return True

            print("Invalid choice, try again.")
