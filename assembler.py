from re import X


class Assemnler:
    def __init__(self,opcodeDict,instructionTypeDict):
        self.opcodeDict = opcodeDict
        self.instructionTypeDict = instructionTypeDict
        self.symbolTable = {}
        self.variableTable = {}
        self.labesTable = {}
        self.locationCounter = 0
        self.raw_input = [];
        self.output = []
        
    def pass1 (self):
        pass
    def pass2(self):
        pass
    def compile(self):
        pass
    