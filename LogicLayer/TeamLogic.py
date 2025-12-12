#from file import class
from DataLayer.dataLayerAPI import DataWrapper


class TeamLogicClass:
    def __init__(self):
        self.DataWrapper = DataWrapper()


    def grab_team_data(self):
        """ Takes the info from the Data layer and make it printable for UI  """
        readTeams = self.DataWrapper.send_to_logic() #Takes what's in sendToLogic
        return readTeams

    def save_new_team(self, team):
        """ Saves a new team to the data layer """
        self.DataWrapper.write_new_team(team)

    def update_team(self, team):
        """ Updates an existing team in the data layer """
        self.DataWrapper.update_team(team)

    def is_team_name_available(self, teamName: str) -> bool:
        """ Checks if a team name is available (not already taken) """
        all_teams = self.DataWrapper.send_to_logic()
        existing_team_names = [team.teamName.lower() for team in all_teams]
        return teamName.lower() not in existing_team_names