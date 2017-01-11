def number_list(a,r):
    i=0
    numbers =[]
    print i
    while i<a:
        print i
        print "At the top i is %d" % i 
        numbers.append(i)

        i =i+r
        print "Numbers now:", numbers
        print "At the bottom i is %d" %i


    print "The numbers: "

    for num in numbers:
        print num

def nl_for(a):
    numbers = []
    for i in range(0,a):
        print i
        print "At the top i is %d" %i
        numbers.append(i)
    print numbers
