#!/bin/bash
#needs to dynamically identify line with answers
counter=0

while read line; do
  if [ $counter -eq 5 ] 
  then
  	echo $line > solverSolution.txt
  	break
  fi
  let counter++
done < solverSolution.txt