from sys import stdin
from Decode import Decoder
from execute import SIM
import simDicts
Mem= [None]*256
i = 0 
for line in stdin:
    Mem[i] = line.strip()
    i+=1

def dumpreg(i):
    with open(f"regdump{i}","w") as file:
        for m,v in simDicts.reg_in.items():
            if m == None:
                continue
            file.write(f"{m} : {v}\n")
def dumpMem(i):
    with open(f"memdump{i}","w") as file:
        for m in Mem:
            if m == None:
                continue
            file.write(m + "\n")
dec = Decoder(simDicts.isa_dict,simDicts.unUsedBitsTable,simDicts.isa_names,simDicts.reg_in)
ex =SIM(simDicts.reg_in,Mem)
pc = 0
i=0
while (ex.halted == 0):
    ex.arr = dec.decode(Mem[pc])
    pc = ex.execute(pc)
    simDicts.reg_in = ex.reg_in
    dumpMem(i)
    dumpreg(i)
    i+=1
     
    
