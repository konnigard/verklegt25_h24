#from file import class
from LogicLayer.logicLayerAPI import LogicWrapper

class TeamUI:
    def __init__(self):
        self.LogicWrapper = LogicWrapper()

    def createTeam(self, teamName, club, teammembers): #Defines the function
        teamLst = [] #Empty list to place all the information
        teamLst.appent(teamName, club, teammembers) #Fills the list
        for item in teamLst: #For loop to replace the commas with semicolons
            comToSemi = item.replace(",", ";")
            teamLst.append(comToSemi)
        return teamLst #Returns a correctly formated filled list
    
    def showTeam(self):
        showTeam = self.LogicWrapper.sendTeamInfoToUI()
        return showTeam
