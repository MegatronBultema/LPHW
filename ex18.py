# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2=args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

#alternat 
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

#just one
def print_one(arg1):
    print "ag1: %r" % arg1

#takes none
def print_none():
    print "I got nothin'."

print_two("zed","shaw")
print_two_again("zed", "shaw")
print_one("First!")
print_none()
