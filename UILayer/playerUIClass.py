from datetime import datetime
from playerModel import Player
from LogicLayer.logicLayerAPI import LogicLayerAPI


class playerUI:
    def __init__(self) -> None:
        self.logic = LogicLayerAPI()

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
        """Ask until user enters a valid date in YYYY-MM-DD format."""
        while True:
            dob = input("Date of birth (YYYY-MM-DD): ").strip()
            try:
                datetime.strptime(dob, "%Y-%m-%d")
                return dob
            except ValueError:
                print("Invalid date. Please use format YYYY-MM-DD.")

    def ask_for_valid_phone(self) -> str:
        """Ask until user enters a phone number with digits only."""
        while True:
            phone = input("Phone number (digits only): ").strip()
            if phone.isdigit():
                return phone
            else:
                print("Phone number must contain digits only.")

    # ---- FLOW For register new player  ----

    def create_player_flow(self) -> None:
        """Ask user for player info, check username availability and confirm."""

        print("\nRegister player")

        name = input("Player name: ").strip()
        dob = self.ask_for_valid_date()
        address = input("Home address: ").strip()
        phone_number = self.ask_for_valid_phone()
        email = input("Email: ").strip()
        link = input("Link: ").strip()

        # username: username available?
        while True:
            username = input("Username: ").strip()

            if hasattr(self.logic, "is_username_available"):
                if self.logic.is_username_available(username):
                    break
                else:
                    print("This username is already taken. Please choose another one.")
            else:
                break

        # show summary and confirm
        print("\nConfirm registration:")
        print(f"  Name:         {name}")
        print(f"  Date of birth:{dob}")
        print(f"  Address:      {address}")
        print(f"  Phone:        {phone_number}")
        print(f"  Email:        {email}")
        print(f"  Link:         {link}")
        print(f"  Username:     {username}")

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
        )

        self.logic.create_player(player)
        print("Player registered.")

    def show_players(self) -> None:
        print("\n[UI] Show players not implemented yet.")
