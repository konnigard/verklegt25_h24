from UILayer.teamUIClass import TeamUI

class Test:
    def __init__(self):
        self.TeamUI = TeamUI()

    def printTeam(self):
        paper = self.TeamUI.showTeam()
        return paper
    