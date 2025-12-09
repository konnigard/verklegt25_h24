from Models.teamModel import Team

class Club:
    def __init__(self, clubname: str, hometown: str, country: str, teamlist: str = ""):
        self.clubname: str = clubname
        self.teamlist: str = teamlist  # Store as comma-separated string
        self.hometown: str = hometown
        self.country: str = country

    def __repr__(self):
        teams_display = self.teamlist if self.teamlist else "No teams"
        return f"Clubname: {self.clubname}\nTeamlist: {teams_display}\nHometown: {self.hometown}\nCountry: {self.country}"
