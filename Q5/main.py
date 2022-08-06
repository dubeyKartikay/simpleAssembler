from math import log2


space_mem = input("input memory space : ")
type_addresable = input("input addressable memory type : ")
if space_mem[-2:] == "mB":
    space_mem = int(space_mem[:-2])*8*1000000
if space_mem[-2:] == "mb":
    space_mem = int(space_mem[:-2])*1000000
if space_mem[-2:] == "kB":
    space_mem = int(space_mem[:-2])*8*1000
if space_mem[-2:] == "kb":
    space_mem = int(space_mem[:-2])*1000
d = {
    "Byte":8,
    "Bit":1,
    "Nibble":4,
    "Word":"LOL"
}
mem_slots = space_mem/d[type_addresable]
bits_required = log2(mem_slots)