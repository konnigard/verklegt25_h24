import csv
from Models.clubModel import Club

class ClubData:
    def __init__(self):
        pass

    def write_club(self, club: Club):
        """ Registers a club to the CSV """
        with open('DataLayer/repository/ClubDB.csv', mode='a', newline='') as dataBase:
            csvWriter = csv.writer(dataBase, delimiter=';')
            csvWriter.writerow([club.clubname, club.hometown, club.country])

    def read_clubs(self) -> list[Club]:
        """ Reads the CSV to find all clubs """
        clubList = []
        try:
            with open('DataLayer/repository/ClubDB.csv', mode='r') as dataBase:
                csvDB = csv.reader(dataBase, delimiter=';')

                for info in csvDB:
                    if len(info) >= 4:
                        # Old format: clubname;teamlist;hometown;country (skip teamlist)
                        clubname = info[0]
                        hometown = info[2]
                        country = info[3]
                        read_club = Club(clubname, hometown, country)
                        clubList.append(read_club)
                    elif len(info) >= 3:
                        # New format: clubname;hometown;country
                        clubname = info[0]
                        hometown = info[1]
                        country = info[2]
                        read_club = Club(clubname, hometown, country)
                        clubList.append(read_club)
        except FileNotFoundError:
            # If file doesn't exist, return empty list
            pass

        return clubList
