import csv
from Models.tournamentTeamModel import TournamentTeam

class TournamentTeamData:
    def __init__(self):
        pass

    def registerTeam(self, tournamentTeam: TournamentTeam) -> None:
        """Registers a team for a tournament (prevents duplicates)"""
        # Check if already registered
        if self.isTeamRegistered(tournamentTeam.tournamentName, tournamentTeam.teamName):
            return  # Already registered, don't add duplicate

        with open('DataLayer/repository/TournamentTeamDB.csv', mode='a', newline='') as dataBase:
            csvWriter = csv.writer(dataBase, delimiter=';')
            csvWriter.writerow([tournamentTeam.tournamentName, tournamentTeam.teamName])

    def getTeamsForTournament(self, tournamentName: str) -> list[str]:
        """Returns list of team names registered for a tournament"""
        teamNames = []
        try:
            with open('DataLayer/repository/TournamentTeamDB.csv', mode='r') as dataBase:
                csvReader = csv.reader(dataBase, delimiter=';')
                for row in csvReader:
                    if len(row) >= 2:
                        if row[0] == tournamentName:
                            teamNames.append(row[1])
        except FileNotFoundError:
            pass
        return teamNames

    def getTournamentsForTeam(self, teamName: str) -> list[str]:
        """Returns list of tournament names a team is registered for"""
        tournamentNames = []
        try:
            with open('DataLayer/repository/TournamentTeamDB.csv', mode='r') as dataBase:
                csvReader = csv.reader(dataBase, delimiter=';')
                for row in csvReader:
                    if len(row) >= 2:
                        if row[1] == teamName:
                            tournamentNames.append(row[0])
        except FileNotFoundError:
            pass
        return tournamentNames

    def isTeamRegistered(self, tournamentName: str, teamName: str) -> bool:
        """Checks if a team is registered for a tournament"""
        try:
            with open('DataLayer/repository/TournamentTeamDB.csv', mode='r') as dataBase:
                csvReader = csv.reader(dataBase, delimiter=';')
                for row in csvReader:
                    if len(row) >= 2:
                        if row[0] == tournamentName and row[1] == teamName:
                            return True
        except FileNotFoundError:
            pass
        return False

    def unregisterTeam(self, tournamentName: str, teamName: str) -> None:
        """Removes a team's registration from a tournament"""
        registrations = []
        try:
            with open('DataLayer/repository/TournamentTeamDB.csv', mode='r') as dataBase:
                csvReader = csv.reader(dataBase, delimiter=';')
                for row in csvReader:
                    if len(row) >= 2:
                        # Keep all registrations except the one to remove
                        if not (row[0] == tournamentName and row[1] == teamName):
                            registrations.append(row)
        except FileNotFoundError:
            return

        # Rewrite file without the removed registration
        with open('DataLayer/repository/TournamentTeamDB.csv', mode='w', newline='') as dataBase:
            csvWriter = csv.writer(dataBase, delimiter=';')
            for reg in registrations:
                csvWriter.writerow(reg)
