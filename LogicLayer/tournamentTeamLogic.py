#from file import class
from DataLayer.dataLayerAPI import DataWrapper
from Models.tournamentTeamModel import TournamentTeam
from LogicLayer.tournamentLogic import TournamentLogicClass
from datetime import datetime

class TournamentTeamLogicClass:
    def __init__(self):
        self.DataWrapper = DataWrapper()
        self.TournamentLogic = TournamentLogicClass()

    def register_team(self, tournamentName: str, teamName: str) -> None:
        """Registers a team for a tournament"""
        # Get the tournament details for the new registration
        newTournament = self.TournamentLogic.get_tournament_by_name(tournamentName)
        if not newTournament:
            raise ValueError(f"Tournament '{tournamentName}' not found")

        # Parse the start date of the new tournament
        newStartDate = datetime.strptime(newTournament.startDate, "%Y-%m-%d")

        # Get all tournaments this team is already registered for
        registeredTournaments = self.DataWrapper.get_tournaments_for_team(teamName)

        # Check for date conflicts
        for regTournamentName in registeredTournaments:
            regTournament = self.TournamentLogic.get_tournament_by_name(regTournamentName)
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
        self.DataWrapper.register_team_for_tournament(tournamentTeam)

    def get_teams_for_tournament(self, tournamentName: str) -> list[str]:
        """Returns list of team names registered for a tournament"""
        return self.DataWrapper.get_teams_for_tournament(tournamentName)

    def get_tournaments_for_team(self, teamName: str) -> list[str]:
        """Returns list of tournaments a team is registered for"""
        return self.DataWrapper.get_tournaments_for_team(teamName)

    def is_team_registered(self, tournamentName: str, teamName: str) -> bool:
        """Checks if a team is registered for a tournament"""
        return self.DataWrapper.is_team_registered_for_tournament(tournamentName, teamName)

    def unregister_team(self, tournamentName: str, teamName: str) -> None:
        """Removes a team's registration from a tournament"""
        self.DataWrapper.unregister_team_from_tournament(tournamentName, teamName)

    def has_date_conflict(self, tournamentName: str, teamName: str) -> bool:
        """Checks if a team has a date conflict with the specified tournament"""
        # Get the tournament details for the new registration
        newTournament = self.TournamentLogic.get_tournament_by_name(tournamentName)
        if not newTournament:
            return False

        # Parse the start date of the new tournament
        newStartDate = datetime.strptime(newTournament.startDate, "%Y-%m-%d")

        # Get all tournaments this team is already registered for
        registeredTournaments = self.DataWrapper.get_tournaments_for_team(teamName)

        # Check for date conflicts
        for regTournamentName in registeredTournaments:
            regTournament = self.TournamentLogic.get_tournament_by_name(regTournamentName)
            if regTournament:
                regStartDate = datetime.strptime(regTournament.startDate, "%Y-%m-%d")
                regEndDate = datetime.strptime(regTournament.endDate, "%Y-%m-%d")

                # Check if the new tournament's start date falls within the existing tournament's date range
                if regStartDate <= newStartDate <= regEndDate:
                    return True

        return False
