def get_raw_file (filename):
    lines =[]
    with open(filename,"r") as file:
        for line in file.readlines():
           line = line.strip()
           line = line.split(";")[0]
           line = line.split(",")
           if line != ['']:
            lines.append(line)
            
        print(lines)
            
            
            
get_raw_file("file.asm")
            