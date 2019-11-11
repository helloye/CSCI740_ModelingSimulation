class Passenger:
    def __init__(self, s, d, a):
        # Source station that this passenger arrived at.
        self.source = s

        # Destination station that this passenger wishes to travel to
        self.destination= d

        # Time this passenger arrived at the station and into the system.
        self.arrival_time = a

        # Time this passenger arrived at the destination and left the system.
        self.departure_time = -1

    def time_in_system(self):
        return self.departure_time - self.arrival_time
