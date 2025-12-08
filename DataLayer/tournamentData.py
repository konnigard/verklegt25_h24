import csv
import os


class Tournament_Data:
    def __init__(self):
        self.file_name = "TournamentsDB.cvs"
    
      
      
      
    def readTournaments(self):
        """ Reads the CSV to find the tournaments """
        filepath = os.path.abspath(__file__)
        print(filepath)
        with open("/Users/thordur/Documents/forritunverklegt/verklegt25_h24/DataLayer/repository/TournamentsDB.csv",mode= 'r') as dataBase: #Opens the file 
            cvsDB = csv.reader(dataBase, delimiter= ';')
            for info in cvsDB: #Returns line per line in csv
                print (info)


if __name__ == "__main__":
    handler = Tournament_Data()
    handler.readTournaments()

    

