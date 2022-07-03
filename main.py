import sys;
from input_module import get_raw_file
import asm
from assembler import Assembler
# print(sys.argv)
input_file = sys.argv[1]
output_file = "a.out" if len(sys.argv) < 3 else sys.argv[2]
inp = get_raw_file(input_file)
# print(inp)
asm = Assembler(asm.Reg_Adress,asm.ISA_Dict,asm.unUsedBitsTable)
asm.setRawInput(inp)
asm.pass1()
asm.pass2()
# print(*asm.processedInput,sep='\n')
print(asm.variableTable,sep='\n')
print(asm.labesTable,sep='\n')
print(asm.locationCounter,sep='\n')
print(*asm.output,sep='\n')
