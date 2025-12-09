from Models.playerModel import Player

class Team:
    def __init__(self, teamID, teamName: str, teamClub: str):
        self.teamID: int = teamID
        self.teamName: str = teamName
        self.teamClub: str = teamClub
        self.teammates: list[Player] = []

    def validateTeamID(self, teamID):
        if isinstance(teamID, self.teamID):
            return True
        else: 
            return False
    
    def validateTeamName(self, teamName):
        if isinstance(teamName, self.teamName):
            return True
        else:
            return False
    
    def validateTeamClub(self, teamClub):
        if isinstance(teamClub, self.teamClub):
            return True
        else:
            return False
    
    def __repr__(self):
        return f"Team Name: {self.teamName} Club: {self.teamClub})"