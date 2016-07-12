from math import factorial
from pprint import pprint as pp

def listComprehension():
    words = "WHy sometimes I have believed as many as six impossible things before breakfast".split()
    #The len() is applied to each one of the word item in the words list
    result = [len(word) for word in words]

    print("List Comprehension:\n",result,"\n")


def setComprehension():
    list = [len(str(factorial(x))) for x in range(20)]
    #sets avoid duplicates, but are unordered
    set = {len(str(factorial(x))) for x in range(20)}
    print("Set Comprehension:\nList:",list)
    print("Set:",set,"\n")

"""This example inverts the keys and values of a map"""
def dicComprehension():
    country_to_capital = {'United Kindom':'London',
                          'Brazil':'Brazilia',
                          'Morocco':'Rabat',
                          'Sweden':'Stockhol'}
    capital_to_country = {capital:country for country, capital in country_to_capital.items()}
    print("Dic Comprehencion:\n")
    pp(capital_to_country)
    print("\n")

"""This example is to show keys bein overwritten"""
def dicCompKeyOverride():
    words = ["hi", "hello", "foxtrot", "hotel"]
    res = {x[0]:x for x in words}
    print("Key Override\nBefore:")
    print(words)
    print("After:")
    print(res)

def main():
    listComprehension()
    setComprehension()
    dicComprehension()
    dicCompKeyOverride()

if __name__=='__main__':
    main()
