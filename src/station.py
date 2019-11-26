import queue


class Station:
    def __init__(self, l):
        # Unique id/(l)ocation of the station in the system
        self.station_id = l

        # Queue of passengers in the station. Infinite queue.
        self.passengers = queue.Queue(maxsize=0)

        # TODO: Determine if current parked bus is needed

    def is_station_empty(self):
        return self.passengers.empty()

    def passenger_count(self):
        return self.passengers.qsize()

    # Queues a passenger to the queue. p is of type Passenger class
    def queue_passenger(self, p):
        self.passengers.put(p)

    def dequeue_passenger(self):
        return self.passengers.get()
