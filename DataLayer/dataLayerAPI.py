#from file imports class
from DataLayer.teamData import TeamData
from Models.teamModel import Team

class DataWrapper:
    def __init__(self):
        self.TeamData = TeamData()
    
####  Functions for Teams  ##################################
    def loadAllTeams(self) -> list[Team]:
        '''Returns all teams or empty list if no teams exist''' 
        teamList = self.TeamData.readAllTeams() 
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