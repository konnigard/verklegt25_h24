from Models.teamModel import Team

class Club:
    def __init__(self, clubname: str, hometown: str, country: str):
        self.clubname: str = clubname
        self.hometown: str = hometown
        self.country: str = country

    def __repr__(self):
        return f"Clubname: {self.clubname}\nHometown: {self.hometown}\nCountry: {self.country}"
