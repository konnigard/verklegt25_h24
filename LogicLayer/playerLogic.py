#from file import class
from DataLayer.dataLayerAPI import DataWrapper

class PlayerLogicClass:
    def __init__(self):
        self.DataWrapper = DataWrapper()

    def grab_player_data(self):
        """ Takes the info from the Data layer and makes it available for UI """
        readPlayers = self.DataWrapper.read_players()
        return readPlayers

    def save_new_player(self, player):
        """ Saves a new player to the data layer """
        self.DataWrapper.write_player(player)

    def grab_players_by_team(self, teamName: str):
        """ Gets players for a specific team """
        players = self.DataWrapper.read_players_by_team(teamName)
        return players

    def is_username_available(self, username: str) -> bool:
        """ Checks if a username is available (not already taken) """
        all_players = self.DataWrapper.read_players()
        existing_usernames = [player.username.lower() for player in all_players]
        return username.lower() not in existing_usernames

    def update_player(self, player):
        """ Updates an existing player through the data layer """
        self.DataWrapper.update_player(player)
