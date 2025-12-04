#from file import class
from DataLayer.dataLayerAPI import DataWrapper
from LogicLayer.logicLayerAPI import LogicWrapper

class TeamLogicClass:
    def __init__(self):
        self.DataWrapper = DataWrapper()
        self.LogicWrapper = LogicWrapper  

    def validateTeamCreation(self):
        """ Checks to see if team already exists """
        readTeam = self.DataWrapper.sendToLogic()
        newTeam = self.LogicWrapper.sendFromUIToLogic()


    def grabTeamData(self):
        """ Takes the info from the Data layer and make it printable for UI  """
        readTeams = self.DataWrapper.sendToLogic() #Takes what's in sendToLogic
        teamList = list(readTeams) #Makes it a list

        teamName = teamList[0] #Reads the Team name
        teamClub = teamList[1] #Reads the Team Club
        teammates = teamList[2] #Reads the Teammates
        
        return teamName, teamClub, teammates 
    
    def sendToDataLayer(self):
        newTeam = self.LogicWrapper.sendFromUIToLogic()
        return newTeam