#from file imports class
from DataLayer.clubData import ClubData
from DataLayer.teamData import TeamData
from DataLayer.playerData import PlayerData
from Models.teamModel import Team
from Models.playerModel import Player

class DataWrapper:
    def __init__(self):
        self.TeamData = TeamData()
        self.ClubData = ClubData()
        self.PlayerData = PlayerData()
    
####  Functions for Teams  ##################################
    def loadAllTeams(self) -> list[Team]:
        '''Returns all teams or empty list if no teams exist''' 
        teamList = self.TeamData.readAllTeams() 

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
    def writePlayer(self, player: Player):
        return self.PlayerData.savePlayer(player)
    
    def readTeam(self) -> list:
        return self.PlayerData.loadPlayer()

##############################################################

####  Functions for Clubs  ##################################
    def getClubsForLogic(self): #Takes what readClubs returns and sends it to logic layer
        clubList = self.ClubData.readClubs()
        return clubList

    def saveClubToData(self, club):
        self.ClubData.writeClub(club)
    
##############################################################    