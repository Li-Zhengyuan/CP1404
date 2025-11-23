from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"
TAXIS = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]

def main():
    """Run the Taxi Simulator program."""
    bill_to_date = 0
    current_taxi = None

    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            print("Taxis available:")
            display_taxis(TAXIS)
            current_taxi = check_taxi(TAXIS)
        elif choice == "d":
            if current_taxi is None:
                print("You need to choose a taxi before you drive")
            else:
                bill_to_date = drive_taxi(current_taxi, bill_to_date)
        else:
            print("Invalid option")

        print(f"Bill to date: ${bill_to_date:.2f}")
        print(MENU)
        choice = input(">>> ").lower()

    print(f"Total trip cost: ${bill_to_date:.2f}")
    print("Taxis are now:")
    display_taxis(TAXIS)



def display_taxis(taxis):
    """Display numbered list of taxis."""
    for i, taxi in enumerate(TAXIS):
        print(f"{i} - {taxi}")



def check_taxi(taxis):
    """Check if taxi is available."""
    try:
        taxi_choice = int(input("Choose taxi: "))
        if 0 <= taxi_choice < len(taxis):
            return taxis[taxi_choice]
        else:
            print("Invalid taxi choice")
            return None
    except ValueError:
        print("Invalid taxi choice")
        return None



def drive_taxi(current_taxi, bill_to_date):
    """Drive the chosen taxi and return updated bill."""
    try:
        distance = float(input("Drive how far? "))
    except ValueError:
        print("Invalid distance")
        return bill_to_date

    current_taxi.start_fare()
    current_taxi.drive(distance)
    trip_cost = current_taxi.get_fare()
    print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
    return bill_to_date + trip_cost



main()