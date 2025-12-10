from Models.playerModel import Player

class Team:
    def __init__(self, teamID: str, teamName: str, teamClub: str, captain: str = ""):
        self.teamID: str = teamID
        self.teamName: str = teamName
        self.teamClub: str = teamClub
        self.captain: str = captain  # Username of the captain
        self.teammates: list[Player] = []

    def __repr__(self):
        captain_info = f"\nCaptain: {self.captain}" if self.captain else ""
        return f"Team ID: {self.teamID}\nTeam Name: {self.teamName}\nClub: {self.teamClub}{captain_info})"
