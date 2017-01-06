def che_and_crak(cheese_count, boxes_of_crackers):
    print "you have %d cheeses" %cheese_count
    print "you have %d boxes of crackers!" % boxes_of_crackers
    print "man that's enough for a party!"
    print "get a blanket.\n"

print "we can just give the functions numbers directly:"
che_and_crak(20, 30)

print "Or we can use variables from our script:"
amount_of_cheese=10
amount_of_crackers=50

che_and_crak(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
che_and_crak(10+20, 5+6)

print "and we can combine the two, variables and math:"
che_and_crak(amount_of_cheese + 100, amount_of_crackers + 10000)

