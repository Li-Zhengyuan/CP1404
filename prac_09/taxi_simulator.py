from prac_09.car import Car
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
    total_bill = 0
    # taxis = [
    #     Taxi("Prius", 100),
    #     SilverServiceTaxi("Limo", 100, 2),
    #     SilverServiceTaxi("Hummer", 200, 4)
    # ]
    current_taxi = None

    print("Let's drive!")
    print(MENU)

    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            print("Taxis available: ")
            display_taxis(TAXIS)
            current_taxi = check_taxi(TAXIS)
        elif choice == "d":
            pass
        else:
            print("Invalid option")

        print(MENU)
        menu_choice = input(">>> ").lower()



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



main()