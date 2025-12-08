from Models.playerModel import Player

class Team:
    def __init__(self, teamName: str, teamClub: str):
        self.teamName: str = teamName
        self.teamClub: str = teamClub
        self.teammates: list[Player] = []

    def __repr__(self):
        return f"Team(teamName= {self.teamName}, teamClub= {self.teamClub})"