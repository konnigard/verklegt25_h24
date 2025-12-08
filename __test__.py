from UILayer.readTeamUIClass import TeamUIRead

class Test:
    def __init__(self):
        self.TeamUI = TeamUIRead()

    def printTeam(self):
        paper = self.TeamUI.showTeam()
        return paper
    
tester = Test()
paper = tester.printTeam()
for team in paper:
    print(team)
    print(team.teamName)