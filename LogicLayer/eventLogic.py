#from file import class
from DataLayer.dataLayerAPI import DataWrapper
from Models.eventModel import Event

class EventLogicClass:
    def __init__(self):
        self.DataWrapper = DataWrapper()

    def grab_event_data(self):
        """Takes the info from the Data layer and makes it available for UI"""
        readEvents = self.DataWrapper.read_events()
        return readEvents

    def grab_events_by_tournament(self, tournamentName: str):
        """Gets events for a specific tournament"""
        events = self.DataWrapper.read_events_by_tournament(tournamentName)
        return events

    def save_new_event(self, event):
        """Saves a new event to the data layer"""
        self.DataWrapper.write_event(event)

    def create_event_from_data(self, tournamentName, teamHome, teamAway,
                           eventDate, eventTime, location, status="scheduled"):
        """Creates an event object from raw data (EventID will be auto-generated)"""
        event = Event(eventID="", tournamentName=tournamentName, teamHome=teamHome, teamAway=teamAway,
                     eventDate=eventDate, eventTime=eventTime, location=location, status=status)
        return event

    def record_event_score(self, eventID: str, homeScore: int, awayScore: int):
        """Records the score for an event"""
        self.DataWrapper.update_event_score(eventID, homeScore, awayScore)

    def check_team_availability(self, teamName: str, eventDate: str, eventTime: str) -> tuple[bool, str]:
        """Checks if a team is available at the given date and time"""
        return self.DataWrapper.check_team_conflict(teamName, eventDate, eventTime)

    def check_team_elimination(self, teamName: str, tournamentName: str) -> tuple[bool, str]:
        """Checks if a team has been eliminated from a tournament (knockout format)"""
        return self.DataWrapper.check_team_eliminated(teamName, tournamentName)
