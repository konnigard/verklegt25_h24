class Event:
    def __init__(self, eventID: str = "", tournamentName: str = "", teamHome: str = "", teamAway: str = "",
                 eventDate: str = "", eventTime: str = "", location: str = "", status: str = "scheduled"):
        self.eventID: str = eventID
        self.tournamentName: str = tournamentName
        self.teamHome: str = teamHome
        self.teamAway: str = teamAway
        self.eventDate: str = eventDate
        self.eventTime: str = eventTime
        self.location: str = location
        self.status: str = status  # scheduled, in_progress, completed
        self.homeScore: int = 0
        self.awayScore: int = 0

    def __repr__(self):
        return f"Event: {self.teamHome} vs {self.teamAway} - {self.eventDate} at {self.eventTime}"
