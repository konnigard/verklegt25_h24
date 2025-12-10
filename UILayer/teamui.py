class teamUI:
    def __init__(self)->None:
        """Ui talar bara vil LogicLayerAPI (LL wrapper)"""
        self.logic = LogicLayerAPI()

    def create_team_flow(self) -> None:
        """As user for team info and send to logic layer."""
        print("\nRegister team")

        name = input("Team name: ").strip()
        team_games = input()
        club_name = input("Club name (optional): ").strip()
        homepage = input("Team homepage link (optional): ").strip()

        # Hér gætum við lika beðið um td fyrirliða 

        # Köllum í logic layer wrapperin 

    self.logic.creat_team(
        team_name = name,
        club_name = club
    )