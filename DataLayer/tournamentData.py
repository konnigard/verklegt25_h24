import csv
from Models.tournamentModel import Tournament

class TournamentData:
    def __init__(self):
        pass

    def save_tournament(self, tournament: Tournament):
        """Saves new tournament detail to the Database"""
        with open('DataLayer/repository/TournamentDB.csv', mode='a', newline='') as dataBase:
            csvWriter = csv.writer(dataBase, delimiter=';')
            # teamlist is now a string, write it directly
            csvWriter.writerow([tournament.name, tournament.game, tournament.location, tournament.startDate, tournament.endDate, tournament.contact, tournament.contactPhone, tournament.contactEmail])

    def load_tournament(self) -> list[Tournament]:
        """Reads the CSV to find all tournaments"""
        #Creates Emptylist that gets added to in the for loop
        tourList = []

        try:
            #Opens the file
            with open('DataLayer/repository/TournamentDB.csv', mode='r') as dataBase:
                cvsDB = csv.reader(dataBase, delimiter=';')

                #Returns line per line in csv
                for info in cvsDB:
                    if len(info) >= 8:  # Ensure we have all required fields
                        tournamentName = info[0]
                        tournamentGame = info[1]
                        tournamentLocation = info[2]
                        tournamentStartDate = info[3]
                        tournamentEndDate = info[4]
                        tournamentContact = info[5]
                        tournamentContactPhone = info[6]
                        tournamentContactEmail = info[7]
                        readTournament = Tournament(tournamentName, tournamentGame, tournamentLocation, tournamentStartDate, tournamentEndDate, tournamentContact, tournamentContactPhone, tournamentContactEmail)
                        tourList.append(readTournament)
        except FileNotFoundError:
            # If file doesn't exist, return empty list
            pass

        return tourList