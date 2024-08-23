score = "Nick"
score = score 
print(score) #We use comments for our code in python!

scores = [200, 1, 2, 3, 4]
print(scores[3])

scores = {
    "John": 200,
    "Jane": 189,
    "Jack": 203,
    "Jill": 198,
    "James": 182
}

print(scores["John"]) # 200
print(scores["Jane"]) # 189


#Example of how to create a funciton. 
def add(n , r):
    if (n == 9) & (r == 10): #Python only has one and symbol
        return 21
    else:
        return n + r
    
#Example function call. 
print(add(9, 11))
