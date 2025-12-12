#from file import class
from LogicLayer.TeamLogic import TeamLogicClass
from LogicLayer.clubLogic import ClubLogicClass
from LogicLayer.playerLogic import PlayerLogicClass
from LogicLayer.tournamentLogic import TournamentLogicClass
from LogicLayer.eventLogic import EventLogicClass
from LogicLayer.tournamentTeamLogic import TournamentTeamLogicClass

class LogicWrapper:
    def __init__(self):
        self.teamLogic = TeamLogicClass()
        self.clubLogic = ClubLogicClass()
        self.playerLogic = PlayerLogicClass()
        self.tournamentLogic = TournamentLogicClass()
        self.eventLogic = EventLogicClass()
        self.tournamentTeamLogic = TournamentTeamLogicClass()

    def send_team_info_to_ui(self):
        """Displays the team details through the logic layer"""
        listOfTeam = self.teamLogic.grab_team_data()
        return listOfTeam


    def send_club_info_to_ui(self): 
        """Displayes the club details through the logic layer"""
        listOfClubs = self.clubLogic.grab_club_data()
        return listOfClubs

    def save_club_from_ui(self, club):
        """Creates a new club by saving it through the logic layer"""
        self.clubLogic.save_new_club(club)

    def create_player(self, player):
        """Creates a new player by saving it through the logic layer"""
        self.playerLogic.save_new_player(player)

    def add_new_team(self, team):
        """Creates a new team by saving it through the logic layer"""
        self.teamLogic.save_new_team(team)

    def update_team(self, team):
        """Updates an existing team through the logic layer"""
        self.teamLogic.update_team(team)

    def is_team_name_available(self, teamName: str) -> bool:
        """Checks if a team name is available (not already taken)"""
        return self.teamLogic.is_team_name_available(teamName)

    def send_player_info_to_ui(self):
        """Makes the player data accessible to the UI"""
        listOfPlayers = self.playerLogic.grab_player_data()
        return listOfPlayers

    def create_tournament(self, name, game, location, start_date, end_date, contact_name, contact_phone, contact_email):
        """Creates a new tournament by saving it through the logic layer"""
        tournament = self.tournamentLogic.create_tournament_from_data(name, game, location, start_date, end_date, contact_name, contact_phone, contact_email)
        self.tournamentLogic.save_new_tournament(tournament)

    def get_all_tournaments(self):
        """Makes the tournament data accessible to the UI"""
        listOfTournaments = self.tournamentLogic.grab_tournament_data()
        return listOfTournaments


    def create_event(self, tournamentName, teamHome, teamAway, eventDate, eventTime, location, status="scheduled"):
        """Creates a new event by saving it through the logic layer (EventID will be auto-generated)"""
        event = self.eventLogic.create_event_from_data(tournamentName, teamHome, teamAway, eventDate, eventTime, location, status)
        self.eventLogic.save_new_event(event)

    def get_all_events(self):
        """Makes the event data accessible to the UI"""
        listOfEvents = self.eventLogic.grab_event_data()
        return listOfEvents

    def get_events_by_tournament(self, tournamentName: str):
        """Gets events for a specific tournament"""
        events = self.eventLogic.grab_events_by_tournament(tournamentName)
        return events

    def record_event_score(self, eventID: str, homeScore: int, awayScore: int):
        """Records the score for an event"""
        self.eventLogic.record_event_score(eventID, homeScore, awayScore)

    def check_team_availability(self, teamName: str, eventDate: str, eventTime: str) -> tuple[bool, str]:
        """Checks if a team is available at the given date and time"""
        return self.eventLogic.check_team_availability(teamName, eventDate, eventTime)

    def check_team_eliminated(self, teamName: str, tournamentName: str) -> tuple[bool, str]:
        """Checks if a team has been eliminated from a tournament (knockout format)"""
        return self.eventLogic.check_team_elimination(teamName, tournamentName)

    def get_players_by_team(self, teamName: str):
        """Gets all players for a specific team"""
        return self.playerLogic.grab_players_by_team(teamName)

    def is_username_available(self, username: str) -> bool:
        """Checks if a username is available (not already taken)"""
        return self.playerLogic.is_username_available(username)

    def update_player(self, player):
        """Updates an existing player through the logic layer"""
        self.playerLogic.update_player(player)

    def register_team_for_tournament(self, tournamentName: str, teamName: str):
        """Registers a team for a tournament"""
        self.tournamentTeamLogic.register_team(tournamentName, teamName)

    def get_teams_for_tournament(self, tournamentName: str):
        """Gets all teams registered for a tournament"""
        return self.tournamentTeamLogic.get_teams_for_tournament(tournamentName)

    def get_tournaments_for_team(self, teamName: str):
        """Gets all tournaments a team is registered for"""
        return self.tournamentTeamLogic.get_tournaments_for_team(teamName)

    def is_team_registered_for_tournament(self, tournamentName: str, teamName: str) -> bool:
        """Checks if a team is registered for a tournament"""
        return self.tournamentTeamLogic.is_team_registered(tournamentName, teamName)

    def unregister_team_from_tournament(self, tournamentName: str, teamName: str):
        """Removes a team's registration from a tournament"""
        self.tournamentTeamLogic.unregister_team(tournamentName, teamName)

    def has_team_tournament_date_conflict(self, tournamentName: str, teamName: str) -> bool:
        """Checks if a team has a date conflict with the specified tournament"""
        return self.tournamentTeamLogic.has_date_conflict(tournamentName, teamName)
