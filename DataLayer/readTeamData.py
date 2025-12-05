import csv

class ReadTeamData:
    def __init__(self):
        pass
    
    def writeTeams(self):
        """ Registers the team to the CSV """


    def readTeams(self):
        """ Reads the CSV to find the teams """

        with open('datalayer/repository/TeamDB.csv', mode= 'r') as dataBase: #Opens the file 
            cvsDB = csv.reader(dataBase, delimiter= ';')
            for info in cvsDB: #Returns line per line in csv
                return info

            #name, club, players

