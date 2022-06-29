class ErrorHandler:
    def __init__(self) -> None:
        pass
    
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
            print("hlt not being used as the last instruction at line number",lineNumber)
