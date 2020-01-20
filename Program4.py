a, b = map(int,input("Enter two numbers ").split(" "))
print("The divisors are:")
for i in range(1, min(a, b)+1): 
    if a%i==b%i==0: 
        print(i)
