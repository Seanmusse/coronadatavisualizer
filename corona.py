import requests 
import json
import datetime
from datetime import timedelta
from operator import itemgetter

class Corona: 
    portugal_url_base = "https://api.covid19api.com/live/country/portugal/status/confirmed/date/"
    sweden_url_base = "https://api.covid19api.com/live/country/sweden/status/confirmed/date/"
    url_suffix = "T13:13:30Z"
    range_num = 7
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
    portugal_new = []
    portugal_deaths = []
    portugal_recovered = []
    sweden_confirmed = []
    sweden_new = []
    sweden_deaths = []
    sweden_recovered = []

    for i in rportugal_json:
        fconfirmed = itemgetter("Confirmed")
        portugal_confirmed.append(fconfirmed(i))

    print(portugal_confirmed)

 
    