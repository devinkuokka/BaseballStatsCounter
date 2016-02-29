import math
import re

class Player(object):
    
    def __init__(self, name):
        self.name = name
        self.atBats = 0
        self.hits = 0
    
    def addAtBats(self, atBats):
        self.atBats += float(atBats)
    
    def addHits(self, hits):
        self.hits += float(hits)
    
    def getName(self):
        return self.name
    
    def getBattingAverage(self):
        avg = round(self.hits/self.atBats,3)
        return avg
        
        
        
        