import sys
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

# Hamiltonian Cycle
formula = "((A^!B)^(!C^D)^(E|F)^(G|H)^(E|G)^(F|H)^(E|G)^(F|H)^(E>!F)^(F>!E)^(G>!H)^(H>!G)^(E>!G)^(G>!E)^(F>!G)^(H>!F)^(D>!K)^(D>!L)^(!O>!G)^(!G|!F))"

# Two Vertexes with one edge
#formula="((E^C)^(!E|!C)^(A^!B))"

#TRUE x11 = A, x22 = E, x33 = H, x14 = D
# x11 is A, x12 is B, x13 is C, x14 is D
#PROBLEM ^(A>!I^!J)
#line1 = "(A^!B^!C^D^(E|F)^(G|H)^(E|G)^(F|H))"
#formula = line1
# x22 is E, x23 is F, x32 is G, x33 is H
#line2 = "(E|F)^(G|H)"
#line3 = "(E|G)^(F|H)"
#line4 = "(E>!F)^(F>!E)^(G>!H)^(H>!G)"
# x21 is I, x31 is J, x24 is K, x34 is L
#line5 = (A>((!I^!J)))^(E>!G)^(G>!E)
#line6 = "(F>!G)^(H>!F)^(D>(!K^!L))"
# y32 is M, x32 is G, x23 is F, y21 is N, x23 is is F, y13 is O
#line7 = "((!M>((!G)|(!F)))^(!N>!F)^(!O>!G))"
# x11 is A, X13 is B, x21 is C, x23 is D, x22 is E, x12 is F





 

def countVariables2(formula):
    global originalVarDictionary2
    for i, item in enumerate(formula):
        if item.isalpha() & item.isupper() & (str(item) not in originalVarDictionary2):
            originalVarDictionary2.append(item)

def printOriginalVarDictionary2():
    global originalVarDictionary2
    print "***********************"
    print "Original Var Dictionary\n"
    for val in originalVarDictionary2:
        print val
    print "***********************\n"

def printFormula():
    print "***********************"
    print "Formula is " , formula, "\n"
    print "***********************\n"

def generateNewParamString():    
    global variableCounter
    temp = "a" + str(variableCounter)
    variableCounter += 1
    return temp

# validity check: make sure parenthesis are balanced
def checkBalancedParen(startParenthesisArr, endParenthesisArr):
    global startArrLen
    startArrLen = len(startParenthesisArr)
    global endArrLen
    endArrLen = len(endParenthesisArr)
    if(startArrLen != endArrLen):
        print("Invalid input!!!!")
        exit()

# Print Index Array
def printIndexArray():
    print "***********************"
    print "Index Array is "
    for item in expressionIndexArr:
        print item.start, item.end
    print "***********************\n"

# create Array holding start index and index for each expression
def createIndexArray(startArrLen):
    del expressionIndexArr[:]
    flagArr = [False for i in range(startArrLen)]
    for idxS, i in enumerate(reversed(startParenthesisArr)):
        for idxE, j in enumerate(endParenthesisArr):
            if j > i and flagArr[idxE] == False:
                x = ExpressionIndexes(startParenthesisArr[startParenthesisArr.index(i)], endParenthesisArr[idxE])
                expressionIndexArr.append(x)
                flagArr[idxE] = True
                break

# Print Clauses Array
def printExpressionArray():
    global expressionArr
    print "***********************"
    print "Printing Expression Array "
    for i,item in enumerate(expressionArr):
        print i, item
    print "***********************\n"

# create expression array 
def createExpressionArray(expressionIndexArr):
    del expressionArr[:] 
    for idx,index in enumerate(expressionIndexArr):
        string = formula[index.start: index.end + 1]
        expressionArr.append(string)

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

   
# Indexing all parenthesis
def indexParenthesis(formula):
    del startParenthesisArr[:]
    del endParenthesisArr[:]
    for i, c in enumerate(formula):
        if(c == "("):
            startParenthesisArr.append(i)
        if(c == ")"):
            endParenthesisArr.append(i)

# Print Parsed Expression Array
def printParsedExpressionArray():
    global parsedExpressionArr
    print "***********************"
    print "Printing Clauses with NOT operator Array "
    for item in parsedExpressionArr:
        print item
    print "***********************\n"

# create Parsed Expression Array (holds literals with NOT)
def createParsedExpressionArr(expressionArr):
    eArrLen = len(expressionArr)
    for idx, char in enumerate(expressionArr[eArrLen - 1]):
        if(char == "!" and expressionArr[eArrLen - 1][idx:idx+2] not in parsedExpressionArr):
            parsedExpressionArr.append(expressionArr[eArrLen - 1][idx:idx+2])

