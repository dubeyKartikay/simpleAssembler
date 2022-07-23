from ast import Return


class Decoder:
    def __init__(self,isa_dict,unUsedBitsTable):
        self.isa_dict=isa_dict
        self.unUsedBitsTable=unUsedBitsTable
    def decode(self,instruction):
        a=[]
        opcode=instruction[:5]
        # func=self.isa_dict[opcode]
        type=self.isa_dict[opcode]
        unusedbits=self.unUsedBitsTable[type]        
        return a
    
# #1010100100000111
# a = ["mul",5,"00000111"]