import csv
from Models.teamModel import Team

class TeamData:
    def __init__(self):
        pass
    
    def saveNewTeam(self, newTeam: Team):
        with open('datalayer/repository/TeamDB.csv', mode='a', newline='') as dataBase:
            csvWriter = csv.writer(dataBase, delimiter=';')
            # teamlist is now a string, write it directly
            csvWriter.writerow([newTeam.teamID, newTeam.teamName, newTeam.teamClub])

    def readAllTeams(self) -> list[Team]: 
        """ Reads the CSV to find the teams """
        
        #Creates Emptylist that gets added to in the for loop
        teamList = []

        #Opens the file 
        with open('datalayer/repository/TeamDB.csv', mode= 'r') as dataBase: 
            cvsDB = csv.reader(dataBase, delimiter= ';')

            #Returns line per line in csv
            for info in cvsDB: 
                teamName = info[0]
                teamClub = info[1]
                readTeam = Team(teamName, teamClub)
                teamList.append(readTeam)
            
        return teamList
    #name, club, players

    def checksTeamName(self):
        teamNameList = []
        with open('datalayer/repository/TeamDB.csv', mode= 'r') as dataBase:
            csvDB = csv.reader(dataBase, delimiter= ';')

            for row in csvDB:
                teamNameList.append(row[1]).upper()
        return teamNameList

