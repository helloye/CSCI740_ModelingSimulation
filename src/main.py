import numpy as np
from scipy.stats import truncnorm
from station import Station
from bus import Bus
from passenger import Passenger

# 720 minute = 12 hrs.
MAX_TIME_MINUTES = 720

# Max number of passenger to simulate
MAX_PASSENGERS_IN_SIMULATION = 100

# Number of stations in simulation
MAX_STATIONS = 5

# Max bus size
MAX_BUS_SIZE = 50

def main():

    '''
    Setup process.
    - Initializes stations
    - Generates random passengers (standard distribution)
    - Assign passengers to station (uniform distribution)
    '''

    # Static stations that will not change throughout the simulation
    s1 = Station('s1')
    s2 = Station('s2')
    s3 = Station('s3')
    s4 = Station('s4')
    s5 = Station('s5')

    mean, sd, low, high = 360, 360, 0, 720
    passenger_randomizer = truncnorm((low-mean)/sd, (high-mean)/sd, loc=mean, scale=sd)
    random_passengers_arrival = passenger_randomizer.rvs(MAX_PASSENGERS_IN_SIMULATION)
    random_passengers_arrival.sort()
    # print(random_passengers_arrival)

    uniform_random_station = np.random.uniform(1, MAX_STATIONS+1, MAX_PASSENGERS_IN_SIMULATION)
    # print(uniform_random_station)

    # For ever ith standard distributed passenger, assign a uniform random distributed station
    for i in range(len(random_passengers_arrival)):
        pas_arrival_time = int(random_passengers_arrival[i])
        pas_station_assignment = 's' + str(int(uniform_random_station[i]))

        # print("Queuing passenger to: " + pas_station_assignment + " | arrived at: " + str(pas_arrival_time))

        if pas_station_assignment == 's1':
            s1.queue_passenger(Passenger('s1', 'nullDestination', pas_arrival_time))
        elif pas_station_assignment == 's2':
            s2.queue_passenger(Passenger('s2', 'nullDestination', pas_arrival_time))
        elif pas_station_assignment == 's3':
            s3.queue_passenger(Passenger('s3', 'nullDestination', pas_arrival_time))
        elif pas_station_assignment == 's4':
            s4.queue_passenger(Passenger('s4', 'nullDestination', pas_arrival_time))
        elif pas_station_assignment == 's5':
            s5.queue_passenger(Passenger('s5', 'nullDestination', pas_arrival_time))

    # s1.print_queue()
    # s2.print_queue()
    # s3.print_queue()
    # s4.print_queue()
    # s5.print_queue()

    # Init buses once system is retroactively set.
    b1 = Bus('s1')

    # Main algorithm - Repeat until end of sim/max time reached.
    # 1) Update clock
    # 2) Move buses (buses come from 5 to 715
    # 3) Load passengers
    # 4) Remove bus once it reaches the end and log for analysis.

    # TESTING
    while(s1.is_station_empty() is False):
        print("S1-------")
        s1.print_queue()
        print("B1-------")
        b1.print_queue()
        print("-------\n\n\n")
        b1.queue_passenger(s1.dequeue_passenger())

    current_time = 0
    buses = []
    # While time is less than simulation time AND there are buses left in the system(?)
    while(current_time < MAX_TIME_MINUTES):
        # We will tick in intervals of 10 mins (constant travel time between stations)
        # 1) Starting at 0, we will update the clock
        current_time += 10
        print("Current time: " + str(current_time))

        # 2) Move buses:
        # 2.1) Move buses to next station (this needs to be done first to make room for arrival)
        # 2.2) Add bus to system current time is on the arrival interval

        # 3) Load passengers
        # 3.1) Determine passengers to load (arrival time is < current time, and there is a bus, and there is room on bus)
        # 3.2) Determine passengers that waited too long and left (add to loss revenue)
        # 3.3) For all passengers to be loaded, tag wait time (current time - arrival time)
        # 3.4) Do the actual dequeue from station and queue to bus

        # 4) Remove bus from system and log analytics
        # 4.1) Buses that reached null station "s6" (?)
        # 4.2) For every passenger in bus_passenger, we will log their wait time and other metrics (profit)?

main()
