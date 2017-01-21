# Expression index will hold index of matching parenthesis
class ExpressionIndexes:
    def __init__(self, startIdx, endIdx):
        self.start = startIdx
        self.end = endIdx

# Global Variables
originalVarDictionary2 = []
finalVarDictionary = []         
startParenthesisArr = []
endParenthesisArr = []
expressionIndexArr = []
expressionArr = []
parsedExpressionArr = []
variableCounter = 0
variableSequence = []
tseitenDictionary = {}
finalTseiten = {}
cnfRepresentationDict = {}
cnfRepCounter = 1
equationCounter = 0
lastTmp = ""
assignmentDictionary = {}

# Print Original Variable Dictionary
def printOriginalVarDictionary2():
    global originalVarDictionary2
    print "***********************"
    print "Original Var Dictionary\n"
    for val in originalVarDictionary2:
        print val
    print "***********************\n"

# Print formula
def printFormula():
    print "***********************"
    print "Formula is " , formula, "\n"
    print "***********************\n"

# Print Index Array
def printIndexArray():
    print "***********************"
    print "Index Array is "
    for item in expressionIndexArr:
        print item.start, item.end
    print "***********************\n"

# Print Clauses Array
def printExpressionArray():
    global expressionArr
    print "***********************"
    print "Printing Expression Array "
    for i,item in enumerate(expressionArr):
        print i, item
    print "***********************\n"

# Print Raw Expression
def printRawExpression():
    print "***********************"
    print "Raw Expression Arr is (before parsing NOT operators): "
    for i, el in enumerate(expressionArr):
        print i, el
    print "***********************\n"

# Print Parenthesis Index Array
def printIndexParentheses():
    global startParenthesisArr
    global endParenthesisArr
    print "***********************"
    print "Start Parenthesis Array"
    print startParenthesisArr
    print "***********************\n"
    print "***********************"
    print "end Parenthesis Array"
    print endParenthesisArr
    print "***********************\n"

# Print Parsed Expression Array
def printParsedExpressionArray():
    global parsedExpressionArr
    print "***********************"
    print "Printing Clauses with NOT operator Array "
    for item in parsedExpressionArr:
        print item
    print "***********************\n"

# Printing Utility function
def printTseitenDictionary():
    print "***********************"
    print "Tseiten Dictionary is \n" 
    for dic in tseitenDictionary:
        print dic, "<-->" ,tseitenDictionary[dic]
    print "***********************\n"

# FinalVarDictionary holds all the keys of TseitenDictionary
def printFinalVarDictionary():
    global finalVarDictionary
    print "***********************"
    print "Final Var Dictionary is "
    for item in finalVarDictionary:
        print item
    print "***********************\n"


def printCNFRepresentationDic():
    global cnfRepresentationDict
    for key in cnfRepresentationDict:
        print key, cnfRepresentationDict[key]
    return 


