import re
from Player import Player
import sys, os
 
if len(sys.argv) < 2:
	sys.exit("Usage: %s filename" % sys.argv[0])

filename = sys.argv[1]
 
if not os.path.exists(filename):
	sys.exit("Error: File '%s' not found" % sys.argv[1])

infile = open(filename)
data = infile.read()

# "\sand\s(?P<runs>\d+)\sruns" could include in parse if needed runs, but unneeded for calculations
#Regex that looks for players name, at bats, and hits
parse = re.findall("(?P<name>\w+\s\w+)\sbatted\s(?P<atBats>\d+)\stimes\swith\s(?P<hits>\d+)\shits", data)

players = [] #creates an array of the players names as strings
repeat = 0 #tracks if a players name has already been seen in the players array

#eliminates player repeats
for x in parse:
    for y in players:
        if x[0]==y:
            repeat = 1
    if repeat==0: 
        players.append(x[0])
    else:
        repeat = 0
           
playerObj = [] #creates an array of player objects 

#populates the playerObj array
for p in players:
    temp = Player(p)
    playerObj.append(temp)

#Totals at bats and hits for players whose names are in the player object array
for x in parse:
    for y in playerObj:
        if x[0]==y.getName():
            y.addAtBats(x[1])
            y.addHits(x[2])

#sorts the batting average for each player
        
sortedAvgs = sorted(playerObj, key=lambda x: x.getBattingAverage(),reverse = True)

# prints name: batting avg in decending order 
for a in sortedAvgs:
	for p in playerObj:
		if p.getName()==a.getName():
			print a.getName()+": "+a.toString()












