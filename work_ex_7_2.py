
filename = input("Enter file name: ")

numlist = []

for line in filename:
    if line.startswith("X-DSPAM-Confidence:"):
        index = line.find(":")
        number = float(line[index + 1:])
        numlist.append(number)
        print(number, type(number))

    
print("\n The total is: ", sum(numlist))
print("\n The average is: ", sum(numlist) / len(numlist))