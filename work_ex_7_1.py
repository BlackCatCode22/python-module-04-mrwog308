file = open("mbox-short.txt")

for line in file:
    line = line.rstrip()
    
    print(line.upper())