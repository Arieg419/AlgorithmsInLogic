print "Reveal assignment!"
d = {}
finalAssignments = {
	'A': 'x11', 
	'B': 'x12', 
	'C': 'x13',
	'D': 'x14', 
	'E': 'x22', 
	'F': 'x23',
	'G': 'x32', 
	'H': 'x33',
	'I': 'x21',
	'J': 'x31', 
	'K': 'x24', 
	'L': 'x34',
} 


with open("solverSolution.txt") as f:
	varAssignments = f.read().split()
	if "Unsatisfiable" in varAssignments:
		print "Logical clauses are unsatisfiable.\n"

with open("cnfRepresentationDict.txt") as f:
    for line in f:
       (key, val) = line.split()
       d[key] = val

print "***************************** SOLVER ASSIGNMENT ************************************"
for key, val in d.iteritems():
	if key == 'O':
		continue
	if key.isalpha() and key.isupper() and val in varAssignments:
		print finalAssignments[key], "is represented as " ,key, " in the formula." " Assignment is TRUE"
	if key.isalpha() and key.isupper() and str("-" + val) in varAssignments:
		print finalAssignments[key], "is represented as ", key, " in the formula." " Assignment is FALSE"
print "***************************** END OF SOLVER ASSIGNMENT ************************************"