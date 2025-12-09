#from file imports class
from DataLayer.clubData import ClubData
from DataLayer.teamData import TeamData
from Models.teamModel import Team
from DataLayer.clubData import ClubData

class DataWrapper:
    def __init__(self):
        self.TeamData = TeamData()
    
####  Functions for Teams  ##################################
    def loadAllTeams(self) -> list[Team]:
        '''Returns all teams or empty list if no teams exist''' 
        teamList = self.TeamData.readAllTeams() 
        self.ClubData = ClubData()

    def sendToLogic(self): #Takes what readTeams returns and sends it to logic layer
        teamList = self.TeamData.readTeams()
        return teamList
    
    def LoadTeamByID(self, teamID ) -> Team:
        t : Team = Team("smuu", "Plee")
        return t
    
    def writeNewTeam(self, team: Team) -> bool:
        print("write new team ran")
        return True

    def updateTeam(self, team: Team) -> bool: 
        print("update Team Ran")
        return True
##############################################################

####  Functions for Players  ##################################

##############################################################

    def sendToData(self):
        from LogicLayer.TeamLogic import TeamLogicClass
        newTeamToData = TeamLogicClass.writeNewTeam()
        return newTeamToData

    def getClubsForLogic(self): #Takes what readClubs returns and sends it to logic layer
        clubList = self.ClubData.readClubs()
        return clubList

    def saveClubToData(self, club):
        self.ClubData.writeClub(club)
    