# print your name 4 times using recursion
# in all cases time complexity = o(N), space complexity = o(N) where N is counter/count
def printName(count): # head recursion
    if count <= 0:
        return
    print("Sharath")
    printName(count-1)

# printName(4)

counter = 0
def printNameTwo(): # head recursion
    global counter
    if counter == 4:
        return
    print("Sharath")
    counter += 1
    printNameTwo()

# printNameTwo()

def printNameThree():
    global counter
    if counter == 4:
        return
    counter += 1
    printNameThree()
    print("Sharath")

printNameThree()