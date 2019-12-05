class Station:
    def __init__(self, l):
        # Unique id/(l)ocation of the station in the system
        self.id = l

        # Queue of passengers in the station. Infinite queue.
        self.passengers = []

    def station_id(self):
        return self.id

    def is_empty(self):
        return len(self.passengers) == 0

    def is_not_empty(self):
        return len(self.passengers) > 0

    def passenger_count(self):
        return len(self.passengers)

    # Queues a passenger to the queue. p is of type Passenger class
    def queue_passenger(self, p):
        self.passengers.append(p)

    def get_passengers(self):
        return self.passengers

    def set_passengers(self, new_passengers):
        self.passengers = new_passengers

    def dequeue_passenger(self):
        p = self.passengers[0]
        del self.passengers[0]
        return p

    def print_queue(self):
        for p in self.passengers:
            print(p.passenger_info())
