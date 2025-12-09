#from file import class
from Models.teamModel import Team
from LogicLayer.logicLayerAPI import LogicWrapper

class TeamUI:
    def __init__(self):
        self.LogicWrapper = LogicWrapper()

    def createTeam(self): #Defines the function
        """ Creates new team through input from user """

        #New line beacause the menu should be :sparkels: pretty :sparkels:
        print("\n Regester New Team") 
        
        #Input from user
        teamID = input("Team ID: ")
        teamName = input("Team Name: ")
        club = input("Club: ") 

        #Fills in the information through the model class
        newTeam: Team = Team(teamID, teamName, club) 
        validation = self.LogicWrapper.addNewTeam(newTeam)
        
        #returns the reasult of Validation
        return validation 
    
    def showTeam(self):
        """ Shows a list of teams """

        showTeam = self.LogicWrapper.printTeam()
        while True:
            print(showTeam) #prints the team
            print()
            print("1) Add Player")
            print("b) Back")
            print("q) Quit")

            #User input
            choice = input("Choose action: ").strip().upper() 
            
            if choice == "1":
                self.addPlayerMenu()
            #Goes back to the previous screen
            elif choice == "B": 
                break
            #Quits the program
            elif choice == "Q": 
                quit()
            #Lovely error message
            else:
                print("Invalid choice, try again.") 
    
    def teamMenu(self):
        """ Team Menu """

        while True:
            print("\n===== TEAM MENU =====")
            #Following options the user can make to use the program
            print("1 Register new team")
            print("2 Show teams")
            print()
            print("b) Back")
            print("q) Quit")

            #Input from use
            choice = input("Choose action: ").strip().upper()

            #Goes to Create Team Menu
            if choice == "1": 
                self.createTeam()
            #Goes to See Team menu
            elif choice == "2": 
                self.showTeam()
            #Returns to the preivious screen
            elif choice == "B": 
                break
            #Quits the program
            elif choice =="Q": 
                quit()
            #Lovely error messsage
            else:
                print("Invalid choice, try again.")

    def addPlayerMenu(self):
        print("AddPlayer Menu Ran")