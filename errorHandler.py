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
            if(a=='add' or a=='sub' or a=='mul' or a=='xor' or a=='or' or a=='and'):
                    b=line[1]
                    c=line[2]
                    d=line[3]
                    if((c not in asm.Reg_Adress and c!='FLAGS') or (d not in asm.Reg_Adress and d!='FLAGS') or (b not in asm.Reg_Adress and b!='FLAGS')):
                        errorcode=1
                        line_number=line[-1]
                        self.handle(errorcode,line_number)
            elif((a=='mov' and line[2][0]!="$") or a=='div' or a=='not' or a=='cmp'):
                    b=line[1]
                    c=line[2]
                    if((c not in asm.Reg_Adress and c!='FLAGS') or (d not in asm.Reg_Adress and d!='FLAGS')):
                        errorcode=1
                        line_number=line[-1]
                        self.handle(errorcode,line_number)  
            elif(a=='jlt' or a=='jgt' or a=='je' or (a=='mov' and line[2][0]=='$')): 
                    b=line[1]
                    c=line[2]
                    if((b not in asm.Reg_Adress and d!='FLAGS')):
                        errorcode=1
                        line_number=line[-1]
                        self.handle(errorcode,line_number)
                    elif(c not in self.label_list):
                        errorcode=3
                        line_number=line[-1]
                        self.handle(errorcode,line_number)
            elif(a=='ld' or a=='st'):
                    b=line[1]
                    c=line[2]
                    if((b not in asm.Reg_Adress and d!='FLAGS') and c not in self.varlist):
                        errorcode=2
                        line_number=line[-1]
                        self.handle(errorcode,line_number)
            elif(a=='ls' or a=='ls' or (a=='mov' and line[2][0]=='$')):
                    b=line[1]
                    c=line[2]
                    d=c[1:]
                    d=int(d)
                    if(b not in asm.Reg_Adress and d!='FLAGS'):
                        errorcode=1
                        line_number=line[-1]
                        self.handle(errorcode,line_number)
                    if(d>255):
                        errorcode=5
                        line_number=line[-1]
                        self.handle(errorcode,line_number)
            if(a=='hlt'):
                    if(line[-1]!='hlt'):
                        errorcode=1
                        line_number=line[-1]
                        self.handle(errorcode,line_number)