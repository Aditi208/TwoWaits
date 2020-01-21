def sortPD(dict):
    print("sorted dictionary by key:")
    for i in sorted(dict.keys()):
        print(i,":",dict[i])
    return

def sumOfLength(dict):
    sol = 0
    for i in dict:
        sol += len(dict[i])
    return sol

def reverseValues(dict):
    print("Reversed Values are: ",end = "")
    for i in dict:
        print(dict[i][::-1], end = " ")
    
if __name__=="__main__":
    dict = {
        'name' : 'ACSDS',
        'age' : '29',
        'gender' : 'M',
        'hobbies' : 'Cricket',
        'fav numbers' : [0,2,7,9]
    }
    sortPD(dict)
    print()
    print("sum of length of all values is", sumOfLength(dict))
    print()
    reverseValues(dict)
