import csv
from Models.teamModel import Team

class TeamData:
    def __init__(self):
        pass
    
    def saveNewTeam(self):
        pass

    def readAllTeams(self) -> list[Team]: 
        """ Reads the CSV to find the teams """
        
        teamList = []
        with open('datalayer/repository/TeamDB.csv', mode= 'r') as dataBase: #Opens the file 
            cvsDB = csv.reader(dataBase, delimiter= ';')
        
            for info in cvsDB: #Returns line per line in csv
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
                teamNameList.append(row[0]).upper()
        return teamNameList

