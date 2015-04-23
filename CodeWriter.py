from Common import CommandType

'''
Translates VM commands into Hack assembly code.
'''
class CodeWriter:
    
    '''
    Opens the output file/stream and gets ready to
    write into it.
    '''
    def __init__(self, outfile):
        self.outfile = open(outfile, 'w')
        self.infile = None        
    
    '''
    Informs the code writer that the translation of a
    new VM file is started.
    '''    
    def setFileName(self, filename):
        self.infile = open(filename, 'r')

    
    def writeAdd(self):
        self.writeComment("add")
        self.point(str(int(segmentBases["temp"]) + 1))
        self.writeline("D=M")
        self.point(str(int(segmentBases["temp"]) + 2))
        self.writeline("D=D+M")
        self.point(str(int(segmentBases["temp"]) + 1))
        self.writeline("M=D")
        self.writePushPop(CommandType.C_PUSH, "temp", 1)

    '''
    Writes the assembly code that is the translation
    of the given arithmetic command.
    '''
    def writeArithmetic(self,command):
        if command in unaryOperators:
            self.writePushPop(CommandType.C_POP, "temp","1")
        elif command in binaryOperators:
            self.writePushPop(CommandType.C_POP, "temp","1")
            self.writePushPop(CommandType.C_POP, "temp","2")

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

    def writeline(self, line):
        self.outfile.write(str(line) + "\n")

    def point(self, base):
        self.writeline("@{0}".format(base))          #Set A to base
        if not base.isdigit():              #For numerical bases, we just want the number
            self.writeline("A=M")           #Set A to the value pointed by base
    
    def pointOffset(self, base, offset):
        self.writeline("@{0}".format(offset))    #Put the offset value in A
        self.writeline("D=A")                    #Save that offset 
        self.writeline("@{0}".format(base))      #Set A to base
        self.writeline("A=A+D")                  #Set A to the value pointed by base

    def incrementSP(self):
        self.writeline("@SP")
        self.writeline("M=M+1")

    def decrementSP(self):
        self.writeline("@SP")
        self.writeline("M=M-1")


    def writePush(self, segment, index):
        self.writeComment('push {0} {1}'.format(segment, index))

        if segment == "constant" and index.isdigit():
            self.writeline("@" + index)                           #Put the constant in A
            self.writeline("D=A")                                 #Save A in D
        elif segment in segmentBases:
            self.pointOffset(segmentBases[segment], index)        #Point to the segement offset
            self.writeline("D=M")                                 #Save the value in that position
        else:
            return

        #At this stae the value to be pushed is in D

        self.point("SP")                                          #Point to the stack top
        self.writeline("M=D")                                     #Set top value to D
        self.incrementSP()                                        #Point to the next open posisiton

    def writePop(self, segment, index):
        self.writeComment('pop {0} {1}'.format(segment, index))
        if segment in segmentBases.keys():
            self.decrementSP()                                    #Make the top the last value inserted
            self.pointOffset(segmentBases[segment], index)        #Point to the target                
            self.writeline("D=A")                                 #Store the target address
            self.point(str(int(segmentBases["general"])))         #Point to the first GP reg
            self.writeline("M=D")                                 #Assign it with the address

            self.point("SP")                                      #Point to the stack top
            self.writeline("D=M")                                 #Store its value

            self.point(str(int(segmentBases["general"])))         #Point to the reg with the address
            self.writeline("A=M")                                 #Point to the address
            self.writeline("M=D")                                 #Set the value of the stack top
        
    '''
    Writes the assembly code that is the translation
    of the given command , where command is either
    C_PUSH or C_POP .
    '''
    def writePushPop(self, commandType, segment, index):

        if commandType == CommandType.C_PUSH:
            self.writePush(segment, index)

        elif commandType == CommandType.C_POP:
            self.writePop(segment, index)
    '''
    Closes the output file.
    '''
    def Close(self):
        self.outfile.close()

segmentBases = {"local":"LCL","argument":"ARG","this":"THIS","that":"THAT","static":"16", "temp":"5", "general":"13"}
binaryOperators = {"add", "sub", "eq", "gt", "lt", "and", "or"}
unaryOperators = {"not", "neg"}
    
def Test():
    cw = CodeWriter("/home/ben/CS/Master/Nand2Tetris/projects/07/StackArithmetic/SimpleAdd/SimpleAdd.asm")
    cw.writePushPop(CommandType.C_PUSH, "constant", "8")
    cw.writePushPop(CommandType.C_PUSH, "constant", "7")
    cw.writeArithmetic("add")
    cw.Close()

Test()






