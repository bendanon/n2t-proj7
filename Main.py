'''
Initializes I/O files and drives the show.
'''
from Parser import Parser
from Common import CommandType
from CodeWriter import CodeWriter
import os
import sys


def main(args):
    '''
    You can set vm_file_path to be either a folder (and then an asm file
    with the folder source_file will be created in the folder) or set it to be
    a vm file (and then an asm file with the file source_file will be created
    in the same location)
    '''
    if len(args) != 1:
        print "Usage: (python) Main.py [<.vm file path>|<source dir path>]"
        return

    vm_file_path = args[0]

    # vm_file_path = "Input/StackArithmetic/SimpleAdd/SimpleAdd.vm"
    # vm_file_path = "Input/StackArithmetic/StackTest/StackTest.vm"
    # vm_file_path = "Input/MemoryAccess/BasicTest/BasicTest.vm"
    # vm_file_path = "Input/MemoryAccess/PointerTest/PointerTest.vm"
    # vm_file_path = "Input/MemoryAccess/StaticTest/StaticTest.vm"
    # vm_file_path = "Input/ProgramFlow/BasicLoop/BasicLoop.vm"
    # vm_file_path = "Input/ProgramFlow/FibonacciSeries/FibonacciSeries.vm"
    # vm_file_path = "Input/FunctionCalls/SimpleFunction/SimpleFunction.vm"

    init_code_required = False
    source_file_paths = []
    sep = '/' if '/' in vm_file_path else os.sep

    if not vm_file_path.endswith(".vm"):
        source_file_names = [file_name for file_name in
                             os.listdir(vm_file_path) if
                             file_name.endswith('.vm')]
        source_file_paths += [os.path.join(vm_file_path, file_name) for
                              file_name in source_file_names]
        init_code_required = 'Sys.vm' in source_file_names
        asm_file_name = "{0}.asm".format(vm_file_path.split(sep)[-2])
        asm_file_path = os.path.join(vm_file_path, asm_file_name)
    else:
        source_file_paths = [vm_file_path]
        asm_file_path = vm_file_path.replace(".vm", ".asm")

    cw = CodeWriter(asm_file_path)
    if init_code_required:
        cw.writeInit()
        cw.writeFinishLoop()

    for source_file in source_file_paths:
        cw.setFileName(source_file)
        p = Parser(source_file)

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

    cw.Close()

if __name__ == '__main__':
    main(sys.argv[1:])
