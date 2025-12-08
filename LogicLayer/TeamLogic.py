#from file import class
from DataLayer.dataLayerAPI import DataWrapper
from Models.teamModel import Team

class TeamLogicClass:
    def __init__(self, datawrapper_inn: DataWrapper):
        self.datawrapper: DataWrapper = datawrapper_inn  


    def grabTeamData(self):
        """ Takes the info from the Data layer and make it printable for UI  """
        readTeams = self.datawrapper.loadAllTeams() #Takes what's in sendToLogic
        return readTeams
    
    def writeNewTeam(self):
        pass
    
    def validateAndAddNewTeam(self, newTeam: Team) :

        # 1) Check if all fileds are valid 

        # 2) check if all uniqe things are uniqe 
        #   - This will require reading all teams from file
        allTeams: list[Team]= self.datawrapper.loadAllTeams()
        for team in allTeams :
            if team.teamName.upper() == newTeam.teamName.upper():
                return "Team name already Exists"
                # Here we should deal with the fact the name is not UNIQE
            # if team.X == newTeam.X   # Some other check to do ??
            
        # 3) If all checks are OK, then call datawrapper and write new team to file 
        #   - check if data call was successfull, 
        #   - if not can we fix it or do we need to raise an exception to pas to the UI
        return "Creates Team YIPPIE"     