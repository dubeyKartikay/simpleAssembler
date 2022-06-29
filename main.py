import sys;
from input_module import get_raw_file
print(sys.argv)
input_file = sys.argv[1]
output_file = "a.out" if len(sys.argv) < 3 else sys.argv[2]

print(get_raw_file(input_file))
    