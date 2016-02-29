import urllib2
import re
from Player import Player

#url = 'http://classes.engineering.wustl.edu/cse330/content/cardinals/cardinals-1940.txt'
#data = urllib2.urlopen(url)

players = []


parse = re.findall("(?P<name>\w+\s\w+)\sbatted\s(?P<atBats>\d+)\stimes\swith\s(?P<hits>\d+)\shits\sand\s(?P<runs>\d+)\sruns", data)
for i in parse:
    print i.group('name')
#    for p in players:
#        name = parse.group('name')
#        print (name)
        
#        if name == p:
#            print (parse.group('atBats'));
#            p.addAtBats(parse.group('atBats')
#            p.addHits(parse.group('hits')
#        else:
#            players.append(Player(name))
#            p.addAtBats(parse.group('atBats')
#            p.addHits(parse.group('hits')
            
            
    