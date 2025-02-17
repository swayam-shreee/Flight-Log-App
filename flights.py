from datetime import datetime
import json

class Flights:

    def __init__(self, filename):
        self.filename = filename
        self.flights = []

        try:
            with open(filename, 'r') as file:
                self.flights = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError): 
            print(f'File {filename} not found')


    def add_flight(self, origin, destination, flight_number, departure, next_day, arrival):
        ''' departure and arrival should be in HHMM format '''

        try:
            # Try to parse the string as a time in HHMM format
            datetime.strptime(departure, "%H%M")
            datetime.strptime(arrival, "%H%M")
        except ValueError:
            return False

        flight_data = {
            'origin': origin,
            'destination': destination,
            'flight_number': flight_number,
            'departure': departure,
            'next_day': next_day,
            'arrival': arrival
        }

        with open(self.filename, 'w') as file:
            self.flights.append(flight_data)
            json.dump(self.flights, file, indent=4)

        return True
    

    def get_flights(self):
        formatted_flights = []

        for flight in self.flights:
            origin = flight['origin']
            destination = flight['destination']
            flight_number = flight['flight_number']

            departure_time = datetime.strptime(flight['departure'], "%H%M")
            departure = departure_time.strftime("%I:%M%p").lstrip('0').lower()

            arrival_time = datetime.strptime(flight['arrival'], "%H%M")
            if flight['next_day']:
                arrival = '+' + arrival_time.strftime("%I:%M%p").lstrip('0').lower()
            else:
                arrival = arrival_time.strftime("%I:%M%p").lstrip('0').lower()

            duration = (arrival_time - departure_time).seconds // 60
            if flight['next_day']:
                duration += 24 * 60
            duration_hours = duration // 60
            duration_minutes = duration % 60
            duration_str = f"{duration_hours}:{duration_minutes:02}"

            formatted_flights.append({
                'origin': origin,
                'destination': destination,
                'flight_number': flight_number,
                'departure': departure,
                'arrival': arrival,
                'duration': duration_str
            })

        return formatted_flights

            