#from file import class
from LogicLayer.logicLayerAPI import logicWrapper

class teamUI:
    def __init__(self, logicWrapper):
        self.logicWrapper = logicWrapper
        self.teamName = input("Please Enter the Team Name: ")
        self.club = input("Please Enter the Team's Club: ")
        self.teammembers = input("Please Enter the number of players in the team: ")

    def createTeam(self, teamName, club, teammembers): #Defines the function
        teamLst = [] #Empty list to place all the information
        teamLst.appent(teamName, club, teammembers) #Fills the list
        for item in teamLst: #For loop to replace the commas with semicolons
            comToSemi = item.replace(",", ";")
            teamLst.append(comToSemi)
        return teamLst #Returns a correctly formated filled list
    
    def printTeamInfo(self):
        teamName = self.logicWrapper.getTeamInfo.team[0]
        teamClub = self.logicWrapper.getTeamInfo.team[1]
        teammembers = self.logicWrapper.getTeamInfo.team[2]

        print(teamName)
        print(teamClub)
        print(teammembers)