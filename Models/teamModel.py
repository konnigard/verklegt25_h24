from Models.playerModel import Player

class Team:
    def __init__(self, teamID, teamName: str, teamClub: str):
        self.teamID: int = teamID
        self.teamName: str = teamName
        self.teamClub: str = teamClub
        self.teammates: list[Player] = []
    
    def __repr__(self):
        return f"Team Name: {self.teamName} Club: {self.teamClub})"