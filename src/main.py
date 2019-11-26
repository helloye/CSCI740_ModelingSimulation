import numpy as np
from scipy.stats import truncnorm
from station import Station
from passenger import Passenger

# 720 minute = 12 hrs.
MAX_TIME_MINUTES = 720

def main():
    # Static stations that will not change throughout the simulation
    s1 = Station('s1')
    s2 = Station('s2')
    s3 = Station('s3')
    s4 = Station('s4')
    s5 = Station('s5')

    # mu, sigma, random_pass_count = 360, 90, 100
    # random_passengers = np.random.normal(mu, sigma, random_pass_count)
    # uniform_random_station = np.random.uniform(1,5,100)

    mean, sd, low, high = 360, 360, 0, 720
    passenger_randomizer = truncnorm((low-mean)/sd, (high-mean)/sd, loc=mean, scale=sd)
    random_passengers_arrival = passenger_randomizer.rvs(100)
    # print(random_passengers_arrival)

    # TODO: Determine if uniform arrival is ok?
    uniform_random_station = np.random.uniform(1, 6, 100)
    # print(uniform_random_station)

    # For ever ith standard distributed passenger, assign a uniform random distributed station
    for i in range(len(random_passengers_arrival)):
        pas_arrival_time = int(random_passengers_arrival[i])
        pas_station_assignment = 's' + str(int(uniform_random_station[i]))

        print("Queuing passenger to: " + pas_station_assignment + " arrived at:" + str(pas_arrival_time))
        # TODO: Queue passenger to station
        # TODO: Determine uniform(?) destination of passenger



main()
