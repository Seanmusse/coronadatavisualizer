import requests 
import json
import datetime
from datetime import timedelta
from operator import itemgetter
import matplotlib.pyplot as plt
import matplotlib.dates


class Corona: 
    portugal_url_base = "https://api.covid19api.com/live/country/portugal/status/confirmed/date/"
    sweden_url_base = "https://api.covid19api.com/live/country/sweden/status/confirmed/date/"
    url_suffix = "T13:13:30Z"
    range_num = 4
    date_today = datetime.datetime.now()
    start_date = date_today - datetime.timedelta(days=range_num)
    start_date_day = start_date.strftime("%d")
    year = date_today.strftime("%Y")
    num_of_month = date_today.strftime("%m")
    day_of_month = date_today.strftime("%d")
    portugal_url = str(portugal_url_base) + year + "-" + num_of_month + "-" + start_date_day + str(url_suffix)
    sweden_url = str(sweden_url_base) + year + "-" + num_of_month + "-" + start_date_day + str(url_suffix)
    rportugal = requests.get(portugal_url).text
    rportugal_json = json.loads(rportugal)
    rsweden = requests.get(sweden_url).text
    rsweden_json = json.loads(rsweden)

    portugal_confirmed = []
    portugal_new_deaths = []
    portugal_new_cases = []
    portugal_deaths = []
    portugal_recovered = []
    sweden_confirmed = []
    sweden_new_deaths = []
    portugal_new_cases = []
    sweden_deaths = []
    sweden_recovered = []
    days_range = []
    fconfirmed = itemgetter("Confirmed")
    fdeaths = itemgetter("Deaths")
    frecovered = itemgetter("Recovered")

    for i in rportugal_json:
        portugal_confirmed.append(fconfirmed(i))
        portugal_deaths.append(fdeaths(i))
        portugal_recovered.append(frecovered(i))

    for i in rsweden_json: 
        sweden_confirmed.append(fconfirmed(i))
        sweden_deaths.append(fdeaths(i))
        sweden_recovered.append(frecovered(i))

    for i in range(4): 
        days_range_items = int(start_date_day) + i
        days_range.append(days_range_items)
    
    # plt.plot_date(days_range, portugal_confirmed, linestyle="solid")
    # plt.plot_date(days_range, sweden_confirmed, linestyle="solid")
    # plt.tight_layout()
    # plt.show()

    fig = plt.figure()
    plt.subplot(3, 1, 1)
    plt.ylabel("Confirmed")
    plt.plot_date(days_range, portugal_confirmed, linestyle="solid", color="g")
    plt.plot_date(days_range, sweden_confirmed, linestyle="solid", color="b")

    plt.subplot(3, 1, 2)
    plt.ylabel("Deaths")
    plt.plot_date(days_range, portugal_deaths, linestyle="solid", color="g")
    plt.plot_date(days_range, sweden_deaths, linestyle="solid", color="b")

    plt.subplot(3, 1, 3)
    plt.ylabel("Recovered")
    plt.plot_date(days_range, portugal_recovered, linestyle="solid", color="g")
    plt.plot_date(days_range, sweden_recovered, linestyle="solid", color="b")
    plt.show()
