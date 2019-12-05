class Passenger:
    def __init__(self, s, d, a):
        # Source station that this passenger arrived at.
        self.source = s

        # Destination station that this passenger wishes to travel to
        self.destination= d

        # Time this passenger arrived at the station and into the system.
        self.arrival_time = a

        # Time this passenger waited in queue in station
        self.wait_time = -1

    def has_waited_more_than_20_min(self, current_time):
        return (current_time - self.arrival_time) > 20

    def has_arrived(self, current_time):
        return self.arrival_time <= current_time

    def has_not_arrived(self, current_time):
        return self.arrival_time > current_time

    def set_wait_time(self, current_time):
        self.wait_time = current_time - self.arrival_time

    def get_wait_time(self):
        return self.wait_time

    def time_in_system(self, current_time):
        return current_time - self.arrival_time

    def passenger_info(self):
        return "[PInfo]:: Station[" + self.source + "] ArrivalTime[" + str(self.arrival_time) + "]"
