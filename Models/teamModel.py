from Models.playerModel import Player

class Team:
    def __init__(self, teamName: str, teamClub: str):
        self.teamName: str = teamName
        self.teamClub: str = teamClub
        self.teammates: list[Player] = []

    def __repr__(self):
        return f"Team Name: {self.teamName}\nClub: {self.teamClub})"