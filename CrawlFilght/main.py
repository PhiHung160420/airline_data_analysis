import os
import time

from google_flight_analysis.scrape import *

AIRPORTS = ["SGN", "HAN", "DAD", "VDO", "PQC", "HPH", "VII", "HUI", "CXR", "DLI", "UIH", "VCA", "PQC"]

def scrap_flight_data(flight_date, from_location, to_location):
    result = Scrape(from_location, to_location, flight_date, None)

    flights = result.data

    if flights is not None:
        flights.to_csv("flight.csv", mode='a', header=False)
    time.sleep(3)

FLIGHT_DATES = ["2023-04-24", "2023-04-25", "2023-04-26", "2023-04-27", "2023-04-28", "2023-04-29", "2023-04-30"
    , "2023-05-01",  "2023-05-02", "2023-05-03", "2023-05-04", "2023-05-05", "2023-05-06", "2023-05-07", "2023-05-08", "2023-05-09", "2023-05-10"
    , "2023-05-11", "2023-05-12", "2023-05-13", "2023-05-14", "2023-05-15", "2023-05-16", "2023-05-17", "2023-05-18", "2023-05-19", "2023-05-20"]
for d in range(0, len(FLIGHT_DATES)):
    flight_date = FLIGHT_DATES[d]
    for i in range(0, len(AIRPORTS) - 1):
        for j in range(i+1, len(AIRPORTS)):
            from_location = AIRPORTS[i]
            to_location = AIRPORTS[j]
            scrap_flight_data(flight_date, from_location, to_location)
            scrap_flight_data(flight_date, to_location, from_location)



