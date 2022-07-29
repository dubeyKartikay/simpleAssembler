var x
var y
mov R1 $0
mov R2 $1
mov R3 $5
mov R4 $1
loop:
    add R4 R1 R1
    mul R1 R2 R2
    cmp R1 R3 
    jlt loop  
st R2 y 
hlt