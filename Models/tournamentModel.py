class Tournament:
    def __init__(self, tourName, tourGame, tourLoc, tourStartDate, tourEndDate, tourContact, tourPhone, tourEmail):
        self.name: str = tourName
        self.game: str = tourGame
        self.location: str = tourLoc
        self.startDate: str = tourStartDate
        self.endDate: str = tourEndDate
        self.contact: str = tourContact
        self.contactPhone: str = tourPhone
        self.contactEmail: str = tourEmail

    def __repr__(self):
        return f"Tournament: {self.name} ({self.game}) - {self.startDate} to {self.endDate}"