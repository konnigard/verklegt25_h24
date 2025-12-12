import csv
from Models.playerModel import Player

class PlayerData:
    def __init__(self):
        pass

    def save_player(self, player: Player):
      with open('DataLayer/repository/PlayersDB.csv', mode='a', newline='') as dataBase:
            csvWriter = csv.writer(dataBase, delimiter=';')
            csvWriter.writerow([player.name, player.dob, player.address, player.phone_number, player.email, player.link, player.username, player.teamName])  

    def load_player(self) -> list[Player]:
        playerList = []
        try:
            with open('DataLayer/repository/PlayersDB.csv', mode='r', encoding='utf-8') as dataBase:
                csvDB = csv.reader(dataBase, delimiter=';')

                for info in csvDB:
                    if len(info) >= 7:  # Ensure we have minimum required fields
                        name = info[0]
                        dob = info[1]
                        address = info[2]
                        phoneNumber = info[3]
                        email = info[4]
                        link = info[5]
                        username = info[6]
                        # Handle team field (backward compatibility)
                        teamName = info[7] if len(info) >= 8 else "Free Agent"
                        readPlayer = Player(name, dob, address, phoneNumber, email, link, username, teamName)
                        playerList.append(readPlayer)
        except FileNotFoundError:
            # If file doesn't exist, return empty list
            pass

        return playerList

    def load_players_by_team(self, teamName: str) -> list[Player]:
        """Returns all players belonging to a specific team"""
        allPlayers = self.load_player()
        return [player for player in allPlayers if player.teamName == teamName]

    def update_player(self, updatedPlayer: Player):
        """Updates an existing player in the CSV database"""
        players = self.load_player()

        with open('DataLayer/repository/PlayersDB.csv', mode='w', newline='') as dataBase:
            csvWriter = csv.writer(dataBase, delimiter=';')

            for player in players:
                if player.username == updatedPlayer.username:
                    # Write updated player
                    csvWriter.writerow([updatedPlayer.name, updatedPlayer.dob,
                                      updatedPlayer.address, updatedPlayer.phone_number,
                                      updatedPlayer.email, updatedPlayer.link,
                                      updatedPlayer.username, updatedPlayer.teamName])
                else:
                    # Write existing player unchanged
                    csvWriter.writerow([player.name, player.dob, player.address,
                                      player.phone_number, player.email, player.link,
                                      player.username, player.teamName])
