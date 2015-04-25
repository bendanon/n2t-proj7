//      push constant 111
@111
D=A
@SP
A=M
M=D
@SP
M=M+1
//      push constant 333
@333
D=A
@SP
A=M
M=D
@SP
M=M+1
//      push constant 888
@888
D=A
@SP
A=M
M=D
@SP
M=M+1
//      pop static 8
@SP
M=M-1
@SP
A=M
D=M
@24
M=D
//      pop static 3
@SP
M=M-1
@SP
A=M
D=M
@19
M=D
//      pop static 1
@SP
M=M-1
@SP
A=M
D=M
@17
M=D
//      push static 3
@19
D=M
@SP
A=M
M=D
@SP
M=M+1
//      push static 1
@17
D=M
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
//      sub
@13
D=M
@14
D=D-M
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
//      push static 8
@24
D=M
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
