//      push constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
//      push constant 17
@17
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
//      eq
@13
D=M
@14
D=D-M
@37
D;JEQ
D=0
@38
0;JMP
D=-1
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
//      push constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
//      push constant 16
@16
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
//      eq
@13
D=M
@14
D=D-M
@84
D;JEQ
D=0
@85
0;JMP
D=-1
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
//      push constant 16
@16
D=A
@SP
A=M
M=D
@SP
M=M+1
//      push constant 17
@17
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
//      eq
@13
D=M
@14
D=D-M
@131
D;JEQ
D=0
@132
0;JMP
D=-1
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
//      push constant 892
@892
D=A
@SP
A=M
M=D
@SP
M=M+1
//      push constant 891
@891
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
//      lt
@13
D=M
@14
D=D-M
@178
D;JLT
D=0
@179
0;JMP
D=-1
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
//      push constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
//      push constant 892
@892
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
//      lt
@13
D=M
@14
D=D-M
@225
D;JLT
D=0
@226
0;JMP
D=-1
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
//      push constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
//      push constant 891
@891
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
//      lt
@13
D=M
@14
D=D-M
@272
D;JLT
D=0
@273
0;JMP
D=-1
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
//      push constant 32767
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1
//      push constant 32766
@32766
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
//      gt
@13
D=M
@14
D=D-M
@319
D;JGT
D=0
@320
0;JMP
D=-1
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
//      push constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
//      push constant 32767
@32767
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
//      gt
@13
D=M
@14
D=D-M
@366
D;JGT
D=0
@367
0;JMP
D=-1
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
//      push constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
//      push constant 32766
@32766
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
//      gt
@13
D=M
@14
D=D-M
@413
D;JGT
D=0
@414
0;JMP
D=-1
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
//      push constant 57
@57
D=A
@SP
A=M
M=D
@SP
M=M+1
//      push constant 31
@31
D=A
@SP
A=M
M=D
@SP
M=M+1
//      push constant 53
@53
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
//      push constant 112
@112
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
//      pop general 0
@SP
M=M-1
@SP
A=M
D=M
@13
M=D
//      neg
@13
M=-M
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
//      and
@13
D=M
@14
D=D&M
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
//      push constant 82
@82
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
//      or
@13
D=M
@14
D=D|M
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
//      pop general 0
@SP
M=M-1
@SP
A=M
D=M
@13
M=D
//      not
@13
M=!M
//      push general 0
@13
D=M
@SP
A=M
M=D
@SP
M=M+1
