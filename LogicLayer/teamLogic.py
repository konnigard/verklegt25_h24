#from file import class
from DataLayer.dataLayerAPI import Wrapper

class teamLogic:
    def __init__():
        pass

    def validateTeamCreation():
        """ Atthugar til að sjá hvort lið sé til núþegar """

    def grabTeamInfo(readTeams):
        """ Nær í teamData frá dataLayerAPI """

        readTeams = Wrapper.readTeams() #Calls upon the function of the same name in the Data Wrapper
        
        teamList = list(readTeams)

        return teamList

