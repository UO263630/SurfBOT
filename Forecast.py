from concurrent.futures import thread
from telegram import ChatAction,InlineKeyboardMarkup, InlineKeyboardButton, InlineQueryResultPhoto, InputMedia, InputMediaPhoto
import telegram
from telegram.ext import CallbackQueryHandler
import arrow
import requests
from tabulate import tabulate
import threading

from uuid import uuid4

import telepot

import Graficas

TABLA1=[]
TABLA2=[]
TABLA3=[]
TABLA4=[]
DIRV=[]
DIRS=[]
DIRV2=[]
DIRS2=[]
MSN=""
TOKEN=""
CHAT=""
AUX=0
buttonI = InlineKeyboardButton(
        text= "<---",
        callback_data="BI"
)
buttonD = InlineKeyboardButton(
        text= "--->",
        callback_data="BD"
)

buttonGV= InlineKeyboardButton(
        text= "Graficas de viento",
        callback_data='BGV'
)

buttonGS= InlineKeyboardButton(
        text= "Grafica de Oleaje",
        callback_data='BGS'
)

buttonI2 = InlineKeyboardButton(
        text= "<--",
        callback_data="B22I s"
)
buttonNUEVO = InlineKeyboardButton(
        text= "-->",
        callback_data="B33I"
)

buttonGV2= InlineKeyboardButton(
        text= "Grafica de viento",
        callback_data='B22GV'
)

buttonGS2= InlineKeyboardButton(
        text= "Grafica de oleaje",
        callback_data='B22GS'
)


