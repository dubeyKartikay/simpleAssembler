import asm as asm
class ErrorHandler:
    def __init__(self,varlist = None,label_list= None):
        self.varlist=varlist
        self.label_list=label_list
        self.errorState = 0
    
    def handle(self,errorCode,lineNumber=""):
        self.errorState =1
        if(errorCode==1):
            print("Typos in instruction name or register name at line number",lineNumber)
        if(errorCode==2):
            print("Use of undefined variables at line number",lineNumber)
        if(errorCode==3):
            print("Use of undefined labels at line number",lineNumber)
        if(errorCode==4):
            print("Illegal use of FLAGS register at line number",lineNumber)
        if(errorCode==5):
            print("Illegal Immediate values (more than 8 bits) at line number",lineNumber)
        if(errorCode==6):
            print("Misuse of labels as variables or vice-versa at line number",lineNumber)
        if(errorCode==7):
            print("Variables not declared at the beginning ")
        if(errorCode==8):
            print("Missing hlt instruction")
        if(errorCode==9):
            print("halt not being used as the last instruction ")
        if(errorCode==10):
            print("multiple halts used")
        if(errorCode==11):
            print("General Syntax Error at line number",lineNumber)
        return -1

    def errorCheck(self,line):
        try:
            ans = self.checkLine(line)
        except :
            ans = -1
            self.handle(11,line[-1])
        return ans
    def checkLine(self,line):
        a=line[0]
        if(a not in asm.ISA_Dict ):
            errorcode=1
            line_Number=line[-1]
            return self.handle(errorcode,line_Number)
        else:
            if ("FLAGS" in line):
                if(a!= "mov"):
                    return self.handle(4,line[-1])
            if(a=='add' or a=='sub' or a=='mul' or a=='xor' or a=='or' or a=='and'):
                    b=line[1]
                    c=line[2]
                    d=line[3]
                    if(len(line)!=5):
                        errorcode=11
                        line_number=line[-1]
                        return self.handle(errorcode,line_number)
                    elif((c not in asm.Reg_Adress.keys() and c!='FLAGS') or (d not in asm.Reg_Adress.keys() and d!='FLAGS') or (b not in asm.Reg_Adress.keys() and b!='FLAGS')):
                        errorcode=1
                        line_number=line[-1]
                        return self.handle(errorcode,line_number)

            elif((a=='mov' and line[2][0]!="$") or a=='div' or a=='not' or a=='cmp'):
                    b=line[1]
                    c=line[2]
                    if(len(line)!=4):
                        errorcode=11
                        line_number=line[-1]
                        return self.handle(errorcode,line_number)
                    elif((c not in asm.Reg_Adress.keys() and c!='FLAGS') or (b not in asm.Reg_Adress.keys() and b!='FLAGS')):
                        errorcode=1
                        line_number=line[-1]
                        return self.handle(errorcode,line_number)  
            elif(a=='jlt' or a=='jgt' or a=='je' or a == "jmp"): 
                    b=line[1]
                    if(len(line)!=3):
                        errorcode=11
                        line_number=line[-1]
                        return self.handle(errorcode,line_number)
                    if (b not in self.label_list):
                        if (b in self.varlist):
                            return self.handle(6,line[-1])
                        else:
                            return self.handle(3,line[-1])
            elif(a=='ld' or a=='st'):
                    b=line[1]
                    c=line[2]
                    if(len(line)!=4):
                        errorcode=11
                        line_number=line[-1]
                        return self.handle(errorcode,line_number)
                    if((b not in asm.Reg_Adress.keys() and b!='FLAGS')):
                        errorcode=1
                        line_number=line[-1]
                        return self.handle(errorcode,line_number)
                    if (c not in self.varlist and c!="FLAGS"):
                        if (c in self.label_list):
                            return self.handle(6,line[-1])
                        else:
                            return self.handle(3,line[-1])
            elif(a=='ls' or a=='rs' or (a=='mov' and line[2][0]=='$')):
                    b=line[1]
                    c=line[2]
                    d=c[1:]
                    d=int(d)
                    if(len(line)!=4):
                        errorcode=11
                        line_number=line[-1]
                        return self.handle(errorcode,line_number)
                    if(b not in asm.Reg_Adress.keys() and b!='FLAGS'):
                        errorcode=1
                        line_number=line[-1]
                        return self.handle(errorcode,line_number)
                    if(d>255):
                        errorcode=5
                        line_number=line[-1]
                        return self.handle(errorcode,line_number)
            if(a=='hlt'):
                    if(len(line)!=2):
                        errorcode=11
                        line_number=line[-1]
                        return self.handle(errorcode,line_number)
                    elif(line[-2]!='hlt'):
                        errorcode=1
                        line_number=line[-1]
                        return self.handle(errorcode,line_number)
            return 0
