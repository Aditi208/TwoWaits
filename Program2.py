n=5
for i in range(1,6):
    for j in range(1,(2*n-1)+1):
        if(j>=(n-(i-1)) and j<=(n+(i-1))):
           print("*",end="")
        else:
            print(" ",end="")
    print("\n")
           
