import numpy as np
from scipy.stats import truncnorm
from station import Station
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

    # TODO: Determine if uniform arrival is ok?
    uniform_random_station = np.random.uniform(1, MAX_STATIONS+1, MAX_PASSENGERS_IN_SIMULATION)
    # print(uniform_random_station)

    # For ever ith standard distributed passenger, assign a uniform random distributed station
    for i in range(len(random_passengers_arrival)):
        pas_arrival_time = int(random_passengers_arrival[i])
        pas_station_assignment = 's' + str(int(uniform_random_station[i]))

        # print("Queuing passenger to: " + pas_station_assignment + " | arrived at: " + str(pas_arrival_time))
        # TODO: Determine uniform(?) destination of passenger (null destination for now/end of line)

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

main()
