from Common import CommandType
'''
Handles the parsing of a single .vm file, and encapsulates access to the input code. It reads VM commands, parses them, and provides convenient access to their components. In addition, it removes all white space and comments.
'''

class Parser:
    def __init__(self, filename):
        self.commands = [self.cleanCommand(line)
                         for line in open(filename).readlines()]
        self.commands = filter(lambda c: c != "", self.commands)

        self.current_index = 0
        self.currentCommand = self.commands[self.current_index]
        self.current_type = self.ParseCommandType(self.currentCommand)

    def hasMoreCommands(self):
        '''
        Are there more commands in the input?
        This method runs to the next meaningful line, and returns true
        if one exists (false otherwise).
        '''
        return self.current_index < len(self.commands)

    def advance(self):
        '''
        Reads the next command from the input and makes it the current
        command. Should be called only if hasMoreCommands is true.
        '''
        self.current_index += 1
        if self.hasMoreCommands():
            self.currentCommand = self.commands[self.current_index]
            self.current_type = self.ParseCommandType(self.currentCommand)

    def commandType(self):
        return self.current_type

    def cleanCommand(self, command):
        '''
        Removes whitespace and comments
        '''
        return command.split('/')[0].strip()

    def ParseCommandType(self, command):
        if command in ArithmeticAndBooleanCommands:
            return CommandType.C_ARITHMETIC
        
        if command.startswith("push "):
            return CommandType.C_PUSH
    
        if command.startswith("pop "):
            return CommandType.C_POP

        return CommandType.C_EMPTY
    
    def arg1(self):
        if(self.current_type == CommandType.C_RETURN or self.current_type == CommandType.C_EMPTY):
            return None

        if (self.current_type == CommandType.C_ARITHMETIC):
            return self.currentCommand
                
        return self.currentCommand.split(' ')[1]

    def arg2(self):
        if not self.current_type in CommandsWithArg2:            
            return None

        return self.currentCommand.split(' ')[2]

ArithmeticAndBooleanCommands = ['add','sub','neg','eq','gt','lt','and','or','not']
CommandsWithArg2 = [CommandType.C_PUSH, CommandType.C_POP, CommandType.C_FUNCTION, CommandType.C_CALL]

def Test():
    p = Parser("/home/ben/CS/Master/Nand2Tetris/projects/07/StackArithmetic/SimpleAdd/SimpleAdd.vm")
    while(p.hasMoreCommands()):        
        print p.commandType()
        
        if(p.commandType() == CommandType.C_ARITHMETIC):
            print "C_ARITHMETIC: " + str(p.currentCommand)
        
        if(p.commandType() == CommandType.C_POP):
            print "C_POP: " + str(p.currentCommand)
        
        if(p.commandType() == CommandType.C_POP):
            print "C_PUSH: " + str(p.currenCommand)
        
        print "ARG1: " + str(p.arg1())
        print "ARG2: " + str(p.arg2())
        p.advance()

Test()
            
