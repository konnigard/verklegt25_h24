#from file imports class
from DataLayer.clubData import ClubData
from DataLayer.teamData import TeamData
from DataLayer.playerData import PlayerData
from DataLayer.tournamentData import TournamentData
from DataLayer.eventData import EventData
from DataLayer.tournamentTeamData import TournamentTeamData
from Models.teamModel import Team
from Models.playerModel import Player
from Models.tournamentModel import Tournament
from Models.eventModel import Event
from Models.tournamentTeamModel import TournamentTeam

class DataWrapper:
    def __init__(self):
        self.TeamData = TeamData()
        self.ClubData = ClubData()
        self.PlayerData = PlayerData()
        self.TournamentData = TournamentData()
        self.EventData = EventData()
        self.TournamentTeamData = TournamentTeamData()
    
####  Functions for Teams  ##################################
    def load_all_teams(self) -> list[Team]:
        '''Returns all teams or empty list if no teams exist'''
        teamList = self.TeamData.read_all_teams()
        return teamList 

    def send_to_logic(self): #Takes what read_all_teams returns and sends it to logic layer
        teamList = self.TeamData.read_all_teams()
        return teamList
    
    def Load_team_by_id(self, teamID ) -> Team:
        t : Team = Team(teamID=teamID, teamName="smuu", teamClub="Plee")
        return t
    
    def write_new_team(self, team: Team):
        """Saves a new team to the CSV database"""
        self.TeamData.save_new_team(team)

    def update_team(self, team: Team) -> bool:
        """Updates an existing team in the CSV database"""
        self.TeamData.update_team(team)
        return True
##############################################################

####  Functions for Players  ##################################
    def write_player(self, player: Player):
        return self.PlayerData.save_player(player)

    def read_players(self) -> list:
        return self.PlayerData.load_player()

    def read_players_by_team(self, teamName: str) -> list:
        return self.PlayerData.load_players_by_team(teamName)

    def update_player(self, player: Player) -> bool:
        """Updates an existing player in the CSV database"""
        self.PlayerData.update_player(player)
        return True

##############################################################

####  Functions for Clubs  ##################################
    def get_clubs_for_logic(self): #Takes what read_clubs returns and sends it to logic layer
        clubList = self.ClubData.read_clubs()
        return clubList

    def save_club_to_data(self, club):
        self.ClubData.write_club(club)
    
##############################################################    

####  Functions for Tournaments  #############################
    def read_tournaments(self):
        return self.TournamentData.load_tournament()

    def write_tournaments(self, tournament: Tournament):
        return self.TournamentData.save_tournament(tournament)
##############################################################

####  Functions for Events  ##################################
    def writeEvent(self, event: Event):
        """Saves an event to the CSV database"""
        return self.EventData.save_event(event)

    def read_events(self) -> list[Event]:
        """Returns all events"""
        return self.EventData.load_events()

    def read_events_by_tournament(self, tournamentName: str) -> list[Event]:
        """Returns events for a specific tournament"""
        return self.EventData.load_events_by_tournament(tournamentName)

    def update_event_score(self, eventID: str, homeScore: int, awayScore: int):
        """Updates the score for an event"""
        return self.EventData.update_event_score(eventID, homeScore, awayScore)

    def check_team_conflict(self, teamName: str, eventDate: str, eventTime: str) -> tuple[bool, str]:
        """Checks if a team has a scheduling conflict"""
        return self.EventData.check_team_conflict(teamName, eventDate, eventTime)

    def check_team_eliminated(self, teamName: str, tournamentName: str) -> tuple[bool, str]:
        """Checks if a team has been eliminated from a tournament"""
        return self.EventData.check_team_eliminated(teamName, tournamentName)
##############################################################

####  Functions for Tournament Team Registrations  ##########
    def register_team_for_tournament(self, tournamentTeam: TournamentTeam) -> None:
        """Registers a team for a tournament"""
        self.TournamentTeamData.register_team(tournamentTeam)

    def get_teams_for_tournament(self, tournamentName: str) -> list[str]:
        """Returns list of team names registered for a tournament"""
        return self.TournamentTeamData.get_teams_for_tournament(tournamentName)

    def get_tournaments_for_team(self, teamName: str) -> list[str]:
        """Returns list of tournaments a team is registered for"""
        return self.TournamentTeamData.get_tournaments_for_team(teamName)

    def is_team_registered_for_tournament(self, tournamentName: str, teamName: str) -> bool:
        """Checks if a team is registered for a tournament"""
        return self.TournamentTeamData.is_team_registered(tournamentName, teamName)

    def unregister_team_from_tournament(self, tournamentName: str, teamName: str) -> None:
        """Removes a team's registration from a tournament"""
        self.TournamentTeamData.unregister_team(tournamentName, teamName)
##############################################################