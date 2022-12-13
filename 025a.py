"""
https://stackoverflow.com/questions/2244270/get-a-try-statement-to-loop-around-until-correct-value-obtained
"""

def isNumberCorrect(x):
   return x in range(4)

def Release():
    num = None # incorrect

    while not isNumberCorrect(num):
        print 'Please select one of the following?\nCompletion = 0\nRelease ID = 1\nVersion ID = 2\nBuild ID = 3\n'
        num_str = raw_input("Please select the type of release required: ")

        try:
            num = int(num_str)
        except ValueError:
            num = None

        if not isNumberCorrect(num):
            print 'Incorrect!'

     # work with num here; it's guaranteed to be correct.

if __name__ == '__main__':
  try:
    Release()
  except:
    print 'Error!'