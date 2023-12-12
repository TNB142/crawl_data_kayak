import json
import os
from time import sleep
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import FirefoxOptions
from bs4 import BeautifulSoup
import re
import numpy as np
from tqdm import tqdm
from datetime import datetime
import pytz
import time

def get_airlines(soup):
    airline = []
    airlines = soup.find_all('div',class_='J0g6-operator-text',text=True)
    for i in airlines:
        airline.append(i.text)
    return airline

def get_total_stops(soup):
    stops_list = []
    stops = soup.find_all('div',class_='JWEO')

    for i in stops:
        for j in i.find_all('span',class_='JWEO-stops-text'):
               stops_list.append(j.text)
    return stops_list

def get_price(soup):
    prices = []
    price = soup.find_all('div',class_='f8F1-above')

    for i in price:
        for j in i.find_all('div', class_='f8F1-price-text'):
            prices.append(j.text)
    return prices

def get_time_flight(soup):
    time_flights = []
    time_flight_div = soup.find_all('div',class_='vmXl vmXl-mod-variant-large')

    for i in time_flight_div:
        time_=[]
        for j in i.find_all('span'):
            time_.append(j.text)
        time_flights.append(f'{time_[0]}')
    return time_flights

def get_duration(soup):
    duration_list = []
    duration = soup.find_all('div' , class_='xdW8 xdW8-mod-full-airport')
    # duration = soup.find_all('div',class_='vmXl vmXl-mod-variant-default')
    for i in duration:
        for j in i.find_all('div',class_='vmXl vmXl-mod-variant-default'):
            duration_list.append(j.text)
    return duration_list

def get_source_destination():
    sources = ['SGN','SGN']
    destinations = ['DAD','HAN']
    print("---All couple of sources and destinations---")
    for i in range(len(sources)):
        print(f"{i} Source: {sources[i]}. Destination: {destinations[i]}")
    return sources, destinations

def get_all_necessary_data(soup):
    airlines = get_airlines(soup)
    # print(airlines)

    total_stops = get_total_stops(soup)
    # print(total_stops)

    prices = get_price(soup)
    # print(prices)

    duration = get_duration(soup)
    # print(duration)

    time_flight=get_time_flight(soup)

    return airlines, total_stops, prices, duration, time_flight

def get_couple_check_and_current_time(check_state = True):
    current_time = datetime.utcnow()
    vn_timezone = pytz.timezone('Asia/Ho_Chi_Minh')
    value_transform = current_time.replace(tzinfo=pytz.utc).astimezone(vn_timezone)
    current_time = value_transform.strftime("%H:%M:%S")
    time_= datetime.strptime(current_time,"%H:%M:%S").time()

    check = datetime.strptime('11:57:00',"%H:%M:%S").time() if check_state else time_
    # print(f"Time set up: {check}. Time current: {time_}")
    return check,time_

def get_current_time():
    current_time = datetime.utcnow()
    vn_timezone = pytz.timezone('Asia/Ho_Chi_Minh')
    value_transform = current_time.replace(tzinfo=pytz.utc).astimezone(vn_timezone)
    current_time = value_transform.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current_datetime: {current_time}")
    return current_time

def get_start_end_time():
    start_date = np.datetime64('2023-12-21')
    end_date = np.datetime64('2023-12-21')
    days = end_date - start_date
    num_days = days.item().days
    print(f"Start_date: {start_date}")
    print(f"End_date: {end_date}")
    print(f"Num days scrawling: {num_days}")
    return start_date, end_date, num_days

def wait_time_count():
    check, time_ = get_couple_check_and_current_time()
    print(f"Wait time:{(check.hour*3600+check.minute*60+check.second)-(time_.hour*3600+time_.minute*60+time_.second)}s")
    return time_
