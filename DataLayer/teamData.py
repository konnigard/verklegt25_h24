import csv
from Models.teamModel import Team

class TeamData:
    def __init__(self):
        pass
    
    def writeTeams(self):
        """ Registers the team to the CSV """

        from DataLayer.dataLayerAPI import DataWrapper
        with open('datalayer/repository/TeamDB', mode= 'w') as dataBase: #Opens file in write
            toBeWritten = DataWrapper.sendToData() #Input from user
            cvsWritter = csv.writer(toBeWritten)
        return "Team Created"


    def readTeams(self): 
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

