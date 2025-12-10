#from file import class
from DataLayer.dataLayerAPI import DataWrapper
from Models.tournamentTeamModel import TournamentTeam
from LogicLayer.tournamentLogic import TournamentLogicClass
from datetime import datetime

class TournamentTeamLogicClass:
    def __init__(self):
        self.DataWrapper = DataWrapper()
        self.TournamentLogic = TournamentLogicClass()

    def registerTeam(self, tournamentName: str, teamName: str) -> None:
        """Registers a team for a tournament"""
        # Get the tournament details for the new registration
        newTournament = self.TournamentLogic.getTournamentByName(tournamentName)
        if not newTournament:
            raise ValueError(f"Tournament '{tournamentName}' not found")

        # Parse the start date of the new tournament
        newStartDate = datetime.strptime(newTournament.startDate, "%Y-%m-%d")

        # Get all tournaments this team is already registered for
        registeredTournaments = self.DataWrapper.getTournamentsForTeam(teamName)

        # Check for date conflicts
        for regTournamentName in registeredTournaments:
            regTournament = self.TournamentLogic.getTournamentByName(regTournamentName)
            if regTournament:
                regStartDate = datetime.strptime(regTournament.startDate, "%Y-%m-%d")
                regEndDate = datetime.strptime(regTournament.endDate, "%Y-%m-%d")

                # Check if the new tournament's start date falls within the existing tournament's date range
                if regStartDate <= newStartDate <= regEndDate:
                    raise ValueError(
                        f"Team '{teamName}' cannot be registered for '{tournamentName}' "
                        f"because it conflicts with '{regTournamentName}' "
                        f"({regTournament.startDate} to {regTournament.endDate})"
                    )

        # If no conflicts, proceed with registration
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

    def hasDateConflict(self, tournamentName: str, teamName: str) -> bool:
        """Checks if a team has a date conflict with the specified tournament"""
        # Get the tournament details for the new registration
        newTournament = self.TournamentLogic.getTournamentByName(tournamentName)
        if not newTournament:
            return False

        # Parse the start date of the new tournament
        newStartDate = datetime.strptime(newTournament.startDate, "%Y-%m-%d")

        # Get all tournaments this team is already registered for
        registeredTournaments = self.DataWrapper.getTournamentsForTeam(teamName)

        # Check for date conflicts
        for regTournamentName in registeredTournaments:
            regTournament = self.TournamentLogic.getTournamentByName(regTournamentName)
            if regTournament:
                regStartDate = datetime.strptime(regTournament.startDate, "%Y-%m-%d")
                regEndDate = datetime.strptime(regTournament.endDate, "%Y-%m-%d")

                # Check if the new tournament's start date falls within the existing tournament's date range
                if regStartDate <= newStartDate <= regEndDate:
                    return True

        return False
