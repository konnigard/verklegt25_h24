#from file import class
from DataLayer.dataLayerAPI import DataWrapper

class PlayerLogicClass:
    def __init__(self):
        self.DataWrapper = DataWrapper()

    def grabPlayerData(self):
        """ Takes the info from the Data layer and makes it available for UI """
        readPlayers = self.DataWrapper.readPlayers()
        return readPlayers

    def saveNewPlayer(self, player):
        """ Saves a new player to the data layer """
        self.DataWrapper.writePlayer(player)

    def grabPlayersByTeam(self, teamName: str):
        """ Gets players for a specific team """
        players = self.DataWrapper.readPlayersByTeam(teamName)
        return players
