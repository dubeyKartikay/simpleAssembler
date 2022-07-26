from ast import Return


class Decoder:
    def __init__(self,isa_dict,unUsedBitsTable,isa_names,reg_in):
        self.isa_dict=isa_dict
        self.unUsedBitsTable=unUsedBitsTable
        self.isa_names=isa_names 
        self.reg_in=reg_in
    def bintodec(self,bin):
        n=len(bin)
        sum=0
        bin=bin[::-1]
        for i in range(n):
            bin[i]=int(bin[i])
            sum=sum+(bin[i]*(2^n))
        return sum    
    def decode(self,instruction):
        opcode=instruction[0:5]
        type=self.isa_dict[opcode]
        func=self.isa_names[opcode]
        a=[]
        a.append(func)
        opcode=instruction[:5]
        if(type=="A"):
            r1 = instruction[7:10]
            r2 = instruction[10:13]
            r3 = instruction[13:16]
            v1=self.reg_in[r1]
            v2=self.reg_in[r2]
            a.append(v1)
            a.append(v2)
            a.append(r3)
        elif(type=='B'):
            r1 = instruction[5:8]
            imm = instruction[8:16]
            imm =self.bintodec(imm)
            v1=self.reg_in[imm]
            a.append(r1)
            a.append(v1)
        elif(type =='C'):
            if(func =='div'):
                r1 = instruction[10:13]
                r2 = instruction[13:16]
                v1=self.reg_in[r1]
                v2=self.reg_in[r2]
                a.append(v1)
                a.append(v2)
            else:    
                r1 = instruction[10:13]
                r2 = instruction[13:16]
                v1=self.reg_in[r1]
                a.append(v1)
                a.append(r2)    
        elif(type =='D'):
            r1 = instruction[5:8]
            madd = instruction[8:16]
            madd =self.bintodec(madd)
            v1=self.reg_in[madd]
            a.append(r1)
            a.append(v1)
        elif(type =='E'):
            madd = instruction[8:16]
            madd =self.bintodec(madd)
            v1=self.reg_in[madd]
            a.append(v1)
                      
        return a
    
# #1010100100000111
# a = ["mul",5,"00000111"]