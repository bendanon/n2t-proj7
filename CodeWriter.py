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
        self.infile = open(filename, 'r')

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
                self.writeline("@{0}".format(int(offset)))                         # Put the offset value in A
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
            self.writeline("@" + index)                                 # Put the constant in A
            self.writeline("D=A")                                       # Save A in D
        else:
            self.point(segment, index)
            self.writeline("D=M")                                       # Save the value in that position

        # At this stage the value to be pushed is in D

        self.point("SP", 0)                                             # Point to the stack top
        self.writeline("M=D")                                           # Set top value to D
        self.incrementSP()                                              # Point to the next open position

    def writePop(self, segment, index):
        self.writeComment('pop {0} {1}'.format(segment, index))

        self.decrementSP()                                      # Make the top the last value inserted

        if segment in runtimeProvidedBases and index != 0:
            self.point(segment, index)                          # Point to the target
            self.writeline("D=A")                               # Store the target address
            self.point("general", 2)                            # Point to the last GP reg
            self.writeline("M=D")                               # Assign it with the address

            self.point("SP", 0)                                    # Point to the stack top
            self.writeline("D=M")                               # Store its value

            self.point("general", 2)                            # Point to the reg with the address
            self.writeline("A=M")                               # Point to the address
            self.writeline("M=D")                               # Set the value of the stack top
        else:
            self.point("SP", 0)                                    # Point to the stack top
            self.writeline("D=M")                               # Store its value
            self.point(segment, index)                             # This point preserves D
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

runtimeProvidedBases = {"SP": "SP", "local": "LCL", "argument": "ARG", "this": "THIS", "that": "THAT", "pointer": 3}
staticProvidedBases = {"static": 16, "temp": 5, "general": 13}

binaryOperators = {"add", "sub", "eq", "gt", "lt", "and", "or"}
unaryOperators = {"not", "neg"}


def Test():
    cw = CodeWriter("Input/StackArithmetic/SimpleAdd/SimpleAdd.asm")
    cw.writePushPop(CommandType.C_PUSH, "constant", "8")
    cw.writePushPop(CommandType.C_PUSH, "constant", "7")
    cw.writeArithmetic("add")
    cw.Close()