def Forecast(lat,lon,BOT_TOKEN,chat_id,evento):

    print("<<<<<<<<<<<<<<<<<<<<<<<")
    #print(threading.get_ident())

    la = lat
    lo = lon
    tz='UTC+1'
    global TABLA1,TABLA2,TABLA3,TABLA4,DIRV,DIRS,DIRV2,DIRS2,MSN,TOKEN,CHAT,AUX
    TOKEN=BOT_TOKEN
    CHAT=chat_id
   
    # Get first hour of today
    start = arrow.now().floor('day')
    print(start)
    # Get last hour of today
    end = start.shift(days=+2)
    print(end)

    
    response = requests.get(
    'https://api.stormglass.io/v2/weather/point',
    params={
        'lat': la,
        'lng': lo,
        'params': ','.join(['airTemperature', 'windSpeed','waveDirection','swellPeriod','swellHeight','swellDirection']),
        'start': start.to('UTC+1').timestamp(),  # Convert to UTC timestamp
        'end': end.to('UTC+1').timestamp()  # Convert to UTC timestamp
    },
    headers={
        'Authorization': '0434d41e-716b-11ec-9e35-0242ac130002-0434d48c-716b-11ec-9e35-0242ac130002'
    }
    )

    # Do something with response data.
    json_data = response.json()

    print(json_data)
        


    """
    json_data = {'hours': [{'airTemperature': {'dwd': 6.08, 'noaa': 9.03, 'sg': 6.08}, 'swellDirection': {'dwd': 112.4, 'icon': 91.48, 'meteo': 88.59, 'noaa': 109.09, 'sg': 88.59}, 'swellHeight': {'dwd': 0.25, 'icon': 0.33, 'meteo': 0.29, 'noaa': 0.36, 'sg': 0.29}, 'swellPeriod': {'dwd': 3.44, 'icon': 4.28, 'meteo': 3.41, 'noaa': 4.19, 'sg': 3.41}, 'time': '2022-03-07T23:00:00+00:00', 'waveDirection': {'icon': 91.48, 'meteo': 108.53, 'noaa': 98.6, 'sg': 108.53}, 'windSpeed': {'icon': 1.34, 'noaa': 1.43, 'sg': 1.34}}, {'airTemperature': {'dwd': 5.84, 'noaa': 8.61, 'sg': 5.84}, 'swellDirection': {'dwd': 110.28, 'icon': 94.35, 'meteo': 68.88, 'noaa': 113.96, 'sg': 68.88}, 'swellHeight': {'dwd': 0.3, 'icon': 0.36, 'meteo': 0.28, 'noaa': 0.38, 'sg': 0.28}, 'swellPeriod': {'dwd': 3.9, 'icon': 4.41, 'meteo': 3.64, 'noaa': 3.89, 'sg': 3.64}, 'time': '2022-03-08T00:00:00+00:00', 'waveDirection': {'icon': 94.35, 'meteo': 110.57, 'noaa': 108.02, 'sg': 110.57}, 'windSpeed': {'icon': 1.51, 'noaa': 1.2, 'sg': 1.51}}, {'airTemperature': {'dwd': 5.72, 'noaa': 8.25, 'sg': 5.72}, 'swellDirection': {'dwd': 112.39, 'icon': 95.77, 'meteo': 72.4, 'noaa': 115.89, 'sg': 72.4}, 'swellHeight': {'dwd': 0.31, 'icon': 0.36, 'meteo': 0.3, 'noaa': 0.38, 'sg': 0.3}, 'swellPeriod': {'dwd': 3.87, 'icon': 4.38, 'meteo': 3.74, 'noaa': 3.94, 'sg': 3.74}, 'time': '2022-03-08T01:00:00+00:00', 'waveDirection': {'icon': 95.77, 'meteo': 108.96, 'noaa': 107.03, 'sg': 108.96}, 'windSpeed': {'icon': 1.5, 'noaa': 1.27, 'sg': 1.5}}, {'airTemperature': {'dwd': 5.28, 'noaa': 7.89, 'sg': 5.28}, 'swellDirection': {'dwd': 113.82, 'icon': 97.2, 'meteo': 75.91, 'noaa': 117.83, 'sg': 75.91}, 'swellHeight': {'dwd': 0.31, 'icon': 0.36, 'meteo': 0.33, 'noaa': 0.37, 'sg': 0.33}, 'swellPeriod': {'dwd': 3.86, 'icon': 4.36, 'meteo': 3.84, 'noaa': 3.99, 'sg': 3.84}, 'time': '2022-03-08T02:00:00+00:00', 'waveDirection': {'icon': 97.2, 'meteo': 107.36, 'noaa': 106.04, 'sg': 107.36}, 'windSpeed': {'icon': 1.48, 'noaa': 1.35, 'sg': 1.48}}, {'airTemperature': {'dwd': 4.97, 'noaa': 7.52, 'sg': 4.97}, 'swellDirection': {'dwd': 114.91, 'icon': 98.62, 'meteo': 79.43, 'noaa': 119.76, 'sg': 79.43}, 'swellHeight': {'dwd': 0.31, 'icon': 0.36, 'meteo': 
    0.35, 'noaa': 0.37, 'sg': 0.35}, 'swellPeriod': {'dwd': 3.84, 'icon': 4.33, 'meteo': 3.94, 'noaa': 4.04, 'sg': 3.94}, 'time': '2022-03-08T03:00:00+00:00', 'waveDirection': {'icon': 98.62, 'meteo': 105.75, 'noaa': 105.05, 'sg': 105.75}, 'windSpeed': {'icon': 1.47, 'noaa': 1.42, 'sg': 1.47}}, {'airTemperature': {'dwd': 4.64, 'noaa': 7.28, 'sg': 4.64}, 'swellDirection': {'dwd': 115.82, 'icon': 99.62, 'meteo': 79.77, 'noaa': 118.83, 'sg': 79.77}, 'swellHeight': {'dwd': 0.31, 'icon': 0.35, 'meteo': 0.34, 'noaa': 0.35, 'sg': 0.34}, 'swellPeriod': {'dwd': 3.83, 'icon': 4.32, 'meteo': 3.94, 'noaa': 4.02, 'sg': 3.94}, 'time': '2022-03-08T04:00:00+00:00', 'waveDirection': {'icon': 99.62, 'meteo': 106.86, 'noaa': 105.46, 'sg': 106.86}, 'windSpeed': {'icon': 1.43, 'noaa': 1.38, 'sg': 1.43}}, {'airTemperature': {'dwd': 4.33, 'noaa': 7.04, 'sg': 4.33}, 'swellDirection': {'dwd': 116.67, 'icon': 100.61, 'meteo': 80.1, 'noaa': 117.91, 'sg': 80.1}, 'swellHeight': {'dwd': 0.3, 'icon': 0.35, 'meteo': 0.34, 'noaa': 0.34, 'sg': 0.34}, 'swellPeriod': {'dwd': 3.82, 'icon': 4.3, 'meteo': 3.93, 'noaa': 4.0, 'sg': 3.93}, 'time': '2022-03-08T05:00:00+00:00', 'waveDirection': {'icon': 100.61, 'meteo': 107.97, 'noaa': 105.87, 'sg': 107.97}, 'windSpeed': {'icon': 1.38, 'noaa': 1.33, 'sg': 1.38}}, {'airTemperature': {'dwd': 3.95, 
    'noaa': 6.8, 'sg': 3.95}, 'swellDirection': {'dwd': 117.55, 'icon': 101.61, 'meteo': 80.44, 'noaa': 116.98, 'sg': 80.44}, 'swellHeight': {'dwd': 0.3, 'icon': 0.34, 'meteo': 0.33, 'noaa': 0.32, 'sg': 0.33}, 'swellPeriod': {'dwd': 3.8, 'icon': 4.29, 'meteo': 3.93, 'noaa': 3.98, 'sg': 3.93}, 'time': '2022-03-08T06:00:00+00:00', 'waveDirection': {'icon': 101.61, 'meteo': 109.08, 'noaa': 106.28, 'sg': 109.08}, 'windSpeed': {'icon': 1.34, 'noaa': 1.29, 'sg': 1.34}}, {'airTemperature': {'dwd': 4.47, 'noaa': 7.77, 'sg': 4.47}, 'swellDirection': {'dwd': 118.47, 'icon': 103.01, 'meteo': 82.04, 'noaa': 117.99, 'sg': 82.04}, 'swellHeight': {'dwd': 0.29, 'icon': 0.34, 'meteo': 0.33, 'noaa': 0.32, 'sg': 0.33}, 'swellPeriod': {'dwd': 3.79, 'icon': 4.25, 'meteo': 3.88, 'noaa': 3.96, 'sg': 3.88}, 'time': '2022-03-08T07:00:00+00:00', 'waveDirection': {'icon': 103.01, 'meteo': 110.1, 'noaa': 108.03, 'sg': 110.1}, 'windSpeed': {'icon': 1.21, 'noaa': 1.24, 'sg': 1.21}}, {'airTemperature': {'dwd': 7.01, 'noaa': 8.74, 'sg': 7.01}, 'swellDirection': {'dwd': 119.75, 'icon': 104.42, 'meteo': 83.64, 'noaa': 119.0, 'sg': 83.64}, 'swellHeight': {'dwd': 0.29, 'icon': 0.33, 'meteo': 0.33, 'noaa': 0.31, 'sg': 0.33}, 'swellPeriod': {'dwd': 3.77, 'icon': 4.21, 'meteo': 3.84, 'noaa': 3.95, 'sg': 3.84}, 'time': '2022-03-08T08:00:00+00:00', 'waveDirection': {'icon': 104.42, 'meteo': 111.13, 'noaa': 109.77, 'sg': 111.13}, 'windSpeed': {'icon': 1.07, 'noaa': 1.2, 'sg': 1.07}}, {'airTemperature': {'dwd': 9.81, 'noaa': 9.71, 'sg': 9.81}, 'swellDirection': {'dwd': 122.38, 'icon': 105.82, 'meteo': 85.24, 'noaa': 120.01, 'sg': 85.24}, 'swellHeight': {'dwd': 0.29, 'icon': 0.33, 'meteo': 0.33, 'noaa': 0.31, 'sg': 0.33}, 'swellPeriod': {'dwd': 3.71, 'icon': 4.17, 'meteo': 3.79, 'noaa': 3.93, 'sg': 3.79}, 'time': '2022-03-08T09:00:00+00:00', 'waveDirection': {'icon': 105.82, 'meteo': 112.15, 'noaa': 111.52, 'sg': 112.15}, 'windSpeed': {'icon': 0.94, 'noaa': 1.15, 'sg': 0.94}}, {'airTemperature': {'dwd': 10.72, 'noaa': 10.51, 'sg': 10.72}, 'swellDirection': {'dwd': 126.96, 'icon': 109.55, 'meteo': 87.43, 'noaa': 117.47, 'sg': 87.43}, 'swellHeight': {'dwd': 0.3, 'icon': 0.34, 'meteo': 0.33, 'noaa': 0.29, 'sg': 
    0.33}, 'swellPeriod': {'dwd': 3.62, 'icon': 4.1, 'meteo': 3.73, 'noaa': 3.9, 'sg': 3.73}, 'time': '2022-03-08T10:00:00+00:00', 'waveDirection': {'icon': 110.92, 'meteo': 112.83, 'noaa': 135.24, 'sg': 112.83}, 'windSpeed': {'icon': 1.85, 'noaa': 1.58, 'sg': 1.85}}, {'airTemperature': {'dwd': 10.94, 'noaa': 11.31, 'sg': 10.94}, 'swellDirection': {'dwd': 131.77, 'icon': 113.28, 'meteo': 89.63, 'noaa': 114.94, 'sg': 89.63}, 'swellHeight': {'dwd': 0.32, 'icon': 0.34, 'meteo': 0.32, 'noaa': 0.28, 'sg': 0.32}, 'swellPeriod': {'dwd': 3.56, 'icon': 4.03, 'meteo': 3.66, 'noaa': 3.87, 'sg': 3.66}, 'time': '2022-03-08T11:00:00+00:00', 'waveDirection': {'icon': 116.01, 'meteo': 113.51, 'noaa': 158.95, 'sg': 113.51}, 'windSpeed': {'icon': 2.77, 'noaa': 2.02, 'sg': 2.77}}, {'airTemperature': {'dwd': 10.8, 'noaa': 12.11, 'sg': 10.8}, 'swellDirection': {'dwd': 129.78, 'icon': 117.01, 
    'meteo': 91.82, 'noaa': 112.4, 'sg': 91.82}, 'swellHeight': {'dwd': 0.31, 'icon': 0.35, 'meteo': 0.32, 'noaa': 0.26, 'sg': 0.32}, 'swellPeriod': {'dwd': 3.7, 'icon': 3.96, 'meteo': 3.6, 'noaa': 3.84, 'sg': 3.6}, 'time': 
    '2022-03-08T12:00:00+00:00', 'waveDirection': {'icon': 121.11, 'meteo': 114.19, 'noaa': 182.67, 'sg': 114.19}, 'windSpeed': {'icon': 3.68, 'noaa': 2.45, 'sg': 3.68}}, {'airTemperature': {'dwd': 10.05, 'noaa': 12.23, 'sg': 10.05}, 'swellDirection': {'dwd': 134.27, 'icon': 122.59, 'meteo': 91.73, 'noaa': 111.76, 'sg': 91.73}, 'swellHeight': {'dwd': 0.33, 'icon': 0.36, 'meteo': 0.31, 'noaa': 0.25, 'sg': 0.31}, 'swellPeriod': {'dwd': 3.62, 
    'icon': 3.85, 'meteo': 3.58, 'noaa': 3.88, 'sg': 3.58}, 'time': '2022-03-08T13:00:00+00:00', 'waveDirection': {'icon': 125.33, 'meteo': 120.0, 'noaa': 184.89, 'sg': 120.0}, 'windSpeed': {'icon': 3.07, 'noaa': 2.72, 'sg': 3.07}}, {'airTemperature': {'dwd': 9.73, 'noaa': 12.36, 'sg': 9.73}, 'swellDirection': {'dwd': 141.45, 'icon': 128.18, 'meteo': 91.64, 'noaa': 111.12, 'sg': 91.64}, 'swellHeight': {'dwd': 0.35, 'icon': 0.38, 'meteo': 0.3, 'noaa': 0.25, 'sg': 0.3}, 'swellPeriod': {'dwd': 3.51, 'icon': 3.75, 'meteo': 3.55, 'noaa': 3.93, 'sg': 3.55}, 'time': '2022-03-08T14:00:00+00:00', 'waveDirection': {'icon': 129.54, 'meteo': 125.8, 'noaa': 187.11, 'sg': 125.8}, 'windSpeed': {'icon': 2.45, 'noaa': 2.99, 'sg': 2.45}}, {'airTemperature': {'dwd': 9.46, 'noaa': 12.48, 'sg': 9.46}, 'swellDirection': {'dwd': 142.43, 'icon': 133.76, 'meteo': 91.55, 'noaa': 110.48, 'sg': 91.55}, 'swellHeight': {'dwd': 0.36, 'icon': 0.39, 'meteo': 0.29, 'noaa': 0.24, 'sg': 0.29}, 'swellPeriod': {'dwd': 3.5, 'icon': 3.64, 'meteo': 3.53, 'noaa': 3.97, 'sg': 3.53}, 'time': '2022-03-08T15:00:00+00:00', 'waveDirection': {'icon': 133.76, 'meteo': 131.61, 'noaa': 189.33, 'sg': 131.61}, 'windSpeed': {'icon': 1.84, 'noaa': 3.26, 'sg': 1.84}}, {'airTemperature': {'dwd': 9.41, 'noaa': 12.05, 'sg': 9.41}, 'swellDirection': {'dwd': 141.2, 'icon': 134.73, 'meteo': 91.29, 'noaa': 104.95, 'sg': 91.29}, 'swellHeight': {'dwd': 0.36, 'icon': 0.39, 'meteo': 0.28, 'noaa': 0.21, 'sg': 0.28}, 'swellPeriod': {'dwd': 3.59, 'icon': 3.66, 'meteo': 3.52, 'noaa': 4.07, 'sg': 3.52}, 'time': '2022-03-08T16:00:00+00:00', 'waveDirection': {'icon': 134.73, 'meteo': 134.68, 'noaa': 188.37, 'sg': 134.68}, 'windSpeed': {'icon': 1.55, 'noaa': 2.79, 'sg': 1.55}}, {'airTemperature': {'dwd': 9.11, 'noaa': 11.62, 'sg': 9.11}, 'swellDirection': {'dwd': 140.73, 'icon': 135.7, 'meteo': 91.04, 'noaa': 99.42, 'sg': 91.04}, 'swellHeight': {'dwd': 0.36, 'icon': 0.39, 'meteo': 0.27, 'noaa': 0.19, 'sg': 0.27}, 'swellPeriod': {'dwd': 3.65, 'icon': 3.69, 'meteo': 3.51, 'noaa': 4.18, 'sg': 3.51}, 'time': '2022-03-08T17:00:00+00:00', 'waveDirection': {'icon': 135.7, 'meteo': 137.74, 'noaa': 187.4, 'sg': 137.74}, 'windSpeed': {'icon': 1.26, 'noaa': 2.31, 'sg': 1.26}}, {'airTemperature': {'dwd': 8.74, 'noaa': 11.18, 'sg': 8.74}, 'swellDirection': {'dwd': 140.6, 'icon': 136.67, 'meteo': 90.78, 'noaa': 93.89, 'sg': 90.78}, 'swellHeight': {'dwd': 0.36, 'icon': 0.39, 'meteo': 0.26, 'noaa': 0.16, 'sg': 0.26}, 'swellPeriod': {'dwd': 3.7, 'icon': 3.71, 'meteo': 3.5, 'noaa': 4.28, 'sg': 3.5}, 'time': '2022-03-08T18:00:00+00:00', 'waveDirection': {'icon': 136.67, 'meteo': 140.81, 'noaa': 186.44, 'sg': 140.81}, 'windSpeed': {'icon': 0.97, 'noaa': 1.84, 'sg': 0.97}}, {'airTemperature': {'dwd': 8.42, 'noaa': 10.91, 'sg': 8.42}, 'swellDirection': {'dwd': 140.9, 'icon': 137.1, 'meteo': 90.83, 'noaa': 92.96, 'sg': 90.83}, 'swellHeight': {'dwd': 0.36, 'icon': 0.38, 'meteo': 0.25, 'noaa': 0.15, 'sg': 0.25}, 'swellPeriod': {'dwd': 3.73, 'icon': 3.72, 'meteo': 3.47, 'noaa': 4.23, 'sg': 3.47}, 'time': '2022-03-08T19:00:00+00:00', 'waveDirection': {'icon': 137.1, 'meteo': 140.68, 'noaa': 185.15, 'sg': 140.68}, 'windSpeed': {'icon': 0.66, 'noaa': 1.49, 'sg': 0.66}}, {'airTemperature': {'dwd': 7.94, 'noaa': 10.63, 'sg': 7.94}, 'swellDirection': {'dwd': 141.6, 'icon': 137.52, 'meteo': 90.88, 'noaa': 92.02, 'sg': 90.88}, 'swellHeight': {'dwd': 0.35, 'icon': 0.38, 'meteo': 0.25, 'noaa': 0.15, 'sg': 0.25}, 'swellPeriod': {'dwd': 3.76, 'icon': 3.74, 'meteo': 3.45, 
    'noaa': 4.17, 'sg': 3.45}, 'time': '2022-03-08T20:00:00+00:00', 'waveDirection': {'icon': 137.52, 'meteo': 140.54, 'noaa': 183.85, 'sg': 140.54}, 'windSpeed': {'icon': 0.36, 'noaa': 1.15, 'sg': 0.36}}, {'airTemperature': {'dwd': 7.47, 'noaa': 10.35, 'sg': 7.47}, 'swellDirection': {'dwd': 142.38, 'icon': 137.95, 'meteo': 90.93, 'noaa': 91.09, 'sg': 90.93}, 'swellHeight': {'dwd': 0.35, 'icon': 0.37, 'meteo': 0.24, 'noaa': 0.14, 'sg': 0.24}, 'swellPeriod': {'dwd': 3.78, 'icon': 3.75, 'meteo': 3.42, 'noaa': 4.12, 'sg': 3.42}, 'time': '2022-03-08T21:00:00+00:00', 'waveDirection': {'icon': 137.95, 'meteo': 140.41, 'noaa': 182.56, 'sg': 140.41}, 'windSpeed': 
    {'icon': 0.05, 'noaa': 0.8, 'sg': 0.05}}, {'airTemperature': {'dwd': 7.25, 'noaa': 10.24, 'sg': 7.25}, 'swellDirection': {'dwd': 142.95, 'icon': 138.2, 'meteo': 90.84, 'noaa': 119.01, 'sg': 90.84}, 'swellHeight': {'dwd': 0.34, 'icon': 0.36, 'meteo': 0.23, 'noaa': 0.27, 'sg': 0.23}, 'swellPeriod': {'dwd': 3.8, 'icon': 3.75, 'meteo': 3.4, 'noaa': 4.06, 'sg': 3.4}, 'time': '2022-03-08T22:00:00+00:00', 'waveDirection': {'icon': 138.2, 'meteo': 140.53, 'noaa': 180.43, 'sg': 140.53}, 'windSpeed': {'icon': 0.32, 'noaa': 0.92, 'sg': 0.32}}, {'airTemperature': {'dwd': 7.26, 'noaa': 10.13, 'sg': 7.26}, 'swellDirection': {'dwd': 143.2, 'icon': 138.44, 'meteo': 90.75, 'noaa': 146.94, 'sg': 90.75}, 'swellHeight': {'dwd': 0.34, 'icon': 0.36, 'meteo': 0.23, 'noaa': 0.4, 'sg': 0.23}, 'swellPeriod': {'dwd': 3.8, 'icon': 3.74, 'meteo': 3.38, 'noaa': 4.01, 'sg': 3.38}, 'time': '2022-03-08T23:00:00+00:00', 'waveDirection': {'icon': 138.44, 'meteo': 140.64, 'noaa': 178.3, 'sg': 140.64}, 'windSpeed': {'icon': 0.59, 'noaa': 1.03, 'sg': 0.59}}, {'airTemperature': {'dwd': 7.4, 'noaa': 10.02, 'sg': 7.4}, 'swellDirection': {'dwd': 143.22, 'icon': 138.69, 'meteo': 90.66, 'noaa': 174.86, 'sg': 90.66}, 'swellHeight': {'dwd': 0.33, 'icon': 0.35, 'meteo': 0.22, 'noaa': 0.53, 'sg': 0.22}, 'swellPeriod': {'dwd': 3.8, 'icon': 3.74, 'meteo': 3.36, 'noaa': 3.95, 'sg': 3.36}, 'time': '2022-03-09T00:00:00+00:00', 'waveDirection': {'icon': 138.69, 'meteo': 140.76, 'noaa': 176.17, 'sg': 140.76}, 'windSpeed': {'icon': 0.86, 'noaa': 1.15, 'sg': 0.86}}, {'airTemperature': {'dwd': 7.3, 'noaa': 9.78, 'sg': 7.3}, 'swellDirection': {'dwd': 143.06, 'icon': 138.56, 'meteo': 90.5, 'noaa': 180.9, 'sg': 90.5}, 'swellHeight': {'dwd': 0.33, 'icon': 0.34, 'meteo': 0.22, 'noaa': 0.46, 'sg': 0.22}, 'swellPeriod': {'dwd': 3.79, 'icon': 3.72, 'meteo': 3.34, 'noaa': 3.89, 'sg': 3.34}, 'time': '2022-03-09T01:00:00+00:00', 'waveDirection': {'icon': 138.56, 'meteo': 138.97, 'noaa': 172.7, 'sg': 138.97}, 'windSpeed': {'icon': 1.01, 'noaa': 1.19, 'sg': 1.01}}, {'airTemperature': {'dwd': 7.23, 'noaa': 9.54, 'sg': 7.23}, 'swellDirection': {'dwd': 142.68, 'icon': 138.42, 'meteo': 90.33, 'noaa': 186.93, 'sg': 90.33}, 'swellHeight': {'dwd': 0.32, 'icon': 0.34, 'meteo': 0.21, 'noaa': 0.39, 'sg': 0.21}, 'swellPeriod': {'dwd': 3.78, 'icon': 3.7, 'meteo': 3.33, 'noaa': 3.83, 'sg': 3.33}, 'time': '2022-03-09T02:00:00+00:00', 'waveDirection': {'icon': 138.42, 'meteo': 137.19, 'noaa': 169.22, 'sg': 137.19}, 'windSpeed': {'icon': 1.15, 'noaa': 1.23, 'sg': 1.15}}, {'airTemperature': {'dwd': 7.19, 'noaa': 9.3, 'sg': 7.19}, 'swellDirection': {'dwd': 142.08, 'icon': 138.29, 
    'meteo': 90.17, 'noaa': 192.97, 'sg': 90.17}, 'swellHeight': {'dwd': 0.31, 'icon': 0.33, 'meteo': 0.21, 'noaa': 0.32, 'sg': 0.21}, 'swellPeriod': {'dwd': 3.75, 'icon': 3.68, 'meteo': 3.31, 'noaa': 3.77, 'sg': 3.31}, 'time': '2022-03-09T03:00:00+00:00', 'waveDirection': {'icon': 138.29, 'meteo': 135.4, 'noaa': 165.75, 'sg': 135.4}, 'windSpeed': {'icon': 1.3, 'noaa': 1.27, 'sg': 1.3}}, {'airTemperature': {'dwd': 7.14, 'noaa': 9.18, 'sg': 
    7.14}, 'swellDirection': {'dwd': 141.26, 'icon': 137.53, 'meteo': 90.22, 'noaa': 175.13, 'sg': 90.22}, 'swellHeight': {'dwd': 0.31, 'icon': 0.32, 'meteo': 0.2, 'noaa': 0.32, 'sg': 0.2}, 'swellPeriod': {'dwd': 3.72, 'icon': 3.67, 'meteo': 3.29, 'noaa': 3.75, 'sg': 3.29}, 'time': '2022-03-09T04:00:00+00:00', 'waveDirection': {'icon': 137.53, 'meteo': 132.75, 'noaa': 161.38, 'sg': 132.75}, 'windSpeed': {'icon': 1.5, 'noaa': 1.26, 'sg': 1.5}}, {'airTemperature': {'dwd': 7.21, 'noaa': 9.05, 'sg': 7.21}, 'swellDirection': {'dwd': 140.24, 'icon': 136.77, 'meteo': 90.27, 'noaa': 157.3, 'sg': 90.27}, 'swellHeight': {'dwd': 0.3, 'icon': 0.32, 'meteo': 0.2, 'noaa': 0.31, 'sg': 0.2}, 'swellPeriod': {'dwd': 3.68, 'icon': 3.65, 'meteo': 3.28, 'noaa': 3.73, 'sg': 3.28}, 'time': '2022-03-09T05:00:00+00:00', 'waveDirection': {'icon': 136.77, 'meteo': 130.1, 'noaa': 157.02, 'sg': 130.1}, 'windSpeed': {'icon': 1.7, 'noaa': 1.24, 'sg': 1.7}}, {'airTemperature': {'dwd': 7.2, 'noaa': 8.92, 'sg': 7.2}, 'swellDirection': {'dwd': 139.03, 'icon': 136.01, 'meteo': 90.32, 'noaa': 139.46, 'sg': 90.32}, 'swellHeight': {'dwd': 0.3, 'icon': 0.31, 'meteo': 0.19, 'noaa': 0.31, 'sg': 0.19}, 'swellPeriod': {'dwd': 3.65, 'icon': 3.64, 'meteo': 3.26, 'noaa': 3.71, 'sg': 3.26}, 'time': '2022-03-09T06:00:00+00:00', 'waveDirection': {'icon': 136.01, 'meteo': 127.45, 'noaa': 152.65, 'sg': 127.45}, 'windSpeed': {'icon': 1.9, 'noaa': 1.23, 'sg': 1.9}}, {'airTemperature': {'dwd': 7.35, 'noaa': 9.36, 'sg': 7.35}, 'swellDirection': {'dwd': 137.54, 'icon': 134.34, 'meteo': 90.94, 'noaa': 136.85, 'sg': 90.94}, 'swellHeight': {'dwd': 0.3, 'icon': 0.31, 'meteo': 0.19, 'noaa': 0.31, 'sg': 0.19}, 'swellPeriod': {'dwd': 3.62, 'icon': 3.64, 'meteo': 3.24, 'noaa': 3.71, 'sg': 3.24}, 'time': '2022-03-09T07:00:00+00:00', 'waveDirection': {'icon': 134.34, 'meteo': 125.38, 'noaa': 148.53, 'sg': 125.38}, 'windSpeed': {'icon': 2.11, 'noaa': 1.24, 'sg': 2.11}}, {'airTemperature': {'dwd': 8.17, 'noaa': 9.79, 
    'sg': 8.17}, 'swellDirection': {'dwd': 135.03, 'icon': 132.66, 'meteo': 91.57, 'noaa': 134.23, 'sg': 91.57}, 'swellHeight': {'dwd': 0.29, 'icon': 0.3, 'meteo': 0.19, 'noaa': 0.3, 'sg': 0.19}, 'swellPeriod': {'dwd': 3.6, 
    'icon': 3.65, 'meteo': 3.22, 'noaa': 3.7, 'sg': 3.22}, 'time': '2022-03-09T08:00:00+00:00', 'waveDirection': {'icon': 132.66, 'meteo': 123.3, 'noaa': 144.4, 'sg': 123.3}, 'windSpeed': {'icon': 2.32, 'noaa': 1.26, 'sg': 2.32}}, {'airTemperature': {'dwd': 9.66, 'noaa': 10.22, 'sg': 9.66}, 'swellDirection': {'dwd': 132.53, 'icon': 130.99, 'meteo': 92.19, 'noaa': 131.62, 'sg': 92.19}, 'swellHeight': {'dwd': 0.29, 'icon': 0.3, 'meteo': 0.19, 'noaa': 0.3, 'sg': 0.19}, 'swellPeriod': {'dwd': 3.62, 'icon': 3.65, 'meteo': 3.2, 'noaa': 3.7, 'sg': 3.2}, 'time': '2022-03-09T09:00:00+00:00', 'waveDirection': {'icon': 130.99, 'meteo': 121.23, 'noaa': 140.28, 'sg': 121.23}, 'windSpeed': {'icon': 2.53, 'noaa': 1.27, 'sg': 2.53}}, {'airTemperature': {'dwd': 10.21, 'noaa': 10.94, 'sg': 10.21}, 'swellDirection': {'dwd': 129.52, 'icon': 129.19, 'meteo': 93.1, 'noaa': 132.14, 'sg': 93.1}, 'swellHeight': {'dwd': 0.28, 'icon': 0.3, 'meteo': 0.19, 'noaa': 0.36, 'sg': 0.19}, 'swellPeriod': {'dwd': 3.65, 'icon': 3.66, 'meteo': 3.18, 'noaa': 3.87, 'sg': 3.18}, 'time': '2022-03-09T10:00:00+00:00', 'waveDirection': {'icon': 129.19, 'meteo': 120.48, 'noaa': 137.04, 'sg': 120.48}, 'windSpeed': {'icon': 2.07, 'noaa': 1.85, 'sg': 2.07}}, {'airTemperature': {'dwd': 10.16, 'noaa': 11.65, 'sg': 10.16}, 'swellDirection': {'dwd': 124.6, 'icon': 127.39, 'meteo': 94.01, 'noaa': 132.67, 'sg': 94.01}, 'swellHeight': {'dwd': 0.31, 'icon': 0.31, 'meteo': 0.19, 'noaa': 0.42, 'sg': 0.19}, 'swellPeriod': {'dwd': 3.48, 'icon': 3.68, 'meteo': 3.15, 'noaa': 4.04, 
    'sg': 3.15}, 'time': '2022-03-09T11:00:00+00:00', 'waveDirection': {'icon': 127.39, 'meteo': 119.73, 'noaa': 133.8, 'sg': 119.73}, 'windSpeed': {'icon': 1.62, 'noaa': 2.42, 'sg': 1.62}}, {'airTemperature': {'dwd': 10.31, 'noaa': 12.37, 'sg': 10.31}, 'swellDirection': {'dwd': 125.93, 'icon': 125.59, 'meteo': 94.92, 'noaa': 133.19, 'sg': 94.92}, 'swellHeight': {'dwd': 0.33, 'icon': 0.31, 'meteo': 0.19, 'noaa': 0.48, 'sg': 0.19}, 'swellPeriod': {'dwd': 3.42, 'icon': 3.69, 'meteo': 3.13, 'noaa': 4.21, 'sg': 3.13}, 'time': '2022-03-09T12:00:00+00:00', 'waveDirection': {'icon': 125.59, 'meteo': 118.98, 'noaa': 130.56, 'sg': 118.98}, 'windSpeed': {'icon': 1.16, 'noaa': 3.0, 'sg': 1.16}}, {'airTemperature': {'dwd': 10.62, 'noaa': 12.38, 'sg': 10.62}, 'swellDirection': {'dwd': 127.31, 'icon': 124.52, 'meteo': 95.88, 'noaa': 150.24, 'sg': 95.88}, 'swellHeight': {'dwd': 0.33, 'icon': 0.32, 'meteo': 0.19, 'noaa': 0.44, 'sg': 0.19}, 'swellPeriod': {'dwd': 3.54, 'icon': 3.72, 'meteo': 3.08, 'noaa': 4.23, 'sg': 3.08}, 'time': '2022-03-09T13:00:00+00:00', 'waveDirection': {'icon': 124.52, 'meteo': 118.82, 'noaa': 129.62, 'sg': 118.82}, 'windSpeed': {'icon': 1.33, 'noaa': 3.12, 'sg': 1.33}}, {'airTemperature': {'dwd': 11.23, 'noaa': 12.4, 'sg': 11.23}, 'swellDirection': {'dwd': 127.61, 'icon': 123.45, 'meteo': 96.84, 'noaa': 167.29, 'sg': 96.84}, 'swellHeight': {'dwd': 0.34, 'icon': 0.32, 'meteo': 0.18, 'noaa': 0.41, 'sg': 0.18}, 'swellPeriod': {'dwd': 3.64, 'icon': 3.76, 'meteo': 3.03, 'noaa': 4.26, 'sg': 3.03}, 'time': '2022-03-09T14:00:00+00:00', 'waveDirection': {'icon': 123.45, 'meteo': 118.65, 'noaa': 128.68, 'sg': 118.65}, 'windSpeed': {'icon': 1.5, 'noaa': 3.25, 'sg': 1.5}}, {'airTemperature': {'dwd': 11.24, 'noaa': 12.42, 'sg': 11.24}, 'swellDirection': {'dwd': 127.0, 'icon': 122.38, 'meteo': 97.8, 'noaa': 184.34, 'sg': 97.8}, 'swellHeight': {'dwd': 0.34, 'icon': 0.33, 'meteo': 0.18, 'noaa': 0.37, 'sg': 0.18}, 'swellPeriod': {'dwd': 3.73, 'icon': 3.79, 'meteo': 2.98, 'noaa': 4.28, 'sg': 2.98}, 'time': '2022-03-09T15:00:00+00:00', 'waveDirection': {'icon': 122.38, 'meteo': 118.49, 'noaa': 127.74, 'sg': 118.49}, 'windSpeed': {'icon': 1.67, 'noaa': 3.37, 'sg': 1.67}}, {'airTemperature': {'dwd': 11.23, 'noaa': 12.15, 'sg': 11.23}, 'swellDirection': {'dwd': 125.81, 'icon': 121.77, 'meteo': 99.5, 'noaa': 163.54, 'sg': 99.5}, 'swellHeight': {'dwd': 0.34, 'icon': 0.33, 'meteo': 0.18, 'noaa': 0.38, 'sg': 0.18}, 'swellPeriod': {'dwd': 3.82, 'icon': 3.82, 'meteo': 2.93, 'noaa': 4.37, 'sg': 2.93}, 'time': '2022-03-09T16:00:00+00:00', 'waveDirection': {'icon': 121.77, 'meteo': 117.42, 'noaa': 128.22, 'sg': 117.42}, 'windSpeed': {'icon': 1.5, 'noaa': 2.79, 'sg': 1.5}}, {'airTemperature': {'dwd': 10.61, 'noaa': 11.89, 'sg': 10.61}, 'swellDirection': {'dwd': 124.42, 'icon': 121.16, 'meteo': 101.21, 'noaa': 142.74, 'sg': 101.21}, 'swellHeight': {'dwd': 0.34, 'icon': 0.34, 'meteo': 0.17, 'noaa': 0.38, 'sg': 0.17}, 'swellPeriod': {'dwd': 3.89, 'icon': 3.86, 'meteo': 2.88, 'noaa': 4.45, 'sg': 2.88}, 'time': '2022-03-09T17:00:00+00:00', 'waveDirection': {'icon': 121.16, 'meteo': 116.34, 'noaa': 128.7, 'sg': 116.34}, 'windSpeed': {'icon': 1.32, 'noaa': 2.21, 'sg': 1.32}}, {'airTemperature': {'dwd': 9.44, 'noaa': 11.63, 'sg': 9.44}, 'swellDirection': {'dwd': 123.19, 'icon': 120.55, 'meteo': 102.91, 'noaa': 121.94, 'sg': 102.91}, 'swellHeight': {'dwd': 0.35, 'icon': 0.34, 'meteo': 0.17, 'noaa': 0.39, 'sg': 0.17}, 'swellPeriod': {'dwd': 3.95, 'icon': 3.89, 'meteo': 2.83, 'noaa': 4.54, 'sg': 2.83}, 'time': '2022-03-09T18:00:00+00:00', 'waveDirection': {'icon': 120.55, 'meteo': 115.27, 'noaa': 129.18, 'sg': 115.27}, 'windSpeed': {'icon': 1.15, 'noaa': 1.63, 'sg': 1.15}}, {'airTemperature': {'dwd': 8.59, 'noaa': 11.18, 'sg': 8.59}, 'swellDirection': {'dwd': 122.28, 'icon': 121.14, 'meteo': 93.33, 'noaa': 121.88, 'sg': 93.33}, 'swellHeight': {'dwd': 0.35, 'icon': 0.34, 'meteo': 0.17, 'noaa': 0.38, 'sg': 0.17}, 'swellPeriod': {'dwd': 3.99, 'icon': 3.9, 'meteo': 3.4, 'noaa': 4.46, 'sg': 3.4}, 'time': '2022-03-09T19:00:00+00:00', 'waveDirection': {'icon': 121.14, 'meteo': 118.37, 'noaa': 128.67, 'sg': 118.37}, 'windSpeed': {'icon': 1.09, 'noaa': 1.58, 'sg': 1.09}}, {'airTemperature': {'dwd': 7.75, 'noaa': 10.72, 'sg': 7.75}, 'swellDirection': {'dwd': 121.8, 'icon': 121.74, 'meteo': 83.76, 'noaa': 121.83, 'sg': 83.76}, 'swellHeight': {'dwd': 0.35, 'icon': 0.35, 'meteo': 0.16, 'noaa': 0.36, 'sg': 0.16}, 'swellPeriod': {'dwd': 4.01, 'icon': 3.92, 'meteo': 3.96, 'noaa': 4.38, 'sg': 3.96}, 'time': '2022-03-09T20:00:00+00:00', 'waveDirection': {'icon': 121.74, 'meteo': 121.47, 'noaa': 128.16, 'sg': 121.47}, 'windSpeed': {'icon': 1.02, 'noaa': 1.52, 'sg': 1.02}}, {'airTemperature': {'dwd': 7.13, 'noaa': 10.27, 'sg': 7.13}, 'swellDirection': {'dwd': 121.74, 'icon': 122.33, 'meteo': 74.18, 'noaa': 121.77, 'sg': 74.18}, 'swellHeight': {'dwd': 0.35, 'icon': 0.35, 'meteo': 0.16, 'noaa': 0.35, 'sg': 0.16}, 'swellPeriod': {'dwd': 4.02, 'icon': 3.93, 'meteo': 4.53, 'noaa': 4.3, 'sg': 4.53}, 'time': '2022-03-09T21:00:00+00:00', 'waveDirection': {'icon': 122.33, 'meteo': 
    124.57, 'noaa': 127.65, 'sg': 124.57}, 'windSpeed': {'icon': 0.96, 'noaa': 1.47, 'sg': 0.96}}, {'airTemperature': {'dwd': 6.76, 'noaa': 9.86, 'sg': 6.76}, 'swellDirection': {'dwd': 122.04, 'icon': 123.74, 'meteo': 73.96, 'noaa': 122.77, 
    'sg': 73.96}, 'swellHeight': {'dwd': 0.35, 'icon': 0.35, 'meteo': 0.17, 'noaa': 0.34, 'sg': 0.17}, 'swellPeriod': {'dwd': 4.03, 'icon': 3.93, 'meteo': 4.48, 'noaa': 4.23, 'sg': 4.48}, 'time': '2022-03-09T22:00:00+00:00', 'waveDirection': {'icon': 123.74, 'meteo': 133.46, 'noaa': 127.45, 'sg': 133.46}, 'windSpeed': {'icon': 1.11, 'noaa': 1.21, 'sg': 1.11}}, {'airTemperature': {'dwd': 6.6, 'noaa': 9.46, 'sg': 6.6}, 'swellDirection': {'dwd': 122.55, 'icon': 125.14, 'meteo': 73.73, 'noaa': 123.77, 'sg': 73.73}, 'swellHeight': {'dwd': 0.35, 'icon': 0.35, 'meteo': 0.17, 'noaa': 0.34, 'sg': 0.17}, 'swellPeriod': {'dwd': 4.02, 'icon': 3.93, 'meteo': 4.44, 'noaa': 4.16, 'sg': 4.44}, 'time': '2022-03-09T23:00:00+00:00', 'waveDirection': {'icon': 125.14, 'meteo': 142.34, 'noaa': 127.24, 'sg': 142.34}, 'windSpeed': {'icon': 1.26, 'noaa': 0.96, 'sg': 1.26}}], 'meta': {'cost': 1, 'dailyQuota': 10, 'end': '2022-03-09 23:00', 'lat': 41.3777, 'lng': 2.1923, 'params': ['airTemperature', 'windSpeed', 'waveDirection', 'swellPeriod', 'swellHeight', 'swellDirection'], 'requestCount': 2, 'start': '2022-03-07 23:00'}}
    """
     

    x=1
    data= []
    data2= []
    data3= []
    data4 = []
    f=str(start).split("T")
    dia=f[0].split("-")
    #print(int(dia[2]))
    
    wd = []

    for row in json_data['hours']:
        if(row['time'] >= str(start) and x%2!=0 ):
            #print(x)
            dyh=row['time']
            fecha=dyh.split("T")
            di=fecha[0].split("-")
            #print(int(di[2]))
            if(fecha[0] == f[0] ):
                fecha=dyh.split("T")
                fecha=fecha[1].split("+")
                time = fecha[0]

                aT = str(row['airTemperature']['noaa']) + " ºC"
            
                wS=str(row['windSpeed']['noaa']) + " m/s"

                wD=row['waveDirection']['noaa']

                sP=str(row['swellPeriod']['noaa']) + " s"

                sH=str(row['swellHeight']['noaa']) + " m"

                sD=row['swellDirection']['noaa'] 
                
                #d= [ time , aT ,  wS, wD ,sP , sH , sD ]
                d= [ time , aT ,  wS ]
                d2= [time, sP,sH]
                data.append(d[:])
                data2.append(d2[:])
                DIRS.append(sD)
                DIRV.append(wD)
            if(int(di[2]) > int(dia[2]) or int(di[1]) > int(dia[1]) ):
                
                fecha=dyh.split("T")
                fecha=fecha[1].split("+")
                time = fecha[0]

                aT = str(row['airTemperature']['noaa']) + " ºC"
            
                wS=str(row['windSpeed']['noaa']) + " m/s"

                wD=row['waveDirection']['noaa']

                sP=str(row['swellPeriod']['noaa']) + " s"

                sH=str(row['swellHeight']['noaa']) + " m"

                sD=row['swellDirection']['noaa'] 

                #d= [ time , aT ,  wS, wD ,sP , sH , sD ]
                d= [ time , aT ,  wS ]
                d2= [time, sP,sH]
                data3.append(d[:])
                data4.append(d2[:])
                DIRS2.append(sD)
                DIRV2.append(wD)
        x=x+1
        
    
    bot= telegram.Bot(BOT_TOKEN)
    
    TABLA1=tabulate( data , headers=["hora","Temperatura" , "Velocidad viento"]  ) 
    
    f=bot.sendMessage( CHAT, TABLA1,
                    reply_markup= InlineKeyboardMarkup([
                        [buttonI , buttonD ]
                    ])
    )
    
    MSN=f['message_id']
    
    print("-----MSN-----")
    print(MSN)
    TABLA2= tabulate( data2 , headers=["hora","Periodo oleaje" , "Altura de ola"]  ) 

    #print(DIRS)
    Graficas.grafica1(DIRS,0)
    DIRS=[]
    Graficas.grafica2(DIRV,0)
    DIRV=[]

    n=bot.sendPhoto(chat_id=CHAT,
        photo=open('WindDirection.png','rb'),
        reply_markup= InlineKeyboardMarkup([
                    [buttonGV , buttonGS]
         ])   
    )
    print("----message_id------")
    print(n['message_id'])
   

    print("Al dia siguiente")
    bot.sendMessage(CHAT,text="Al dia siguiente")
   

    TABLA3=tabulate( data3 , headers=["hora","Temperatura" , "Velocidad viento"]  ) 
    bot.sendMessage( CHAT, TABLA3 ,
        reply_markup= InlineKeyboardMarkup([
                        [buttonI2 , buttonNUEVO ]
                    ])
    )

    TABLA4=tabulate( data4 , headers=["hora","Periodo oleaje" , "Altura de ola"]  )

    Graficas.grafica1(DIRS2,1)
    DIRS2=[]
    Graficas.grafica2(DIRV2,1)
    DIRV2=[]


    bot.sendPhoto(chat_id=CHAT,
        photo=open('WindDirection2.png','rb'),
        reply_markup= InlineKeyboardMarkup([
                    [buttonGV2 , buttonGS2]
         ])   
    )
    
    print(len(data))
    #aux=0
    #evento.set()
    #while True:
        #aux=0
    





