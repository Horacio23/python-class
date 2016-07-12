#Symple function

def simple():
    print('Hey look, i work')

def takeInput(input):
    print('This is my input {}'.format(input))

def defaultValues(text, border='-'):
    line = border * len(text)
    print(line)
    print(text)
    print(line)

def main():
    simple()
    takeInput("hello")
    defaultValues("My message")
    defaultValues("My other Message",'*')
    defaultValues("Message with key value",border='+')

if __name__ == '__main__':
    main()
