'''
Initializes I/O files and drives the show.
'''
from Parser import Parser
from Common import CommandType
from CodeWriter import CodeWriter
import os

def main():
    #vm_file_path = "Input/StackArithmetic/SimpleAdd/SimpleAdd.vm"
    #vm_file_path = "Input/StackArithmetic/StackTest/StackTest.vm"
    #vm_file_path = "Input/MemoryAccess/BasicTest/BasicTest.vm"
    #vm_file_path = "Input/MemoryAccess/PointerTest/PointerTest.vm"
    #vm_file_path = "Input/MemoryAccess/StaticTest/StaticTest.vm"
    #vm_file_path = "Input/ProgramFlow/BasicLoop/BasicLoop.vm"
    #vm_file_path = "Input/ProgramFlow/FibonacciSeries/FibonacciSeries.vm"
    #vm_file_path = "Input/FunctionCalls/SimpleFunction/SimpleFunction.vm"
    vm_file_path = "StamFolder/"
    
    sources = []

    if not vm_file_path.endswith(".vm"):
        sources += [os.path.join(vm_file_path, name) for name in os.listdir(vm_file_path) if name.endswith('.vm')]
    else:
        sources += vm_file_path

    cw = CodeWriter(name.replace(".vm", ".asm"))
    
    for name in sources:
        cw.setFileName(name)
        p = Parser(name)

        while(p.hasMoreCommands()):
            cmdType = p.commandType()

            if(cmdType == CommandType.C_ARITHMETIC):
                cw.writeArithmetic(p.arg1())

            elif(cmdType == CommandType.C_PUSH or cmdType == CommandType.C_POP):
                cw.writePushPop(cmdType, p.arg1(), p.arg2())
        
            elif(cmdType == CommandType.C_LABEL):
                cw.writeLabel(p.arg1())

            elif(cmdType == CommandType.C_GOTO):
                cw.writeGoto(p.arg1())

            elif(cmdType == CommandType.C_IF):
                cw.writeIf(p.arg1())
        
            elif(cmdType == CommandType.C_CALL):
                cw.writeCall(p.arg1(), p.arg2())

            p.advance()

if __name__ == '__main__':
    main()
