#from file import class
from DataLayer.dataLayerAPI import DataWrapper

class TeamLogicClass:
    def __init__(self):
        self.DataWrapper = DataWrapper()

    def validateTeamCreation(self):
        """ Atthugar til að sjá hvort lið sé til núþegar """

    def grabTeamData(self):
        """  """
        readTeams = self.DataWrapper.sendToLogic() #Takes what's in sendToLogic
        teamList = list(readTeams) #Makes it a list

        teamName = teamList[0]
        teamClub = teamList[1]
        teammates = teamList[2]
        
        return teamName, teamClub, teammates 