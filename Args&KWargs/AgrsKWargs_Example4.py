# Python program to illustrate 
# *args
def testify(arg1, *argv):
    print ("first argument :", arg1)
    for arg in argv:
        print ("Next argument through *argv :", arg)
 
testify('Hello', 'Welcome', 'to', 'GeeksforGeeks')