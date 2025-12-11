from UILayer.teamUIClass import TeamUI
class Captain:
    def __init__(self):
        pass

    def whatsYourTeamMenu(self):
        """ Shows a list of teams """
        teamList = self.LogicWrapper.sendTeamInfoToUI()

        # Sort teams by name using Icelandic sorting order
        if teamList:
            teamList = sort_by_name(teamList, 'teamName')

        while True:
            print("\n===== REGISTERED TEAMS =====")
            if not teamList:
                print("No teams registered yet.")
            else:
                for idx, team in enumerate(teamList, start=1):
                    print(f"{idx}. {team.teamName} (Club: {team.teamClub})")

            print()
            print("b) Back")
            print("q) Quit")

            #User input
            choice = input("Choose action: ").strip().upper()

            #Goes back to the previous screen
            if choice == "B":
                break
            #Quits the program
            elif choice == "Q":
                quit()
            else:
                # Try to parse as team selection number
                try:
                    teamIndex = int(choice) - 1
                    if 0 <= teamIndex < len(teamList):
                        self.showTeamDetails(teamList[teamIndex])
                    else:
                        print("Invalid team number, try again.")
                except ValueError:
                    print("Invalid choice, try again.")
