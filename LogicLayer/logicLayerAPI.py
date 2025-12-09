#from file import class
from LogicLayer.TeamLogic import TeamLogicClass
from LogicLayer.clubLogic import ClubLogicClass

class LogicWrapper:
    def __init__(self):
        self.teamLogic = TeamLogicClass()
        self.clubLogic = ClubLogicClass()

    def sendTeamInfoToUI(self): #Makes the teamData accessable to the UI
        listOfTeam = self.teamLogic.grabTeamData()
        return listOfTeam

    def sendFromUItoLogic(self):
        from UILayer.teamUIClass import TeamUI
        newTeam = TeamUI.createTeam()
        return newTeam

    def sendClubInfoToUI(self): #Makes the clubData accessible to the UI
        listOfClubs = self.clubLogic.grabClubData()
        return listOfClubs

    def saveClubFromUI(self, club):
        self.clubLogic.saveNewClub(club)
    