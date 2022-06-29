from errorHandler import ErrorHandler
def get_raw_file (filename):
    errorHandler = ErrorHandler()
    lines =[]
    lineNumber = 0
    foundHalt =False
    with open(filename,"r") as file:
        for line in file.readlines():
           lineNumber+=1
           line = line.strip()
           line = line.split(";")[0]
           line = line.replace(","," ")
           line = line.split()
           if "hlt" in  line:
               foundHalt = True
          # line = line.split()
           if line != ['']:
            lines.append(line.append(lineNumber))

    if (not(foundHalt)):
        errorHandler.handle(8)
    elif (lines[-1][0] != "hlt"):
        errorHandler.handle(9)
            
    return lines
    
    
            