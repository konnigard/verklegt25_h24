from datetime import date, datetime








class Tournament:
    def __init__(self,name, start_date, end_date, location, contact_name, contact_email, contact_phone, teams=[], games=[]):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.location = location

        self.contact_name = contact_name
        self.contact_email = contact_email
        self.contact_phone = contact_phone

        self.teams = teams 
        self.games = games 
        