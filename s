var x
var y
var z
add R0 R1 R2
sub R3 R1 R0
mov R5 R4
mov R3 $7
ld R0 x
st R0 y
mul R2 R1 R0
div R3 R0
rs R1 $4
ls R2 $0
xor R4 R2 R6
label1:
add R1 R2 R6
or R0 R6 R5
and R1 R4 R3
not R3 R2
cmp R4 R6
jmp label1
label2:
div R6 R0
not R1 R0
jlt label2
jgt label1
hlt