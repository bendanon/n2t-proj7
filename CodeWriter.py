from Common import CommandType

'''
Translates VM commands into Hack assembly code.
'''


class CodeWriter:
    def __init__(self, outfile):
        '''
        Opens the output file/stream and gets ready to
        write into it.
        '''
        self.outfile = open(outfile, 'w')
        self.infile = None

        self.line_counter = 0

    def setFileName(self, filename):
        '''
        Informs the code writer that the translation of a
        new VM file is started.
        '''
        if(self.infile is not None):
            self.infile.close()
        self.infile = open(filename, 'r')

    def writeInit(self):
        '''
        Writes the assembley code that effects the VM initialization,
        also called bootstrap code. This code must be placed at the
        beginning of the output file
        '''
        return None

    def writeLabel(self, label):
        '''
        Writes the assembley code that is the translation of the
        label command
        '''
        self.writeComment("Label " + label)
        self.writeline("(" + label + ")")

    def writeGoto(self, label):
        '''
        Writes the assembley code that is the translation of the
        goto command
        '''
        self.writeComment("Goto " + label)
        self.writeline("@" + label)
        self.writeline("0;JMP")

    def writeIf(self, label):
        '''
        Writes the assembley code that is the translation of the
        if command
        '''
        self.writeComment("If " + label)

        self.decrementSP()              #Remove the empty spot at the top
        self.point("SP", 0)             #Point to the top value
        self.writeline("D=M")           #Save the value on the top
        self.writeline("@" + label)     #Point at the label
        self.writeline("D;JNE")         #Jump if the stack top value is not zero

    def writeCall(self, functionName, numArgs):
        '''
        Writes the assembley code that is the translation of the
        call command
        '''
        counter_at_start = self.line_counter
        self.writePush("constant", self.line_counter + 55)  #The asm line count between here and the call end
        self.writePush("local", 0)
        self.writePush("argument", 0)
        self.writePush("this", 0)
        self.writePush("that", 0)

        # repositions ARG for g
        self.point("SP", 0)
        self.writeline("D=M")
        self.writeline("@"+str(int(numArgs)-5))
        self.writeline("D=D+A")
        self.point("argument", 0)
        self.writeline("M=D")

        # repositions LCL for g
        self.point("SP", 0)
        self.writeline("D=M")
        self.point("local", 0)
        self.writeline("M=D")

        # transfers control to g
        self.writeGoto(functionName)

        print "diff is " + str(self.line_counter - counter_at_start)

    def writeReturn(self):
        '''
        Writes the assembley code that is the translation of the
        return command
        '''
        return None

    def writeFunction(self, functionName, numLocals):
        '''
        Writes the assembley code that is the translation of the
        given function command
        '''
        return None

    def writeAdd(self):
        self.writeBinOpOnT0AndT1("+", "add")

    def writeSub(self):
        self.writeBinOpOnT0AndT1("-", "sub")

    def writeNeg(self):
        self.writeUnaryOpOnT0("-", "neg")

    def writeEq(self):
        self.writeConditionalJump("JEQ", "eq")

    def writeGt(self):
        self.writeConditionalJump("JGT", "gt")

    def writeLt(self):
        self.writeConditionalJump("JLT", "lt")

    def writeAnd(self):
        self.writeBinOpOnT0AndT1("&", "and")

    def writeOr(self):
        self.writeBinOpOnT0AndT1("|", "or")

    def writeNot(self):
        self.writeUnaryOpOnT0("!", "not")

    def writeUnaryOpOnT0(self, operator, comment):
        self.writeComment(comment)

        self.point("general", 0)
        self.writeline("M={0}M".format(operator))

        self.writePush("general", 0)

    def writeBinOpOnT0AndT1(self, operator, comment):
        self.writeComment(comment)

        self.point("general", 0)
        self.writeline("D=M")
        self.point("general", 1)
        self.writeline("D=D{0}M".format(operator))
        self.point("general", 0)
        self.writeline("M=D")

        self.writePush("general", 0)

    def writeConditionalJump(self, operator, comment):
        self.writeComment(comment)

        self.point("general", 0)
        self.writeline("D=M")
        self.point("general", 1)
        self.writeline("D=D-M")

        current_line_counter = self.line_counter
        true_case_address = current_line_counter + 5
        finish_address = current_line_counter + 6

        self.point(true_case_address, 0)            # 0
        self.writeline("D;{0}".format(operator))    # 1

        # false case
        self.writeline("D=0")                       # 2

        self.point(finish_address, 0)               # 3
        self.writeline("0;JMP")                     # 4

        # true case
        self.writeline("D=-1")                      # 5

        # finish
        self.point("general", 0)                    # 6
        self.writeline("M=D")
        self.writePush("general", 0)

    def writeArithmetic(self, command):
        '''
        Writes the assembly code that is the translation
        of the given arithmetic command.
        '''
        if command in unaryOperators:
            self.writePop("general", 0)
        elif command in binaryOperators:
            self.writePop("general", 1)
            self.writePop("general", 0)

        if command == "add":
            self.writeAdd()
        elif command == "sub":
            self.writeSub()
        elif command == "neg":
            self.writeNeg()
        elif command == "eq":
            self.writeEq()
        elif command == "gt":
            self.writeGt()
        elif command == "lt":
            self.writeLt()
        elif command == "and":
            self.writeAnd()
        elif command == "or":
            self.writeOr()
        elif command == "not":
            self.writeNot()

    def writeComment(self, comment):
        self.writeline("//      " + comment)
        self.line_counter -= 1

    def writeline(self, line):
        self.outfile.write(str(line) + "\n")
        self.line_counter += 1

    def point(self, base, offset):
        if base in runtimeProvidedBases:
            if int(offset) != 0:
                self.writeline("@{0}".format(int(offset)))                    # Put the offset value in A
                self.writeline("D=A")                                         # Save that offset
                self.writeline("@{0}".format(runtimeProvidedBases[base]))     # Set A to base
                self.writeline("A=M+D")                                       # Set A to the value pointed by base
            else:
                self.writeline("@{0}".format(runtimeProvidedBases[base]))     # Set A to base
                self.writeline("A=M")                                         # Set A to the value pointed by base
        elif base in staticProvidedBases:
            self.writeline("@{0}".format(staticProvidedBases[base] + int(offset)))
        else:
            self.writeline("@{0}".format(int(base) + int(offset)))

    def incrementSP(self):
        self.writeline("@SP")
        self.writeline("M=M+1")

    def decrementSP(self):
        self.writeline("@SP")
        self.writeline("M=M-1")

    def writePush(self, segment, index):
        self.writeComment('push {0} {1}'.format(segment, index))

        if segment == "constant":
            self.writeline("@" + str(index))                    # Put the constant in A
            self.writeline("D=A")                               # Save A in D
        else:
            self.point(segment, index)
            self.writeline("D=M")                               # Save the value in that position

        # At this stage the value to be pushed is in D

        self.point("SP", 0)                                     # Point to the stack top
        self.writeline("M=D")                                   # Set top value to D
        self.incrementSP()                                      # Point to the next open position

    def writePop(self, segment, index):
        self.writeComment('pop {0} {1}'.format(segment, index))

        self.decrementSP()                                      # Make the top the last value inserted

        if segment in runtimeProvidedBases and index != 0:
            self.point(segment, index)                          # Point to the target
            self.writeline("D=A")                               # Store the target address
            self.point("general", 2)                            # Point to the last GP reg
            self.writeline("M=D")                               # Assign it with the address

            self.point("SP", 0)                                 # Point to the stack top
            self.writeline("D=M")                               # Store its value

            self.point("general", 2)                            # Point to the reg with the address
            self.writeline("A=M")                               # Point to the address
            self.writeline("M=D")                               # Set the value of the stack top
        else:
            self.point("SP", 0)                                 # Point to the stack top
            self.writeline("D=M")                               # Store its value
            self.point(segment, index)                          # This point preserves D
            self.writeline("M=D")                               # Set the value of the stack top

    def writePushPop(self, commandType, segment, index):
        '''
        Writes the assembly code that is the translation
        of the given command , where command is either
        C_PUSH or C_POP .
        '''
        if commandType == CommandType.C_PUSH:
            self.writePush(segment, index)

        elif commandType == CommandType.C_POP:
            self.writePop(segment, index)

    def Close(self):
        '''
        Closes the output file.
        '''
        self.outfile.close()

runtimeProvidedBases = {"SP": "SP", "local": "LCL", "argument": "ARG",
                        "this": "THIS", "that": "THAT"}
staticProvidedBases = {"static": 16, "temp": 5, "general": 13, "pointer": 3}

binaryOperators = {"add", "sub", "eq", "gt", "lt", "and", "or"}
unaryOperators = {"not", "neg"}


def Test():
    cw = CodeWriter("Input/StackArithmetic/SimpleAdd/SimpleAdd.asm")
    cw.writePushPop(CommandType.C_PUSH, "constant", "8")
    cw.writePushPop(CommandType.C_PUSH, "constant", "7")
    cw.writeArithmetic("add")
    cw.Close()
