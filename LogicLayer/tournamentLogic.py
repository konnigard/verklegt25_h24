#from file import class
from DataLayer.dataLayerAPI import DataWrapper
from Models.tournamentModel import Tournament

class TournamentLogicClass:
    def __init__(self):
        self.DataWrapper = DataWrapper()

    def grabTournamentData(self):
        """ Takes the info from the Data layer and makes it available for UI """
        readTournaments = self.DataWrapper.readTournaments()
        return readTournaments

    def saveNewTournament(self, tournament):
        """ Saves a new tournament to the data layer """
        self.DataWrapper.writeTournaments(tournament)

    def createTournamentFromData(self, name, game, location, start_date, end_date, contact_name, contact_phone, contact_email):
        """ Creates a tournament object from raw data """
        tournament = Tournament(name, game, location, start_date, end_date, contact_name, contact_phone, contact_email)
        return tournament

    def getTournamentByName(self, tournamentName: str) -> Tournament:
        """ Returns a tournament by name or None if not found """
        tournaments = self.DataWrapper.readTournaments()
        for tournament in tournaments:
            if tournament.name == tournamentName:
                return tournament
        return None
