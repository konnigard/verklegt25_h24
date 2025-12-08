from LogicLayer.logicLayerAPI import LogicWrapper

class Test:
    def __init__(self):
        self.currentClass = LogicWrapper()

    def printTeam(self):
        paper = self.currentClass.sendFromUItoLogic()
        return paper
    
tester = Test()
paper = tester.printTeam()