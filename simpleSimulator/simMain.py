from sys import stdin
from Decode import Decoder
from execute import SIM
import simDicts
from utils import getBin8Bits,final
Mem= [0]*256
i = 0 
for line in stdin:
    if i > 255:
        continue
    if line.strip() == '':
        i+=1    
        continue
    Mem[i] = line.strip()
    i+=1
    def dectobin(dec):
        j=""
        while dec>0:
            k=dec%2
            dec=dec//2
            k=str(k)
            j=j+k
        j=j[::-1]
        j=str(j)
        result=""
        result+="0"*(16-len(j))
        result+=j
        return result[-16:]
def encodeNum(num):
    if num == int(num):
        return dectobin(num)
    else:
        return final(num)
def dumpreg(i):
    # with open(f"regdump{i}","w") as file:
    #     for m,v in simDicts.reg_in.items():
    #         if m == None:
    #             continue
    #         file.write(f"{m} : {v}\n")
    for m,v in simDicts.reg_in.items():
            if m == None:
                continue
            print(encodeNum(v),end=" ")
def dumpMem(i):
    # with open(f"memdump{i}","w") as file:
    for m in Mem:
        if m == None:
            print("0"*16)
            continue
        if type(m) == str:
            print(m)
            continue
        print(encodeNum(m))
dec = Decoder(simDicts.isa_dict,simDicts.unUsedBitsTable,simDicts.isa_names,simDicts.reg_in)
ex =SIM(simDicts.reg_in,Mem)
pc = 0
i=0
while (ex.halted == 0):
    print(getBin8Bits(pc,1),end= " ")
    ex.arr = dec.decode(Mem[pc])
    # print(dec.decode(Mem[pc]))
    pc = ex.execute(pc)
    dumpreg(i)
    simDicts.reg_in = ex.reg_in
    print()
    i+=1
     
dumpMem(i)
    
