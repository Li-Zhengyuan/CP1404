from unreliable_car import UnreliableCar

def main():
    """Test some UnreliableCars."""

    reliable_car = UnreliableCar("Mostly Good", 100, 90)
    unreliable_car  = UnreliableCar("Dodgy", 100, 9)

    for i in range(1, 12):
        print(f"Attempting to drive {i}km:")
        print(f"{reliable_car.name:12} drove {reliable_car.drive(i):2}km")
        print(f"{unreliable_car.name:12} drove {unreliable_car.drive(i):2}km")

    print(reliable_car)
    print(unreliable_car)

main()