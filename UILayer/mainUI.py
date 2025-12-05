from LogicLayer.logicLayerAPI import LogicWrapper
from UILayer.readTeamUIClass import TeamUI


class MainUI:
    def __init__(self):
        self.LogicWrapper = LogicWrapper()

        self.TeamUI = TeamUI(self.LogicWrapper)

