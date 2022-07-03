import sys;
from input_module import get_raw_file
import asm as asmData
from assembler import Assembler
# print(sys.argv)
input_file = sys.argv[1]
output_file = "a.out" if len(sys.argv) < 3 else sys.argv[2]
inp = get_raw_file(input_file)
# print(inp)
asm = Assembler(asmData.Reg_Adress,asmData.ISA_Dict,asmData.unUsedBitsTable)
asm.setRawInput(inp)
output = asm.compile()
if(asm.errorHandler.errorState != 0):
    print("Compilation not done due to errors")
else:
    print(*asm.output,sep="\n")