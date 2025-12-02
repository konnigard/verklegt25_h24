#from file import class
from LogicLayer.teamLogic import teamLogic

class logicWrapper:
    def __init__(self, teamloic):
        self.teamLogic = teamLogic

    def getTeamInfo(self): #Grabs the function of the same name from the teamLogic file
        team = teamLogic.grabTeamInfo
        return team