cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_drivers = drivers
carpool_capacity = cars_drivers * space_in_a_car
average_passengers_per_car = passengers / cars_drivers

print("There are", cars, "cars avaiable.")
print("There are only", drivers, "Drivers avaiable.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "passengers to carpool today.")
print("We need to put about", average_passengers_per_car, "in eache car")

