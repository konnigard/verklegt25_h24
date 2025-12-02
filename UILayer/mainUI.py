from LogicLayer.logicLayerAPI import logicWrapper
from UILayer.teamUIClass import teamUI


class MainUI:
    def __init__(self):
        self.logicWrapper = logicWrapper()

        self.teamUI = teamUI(self.logicWrapper)

