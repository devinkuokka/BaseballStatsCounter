#print "Hello World"

#width = 20
#height= 5 * 9
#print width * height
#width = "really wide"
#print width

import urllib2
url = 'http://classes.engineering.wustl.edu/cse330/content/cardinals/cardinals-1930.txt'

data = urllib2.urlopen(url)
for line in data:
    if not '=== ' in line:
        print line