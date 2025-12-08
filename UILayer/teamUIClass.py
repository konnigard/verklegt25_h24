#from file import class
from Models.teamModel import Team
from LogicLayer.logicLayerAPI import LogicWrapper

class TeamUI:
    def __init__(self):
        self.LogicWrapper = LogicWrapper()

    def createTeam(self, teamName: str, club: str, teammembers): #Defines the function
        newTeam = Team(teamName, club) #Empty list to place all the information
        return newTeam #Returns a correctly formated filled list
    
    def showTeam(self):
        showTeam = self.LogicWrapper.sendTeamInfoToUI()
        return showTeam
