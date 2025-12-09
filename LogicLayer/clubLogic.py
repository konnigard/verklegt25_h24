#from file import class
from DataLayer.dataLayerAPI import DataWrapper

class ClubLogicClass:
    def __init__(self):
        self.DataWrapper = DataWrapper()

    def grabClubData(self):
        """ Takes the info from the Data layer and makes it available for UI """
        readClubs = self.DataWrapper.getClubsForLogic()
        return readClubs

    def saveNewClub(self, club):
        """ Saves a new club to the data layer """
        self.DataWrapper.saveClubToData(club)
