for i in range(0,4):
    num1=1
    for j in range(0,4):
        if i>=j:
           print(num1,'', end='')
           num1 +=1
    print()        
        


for i in range(0,4): 
    for j in range(0, i + 1):
        if i>=j:
           if (i + j) % 2 == 0:
              print(1, end=" ")
           else:
             print(0, end=" ")
    print()  
       