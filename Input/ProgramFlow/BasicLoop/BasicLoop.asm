//      push constant 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
//      pop local 0
@SP
M=M-1
@LCL
A=M
D=A
@15
M=D
@SP
A=M
D=M
@15
A=M
M=D
//      Label LOOP_START
(LOOP_START)
//      push argument 0
@ARG
A=M
D=M
@SP
A=M
M=D
@SP
M=M+1
//      push local 0
@LCL
A=M
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
//      pop local 0
@SP
M=M-1
@LCL
A=M
D=A
@15
M=D
@SP
A=M
D=M
@15
A=M
M=D
//      push argument 0
@ARG
A=M
D=M
@SP
A=M
M=D
@SP
M=M+1
//      push constant 1
@1
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
//      pop argument 0
@SP
M=M-1
@ARG
A=M
D=A
@15
M=D
@SP
A=M
D=M
@15
A=M
M=D
//      push argument 0
@ARG
A=M
D=M
@SP
A=M
M=D
@SP
M=M+1
//      If LOOP_START
@SP
M=M-1
@SP
A=M
D=M
@LOOP_START
D;JNE
//      push local 0
@LCL
A=M
D=M
@SP
A=M
M=D
@SP
M=M+1
