#from file import class
from LogicLayer.TeamLogic import TeamLogicClass
from LogicLayer.clubLogic import ClubLogicClass
from DataLayer.dataLayerAPI import DataWrapper

class LogicWrapper:
    def __init__(self):
        datawrapper = DataWrapper()
        self.teamLogic = TeamLogicClass( datawrapper )
        # Only once instance of the wrapper, sent in to the logic classes
        self.clubLogic = ClubLogicClass()

####  Functions for Teams  #####################################
    def printTeam(self): #Makes the teamData accessable to the UI
        return self.teamLogic.grabTeamData()

    def addNewTeam(self, newTeam):
        return self.teamLogic.validateAndAddNewTeam(newTeam)
###############################################################

####  Functions for Players  ##################################

#################################################

####  Functions for Clubs  ##################################

    def sendClubInfoToUI(self): #Makes the clubData accessible to the UI
        listOfClubs = self.clubLogic.grabClubData()
        return listOfClubs

    def saveClubFromUI(self, club):
        self.clubLogic.saveNewClub(club)
#################################################