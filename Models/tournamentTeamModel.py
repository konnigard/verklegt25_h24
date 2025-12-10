class TournamentTeam:
    """Represents a team's registration in a tournament"""
    def __init__(self, tournamentName: str, teamName: str):
        self.tournamentName: str = tournamentName
        self.teamName: str = teamName

    def __repr__(self):
        return f"Tournament: {self.tournamentName} - Team: {self.teamName}"
