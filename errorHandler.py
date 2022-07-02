import asm as asm
class ErrorHandler:
    def __init__(self,varlist,label_list):
        self.varlist=varlist
        self.label_list=label_list
    
    def handle(self,errorCode,lineNumber):
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
            print("Variables not declared at the beginning at line number",lineNumber)
        if(errorCode==8):
            print("Missing hlt instruction at line number",lineNumber)
        if(errorCode==9):
            print("halt not being used as the last instruction at line number",lineNumber)
        if(errorCode==10):
            print("multiple halts used at line number",lineNumber)
        if(errorCode==11):
            print("General Syntax Error at line number",lineNumber)

    def check(self,line):
        a=line[0]
        if(a not in asm.ISA_Dict ):
            errorcode=1
            line_Number=line[-1]
            self.handle(errorcode,line_Number)
        else:
            b=line[1]
            if(b not in asm.Reg_Adress and b!='FLAGS'):
                errorcode=1
                line_number=line[-1]
                self.handle(errorcode,line_number)
            elif(b in asm.Reg_Adress and b!="FLAGS"):
                if(a=='add' or a=='sub' or a=='mul' or a=='xor' or a=='or' or a=='and'):
                    c=line[2]
                    d=line[3]
                    if((c not in asm.Reg_Adress and c!='FLAGS') or (d not in asm.Reg_Adress and d!='FLAGS')):
                        errorcode=1
                        line_number=line[-1]
                        self.handle(errorcode,line_number)
                elif(a=='mov' or a=='div' or a=='not' or a=='cmp'):
                    c=line[2]
                    if(c not in asm.Reg_Adress and c!='FLAGS'):
                        errorcode=1
                        line_number=line[-1]
                        self.handle(errorcode,line_number)  
            elif(a=='ld' or a=='st' or a=='jmp' or a=='jlt' or a=='jgt' or a=='je'): 







