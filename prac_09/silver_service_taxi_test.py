from prac_09.silver_service_taxi import SilverServiceTaxi

EXPECTED_FARE = 48.8
TEST_THRESHOLD = 0.01

def main():
    """Test the SilverServiceTaxi functionality with simple asserts."""
    test_taxi = SilverServiceTaxi("Test Taxi", 100, 2)
    test_taxi.drive(18)
    fare = test_taxi.get_fare()
    print(test_taxi)
    print(f"Fare for 18 km trip: ${fare:.2f}")

    expected_fare = EXPECTED_FARE
    assert abs(fare - expected_fare) < TEST_THRESHOLD, (
        f"Expected {expected_fare}, got {fare}"
    )

main()