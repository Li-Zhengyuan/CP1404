from taxi import Taxi

# 1. Create a new taxi object
my_taxi = Taxi("Prius 1", 100)

# 2. Drive 40 km
my_taxi.drive(40)

# 3. Print taxi details and current fare
print(my_taxi)
print(f"Current fare: ${my_taxi.get_fare()}")


# 4. Restart fare and drive another 100 km
my_taxi.start_fare()
my_taxi.drive(100)
