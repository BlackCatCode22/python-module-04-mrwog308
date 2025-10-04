
file = open("mbox-short.txt")

for line in file:
    line = line.rstrip()
    # print(line,line)
    words = line.split()
    # print("Words:", words)
    # guardian in a compound statement
    if len(words) < 3 or words[0] != "From" : continue
    print(words[2])