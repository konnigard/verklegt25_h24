import csv
from Models.eventModel import Event

class EventData:
    def __init__(self):
        pass

    def saveEvent(self, event: Event):
        """Saves an event to the CSV database"""
        with open('DataLayer/repository/EventDB.csv', mode='a', newline='') as dataBase:
            csvWriter = csv.writer(dataBase, delimiter=';')
            csvWriter.writerow([
                event.eventID,
                event.tournamentName,
                event.teamHome,
                event.teamAway,
                event.eventDate,
                event.eventTime,
                event.location,
                event.status,
                event.homeScore,
                event.awayScore
            ])

    def loadEvents(self) -> list[Event]:
        """Reads the CSV to find all events"""
        eventList = []

        try:
            with open('DataLayer/repository/EventDB.csv', mode='r') as dataBase:
                csvDB = csv.reader(dataBase, delimiter=';')

                for info in csvDB:
                    if len(info) >= 10:  # Ensure we have all required fields
                        event = Event(
                            eventID=info[0],
                            tournamentName=info[1],
                            teamHome=info[2],
                            teamAway=info[3],
                            eventDate=info[4],
                            eventTime=info[5],
                            location=info[6],
                            status=info[7]
                        )
                        event.homeScore = int(info[8]) if info[8] else 0
                        event.awayScore = int(info[9]) if info[9] else 0
                        eventList.append(event)
        except FileNotFoundError:
            # If file doesn't exist, return empty list
            pass

        return eventList

    def loadEventsByTournament(self, tournamentName: str) -> list[Event]:
        """Reads the CSV to find events for a specific tournament"""
        allEvents = self.loadEvents()
        return [event for event in allEvents if event.tournamentName == tournamentName]

    def updateEventScore(self, eventID: str, homeScore: int, awayScore: int):
        """Updates the score for a specific event"""
        events = self.loadEvents()

        # Update the event in memory
        for event in events:
            if event.eventID == eventID:
                event.homeScore = homeScore
                event.awayScore = awayScore
                event.status = "completed"
                break

        # Rewrite the entire CSV with updated data
        with open('DataLayer/repository/EventDB.csv', mode='w', newline='') as dataBase:
            csvWriter = csv.writer(dataBase, delimiter=';')
            for event in events:
                csvWriter.writerow([
                    event.eventID,
                    event.tournamentName,
                    event.teamHome,
                    event.teamAway,
                    event.eventDate,
                    event.eventTime,
                    event.location,
                    event.status,
                    event.homeScore,
                    event.awayScore
                ])

    def checkTeamConflict(self, teamName: str, eventDate: str, eventTime: str) -> tuple[bool, str]:
        """
        Checks if a team has a conflict at the given date and time.
        Returns (has_conflict, conflict_message)
        """
        events = self.loadEvents()

        for event in events:
            # Skip completed events
            if event.status == "completed":
                continue

            # Check if team is playing at this date and time
            if event.eventDate == eventDate and event.eventTime == eventTime:
                if event.teamHome == teamName or event.teamAway == teamName:
                    conflict_msg = f"{teamName} is already scheduled at {eventDate} {eventTime} ({event.teamHome} vs {event.teamAway})"
                    return (True, conflict_msg)

        return (False, "")

    def checkTeamEliminated(self, teamName: str, tournamentName: str) -> tuple[bool, str]:
        """
        Checks if a team has lost a match in the tournament (knockout format).
        Returns (is_eliminated, elimination_message)
        """
        events = self.loadEvents()

        for event in events:
            # Only check completed events in this tournament
            if event.status == "completed" and event.tournamentName == tournamentName:
                # Check if this team lost
                if event.teamHome == teamName and event.homeScore < event.awayScore:
                    elim_msg = f"{teamName} has been eliminated from {tournamentName} (lost {event.homeScore}-{event.awayScore} to {event.teamAway})"
                    return (True, elim_msg)
                elif event.teamAway == teamName and event.awayScore < event.homeScore:
                    elim_msg = f"{teamName} has been eliminated from {tournamentName} (lost {event.awayScore}-{event.homeScore} to {event.teamHome})"
                    return (True, elim_msg)

        return (False, "")
