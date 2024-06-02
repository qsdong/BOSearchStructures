# import json
from decimal import Decimal

# This class is used to change the parameters in the json file

class BlockCopolymer:
    def __init__(self):
        self.SpaceGroup = None
        self.Ai = None
        self.level = None

        self.lx = None
        self.ly = None
        self.lz = None

    def changeParaSingle(self,paraName,paraDict,paraInJson):
        if paraName in paraDict:
            paraValue = Decimal(paraDict[paraName])
        else:
            paraValue = Decimal(paraInJson)
        return paraValue

    def changePara(self,paraDict,jsonDict):

        self.lx = self.changeParaSingle("lx",paraDict,jsonDict['Initializer']['UnitCell']["Length"][0])
        self.ly = self.changeParaSingle("ly",paraDict,jsonDict['Initializer']['UnitCell']["Length"][1])
        self.lz = self.changeParaSingle("lz",paraDict,jsonDict['Initializer']['UnitCell']["Length"][2])

        self.SpaceGroup = self.changeParaSingle("SpaceGroup",paraDict,jsonDict['Initializer']["LevelsetInitializer"]["SpaceGroup"])

        jsonDict['Initializer']['UnitCell']["Length"][0] = float(Decimal(self.lx))
        jsonDict['Initializer']['UnitCell']["Length"][1] = float(Decimal(self.ly))
        jsonDict['Initializer']['UnitCell']["Length"][2] = float(Decimal(self.lz))

        jsonDict['Initializer']["LevelsetInitializer"]["SpaceGroup"] = int(self.SpaceGroup)
        jsonDict['Initializer']["LevelsetInitializer"]["Ai"] = paraDict["ai"]
        jsonDict['Initializer']["LevelsetInitializer"]["theta"] = paraDict["theta"]
        jsonDict['Initializer']["LevelsetInitializer"]["Level"] = paraDict["level"] 
        jsonDict['Initializer']["LevelsetInitializer"]["Sequence"] = paraDict["Sequence"]

        jsonDict['Initializer']["LevelsetInitializer"]["iter"] = paraDict["iter"]

        return jsonDict
    

