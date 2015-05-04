from Common import CommandType

# Constant definitions for bootstrap
SP_INITIAL_VALUE = 256
SP_POSITION = 0

runtimeProvidedBases = {"SP": "SP", "local": "LCL", "argument": "ARG",
                        "this": "THIS", "that": "THAT"}
staticProvidedBases = {"static": 16, "temp": 5, "general": 13, "pointer": 3}

binaryOperators = {"add", "sub", "eq", "gt", "lt", "and", "or"}
unaryOperators = {"not", "neg"}


class CodeWriter:
    '''
    Translates VM commands into Hack assembly code.
    '''
    def __init__(self, outfile):
        '''
        Opens the output file/stream and gets ready to write into it.
        '''
        self.outfile = open(outfile, 'w')
        self.infile = None

        self.currentFunction = None
        self.retLabelIndex = 0
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
        Writes the assembly code that effects the VM initialization,
        also called bootstrap code. This code must be placed at the
        beginning of the output file
        '''
        self.writeline("@{0}".format(SP_INITIAL_VALUE))  # The stack base in the memory
        self.writeline("D=A")                            # Save the stack base memory address
        self.writeline("@{0}".format(SP_POSITION))       # The position of the uninitialized SP
        self.writeline("M=D")                            # SP = SP_INITIAL_VALUE
        self.writeCall("Sys.init", 0)                    # Call the sys function that calls Main.main 

    def writeLabel(self, label):
        '''
        Writes the assembly code that is the translation of the label command.
        '''
        self.writeComment("Label " + label)
        if self.currentFunction is None:
            self.writeline("({0})".format(label))
        else:
            self.writeline("({0}${1})".format(self.currentFunction, label))

    def writeGoto(self, label):
        '''
        Writes the assembly code that is the translation of the goto command.
        '''
        self.writeComment("Goto " + label)

        if self.currentFunction is None:
            self.writeline("@{0}".format(label))
        else:
            self.writeline("@{0}${1}".format(self.currentFunction, label))
        self.writeline("0;JMP")

    def writeIf(self, label):
        '''
        Writes the assembly code that is the translation of
        the if-goto command.
        '''
        self.writeComment("If " + label)

        self.decrementSP()              # Remove the empty spot at the top
        self.point("SP", 0)             # Point to the top value
        self.writeline("D=M")           # Save the value on the top
        self.writeline("@" + label)     # Point at the label
        self.writeline("D;JNE")         # Jump if the stack top value is not zero

    def generateUniqueRetLabel(self):
        self.retLabelIndex += 1
        return "ret{0}".format(self.retLabelIndex)

    def writeCall(self, functionName, numArgs):
        '''
        Writes the assembly code that is the translation of the call command.
        '''
        self.writeComment("call {0} {1}".format(functionName, numArgs))

        retLabel = self.generateUniqueRetLabel()

        self.writeline("@{0}".format(retLabel))
        self.writeline("D=A")
        self.point("general", 0)
        self.writeline("M=D")

        # Save the return address, one command after call
        self.writePush("general", 0)

        for segmentPointer in ["LCL", "ARG", "THIS", "THAT"]:
            self.writeline("@{0}".format(segmentPointer))
            self.writeline("D=M")
            self.point("general", 0)
            self.writeline("M=D")
            self.writePush("general", 0)

        # Set argument for callee
        self.writeline("@SP")
        self.writeline("D=M")
        self.writeline("@"+str(int(numArgs)+5))
        self.writeline("D=D-A")
        self.writeline("@ARG")
        self.writeline("M=D")

        # Set local for callee
        self.writeline("@SP")
        self.writeline("D=M")
        self.writeline("@LCL")
        self.writeline("M=D")

        # Jump to the start point of the callee
        self.writeline("@{0}".format(functionName))
        self.writeline("0;JMP")

        self.writeline("({0})".format(retLabel))

    def writeReturn(self):
        '''
        Writes the assembly code that is the translation of the
        return command.
        '''
        self.writeComment("return")

        # frame = LCL
        self.writeline("@LCL")
        self.writeline("D=M")
        self.point("general", 0)  # frame
        self.writeline("M=D")

        # *ARG = pop
        self.writePop("argument", 0)

        #SP=ARG+1
        self.writeline("@ARG")
        self.writeline("D=M")
        self.writeline("@SP")
        self.writeline("M=D+1")
        
        for segmentPointer in ["THAT","THIS","ARG","LCL"]: 
            self.point("general", 0)  # frame
            self.writeline("AM=M-1")  # Decrement and point
            self.writeline("D=M")     # Save the base of current segment
            self.writeline("@{0}".format(segmentPointer))
            self.writeline("M=D")

        self.point("general", 0)  # frame
        self.writeline("A=M-1")
        self.writeline("A=M")
        self.writeline("0;JMP")

        self.currentFunction = None

    def writeFunction(self, functionName, numLocals):
        '''
        Writes the assembly code that is the translation of the
        given function command.
        '''
        self.writeComment("function {0} {1}".format(functionName, numLocals))

        # Set the current function
        self.currentFunction = functionName

        # Create the label which callers will jump to
        self.writeline("({0})".format(functionName))

        # Initialize numLocals local variables
        for _ in range(0, int(numLocals)):
            self.writePush("constant", 0)

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
        offset = int(offset)
        if base in runtimeProvidedBases:
            runtime_base = runtimeProvidedBases[base]
            if offset != 0:
                # Put the offset in D
                self.writeline("@{0}".format(offset))
                self.writeline("D=A")
                # Set A to D plus the segment's base address
                self.writeline("@{0}".format(runtime_base))
                self.writeline("A=M+D")
            else:
                # Set A to the segment's base address
                self.writeline("@{0}".format(runtime_base))
                self.writeline("A=M")
        elif base in staticProvidedBases:
            self.writeline("@{0}".format(staticProvidedBases[base] +
                                         offset))
        else:
            self.writeline("@{0}".format(int(base) + offset))

    def incrementSP(self):
        self.writeline("@SP")
        self.writeline("M=M+1")

    def decrementSP(self):
        self.writeline("@SP")
        self.writeline("M=M-1")

    def writePush(self, segment, index):
        self.writeComment('push {0} {1}'.format(segment, index))

        if segment == "constant":
            # Put the constant in A, Save A in D
            self.writeline("@" + str(index))
            self.writeline("D=A")
        else:
            # Save the value in that position
            self.point(segment, index)
            self.writeline("D=M")

        # At this stage the value to be is in D
        # Point to the stack top, set top value to D,
        # and Point to the next open position
        self.point("SP", 0)
        self.writeline("M=D")
        self.incrementSP()

    def writePop(self, segment, index):
        self.writeComment('pop {0} {1}'.format(segment, index))

        self.decrementSP()  # Make the top the last value inserted

        if segment in runtimeProvidedBases and int(index) != 0:
            self.point(segment, index)      # Point to the target
            self.writeline("D=A")           # Store the target address
            self.point("general", 2)        # Point to the last GP reg
            self.writeline("M=D")           # Assign it with the address

            self.point("SP", 0)             # Point to the stack top
            self.writeline("D=M")           # Store its value

            self.point("general", 2)        # Point to the reg with the address
            self.writeline("A=M")           # Point to the address
            self.writeline("M=D")           # Set the value of the stack top
        else:
            self.point("SP", 0)             # Point to the stack top
            self.writeline("D=M")           # Store its value
            self.point(segment, index)      # This point preserves D
            self.writeline("M=D")           # Set the value of the stack top

    def writePushPop(self, commandType, segment, index):
        '''
        Writes the assembly code that is the translation
        of the given command , where command is either
        C_PUSH or C_POP.
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
        self.infile.close() 

