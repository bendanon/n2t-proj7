//      push constant 10
@10
D=A
@SP
A=M
M=D
@SP
M=M+1
//      pop local 0
@SP
M=M-1
@0
D=A
@LCL
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
//      push constant 21
@21
D=A
@SP
A=M
M=D
@SP
M=M+1
//      push constant 22
@22
D=A
@SP
A=M
M=D
@SP
M=M+1
//      pop argument 2
@SP
M=M-1
@2
D=A
@ARG
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
//      pop argument 1
@SP
M=M-1
@1
D=A
@ARG
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
//      push constant 36
@36
D=A
@SP
A=M
M=D
@SP
M=M+1
//      pop this 6
@SP
M=M-1
@6
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
//      push constant 42
@42
D=A
@SP
A=M
M=D
@SP
M=M+1
//      push constant 45
@45
D=A
@SP
A=M
M=D
@SP
M=M+1
//      pop that 5
@SP
M=M-1
@5
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
//      pop that 2
@SP
M=M-1
@2
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
//      push constant 510
@510
D=A
@SP
A=M
M=D
@SP
M=M+1
//      pop temp 6
@SP
M=M-1
@6
D=A
@5
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
//      push local 0
@0
D=A
@LCL
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1
//      push that 5
@5
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
//      push argument 1
@1
D=A
@ARG
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
//      push this 6
@6
D=A
@THIS
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1
//      push this 6
@6
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
//      push temp 6
@6
D=A
@5
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
