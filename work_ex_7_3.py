
while True:

    filename = input("Enter file name: ")

    if filename == "NA NA BOO BOO":
        print("NA NA BOO BOO TO YOU - You have been punk'd!")
        quit()
    
    try:
        file = open(filename)
        break
    except:
        print("File cannot be opened:", filename)
        continue

numlist = []

for line in file:
    if line.startswith("X-DSPAM-Confidence:"):
        index = line.find(":")
        number = float(line[index + 1:])
        numlist.append(number)
        print(number, type(number))

    
print("\n The total is: ", sum(numlist))
print("\n The average is: ", sum(numlist) / len(numlist))