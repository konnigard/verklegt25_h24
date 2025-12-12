#from file import class
from DataLayer.dataLayerAPI import DataWrapper

class ClubLogicClass:
    def __init__(self):
        self.DataWrapper = DataWrapper()

    def grab_club_data(self):
        """ Takes the info from the Data layer and makes it available for UI """
        read_clubs = self.DataWrapper.get_clubs_for_logic()
        return read_clubs

    def save_new_club(self, club):
        """ Saves a new club to the data layer """
        self.DataWrapper.save_club_to_data(club)
