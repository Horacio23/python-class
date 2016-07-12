from math import factorial

def listComprehension():
    words = "WHy sometimes I have believed as many as six impossible things before breakfast".split()
    #The len() is applied to each one of the word item in the words list
    result = [len(word) for word in words]
    print(result)


def setComprehension():
    list = [len(str(factorial(x))) for x in range(20)]
    #sets avoid duplicates, but are unordered
    set = {len(str(factorial(x))) for x in range(20)}
    print("List:",list)
    print("Set:",set)

def main():
    listComprehension()
    setComprehension()

if __name__=='__main__':
    main()
