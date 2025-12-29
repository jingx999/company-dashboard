import requests
import matplotlib.pyplot as plt
from datetime import datetime
from meteostat import Point, Daily

def one_task_job():
    start_time = datetime(2018,1,1)
    end_time = datetime(2018,1,2)
    print(start_time)
    print(end_time)
    vancouver = Point(39.9042, 116.4074)
    data = Daily(vancouver, start_time, end_time)
    data_fetch = data.fetch()
    # print(data_fetch)
    data_fetch.plot(y=['tavg', 'tmin', 'tmax'])
    plt.show()

if __name__ == '__main__':
    one_task_job()
