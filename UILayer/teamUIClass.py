class teamUI:
    def __init__(self):
        self.teamName = input("Please Enter the Team Name: ")
        self.club = input("Please Enter the Team's Club: ")
        self.teammembers = input("Please Enter the number of players in the team: ")

    def createTeam(teamName, club, teammembers):
        teamLst = []
        teamLst.appent(teamName; club; teammembers)
        return teamLst