def cambioI(update):
    
    if(update!=0):
        global MSN,AUX
        MSN1=MSN
        print("---")
        
        print(MSN1)
        print("<<<<<<<<<<<<<<<<<<<<<<<")
        print(threading.get_ident())
        bot2=telegram.Bot(TOKEN)
        bot2.editMessageText(text=TABLA1,
                                        reply_markup= InlineKeyboardMarkup([
                            [buttonI , buttonD ]
                        ]),
                        chat_id=CHAT,
                        message_id=MSN1
        )


def cambioD(update):
    if(update!=0):
        global MSN,AUX
        print("---")
        MSN1=MSN
        print("<<<<<<<<<<<<<<<<<<<<<<<")
        print(threading.get_ident())
        print(MSN1)
        bot=telegram.Bot(TOKEN)
        bot.editMessageText(text=TABLA2,
                                        reply_markup= InlineKeyboardMarkup([
                            [buttonI , buttonD ]
                        ]),
                        chat_id=CHAT,
                        message_id=MSN1
        )


def cambioGS(update):
    if(update!=0):

        global MSN,AUX
        print(MSN)
        MSN2=MSN+1
        print("---HOLA2")
        print(MSN2)
        bot=telegram.Bot(TOKEN)
        bot.editMessageMedia(
                                        media=InputMediaPhoto(media = open('SwellDirection.png','rb')),
                                        reply_markup= InlineKeyboardMarkup([
                                        [buttonGV , buttonGS]
                                        ]),
                            chat_id=CHAT,
                            message_id=MSN2
        )


