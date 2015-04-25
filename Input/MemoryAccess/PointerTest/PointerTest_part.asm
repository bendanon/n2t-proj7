//      push constant 3030
@3030
D=A
@SP
A=M
M=D
@SP
M=M+1
//      pop pointer 0
@SP
M=M-1
@0
D=A
@3
A=M+D
D=A
@15
M=D
@SP
A=M
D=M
@15
A=M
M=D
