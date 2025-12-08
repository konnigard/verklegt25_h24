#from file import class
from DataLayer.dataLayerAPI import DataWrapper


class TeamLogicClass:
    def __init__(self):
        self.DataWrapper = DataWrapper()  


    def grabTeamData(self):
        """ Takes the info from the Data layer and make it printable for UI  """
        readTeams = self.DataWrapper.sendToLogic() #Takes what's in sendToLogic
        return readTeams
    
    def writeNewTeam(self):
        from LogicLayer.logicLayerAPI import logicWrapper
        newTeam = logicWrapper.sendFromUIToLogic()
        return newTeam