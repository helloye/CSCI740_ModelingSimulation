class Bus:
    def __init__(self, arrival_time):
        # Time bus arrived into simulation (s1 arrival time)
        # Use this to calculate what time bus should be in s2-5
        self.arrival_time = arrival_time

        self.s2_arrival_time = arrival_time + 10
        self.s3_arrival_time = arrival_time + 20
        self.s4_arrival_time = arrival_time + 30
        self.s5_arrival_time = arrival_time + 40

        # This should be the max len(self.passengers)
        self.bus_size = 50

        # List of passengers currently on the bus
        self.passengers = []

    def get_passengers(self):
        return self.passengers

    def passenger_count(self):
        return len(self.passengers)

    def board_passenger(self, p):
        self.passengers.append(p)

    def print_queue(self):
        for p in self.passengers:
            print(p.passenger_info())

    def is_at_station(self, s, curr_time):
        if s == 's1' and curr_time == self.arrival_time:
            return True
        elif s == 's2' and curr_time == self.s2_arrival_time:
            return True
        elif s == 's3' and curr_time == self.s3_arrival_time:
            return True
        elif s == 's4' and curr_time == self.s4_arrival_time:
            return True
        elif s == 's5' and curr_time == self.s5_arrival_time:
            return True
        else:
            return False

    def has_room_on_bus(self):
        return len(self.passengers) < self.bus_size

    def has_left_system(self, current_time):
        # Determine if bus has left s5 and gone out of system
        return current_time > self.s5_arrival_time
