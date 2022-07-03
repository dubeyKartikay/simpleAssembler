from errorHandler import ErrorHandler
def get_raw_file (filename):
    errorHandler = ErrorHandler()
    lines =[]
    lineNumber = 0
    foundHalt =0
    with open(filename,"r") as file:
        for line in file.readlines():
           lineNumber+=1
           line = line.strip()
           line = line.split(";")[0]
           line = line.replace(","," ")
           line = line.split()
           if "hlt" in  line:
               foundHalt += 1
          # line = line.split()
           if line != [''] and line != []:
            line.append(lineNumber)
            lines.append(line)

    if (foundHalt==0):
        errorHandler.handle(8,"NA")
    elif (foundHalt >1):
        errorHandler.handle(10,"NA")
    elif (lines[-1][-2] != "hlt"):
        errorHandler.handle(9,"NA")
#    
    return lines
    
    
            