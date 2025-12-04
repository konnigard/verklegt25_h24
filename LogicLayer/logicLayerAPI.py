#from file import class
from LogicLayer.teamLogic  import TeamLogicClass
from UILayer.teamUIClass import TeamUI

class LogicWrapper:
    def __init__(self):
        self.TeamLogic = TeamLogicClass()
        self.TeamUI = TeamUI
    
    def sendTeamInfoToUI(self): #Makes the teamData accessable to the UI
        listOfTeam = self.TeamLogic.grabTeamData()
        return listOfTeam
    
    def sendFromUIToLogic(self):
        newInput = self.TeamUI.createTeam()
        return newInput