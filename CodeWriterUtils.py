'''
This file conatains small utility classes for CodeWriter
'''

class Function:
    def __init__(self, functionName, numArgs):
        self.functionName = functionName
        self.numArgs = numArgs

    def getRetSymbol(self):
        return "#{1}".format(self.functionName)

    def getNumArgs(self):
        return self.numArgs

class Label:
    def __init__(self, containingFunction, labelName):
        self.containingFunction = containingFunction
        self.labelName = labelName

    def getUniqueLabelName(self):
        return "{0}${1}".format(self.containingFunction, self.labelName)

class StaticVariable:

    currentOffsetFromStaticBase = 0

    def __init__(self, containingFile, variableName):
        self.containingFile = containingFile
        self.variableName = variableName

        #This is the variable allocation
        self.address = staticProvidedBases["static"] + currentOffsetFromStaticBase

        #Increment the current offset for the next allocation
        currentOffsetFromStaticBase += 1

    def getUniqueSymbolName(self):
        return "{0}.{1}".format(self.containingFile, self.variableName)

    def getMemoryAddress(self):
        return self.address
