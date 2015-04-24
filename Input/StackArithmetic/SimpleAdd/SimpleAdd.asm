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
//      pop temp 0
@SP
M=M-1
@SP
A=M
D=M
@5
M=D
//      pop temp 1
@SP
M=M-1
@SP
A=M
D=M
@6
M=D
//      add
@5
D=M
@6
D=D+M
@5
M=D
//      push temp 0
@5
D=M
@SP
A=M
M=D
@SP
M=M+1
