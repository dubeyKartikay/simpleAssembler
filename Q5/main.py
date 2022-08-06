from math import log2
space_mem = input("input memory space : ")
type_addresable = input("input addressable memory type : ")
if space_mem[-2:] == "mB":
    space_mem = int(space_mem[:-2])*((2**20)*8)
elif space_mem[-2:] == "mb":
    space_mem = int(space_mem[:-2])*((2**20))
elif space_mem[-2:] == "kB":
    space_mem = int(space_mem[:-2])*((2**10)*8)
elif space_mem[-2:] == "kb":
    space_mem = int(space_mem[:-2])*((2**10))
d = {
    "Byte":8,
    "Bit":1,
    "Nibble":4,
    "Word":"LOL"
}
mem_slots = space_mem/d[type_addresable]
bits_required = log2(mem_slots)
query_type = int(input("input the type of question (1/2) : "))
if query_type == 0:
    lenofins = int(input("input length of one instruction :"))
    lenofreg = int(input("input length of registers :"))
    print("bits required to represent an address is : ",bits_required)
    q = lenofins-lenofreg-bits_required
    print("bits needed by opcode : ",q)
    print("filler bits in instruction type 2 : ",lenofins-2*lenofreg-q)
else:
    x=int(input("Enter the Type (1/2) : "))
    if x==1:
        cpu_bit = int(input("how many bits the cpu is : "))
        new_type_addresable = input("input new addressable memory type : ")
        if(new_type_addresable=='Word'):
            d['Word']=cpu_bit
        mem_slots_new=space_mem/d[new_type_addresable]
        bits_reqd_new=log2(mem_slots_new)
        otpt=bits_reqd_new-bits_required
        flag=0
        if(otpt<0):
            flag=1
        print(otpt)
        if flag==1:
            print(abs(otpt)," bits saved")
        elif flag==2:
            print(abs(otpt)," bits required")
    elif x==2:
        cpu_bit = int(input("how many bits the cpu is : "))
        pins= int(input("Enter adress pins : "))
        new_type_addresable = input("input new addressable memory type : ")
        if(new_type_addresable=='Word'):
            d['Word']=cpu_bit
        total=(2**pins)*d[new_type_addresable]/d[type_addresable]
        final=total/(2**30)
        print(final,' GB')