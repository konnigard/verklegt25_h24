#from file import class
from DataLayer.dataLayerAPI import DataWrapper
from Models.tournamentModel import Tournament

class TournamentLogicClass:
    def __init__(self):
        self.DataWrapper = DataWrapper()

    def grab_tournament_data(self):
        """ Takes the info from the Data layer and makes it available for UI """
        readTournaments = self.DataWrapper.read_tournaments()
        return readTournaments

    def save_new_tournament(self, tournament):
        """ Saves a new tournament to the data layer """
        self.DataWrapper.write_tournaments(tournament)

    def create_tournament_from_data(self, name, game, location, start_date, end_date, contact_name, contact_phone, contact_email):
        """ Creates a tournament object from raw data """
        tournament = Tournament(name, game, location, start_date, end_date, contact_name, contact_phone, contact_email)
        return tournament

    def get_tournament_by_name(self, tournamentName: str) -> Tournament:
        """ Returns a tournament by name or None if not found """
        tournaments = self.DataWrapper.read_tournaments()
        for tournament in tournaments:
            if tournament.name == tournamentName:
                return tournament
        return None
