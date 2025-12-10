import csv
from Models.clubModel import Club

class ClubData:
    def __init__(self):
        pass

    def writeClub(self, club: Club):
        """ Registers a club to the CSV """
        with open('datalayer/repository/ClubDB.csv', mode='a', newline='') as dataBase:
            csvWriter = csv.writer(dataBase, delimiter=';')
            # teamlist is now a string, write it directly
            csvWriter.writerow([club.clubname, club.teamlist, club.hometown, club.country])

    def readClubs(self) -> list[Club]:
        """ Reads the CSV to find all clubs """
        clubList = []
        try:
            with open('datalayer/repository/ClubDB.csv', mode='r') as dataBase:
                csvDB = csv.reader(dataBase, delimiter=';')

                for info in csvDB:
                    if len(info) >= 4:  # Ensure we have all required fields
                        clubname = info[0]
                        teamlist = info[1]
                        hometown = info[2]
                        country = info[3]
                        readClub = Club(clubname, hometown, country, teamlist)
                        clubList.append(readClub)
        except FileNotFoundError:
            # If file doesn't exist, return empty list
            pass

        return clubList
