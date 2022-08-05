from sys import stdin
from Decode import Decoder
from execute import SIM
import simDicts
from utils import getBin8Bits
Mem= [None]*256
i = 0 
for line in stdin:
    if i > 255:
        continue
    Mem[i] = line.strip()
    i+=1

def dumpreg(i):
    # with open(f"regdump{i}","w") as file:
    #     for m,v in simDicts.reg_in.items():
    #         if m == None:
    #             continue
    #         file.write(f"{m} : {v}\n")
    for m,v in simDicts.reg_in.items():
            if m == None:
                continue
            print(v,end=" ")
def dumpMem(i):
    # with open(f"memdump{i}","w") as file:
    for m in Mem:
        if m == None:
            print("0"*16)
            continue
        print(m)
dec = Decoder(simDicts.isa_dict,simDicts.unUsedBitsTable,simDicts.isa_names,simDicts.reg_in)
ex =SIM(simDicts.reg_in,Mem)
pc = 0
i=0
while (ex.halted == 0):
    print(getBin8Bits(pc,1),end= " ")
    ex.arr = dec.decode(Mem[pc])
    # print(dec.decode(Mem[pc]))
    pc = ex.execute(pc)
    simDicts.reg_in = ex.reg_in
    dumpreg(i)
    print()
    i+=1
     
dumpMem(i)
    
