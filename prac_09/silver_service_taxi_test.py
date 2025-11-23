from prac_09.silver_service_taxi import SilverServiceTaxi

def main():
    """Test the SilverServiceTaxi functionality with simple asserts."""
    test_taxi = SilverServiceTaxi("Test Taxi", 100, 2)
    test_taxi.drive(18)
    fare = test_taxi.get_fare()
    print(test_taxi)
    print(f"Fare for 18 km trip: ${fare:.2f}")

    expected_fare = 48.80
    assert abs(fare - expected_fare) < 0.01, (
        f"Expected {expected_fare}, got {fare}"
    )

main()