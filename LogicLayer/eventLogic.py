#from file import class
from DataLayer.dataLayerAPI import DataWrapper
from Models.eventModel import Event

class EventLogicClass:
    def __init__(self):
        self.DataWrapper = DataWrapper()

    def grabEventData(self):
        """Takes the info from the Data layer and makes it available for UI"""
        readEvents = self.DataWrapper.readEvents()
        return readEvents

    def grabEventsByTournament(self, tournamentName: str):
        """Gets events for a specific tournament"""
        events = self.DataWrapper.readEventsByTournament(tournamentName)
        return events

    def saveNewEvent(self, event):
        """Saves a new event to the data layer"""
        self.DataWrapper.writeEvent(event)

    def createEventFromData(self, tournamentName, teamHome, teamAway,
                           eventDate, eventTime, location, status="scheduled"):
        """Creates an event object from raw data (EventID will be auto-generated)"""
        event = Event(eventID="", tournamentName=tournamentName, teamHome=teamHome, teamAway=teamAway,
                     eventDate=eventDate, eventTime=eventTime, location=location, status=status)
        return event

    def recordEventScore(self, eventID: str, homeScore: int, awayScore: int):
        """Records the score for an event"""
        self.DataWrapper.updateEventScore(eventID, homeScore, awayScore)

    def checkTeamAvailability(self, teamName: str, eventDate: str, eventTime: str) -> tuple[bool, str]:
        """Checks if a team is available at the given date and time"""
        return self.DataWrapper.checkTeamConflict(teamName, eventDate, eventTime)

    def checkTeamElimination(self, teamName: str, tournamentName: str) -> tuple[bool, str]:
        """Checks if a team has been eliminated from a tournament (knockout format)"""
        return self.DataWrapper.checkTeamEliminated(teamName, tournamentName)
