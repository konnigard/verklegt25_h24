#from file imports class
from DataLayer.teamData import TeamData

class DataWrapper:
    def __init__(self):
        self.TeamData = TeamData()
    
    def sendToLogic(self): #Takes what readTeams returns and sends it to logic layer 
        teamList = self.TeamData.readTeams()
        return teamList
    
    def sendToData(self):
        from LogicLayer.TeamLogic import TeamLogicClass
        newTeamToData = TeamLogicClass.writeNewTeam()
        return newTeamToData
    