#from file import class
from LogicLayer.teamLogic  import TeamLogicClass

class LogicWrapper:
    def __init__(self):
        self.TeamLogic = TeamLogicClass()
    
    def sendTeamInfoToUI(self): #Makes the teamData accessable to the UI
        listOfTeam = self.TeamLogic.grabTeamData()
        return listOfTeam