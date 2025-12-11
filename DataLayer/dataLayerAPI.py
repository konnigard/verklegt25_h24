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
    def loadAllTeams(self) -> list[Team]:
        '''Returns all teams or empty list if no teams exist'''
        teamList = self.TeamData.readAllTeams()
        return teamList 

    def sendToLogic(self): #Takes what readAllTeams returns and sends it to logic layer
        teamList = self.TeamData.readAllTeams()
        return teamList
    
    def LoadTeamByID(self, teamID ) -> Team:
        t : Team = Team(teamID=teamID, teamName="smuu", teamClub="Plee")
        return t
    
    def writeNewTeam(self, team: Team):
        """Saves a new team to the CSV database"""
        self.TeamData.saveNewTeam(team)

    def updateTeam(self, team: Team) -> bool:
        """Updates an existing team in the CSV database"""
        self.TeamData.updateTeam(team)
        return True
##############################################################

####  Functions for Players  ##################################
    def writePlayer(self, player: Player):
        return self.PlayerData.savePlayer(player)

    def readPlayers(self) -> list:
        return self.PlayerData.loadPlayer()

    def readPlayersByTeam(self, teamName: str) -> list:
        return self.PlayerData.loadPlayersByTeam(teamName)

##############################################################

####  Functions for Clubs  ##################################
    def getClubsForLogic(self): #Takes what readClubs returns and sends it to logic layer
        clubList = self.ClubData.readClubs()
        return clubList

    def saveClubToData(self, club):
        self.ClubData.writeClub(club)
    
##############################################################    

####  Functions for Tournaments  #############################
    def readTournaments(self):
        return self.TournamentData.loadTournament()

    def writeTournaments(self, tournament: Tournament):
        return self.TournamentData.saveTournament(tournament)
##############################################################

####  Functions for Events  ##################################
    def writeEvent(self, event: Event):
        """Saves an event to the CSV database"""
        return self.EventData.saveEvent(event)

    def readEvents(self) -> list[Event]:
        """Returns all events"""
        return self.EventData.loadEvents()

    def readEventsByTournament(self, tournamentName: str) -> list[Event]:
        """Returns events for a specific tournament"""
        return self.EventData.loadEventsByTournament(tournamentName)

    def updateEventScore(self, eventID: str, homeScore: int, awayScore: int):
        """Updates the score for an event"""
        return self.EventData.updateEventScore(eventID, homeScore, awayScore)

    def checkTeamConflict(self, teamName: str, eventDate: str, eventTime: str) -> tuple[bool, str]:
        """Checks if a team has a scheduling conflict"""
        return self.EventData.checkTeamConflict(teamName, eventDate, eventTime)

    def checkTeamEliminated(self, teamName: str, tournamentName: str) -> tuple[bool, str]:
        """Checks if a team has been eliminated from a tournament"""
        return self.EventData.checkTeamEliminated(teamName, tournamentName)
##############################################################

####  Functions for Tournament Team Registrations  ##########
    def registerTeamForTournament(self, tournamentTeam: TournamentTeam) -> None:
        """Registers a team for a tournament"""
        self.TournamentTeamData.registerTeam(tournamentTeam)

    def getTeamsForTournament(self, tournamentName: str) -> list[str]:
        """Returns list of team names registered for a tournament"""
        return self.TournamentTeamData.getTeamsForTournament(tournamentName)

    def getTournamentsForTeam(self, teamName: str) -> list[str]:
        """Returns list of tournaments a team is registered for"""
        return self.TournamentTeamData.getTournamentsForTeam(teamName)

    def isTeamRegisteredForTournament(self, tournamentName: str, teamName: str) -> bool:
        """Checks if a team is registered for a tournament"""
        return self.TournamentTeamData.isTeamRegistered(tournamentName, teamName)

    def unregisterTeamFromTournament(self, tournamentName: str, teamName: str) -> None:
        """Removes a team's registration from a tournament"""
        self.TournamentTeamData.unregisterTeam(tournamentName, teamName)
##############################################################