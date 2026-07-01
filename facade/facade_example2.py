

class CarRental:
    def rent_car(self, destination):
        print(f"Car rented in {destination}")


class FlightBooking:
    def book_flight(self, destination):
       print(f"Flight booked from {destination}")


class HotelBooking:
    def book_hotel(self, destination):
        print(f"Hotel booked from {destination}")


class TravelFacade:
    def __init__(self, flight_booking, hotel_booking, car_rental):
        self.flight_booking = flight_booking
        self.hotel_booking = hotel_booking
        self.car_rental = car_rental

    def arrange_trip(self, destination):
        print(f"Arranging trip to {destination}")
        self.flight_booking.book_flight(destination)
        self.hotel_booking.book_hotel(destination)
        self.car_rental.rent_car(destination)

flight_booking = FlightBooking()
hotel_booking = HotelBooking()
car_rental = CarRental()

travel_facade = TravelFacade(flight_booking, hotel_booking, car_rental)
travel_facade.arrange_trip("New York")



