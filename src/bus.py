class Bus:
    def __init__(self, l):
        # Current location of bus in the system.
        self.location = l

        # List of passengers currently on the bus
        self.passengers = []

        # TODO: Determine if arrival/departure time is needed?

    def passenger_count(self):
        return len(self.passengers)
