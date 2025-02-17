from flights import Flights


def main():
    filename = 'flights.json'
    flights = Flights(filename)
    
    while True:
        print("\n*** FLIGHT SCHEDULE MAIN MENU")
        print("1. Add flight")
        print("2. Print flight schedule")
        print("3. Set flight schedule filename")
        print("9. Exit the program\n")
        choice = input("Enter menu choice: ")
        print()

        if choice == '1':
            origin = input("Enter origin: ")
            destination = input("Enter destination: ")
            flight_number = input("Enter flight number: ")
            departure = input("Enter departure time (HHMM): ")
            arrival = input("Enter arrival time (HHMM): ")
            next_day = input("Is arrival next day (Y/N): ").strip().upper() == 'Y'

            try:
                flight_number = int(flight_number)
            except ValueError:
                print("\nInvalid flight number. Please try again.")
                continue
            
            flights.add_flight(origin, destination, flight_number, departure, next_day, arrival)
        elif choice == '2':
            flight_schedule = flights.get_flights()
            print("================== FLIGHT SCHEDULE ==================")
            print("Origin Destination Number Departure Arrival Duration")
            print("====== =========== ====== ========= ======== ========")
            for flight in flight_schedule:
                print(f"{flight['origin']:<6} {flight['destination']:<11} {flight['flight_number']:>6} {flight['departure']:>9} {flight['arrival']:>8} {flight['duration']:>8}")
        elif choice == '3':
            new_filename = input("Enter flight schedule filename: ")
            flights = Flights(new_filename)
        elif choice == '9':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
