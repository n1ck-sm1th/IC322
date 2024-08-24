#Nicholas Smith
#265904

#Open the file.
with open("invictus.txt", "r") as file:
    #Essentially straight from the notes, but read the file 
    #and store the contents for further printing. 

    #Empty dictionary for the words.
    wordCount = {}
    for line in file:
        line = line.lower()
        for word in line.split():
            if word in wordCount:
                wordCount[word] += 1
            else:
                wordCount[word] = 1

    #Tuples are like arrays
    solution = sorted(wordCount.items(), key=lambda t : t[1], reverse=True)
    
    for index in range(5):
        print(solution[index])
   # wordArray = []
  #  for word, count in wordCount.items():
 #       wordArray.append(count)
        #print(f"{word}: {count}")
    
  #  wordArray.sort(reverse=True)
  #  for index in range(5):
   #     print(wordArray[index])
