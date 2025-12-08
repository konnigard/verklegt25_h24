#from file import class
from Models.teamModel import Team
from LogicLayer.logicLayerAPI import LogicWrapper

class TeamUI:
    def __init__(self):
        self.LogicWrapper = LogicWrapper()

    def createTeam(self): #Defines the function
        """ Creates new team through input from user """
        
        print("\n Regester New Team") #New line beacause the menu should be :sparkels: pretty :sparkels:

        teamName = input("Team Name: ") #Input for the team name
        club = input("Club: ") #Input for club
        newTeam: Team = Team(teamName, club) #Fills in the information through the model class
        validation = self.LogicWrapper.addNewTeam(newTeam)
        
        return validation #returns the reasult of Validation
    
    def showTeam(self):
        """ Shows a list of teams """

        showTeam = self.LogicWrapper.printTeam()
        while True:
            print(showTeam) #prints the team
            print()
            print("b) Back")
            print("q) Quit")
            choice = input("Choose action: ").strip().upper() #User input

            if choice == "B": #Goes back to the previous screen
                break
            elif choice == "Q": #Quits the program
                quit()
            else:
                print("Invalid choice, try again.") #Lovely error message
    
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
            choice = input("Choose action: ").strip().upper() #Input from user

            if choice == "1": #Goes to Create Team Menu
                self.createTeam()
            elif choice == "2": #Goes to See Team menu
                self.showTeam()
            elif choice == "B": #Returns to the preivious screen
                break
            elif choice =="Q": #Quits the program
                quit()
            else:
                print("Invalid choice, try again.") #Lovely error messsage