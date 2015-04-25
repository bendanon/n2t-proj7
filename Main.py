'''
Initializes I/O files and drives the show.
'''
from Parser import Parser
from Common import CommandType
from CodeWriter import CodeWriter


def main():
    #vm_file_path = "Input/StackArithmetic/SimpleAdd/SimpleAdd.vm"
    vm_file_path = "Input/StackArithmetic/StackTest/StackTest.vm"
    #vm_file_path = "Input/MemoryAccess/BasicTest/BasicTest.vm"

    p = Parser(vm_file_path)

    cw = CodeWriter(vm_file_path.replace(".vm", ".asm"))

    while(p.hasMoreCommands()):
        cmdType = p.commandType()

        if(cmdType == CommandType.C_ARITHMETIC):
            cw.writeArithmetic(p.arg1())

        elif(cmdType == CommandType.C_PUSH or cmdType == CommandType.C_POP):
            cw.writePushPop(cmdType, p.arg1(), p.arg2())

        p.advance()

if __name__ == '__main__':
    main()
