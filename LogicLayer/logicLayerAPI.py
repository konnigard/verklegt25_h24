#from file import class
from LogicLayer.readTeamLogic  import TeamLogicClassRead

class LogicWrapper:
    def __init__(self):
        self.teamLogic = TeamLogicClassRead()
    
    def sendTeamInfoToUI(self): #Makes the teamData accessable to the UI
        listOfTeam = self.teamLogic.grabTeamData()
        return listOfTeam