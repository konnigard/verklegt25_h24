import csv
from Models.tournamentModel import Tournament

class TournamentData:
    def __init__(self):
        pass

    def saveTournament(self, tournament: Tournament):
        with open('datalayer/repository/TournamentDB.csv', mode='a', newline='') as dataBase:
            csvWriter = csv.writer(dataBase, delimiter=';')
            # teamlist is now a string, write it directly
            csvWriter.writerow([tournament.name, tournament.game, tournament.location, tournament.startDate, tournament.endDate, tournament.contact, tournament.contactPhone, tournament.conactEmail])

    def loadTournament(self) -> list[Tournament]:
         #Creates Emptylist that gets added to in the for loop
        tourList = []

        #Opens the file 
        with open('datalayer/repository/TeamDB.csv', mode= 'r') as dataBase: 
            cvsDB = csv.reader(dataBase, delimiter= ';')

            #Returns line per line in csv
            for info in cvsDB: 
                tournamentName = info[0]
                tournamentGame = info[1]
                tournamentLocation = info[2]
                tournamentStartDate = info[3]
                tournamentEndDate = info[4]
                tournamentContact = info[5]
                tournamentContactPhone = info[6]
                tournamentContactEmail = info[7]
                readTeam = Tournament(tournamentName, tournamentGame, tournamentLocation, tournamentStartDate, tournamentEndDate, tournamentContact, tournamentContactPhone, tournamentContactEmail)
                tourList.append(readTeam)
            
        return tourList
    
    def loadTournamentByName(self) -> list[Tournament]:
        tourNameList = []
        with open('datalayer/repository/TeamDB.csv', mode= 'r') as dataBase:
            csvDB = csv.reader(dataBase, delimiter= ';')

            for row in csvDB:
                tourNameList.append(row[0])
        return tourNameList