# replace not operators on literal
def cleanFormulaFromNot(parsedExpressionArr):
    for item in enumerate(parsedExpressionArr):
        temp = generateNewParamString()
        tseitenDictionary[str(temp)] = str(item[1])
        global formula 
        formula = formula.replace(str(item[1]), str(temp))
    indexParenthesis(formula)
    newLen = len(startParenthesisArr)
    createIndexArray(newLen)
    createExpressionArray(expressionIndexArr)

# Printing Utility function
def printTseitenDictionary():
    print "***********************"
    print "Tseiten Dictionary is \n" 
    for dic in tseitenDictionary:
        print dic, "<-->" ,tseitenDictionary[dic]
    print "***********************\n"

# Creating Tseiten Dictionary
def createTseitenDictionary():
    global formula
    global lastTmp

    for i,item in enumerate(expressionArr): 
        lastTmp = temp = generateNewParamString()
        tseitenDictionary[str(temp)] = expressionArr[i]
        formula = formula.replace(expressionArr[i], temp)

    for i, item in tseitenDictionary.iteritems():
        if(tseitenDictionary[lastTmp].find(item) != -1 and i != lastTmp):
            tseitenDictionary[lastTmp] = tseitenDictionary[lastTmp].replace(item, i)

    formula = lastTmp
    




# Printing Utility function
def printTseitenFinal(booleanThang):
    global lastTmp
    for dic in finalTseiten:
        print finalTseiten[dic], " 0"
    if(booleanThang):
        print cnfRepresentationDict[lastTmp], " 0"
    # how do i add lastTmp is true?


def findParenthesisAndOperatorIndex(secondArg, pattern):
    arrOfIdx = []
    for i,item in enumerate(secondArg):
        if(item == "("):
            arrOfIdx.append(i)
        elif(item == pattern):
            arrOfIdx.append(i)
        elif(item == ")"):
            arrOfIdx.append(i)
    return arrOfIdx

# FinalVarDictionary holds all the keys of TseitenDictionary
def printFinalVarDictionary():
    global finalVarDictionary
    print "***********************"
    print "Final Var Dictionary is "
    for item in finalVarDictionary:
        print item
    print "***********************\n"

def convertToCNF(firstArg, secondArg):
    global finalTseiten
    if secondArg.find("!") != -1:
        secondArg = secondArg.replace("!", "")
        temp = generateNewParamString()
        finalTseiten[str(temp)] = str (   "(" + "!" + firstArg + " v " + "!" + secondArg + ")" + " ^ " + "(" + firstArg + " v " + secondArg + ")" )
        if (str(firstArg) not in finalVarDictionary):
            finalVarDictionary.append(firstArg)
        if (str(secondArg) not in finalVarDictionary):
            finalVarDictionary.append(secondArg)
        return
 
    elif secondArg.find("|") != -1:
        arrOfIdx = findParenthesisAndOperatorIndex(secondArg, "|")
        secondParameter = secondArg[ arrOfIdx[0] + 1 : arrOfIdx[1] ]
        thirdParameter = secondArg[ arrOfIdx[1] + 1 : arrOfIdx[2] ]
        temp = generateNewParamString()
        finalTseiten[str(temp)] = str( "(" + "!" + secondParameter + " v " + firstArg +")" + " ^ " + "(" + "!" + thirdParameter + " v " + firstArg + ")" + " ^ " + "(" + "!" + firstArg + " v " + secondParameter + " v " + thirdParameter + ")" )

        if (str(firstArg) not in finalVarDictionary):
            finalVarDictionary.append(firstArg)
        if (str(secondParameter) not in finalVarDictionary):
            finalVarDictionary.append(secondParameter)
        if (str(thirdParameter) not in finalVarDictionary):
            finalVarDictionary.append(thirdParameter)
        return


    elif secondArg.find(">") != -1:
        arrOfIdx = findParenthesisAndOperatorIndex(secondArg, ">")
        secondParameter = secondArg[ arrOfIdx[0] + 1 : arrOfIdx[1] ]
        thirdParameter = secondArg[ arrOfIdx[1] + 1 : arrOfIdx[2] ]
        temp = generateNewParamString()
        finalTseiten[str(temp)] = str( "(" + "!" + firstArg + " v " + "!" + secondParameter + " v " + thirdParameter + ")" + " ^ " + "(" + firstArg + " v " + secondParameter + ")" + " ^ " + "(" + firstArg + " v " + "!" + thirdParameter + ")" ) 

        if (str(firstArg) not in finalVarDictionary):
            finalVarDictionary.append(firstArg)
        if (str(secondParameter) not in finalVarDictionary):
            finalVarDictionary.append(secondParameter)
        if (str(thirdParameter) not in finalVarDictionary):
            finalVarDictionary.append(thirdParameter)
        return

    elif secondArg.find("^") != -1:
        arrOfIdx = findParenthesisAndOperatorIndex(secondArg, "^")
        secondParameter = secondArg[ arrOfIdx[0] + 1 : arrOfIdx[1] ]
        thirdParameter = secondArg[ arrOfIdx[1] + 1 : arrOfIdx[2] ]
        temp = generateNewParamString()
        finalTseiten[str(temp)] = str( "(" + "!" + firstArg + " v " +  secondParameter + ")" + " ^ " + "(" + "!" + firstArg + " v " + thirdParameter + ")" + " ^ " + "(" + "!" + secondParameter + " v " + "!" + thirdParameter + " v " + firstArg + ")"  ) 
        if (str(firstArg) not in finalVarDictionary):
            finalVarDictionary.append(firstArg)
        if (str(secondParameter) not in finalVarDictionary):
            finalVarDictionary.append(secondParameter)
        if (str(thirdParameter) not in finalVarDictionary):
            finalVarDictionary.append(thirdParameter)
        return

