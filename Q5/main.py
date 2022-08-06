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
query_type = int(input("input the type of question [0/1]"))
if query_type == 0:
    lenofins = int(input("input length of one instruction :"))
    lenofreg = int(input("input length of registers :"))
    mem_slots = space_mem/d[type_addresable]
    bits_required = int(log2(mem_slots-1)) + 1
    print("bits required to represent an address is",bits_required)
    q = lenofins-lenofreg-bits_required
    print("bits needed by opcode",q)
    print("filler bits in instruction type 2",lenofins-2*lenofreg-q)
else:
    cpu_bit = int(input("how many bits the cpu is :"))
    new_type_addresable = input("input new addressable memory type : ")