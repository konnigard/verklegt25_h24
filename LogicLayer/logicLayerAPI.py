#from file import class
from LogicLayer.TeamLogic import TeamLogicClass
from DataLayer.dataLayerAPI import DataWrapper

class LogicWrapper:
    def __init__(self):
        datawrapper = DataWrapper()
        self.teamLogic = TeamLogicClass( datawrapper )
        # Only once instance of the wrapper, sent in to the logic classes
        # self.nextLogic = XXXX ( datawrapper )

####  Functions for Teams  #####################################
    def printTeam(self): #Makes the teamData accessable to the UI
        return self.teamLogic.grabTeamData()

    def addNewTeam(self, newTeam):
        return self.teamLogic.validateAndAddNewTeam(newTeam)
###############################################################

####  Functions for Players  ##################################

#################################################