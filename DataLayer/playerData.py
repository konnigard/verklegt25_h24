import csv
from Models.playerModel import Player

class PlayerData:
    def __init__(self):
        pass

    def savePlayer(self, player: Player):
      with open('datalayer/repository/PlayersDB.csv', mode='a', newline='') as dataBase:
            csvWriter = csv.writer(dataBase, delimiter=';')
            # teamlist is now a string, write it directly
            csvWriter.writerow([player.name, player.dob, player.address, player.phone_number, player.email, player.link, player.username])  

    def loadPlayer(self) -> list[Player]:
        playerList = []
        try:
            with open('datalayer/repository/PlayersDB.csv', mode='r') as dataBase:
                csvDB = csv.reader(dataBase, delimiter=';')

                for info in csvDB:
                    if len(info) >= 7:  # Ensure we have all required fields
                        name = info[0]
                        dob = info[1]
                        address = info[2]
                        phoneNumber = info[3]
                        email = info[4]
                        link = info[5]
                        username = info[6]
                        readClub = Player(name, dob, address, phoneNumber, email, link, username)
                        playerList.append(readClub)
        except FileNotFoundError:
            # If file doesn't exist, return empty list
            pass

        return playerList
