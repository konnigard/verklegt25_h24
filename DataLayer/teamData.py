import csv

def writeTeams():
    """ Skrifar inn team á CSV skjalið """


def readTeams():
    """ Skoðar CSV til að sjá liðið """

    with open('datalayer/repository/TeamDB.csv', mode= 'r') as dataBase: #Opens the file 
        cvsDB = csv.reader(dataBase, delimiter= ';')
        for info in cvsDB: #Returns line per line in csv
            return info

    #name, club, players

test = readTeams()

print(test)