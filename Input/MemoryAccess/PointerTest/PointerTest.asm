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
@SP
A=M
D=M
@3
M=D
//      push constant 3040
@3040
D=A
@SP
A=M
M=D
@SP
M=M+1
//      pop pointer 1
@SP
M=M-1
@SP
A=M
D=M
@4
M=D
//      push constant 32
@32
D=A
@SP
A=M
M=D
@SP
M=M+1
//      pop this 2
@SP
M=M-1
@2
D=A
@THIS
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
//      push constant 46
@46
D=A
@SP
A=M
M=D
@SP
M=M+1
//      pop that 6
@SP
M=M-1
@6
D=A
@THAT
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
//      push pointer 0
@3
D=M
@SP
A=M
M=D
@SP
M=M+1
//      push pointer 1
@4
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
//      push this 2
@2
D=A
@THIS
A=M+D
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
//      push that 6
@6
D=A
@THAT
A=M+D
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
