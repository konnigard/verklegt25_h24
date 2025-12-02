import csv

def writeTeams():
    """ Skrifar inn team á CSV skjalið """


def readTeams():
    """ Skoðar CSV til að sjá liðið """

    with open('TeamDB.csv', mode= 'r') as file: 
        cvsFile = csv.reader(file)
        for info in cvsFile:
            return info

    #name, club, players