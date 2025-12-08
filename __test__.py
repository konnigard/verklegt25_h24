from UILayer.readTeamUIClass import TeamUIRead

class Test:
    def __init__(self):
        self.TeamUI = TeamUIRead()

    def printTeam(self):
        paper = self.TeamUI.showTeam()
        return paper
    
tester = Test()
paper = tester.printTeam()
print(paper[0])
print(paper[1])
print(paper[2])