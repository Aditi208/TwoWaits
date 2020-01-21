str = input("Enter any sentence\n")
lowerCount = 0
upperCount = 0
for i in str:
    if i>='a' and i <= 'z':
        lowerCount += 1
    elif i>='A' and i <= 'Z':
        upperCount += 1
print("LowerCase: ",lowerCount,"\nUpperCase: ",upperCount)
