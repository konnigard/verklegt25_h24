#from file import class
from DataLayer.dataLayerAPI import DataWrapper
from Models.teamModel import Team

class TeamLogicClass:
    def __init__(self):
        self.DataWrapper = DataWrapper()


    def grabTeamData(self):
        """ Takes the info from the Data layer and make it printable for UI  """
        readTeams = self.datawrapper.loadAllTeams() #Takes what's in sendToLogic
        return readTeams

    def saveNewTeam(self, team):
        """ Saves a new team to the data layer """
        self.DataWrapper.writeNewTeam(team)

    def updateTeam(self, team):
        """ Updates an existing team in the data layer """
        self.DataWrapper.updateTeam(team)
