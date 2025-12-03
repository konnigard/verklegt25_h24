#from file import class
from LogicLayer.teamLogic import TeamLogic

class LogicWrapper:
    def __init__(self, Teamlogic):
        self.TeamLogic = TeamLogic

    def getTeamInfo(self): #Grabs the function of the same name from the teamLogic file
        team = TeamLogic.grabTeamInfo
        return team