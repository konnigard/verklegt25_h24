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

    def sendTeamInfoToUI(self): #Makes the teamData accessable to the UI
        listOfTeam = self.teamLogic.grabTeamData()
        return listOfTeam

    def sendFromUItoLogic(self):
        from UILayer.teamUIClass import TeamUI
        newTeam = TeamUI.createTeam()
        return newTeam

    def sendClubInfoToUI(self): #Makes the clubData accessible to the UI
        listOfClubs = self.clubLogic.grabClubData()
        return listOfClubs

    def saveClubFromUI(self, club):
        self.clubLogic.saveNewClub(club)

    def create_player(self, player):
        """Creates a new player by saving it through the logic layer"""
        self.playerLogic.saveNewPlayer(player)

    def addNewTeam(self, team):
        """Creates a new team by saving it through the logic layer"""
        self.teamLogic.saveNewTeam(team)

    def updateTeam(self, team):
        """Updates an existing team through the logic layer"""
        self.teamLogic.updateTeam(team)

    def sendPlayerInfoToUI(self):
        """Makes the player data accessible to the UI"""
        listOfPlayers = self.playerLogic.grabPlayerData()
        return listOfPlayers

    def create_tournament(self, name, game, location, start_date, end_date, contact_name, contact_phone, contact_email):
        """Creates a new tournament by saving it through the logic layer"""
        tournament = self.tournamentLogic.createTournamentFromData(name, game, location, start_date, end_date, contact_name, contact_phone, contact_email)
        self.tournamentLogic.saveNewTournament(tournament)

    def get_all_tournaments(self):
        """Makes the tournament data accessible to the UI"""
        listOfTournaments = self.tournamentLogic.grabTournamentData()
        return listOfTournaments

    def get_open_matches_for_tournament(self, tournament_id):
        """Placeholder for getting open matches - not yet implemented"""
        return []

    def record_match_result(self, match_id, tournament_id, home_score, away_score):
        """Placeholder for recording match results - not yet implemented"""
        print("Match result recording not yet implemented")

    def create_event(self, eventID, tournamentName, teamHome, teamAway, eventDate, eventTime, location, status="scheduled"):
        """Creates a new event by saving it through the logic layer"""
        event = self.eventLogic.createEventFromData(eventID, tournamentName, teamHome, teamAway, eventDate, eventTime, location, status)
        self.eventLogic.saveNewEvent(event)

    def get_all_events(self):
        """Makes the event data accessible to the UI"""
        listOfEvents = self.eventLogic.grabEventData()
        return listOfEvents

    def get_events_by_tournament(self, tournamentName: str):
        """Gets events for a specific tournament"""
        events = self.eventLogic.grabEventsByTournament(tournamentName)
        return events

    def record_event_score(self, eventID: str, homeScore: int, awayScore: int):
        """Records the score for an event"""
        self.eventLogic.recordEventScore(eventID, homeScore, awayScore)

    def check_team_availability(self, teamName: str, eventDate: str, eventTime: str) -> tuple[bool, str]:
        """Checks if a team is available at the given date and time"""
        return self.eventLogic.checkTeamAvailability(teamName, eventDate, eventTime)

    def check_team_eliminated(self, teamName: str, tournamentName: str) -> tuple[bool, str]:
        """Checks if a team has been eliminated from a tournament (knockout format)"""
        return self.eventLogic.checkTeamElimination(teamName, tournamentName)

    def get_players_by_team(self, teamName: str):
        """Gets all players for a specific team"""
        return self.playerLogic.grabPlayersByTeam(teamName)

    def register_team_for_tournament(self, tournamentName: str, teamName: str):
        """Registers a team for a tournament"""
        self.tournamentTeamLogic.registerTeam(tournamentName, teamName)

    def get_teams_for_tournament(self, tournamentName: str):
        """Gets all teams registered for a tournament"""
        return self.tournamentTeamLogic.getTeamsForTournament(tournamentName)

    def get_tournaments_for_team(self, teamName: str):
        """Gets all tournaments a team is registered for"""
        return self.tournamentTeamLogic.getTournamentsForTeam(teamName)

    def is_team_registered_for_tournament(self, tournamentName: str, teamName: str) -> bool:
        """Checks if a team is registered for a tournament"""
        return self.tournamentTeamLogic.isTeamRegistered(tournamentName, teamName)

    def unregister_team_from_tournament(self, tournamentName: str, teamName: str):
        """Removes a team's registration from a tournament"""
        self.tournamentTeamLogic.unregisterTeam(tournamentName, teamName)
