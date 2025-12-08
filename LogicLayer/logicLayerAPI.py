#from file import class
from LogicLayer.TeamLogic import TeamLogicClass

class LogicWrapper:
    def __init__(self):
        self.teamLogic = TeamLogicClass()
    
    def sendTeamInfoToUI(self): #Makes the teamData accessable to the UI
        listOfTeam = self.teamLogic.grabTeamData()
        return listOfTeam
    
    def sendFromUItoLogic(self):
        from UILayer.teamUIClass import TeamUI
        newTeam = TeamUI.createTeam()
        return newTeam
    