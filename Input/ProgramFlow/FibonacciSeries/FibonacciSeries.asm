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
//      pop pointer 1
@SP
M=M-1
@SP
A=M
D=M
@4
M=D
//      push constant 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
//      pop that 0
@SP
M=M-1
@THAT
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
//      push constant 1
@1
D=A
@SP
A=M
M=D
@SP
M=M+1
//      pop that 1
@SP
M=M-1
@1
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
//      push argument 0
@ARG
A=M
D=M
@SP
A=M
M=D
@SP
M=M+1
//      push constant 2
@2
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
//      Label MAIN_LOOP_START
(MAIN_LOOP_START)
//      push argument 0
@ARG
A=M
D=M
@SP
A=M
M=D
@SP
M=M+1
//      If COMPUTE_ELEMENT
@SP
M=M-1
@SP
A=M
D=M
@COMPUTE_ELEMENT
D;JNE
//      Goto END_PROGRAM
@END_PROGRAM
0;JMP
//      Label COMPUTE_ELEMENT
(COMPUTE_ELEMENT)
//      push that 0
@THAT
A=M
D=M
@SP
A=M
M=D
@SP
M=M+1
//      push that 1
@1
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
//      push pointer 1
@4
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
//      pop pointer 1
@SP
M=M-1
@SP
A=M
D=M
@4
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
//      Goto MAIN_LOOP_START
@MAIN_LOOP_START
0;JMP
//      Label END_PROGRAM
(END_PROGRAM)
