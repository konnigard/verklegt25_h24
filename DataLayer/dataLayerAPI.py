#from file imports class
from DataLayer.teamData import Data

class Wrapper:
    def __init__(self, Data):
        self.Data = Data
    
    def readTeams():
        Teams = Data.readTeams()
        return Teams