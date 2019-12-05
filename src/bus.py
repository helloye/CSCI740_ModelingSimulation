class Bus:
    def __init__(self, l):
        # Current location of bus in the system.
        self.location = l

        # List of passengers currently on the bus
        self.passengers = []

    def passenger_count(self):
        return len(self.passengers)

    def queue_passenger(self, p):
        self.passengers.append(p)

    def print_queue(self):
        for p in self.passengers:
            print(p.passenger_info())

    def move_to_next_station(self):
        if self.location == 's1':
            self.location = 's2'
        elif self.location == 's2':
            self.location = 's3'
        elif self.location == 's3':
            self.location = 's4'
        elif self.location == 's4':
            self.location = 's5'
        elif self.location == 's5':
            self.location = 's6'
        else:
            # Default safety case...
            self.location = 's6'
