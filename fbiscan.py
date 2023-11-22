import sys
import re
print("Usage: python3 fbiscan.py 'search term' 'nationalist | fbi'")
if (sys.argv[2] == "fbi"):
    with open("namefile FBI.mhtml", "r") as f:
        for line in f:
            if re.search(sys.argv[1].lower(), line.lower()):
                print(line)
if(sys.argv[2] == "nationalist"):
    with open("meinkampf.mhtml", "r") as f:
        for line in f:
            if re.search(sys.argv[1].lower(), line.lower()):
                print(line)  

if(sys.argv[2] == "Rosdesto"):
    with open("namelist", "r") as f:
        for line in f:
            if re.search(sys.argv[1].lower(), line.lower()):
                print(line)
           
print("end")