def printCNFRepresentationDic():
    global cnfRepresentationDict
    for key in cnfRepresentationDict:
        print key, cnfRepresentationDict[key]
    return 
    


# Checking if original vars are detected correctly
#countVariables2(formula)
# TODO , take all original vals and find their value in the CNFREPRESENTATIONdictionary, and find the hasama in zchaff pelet 
#printOriginalVarDictionary2()

# check input validity
indexParenthesis(formula)
#printIndexParentheses()

# Checking for edge case, parenthesis count should be balanced
checkBalancedParen(startParenthesisArr, endParenthesisArr)

# Create Index Array, creates Expression index array
createIndexArray(startArrLen)
#printIndexArray()

# Create Raw Expression Array
createExpressionArray(expressionIndexArr)
#printExpressionArray()

# Create Array that holds all Literals with "!", BAD NAMED VARIABLE, Excuse me ;)
createParsedExpressionArr(expressionArr)
#printParsedExpressionArray() # show all literal with "!" operator

# Clean Original Formula from NOT operator on literals
cleanFormulaFromNot(parsedExpressionArr)
#printFormula()

#TODO, check that all data is update after Cleaning Formula from NOT
indexParenthesis(formula)
checkBalancedParen(startParenthesisArr, endParenthesisArr)
createIndexArray(startArrLen)
createExpressionArray(expressionIndexArr)
#printExpressionArray()


# Creating Tseiten Dictionary, all variables that Tseiten Algo introduces. ie. NOT A, B,C ..., F
createTseitenDictionary()
#printTseitenDictionary()

# Final Transformation, with Tseiten, creates FinalVarDictionary with ALL variables
for key in tseitenDictionary:
    convertToCNF(key, tseitenDictionary[key])


# Creating CNFRepresentation Dic for Last Stage (see below comments)
for key in finalVarDictionary:
    if key == "":
        continue
    cnfRepresentationDict[str(key)] = cnfRepCounter
    cnfRepCounter = cnfRepCounter + 1
orig_stdout = sys.stdout
f = file('cnfRepresentationDict.txt', 'w')
sys.stdout = f
printCNFRepresentationDic()
sys.stdout = orig_stdout
f.close()




# Parsing Expression from Parenthesis, ^,v,! operators. Preparing for cnf line format.
for dic in finalTseiten:
    finalTseiten[dic] = finalTseiten[dic].replace("!", "-")
    if finalTseiten[dic].find(" ^ ") != -1:
        equationCounter = equationCounter + finalTseiten[dic].count(" ^ ")
        finalTseiten[dic] = finalTseiten[dic].replace(" ^ ", " 0 \n")
    finalTseiten[dic] = finalTseiten[dic].replace("(", "")
    finalTseiten[dic] = finalTseiten[dic].replace(")", "")
    finalTseiten[dic] = finalTseiten[dic].replace("v", "")
    equationCounter = equationCounter + 1

# Replaces variables from form of A, B, a11 etc. to -23 32 12 etc, Last Stage
for key, val in finalTseiten.iteritems():
    for pattern, value in cnfRepresentationDict.iteritems():
        finalTseiten[key] = finalTseiten[key].replace( str(pattern) , str(value))

orig_stdout = sys.stdout
f = file('cnfFormula.cnf', 'w')
sys.stdout = f
print "p cnf", len(cnfRepresentationDict), equationCounter + 1
printTseitenFinal(True)
sys.stdout = orig_stdout
f.close()


for key, val in cnfRepresentationDict.iteritems():
    if key in originalVarDictionary2:
        print key, val
