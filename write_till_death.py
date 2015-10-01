# -*- coding: utf-8 -*-
#!/usr/bin/env python


import os
from sys import argv

print "ACHTUNG!!!"
print "Skript läuft in Endlossschleife und hört erst auf, wenn man es manuel abbricht!"

script, path = argv

write = "%swrite_till_death" %path

if os.path.exists(write):
    pass

else:
    os.system("mkdir " + write)

i = 0
while True:
    iString = str(i)
    print "Bin gerade bei %s" %iString
    os.system("touch " + path + iString + " txt" )
    iInt = int(iString)

    if iInt >= 1000000:
        "Bin Bei 100000. Lösche Ordner und fange wieder bei 0 an"
        os.system(" rm -r " + write)
        i = 0

    else:
        pass

    i = i+1








