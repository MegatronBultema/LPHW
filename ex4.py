#define objects
cars=100
space_in_a_car=4
drivers=30
passengers=90
cars_not_driven=cars-drivers
cars_driven=drivers
carpool_capacity=cars_driven*space_in_a_car
avg_pass_per_car=passengers/cars_driven

print "there are", cars, "cars avialable."
print "there are only", drivers, "drivers avialable"
print "there will be", cars_not_driven, "empty cars today"
print "we can transport", carpool_capacity, "people today"
print "we have", passengers, "to carpool today"
print "we need to put about", avg_pass_per_car, "in each car"

