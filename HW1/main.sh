#!/bin/bash
echo "Running Tseiten Algorithm...."
python ConvertToCNF.py
echo "Running zchaff with Tseiten output..."
zchaff cnfFormula.cnf > solverSolution.txt
echo "Analyzing solver output..."
./AnalyzeSolver.sh solverSolution.txt 
echo "Finding solver assignment..."
python revealAssignment.py
echo "cleaning up utility files..."
rm solverSolution.txt
rm cnfRepresentationDict.txt
rm cnfFormula.cnf
