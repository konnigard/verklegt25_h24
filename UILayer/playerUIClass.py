from datetime import datetime
from playerModel import Player
from LogicLayer.logicLayerAPI import LogicLayerAPI


class playerUI:
    def __init__(self) -> None:
        self.logic = LogicLayerAPI()

    def player_menu(self) -> None:
        while True:
            print("\n===== LEIKMANSSKJÁR=====")
            print("1 Skrá nýjan leikmann")
            print("2 Skoða leikmann ")
            print("B Back")
            choice = input("Veldu aðgerð: ").strip().upper()

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
            dob = input("Fæðingardagur (YYYY-MM-DD): ").strip()
            try:
                datetime.strptime(dob, "%Y-%m-%d")
                return dob
            except ValueError:
                print("Invalid date. Vinsamlegast sláðu þetta inn svona YYYY-MM-DD.")

    def ask_for_valid_phone(self) -> str:
        """Ask until user enters a phone number with digits only."""
        while True:
            phone = input("Símanúmer (Einungis tölustafir): ").strip()
            if phone.isdigit():
                return phone
            else:
                print("Símanúmer getur bara innihaldið tölustafi.")

    # ---- FLOW For register new player  ----

    def create_player_flow(self) -> None:
        """Ask user for player info, check username availability and confirm."""

        print("\nSkrá nýjan leikmann")

        name = input("Nafn leikmans: ").strip()
        dob = self.ask_for_valid_date()
        address = input("Heimilisfang: ").strip()
        phone_number = self.ask_for_valid_phone()
        email = input("Tölvupóstur: ").strip()
        link = input("Hlekkur: ").strip()

        # username: username available?
        while True:
            username = input("Notendanafn: ").strip()

            if hasattr(self.logic, "is_username_available"):
                if self.logic.is_username_available(username):
                    break
                else:
                    print("Þetta notendarnafn er nú þegar tekið. Vinsamlegast veldu annað.")
            else:
                break

        # show summary and confirm
        print("\nConfirm registration:")
        print(f"  Nafn:         {name}")
        print(f"  Fæðingrdagur:{dob}")
        print(f"  Heimilisfang:      {address}")
        print(f"  Símanúmer:        {phone_number}")
        print(f"  Email:        {email}")
        print(f"  Hlekkur:         {link}")
        print(f"  Notendanafn:     {username}")

        confirm = input("Samþykkja skráningu (y/n): ").strip().lower()

        if confirm != "y":
            print("Hætt við skráningu.")
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
        print("\n.")
