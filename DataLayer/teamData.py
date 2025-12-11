import csv
from Models.teamModel import Team

class TeamData:
    def __init__(self):
        pass

    def _getNextTeamID(self) -> str:
        """Generates the next available TeamID"""
        teams = self.readAllTeams()
        if not teams:
            return "1"

        # Find the maximum ID and increment
        max_id = max(int(team.teamID) for team in teams)
        return str(max_id + 1)

    def saveNewTeam(self, newTeam: Team):
        # Auto-generate TeamID if not set or empty
        if not newTeam.teamID:
            newTeam.teamID = self._getNextTeamID()

        with open('DataLayer/repository/TeamDB.csv', mode='a', newline='') as dataBase:
            csvWriter = csv.writer(dataBase, delimiter=';')
            # Write team with captain field (username)
            csvWriter.writerow([newTeam.teamID, newTeam.teamName, newTeam.teamClub, newTeam.captain])

    def readAllTeams(self) -> list[Team]:
        """ Reads the CSV to find the teams """

        #Creates Emptylist that gets added to in the for loop
        teamList = []

        try:
            #Opens the file
            with open('DataLayer/repository/TeamDB.csv', mode='r') as dataBase:
                cvsDB = csv.reader(dataBase, delimiter= ';')

                #Returns line per line in csv
                for info in cvsDB:
                    if len(info) >= 3:  # Ensure we have all required fields
                        teamID = info[0]
                        teamName = info[1]
                        teamClub = info[2]
                        captain = info[3] if len(info) >= 4 else ""
                        readTeam = Team(teamID, teamName, teamClub, captain)
                        teamList.append(readTeam)
        except FileNotFoundError:
            # If file doesn't exist, return empty list
            pass

        return teamList
    #name, club, players

    def updateTeam(self, updatedTeam: Team):
        """ Updates an existing team in the CSV """
        teams = self.readAllTeams()

        with open('DataLayer/repository/TeamDB.csv', mode='w', newline='') as dataBase:
            csvWriter = csv.writer(dataBase, delimiter=';')

            for team in teams:
                if team.teamID == updatedTeam.teamID:
                    # Write the updated team
                    csvWriter.writerow([updatedTeam.teamID, updatedTeam.teamName, updatedTeam.teamClub, updatedTeam.captain])
                else:
                    # Write the existing team unchanged
                    csvWriter.writerow([team.teamID, team.teamName, team.teamClub, team.captain])

    def checksTeamName(self):
        teamNameList = []
        with open('DataLayer/repository/TeamDB.csv', mode='r') as dataBase:
            csvDB = csv.reader(dataBase, delimiter= ';')

            for row in csvDB:
                teamNameList.append(row[1].upper())
        return teamNameList

