import math
import re

class Player(object):
    
    #initializes player
    def __init__(self, name):
        self.name = name
        self.atBats = 0
        self.hits = 0
    
    #increases total at bats
    def addAtBats(self, atBats):
        self.atBats += float(atBats)
    
    #increases total hits
    def addHits(self, hits):
        self.hits += float(hits)
    
    # name getter
    def getName(self):
        return self.name
    
    # gets batting average rounded to at most 3 decimals places
    def getBattingAverage(self):
        return round(self.hits/self.atBats,3)
    
    #converts the batting average into a string with exactly 3 decimal places
    def toString(self):
        return '{0:.3f}'.format(self.getBattingAverage())
        
        