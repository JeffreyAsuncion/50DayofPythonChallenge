import sys

def jeffy(stry):
    print(stry)

if __name__ == '__main__':
    print(f"Arguments count: {len(sys.argv)}")
    stry = ''
    for i, arg in enumerate(sys.argv):
        print(f"Argument {i:>6}: {arg}")
        if i != 0:
            stry = stry + ' '  +arg    
    jeffy(stry)
    a = [1,2,3]
    print(sum(a))