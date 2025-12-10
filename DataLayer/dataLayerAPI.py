#from file imports class
from DataLayer.teamData import TeamData
from DataLayer.clubData import ClubData

class DataWrapper:
    def __init__(self):
        self.TeamData = TeamData()
        self.ClubData = ClubData()

    def sendToLogic(self): #Takes what readTeams returns and sends it to logic layer
        teamList = self.TeamData.readTeams()
        return teamList

    def sendToData(self):
        from LogicLayer.TeamLogic import TeamLogicClass
        newTeamToData = TeamLogicClass.writeNewTeam()
        return newTeamToData

    def getClubsForLogic(self): #Takes what readClubs returns and sends it to logic layer
        clubList = self.ClubData.readClubs()
        return clubList

    def saveClubToData(self, club):
        self.ClubData.writeClub(club)
    