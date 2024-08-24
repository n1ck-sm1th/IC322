#Nicholas Smith
#265904

#Open the file.
with open("numbers.txt", "r") as file:
    #Essentially straight from the notes, but read the file 
    #and store the contents for further printing. 
    numbers = []
    for line in file:
        numbers.append(float(line))        
    #Sort the numbers in the array
    numbers.sort()
    #Will go through array for you instead of using numbers[i]
    for index in numbers:
        print(index)