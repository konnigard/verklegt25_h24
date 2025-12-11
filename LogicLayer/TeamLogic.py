#from file import class
from DataLayer.dataLayerAPI import DataWrapper
from Models.teamModel import Team

class TeamLogicClass:
    def __init__(self):
        self.DataWrapper = DataWrapper()


    def grabTeamData(self):
        """ Takes the info from the Data layer and make it printable for UI  """
        readTeams = self.datawrapper.loadAllTeams() #Takes what's in sendToLogic
        return readTeams

    def saveNewTeam(self, team):
        """ Saves a new team to the data layer """
        self.DataWrapper.writeNewTeam(team)

    def updateTeam(self, team):
        """ Updates an existing team in the data layer """
        self.DataWrapper.updateTeam(team)

    def isTeamNameAvailable(self, teamName: str) -> bool:
        """ Checks if a team name is available (not already taken) """
        all_teams = self.DataWrapper.sendToLogic()
        existing_team_names = [team.teamName.lower() for team in all_teams]
        return teamName.lower() not in existing_team_names
