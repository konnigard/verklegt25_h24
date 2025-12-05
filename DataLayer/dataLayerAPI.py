#from file imports class
from DataLayer.readTeamData import ReadTeamData

class DataWrapper:
    def __init__(self):
        self.TeamData = ReadTeamData()
    
    def sendToLogic(self): #Takes what readTeams returns and sends it to logic layer 
        teamList = self.TeamData.readTeams()
        return teamList
    