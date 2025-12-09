#from file import class
from LogicLayer.readTeamLogic  import TeamLogicClassRead
from playerModel import Player


class LogicLayerAPI:
    def __init__(self) -> None:
        # Temporary storage so username checking and showing players works
        self._players: list[Player] = []
        self.teamLogic = TeamLogicClassRead()
    
    def sendTeamInfoToUI(self): #Makes the teamData accessable to the UI
        listOfTeam = self.teamLogic.grabTeamData()
        return listOfTeam
    
    def is_username_available(self, username: str) -> bool:
        """Return True if no stored player has this username."""
        for p in self._players:
            if p.username == username:
                return False
        return True

    def create_player(self, player: Player) -> None:
        """Add a player to storage. Later this will save to DataLayer."""
        if not self.is_username_available(player.username):
            raise ValueError("Username already exists.")

        self._players.append(player)

        print("\n[LogicLayer] Player saved:")
        print("Name:", player.name)
        print("Username:", player.username)
        print("Email:", player.email)

    def get_all_players(self) -> list[Player]:
        """Return all stored players (for Show Players)."""
        return self._players
