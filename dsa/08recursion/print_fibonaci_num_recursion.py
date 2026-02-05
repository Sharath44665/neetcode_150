# come to this code after finishing functional recursion

def printFibonaciNum(num, f1, f2):
    
    if num == 1: 
        return
    
    f3 = f1+f2
    if f3 == 1:
        print(0)
        print(1) 
    f1,f2 = f2, f3
    if num >= 3:
        print(f3)
    printFibonaciNum(num-1, f1, f2 )
    
printFibonaciNum(10,0, 1)
