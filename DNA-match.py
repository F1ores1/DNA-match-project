from sys import exit
import re
import csv


"""
if len(argv) != 3:
    print("Usage: python dna.py data.csv sequence.txt")
    exit(1)

size = 0
if argv[1] == "databases/large.csv":
    size = "large"
elif argv[1] == "databases/small.csv":
    size = "small"
"""

size = "large"

finder = []
largelist = ["AGATC","TTTTTTCT","AATG","TCTAG","GATA","TATC","GAAA","TCTG"]
smallerlist = []
f = open("6.txt", "r")
for i in f:
    if size == "large":
        for z in range(len(largelist)):
            count = 0
            hcount = 0
            loc = 0
            add = len(largelist[z])
            while True:
                
                if count > hcount:
                    hcount = count
                    
                loc = i.find(largelist[z],loc)
                
                if loc == -1:
                    break
                count = 0
                
                while True:
                     
                    if  i[loc:(loc+add)] == largelist[z]:
                        count +=1
                    else:
                        break
                    loc += add
            finder.append(hcount)
            

    elif size == "small":
        AGATC = re.findall('AGATC', i)
        finder.append(len(AGATC))

        AATG = re.findall('AATG', i)
        finder.append(len(AATG))

        TATC = re.findall('TATC', i)
        finder.append(len(TATC))

print(finder)

with open("large.csv", newline='') as file:
    read = csv.reader(file, delimiter=',')
    line_count = 0
    for row in read:
        iterater = []
        if line_count !=0:

            x = len(row)
            for j in range(x):
                if j != 0:
                    iterater.append(int(row[j]))



        line_count += 1
        if finder == iterater:
            print(row[0])
            exit(0)

print("No match")