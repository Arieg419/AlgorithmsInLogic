print "Reveal assignment!"
d = {}
finalAssignments = {} # connect a and x11?

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
	if key.isalpha() and key.isupper() and val in varAssignments:
		print key, "TRUE", val, "\n"
	if key.isalpha() and key.isupper() and str("-" + val) in varAssignments:
		print key, "FALSE", str("-" + val), "\n"
print "***************************** END OF SOLVER ASSIGNMENT ************************************"