def get_raw_file (filename):
    lines =[]
    with open(filename,"r") as file:
        for line in file.readlines():
           line = line.strip()
           line = line.split(";")[0]
           line = line.replace(","," ")
           line = line.split()
           if 'hlt' in line:
               lines.append(line)
               break
          # line = line.split()
           if line != ['']:
            lines.append(line)
            
    return lines
    
    
            