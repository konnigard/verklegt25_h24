#from file import class
from Models.teamModel import Team
from LogicLayer.logicLayerAPI import LogicWrapper

class TeamUI:
    def __init__(self):
        self.LogicWrapper = LogicWrapper()

    def createTeam(self, teamName: str, club: str, teammembers): #Defines the function
        newTeam = Team(teamName, club) #Fills in the information through the model class
        return newTeam #Returns a correctly formated filled list
    
    def showTeam(self):
        showTeam = self.LogicWrapper.sendTeamInfoToUI()
        while True:
            print(showTeam)
            print()
            print("b) Back")
            print("q) Quit")
            choice = input("Choose action: ").strip().upper()

            if choice == "B":
                break
            elif choice == "Q":
                quit()
            else:
                print("Invalid choice, try again.")
    
    def teamMenu(self):
        while True:
            print("\n===== TEAM MENU =====")
            print("1 Register new team")
            print("2 Show teams")
            print()
            print("b) Back")
            print("q) Quit")
            choice = input("Choose action: ").strip().upper()

            if choice == "1":
                self.createTeam()
            elif choice == "2":
                self.showTeam()
            elif choice == "B":
                break
            elif choice =="Q":
                quit()
            else:
                print("Invalid choice, try again.")