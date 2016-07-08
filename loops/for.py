def rangeFor():
    for i in range(5):
        print('Index: {}'.format(i))

def enumerateFor():
    s = "The dog jumped over the rotten fence".split()
    for i,v in enumerate(s):
        print('Index: {}, Value: {}'.format(i,v))


def main():
    rangeFor()
    enumerateFor()

if __name__=='__main__':
    main()
