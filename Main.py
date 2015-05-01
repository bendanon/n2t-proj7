'''
Initializes I/O files and drives the show.
'''
from Parser import Parser
from Common import CommandType
from CodeWriter import CodeWriter
import os
import sys


def main():
    '''
    You can set vm_file_path to be either a folder (and then an asm file
    with the folder name will be created in the folder) or set it to be
    a vm file (and then an asm file with the file name will be created
    in the same location)
    '''
    vm_file_path = sys.argv[1]

    # vm_file_path = "Input/StackArithmetic/SimpleAdd/SimpleAdd.vm"
    # vm_file_path = "Input/StackArithmetic/StackTest/StackTest.vm"
    # vm_file_path = "Input/MemoryAccess/BasicTest/BasicTest.vm"
    # vm_file_path = "Input/MemoryAccess/PointerTest/PointerTest.vm"
    # vm_file_path = "Input/MemoryAccess/StaticTest/StaticTest.vm"
    # vm_file_path = "Input/ProgramFlow/BasicLoop/BasicLoop.vm"
    # vm_file_path = "Input/ProgramFlow/FibonacciSeries/FibonacciSeries.vm"
    # vm_file_path = "Input/FunctionCalls/SimpleFunction/SimpleFunction.vm"

    sources = []
    cw = None

    if not vm_file_path.endswith(".vm"):
        sources += [os.path.join(vm_file_path, name) for name
                    in os.listdir(vm_file_path) if name.endswith('.vm')]
        asm_file_path = "{0}.asm".format(vm_file_path.split(os.sep)[-2])
        cw = CodeWriter(os.path.join(vm_file_path, asm_file_path))
    else:
        cw = CodeWriter(vm_file_path.replace(".vm", ".asm"))
        sources = [vm_file_path]

    for name in sources:
        cw.setFileName(name)
        p = Parser(name)

        while(p.hasMoreCommands()):
            cmdType = p.commandType()

            if(cmdType == CommandType.C_ARITHMETIC):
                cw.writeArithmetic(p.arg1())

            elif(cmdType == CommandType.C_PUSH or
                 cmdType == CommandType.C_POP):
                cw.writePushPop(cmdType, p.arg1(), p.arg2())

            elif(cmdType == CommandType.C_LABEL):
                cw.writeLabel(p.arg1())

            elif(cmdType == CommandType.C_GOTO):
                cw.writeGoto(p.arg1())

            elif(cmdType == CommandType.C_IF):
                cw.writeIf(p.arg1())

            elif(cmdType == CommandType.C_CALL):
                cw.writeCall(p.arg1(), p.arg2())

            elif(cmdType == CommandType.C_FUNCTION):
                cw.writeFunction(p.arg1(), p.arg2())

            elif(cmdType == CommandType.C_RETURN):
                cw.writeReturn()

            p.advance()

if __name__ == '__main__':
    main()
