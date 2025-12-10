#from file import class
from DataLayer.dataLayerAPI import DataWrapper
from Models.tournamentTeamModel import TournamentTeam

class TournamentTeamLogicClass:
    def __init__(self):
        self.DataWrapper = DataWrapper()

    def registerTeam(self, tournamentName: str, teamName: str) -> None:
        """Registers a team for a tournament"""
        tournamentTeam = TournamentTeam(tournamentName, teamName)
        self.DataWrapper.registerTeamForTournament(tournamentTeam)

    def getTeamsForTournament(self, tournamentName: str) -> list[str]:
        """Returns list of team names registered for a tournament"""
        return self.DataWrapper.getTeamsForTournament(tournamentName)

    def getTournamentsForTeam(self, teamName: str) -> list[str]:
        """Returns list of tournaments a team is registered for"""
        return self.DataWrapper.getTournamentsForTeam(teamName)

    def isTeamRegistered(self, tournamentName: str, teamName: str) -> bool:
        """Checks if a team is registered for a tournament"""
        return self.DataWrapper.isTeamRegisteredForTournament(tournamentName, teamName)

    def unregisterTeam(self, tournamentName: str, teamName: str) -> None:
        """Removes a team's registration from a tournament"""
        self.DataWrapper.unregisterTeamFromTournament(tournamentName, teamName)
