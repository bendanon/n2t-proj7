//      push constant 7
@7
D=A
@SP
A=M
M=D
@SP
M=M+1
//      push constant 8
@8
D=A
@SP
A=M
M=D
@SP
M=M+1
//      pop general 1
@SP
M=M-1
@SP
A=M
D=M
@14
M=D
//      pop general 0
@SP
M=M-1
@SP
A=M
D=M
@13
M=D
//      add
@13
D=M
@14
D=D+M
@13
M=D
//      push general 0
@13
D=M
@SP
A=M
M=D
@SP
M=M+1