def cambioGV(update):

    if(update!=0):
        global MSN;AUX
        print(MSN)
        MSN2=MSN+1
        print("---HOLA2")
        print(MSN2)
        bot=telegram.Bot(TOKEN)
        bot.editMessageMedia(
                                        media=InputMediaPhoto(media = open('WindDirection.png','rb')),
                                        reply_markup= InlineKeyboardMarkup([
                                        [buttonGV , buttonGS]
                                        ]),
                            chat_id=CHAT,
                            message_id=MSN2
        )



def cambioI2(update):
    if(update!=0):
        global MSN,AUX
        print(MSN)
        MSN2=MSN+3
        print("---HOLA")
        print(MSN2)
        bot=telegram.Bot(TOKEN)
        bot.editMessageText(text=TABLA3,
                                        reply_markup= InlineKeyboardMarkup([
                                        [buttonI2 , buttonNUEVO ]
                                        ]),
                                        chat_id=CHAT,
                                        message_id=MSN2
        )


def cambioD2(update):
    if(update!=0):
        global MSN,AUX
        print(MSN)
        MSN2=MSN+3
        print("---HOLA")
        print(MSN2)
        bot=telegram.Bot(TOKEN)
        bot.editMessageText(text=TABLA4,
                            reply_markup= InlineKeyboardMarkup([
                                    [buttonI2 , buttonNUEVO ]
                            ]),
                            chat_id=CHAT,
                            message_id=MSN2
        )

def cambioGS2(update):
    if(update!=0):
        global MSN,AUX
        
        MSN4=MSN+4
        print("---HOLA5")
        print(MSN4)
        bot=telegram.Bot(TOKEN)
        bot.editMessageMedia(media=InputMediaPhoto(media = open('SwellDirection2.png','rb')),
                                    reply_markup= InlineKeyboardMarkup([
                                    [buttonGV2 , buttonGS2]
                                    ]),
                            chat_id=CHAT,
                            message_id=MSN4
    )


def cambioGV2(update):
    if(update!=0):
        global MSN,AUX
        
        MSN4=MSN+4
        print("---HOLA5")
        print(MSN4)
        bot=telegram.Bot(TOKEN)
        bot.editMessageMedia(media=InputMediaPhoto(media = open('WindDirection2.png','rb')),
                                        reply_markup= InlineKeyboardMarkup([
                                        [buttonGV2 , buttonGS2]
                                        ]),
                            chat_id=CHAT,
                            message_id=MSN4
        )
