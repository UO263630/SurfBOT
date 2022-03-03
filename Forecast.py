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


def Forecast(lat,lon,BOT_TOKEN,chat_id):

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
    json_data =  {'hours': [{'airTemperature': {'dwd': 12.19, 'noaa': 9.78, 'sg': 12.19}, 'swellDirection': {'dwd': 316.68, 'icon': 304.55, 'meteo': 316.68, 'noaa': 316.34, 'sg': 316.68}, 'swellHeight': {'dwd': 2.88, 'icon': 3.26, 'meteo': 2.51, 'noaa': 2.24, 'sg': 2.51}, 'swellPeriod': {'dwd': 14.01, 'icon': 13.4, 'meteo': 11.24, 'noaa': 13.81, 'sg': 11.24}, 'time': '2022-03-01T23:00:00+00:00', 'waveDirection': {'icon': 304.53, 'meteo': 305.22, 'noaa': 318.25, 'sg': 305.22}, 'windSpeed': {'icon': 3.74, 'noaa': 1.07, 'sg': 3.74}}, {'airTemperature': {'dwd': 12.07, 'noaa': 9.37, 'sg': 12.07}, 'swellDirection': {'dwd': 315.86, 'icon': 304.19, 'meteo': 317.03, 'noaa': 315.39, 'sg': 317.03}, 'swellHeight': {'dwd': 2.72, 'icon': 3.16, 'meteo': 2.46, 'noaa': 2.23, 'sg': 2.46}, 'swellPeriod': {'dwd': 13.56, 'icon': 13.16, 'meteo': 11.14, 'noaa': 13.75, 'sg': 11.14}, 'time': '2022-03-02T00:00:00+00:00', 'waveDirection': {'icon': 304.17, 'meteo': 305.27, 'noaa': 318.97, 'sg': 305.27}, 'windSpeed': {'icon': 5.08, 'noaa': 1.21, 'sg': 5.08}}, {'airTemperature': {'dwd': 11.36, 'noaa': 8.79, 'sg': 11.36}, 'swellDirection': {'dwd': 315.54, 'icon': 303.92, 'meteo': 318.55, 'noaa': 314.52, 'sg': 318.55}, 'swellHeight': {'dwd': 2.66, 'icon': 3.13, 'meteo': 2.43, 'noaa': 2.21, 'sg': 2.43}, 'swellPeriod': {'dwd': 13.41, 'icon': 13.02, 'meteo': 11.28, 'noaa': 13.68, 'sg': 11.28}, 'time': '2022-03-02T01:00:00+00:00', 'waveDirection': {'icon': 303.9, 'meteo': 303.94, 'noaa': 319.9, 'sg': 303.94}, 'windSpeed': {'icon': 4.66, 'noaa': 1.49, 'sg': 4.66}}, {'airTemperature': {'dwd': 10.15, 'noaa': 8.21, 'sg': 10.15}, 'swellDirection': {'dwd': 315.49, 'icon': 303.66, 'meteo': 320.06, 'noaa': 313.64, 'sg': 320.06}, 'swellHeight': {'dwd': 2.64, 'icon': 3.09, 'meteo': 2.41, 'noaa': 2.18, 
    'sg': 2.41}, 'swellPeriod': {'dwd': 13.32, 'icon': 12.88, 'meteo': 11.42, 'noaa': 13.61, 'sg': 11.42}, 'time': '2022-03-02T02:00:00+00:00', 'waveDirection': {'icon': 303.64, 'meteo': 302.61, 'noaa': 320.84, 'sg': 302.61}, 'windSpeed': {'icon': 4.24, 'noaa': 1.77, 'sg': 4.24}}, {'airTemperature': {'dwd': 9.45, 'noaa': 7.63, 'sg': 9.45}, 'swellDirection': {'dwd': 315.57, 'icon': 303.39, 'meteo': 321.58, 'noaa': 312.77, 'sg': 321.58}, 'swellHeight': {'dwd': 2.62, 'icon': 3.06, 'meteo': 2.38, 'noaa': 2.16, 'sg': 2.38}, 'swellPeriod': {'dwd': 13.26, 'icon': 12.74, 'meteo': 11.56, 'noaa': 13.54, 'sg': 11.56}, 'time': '2022-03-02T03:00:00+00:00', 'waveDirection': {'icon': 303.37, 'meteo': 301.28, 'noaa': 321.77, 'sg': 301.28}, 'windSpeed': {'icon': 3.82, 'noaa': 2.05, 'sg': 3.82}}, {'airTemperature': {'dwd': 10.43, 'noaa': 8.31, 'sg': 10.43}, 'swellDirection': {'dwd': 315.59, 'icon': 303.38, 'meteo': 321.2, 'noaa': 316.13, 'sg': 321.2}, 'swellHeight': {'dwd': 2.59, 'icon': 3.03, 'meteo': 2.37, 'noaa': 2.04, 'sg': 2.37}, 'swellPeriod': {'dwd': 13.16, 'icon': 12.64, 'meteo': 11.51, 'noaa': 13.46, 'sg': 11.51}, 'time': '2022-03-02T04:00:00+00:00', 'waveDirection': {'icon': 302.52, 'meteo': 300.79, 'noaa': 322.48, 'sg': 300.79}, 'windSpeed': {'icon': 5.22, 'noaa': 2.34, 'sg': 5.22}}, {'airTemperature': {'dwd': 10.76, 'noaa': 8.99, 'sg': 10.76}, 'swellDirection': {'dwd': 315.45, 'icon': 303.38, 'meteo': 320.83, 'noaa': 319.49, 'sg': 320.83}, 'swellHeight': {'dwd': 2.57, 'icon': 2.99, 'meteo': 2.36, 'noaa': 1.93, 'sg': 2.36}, 'swellPeriod': {'dwd': 12.99, 'icon': 12.53, 'meteo': 
    11.47, 'noaa': 13.39, 'sg': 11.47}, 'time': '2022-03-02T05:00:00+00:00', 'waveDirection': {'icon': 301.68, 'meteo': 300.29, 'noaa': 323.2, 'sg': 300.29}, 'windSpeed': {'icon': 6.62, 'noaa': 2.64, 'sg': 6.62}}, {'airTemperature': {'dwd': 11.3, 'noaa': 9.67, 'sg': 11.3}, 'swellDirection': {'dwd': 315.05, 'icon': 303.37, 'meteo': 320.45, 'noaa': 322.85, 'sg': 320.45}, 'swellHeight': {'dwd': 2.56, 'icon': 2.96, 'meteo': 2.35, 'noaa': 1.81, 'sg': 2.35}, 'swellPeriod': {'dwd': 12.7, 'icon': 12.43, 'meteo': 11.42, 'noaa': 13.31, 'sg': 11.42}, 'time': '2022-03-02T06:00:00+00:00', 'waveDirection': {'icon': 300.83, 'meteo': 299.8, 'noaa': 323.91, 'sg': 299.8}, 'windSpeed': {'icon': 8.02, 'noaa': 2.93, 'sg': 8.02}}, {'airTemperature': {'dwd': 11.24, 'noaa': 9.86, 'sg': 11.24}, 'swellDirection': {'dwd': 314.26, 'icon': 304.84, 'meteo': 320.67, 'noaa': 322.93, 'sg': 320.67}, 'swellHeight': {'dwd': 2.61, 'icon': 2.82, 'meteo': 2.29, 'noaa': 1.78, 'sg': 2.29}, 'swellPeriod': {'dwd': 12.19, 'icon': 12.68, 'meteo': 11.34, 'noaa': 13.22, 'sg': 11.34}, 'time': '2022-03-02T07:00:00+00:00', 'waveDirection': {'icon': 299.31, 'meteo': 299.57, 'noaa': 322.63, 'sg': 299.57}, 'windSpeed': {'icon': 9.36, 'noaa': 3.03, 'sg': 9.36}}, {'airTemperature': {'dwd': 11.74, 'noaa': 10.05, 'sg': 11.74}, 'swellDirection': {'dwd': 315.14, 'icon': 306.3, 'meteo': 320.9, 'noaa': 323.0, 'sg': 320.9}, 'swellHeight': {'dwd': 2.59, 'icon': 2.67, 'meteo': 2.23, 'noaa': 1.74, 'sg': 2.23}, 'swellPeriod': {'dwd': 12.14, 'icon': 12.93, 'meteo': 11.27, 'noaa': 13.12, 'sg': 11.27}, 'time': '2022-03-02T08:00:00+00:00', 'waveDirection': {'icon': 297.8, 'meteo': 299.33, 'noaa': 321.34, 'sg': 299.33}, 'windSpeed': {'icon': 10.71, 'noaa': 3.14, 'sg': 10.71}}, {'airTemperature': {'dwd': 12.03, 'noaa': 10.24, 'sg': 12.03}, 'swellDirection': {'dwd': 315.08, 'icon': 307.77, 'meteo': 321.12, 'noaa': 323.08, 'sg': 321.12}, 'swellHeight': {'dwd': 2.6, 'icon': 2.53, 'meteo': 2.17, 'noaa': 1.71, 'sg': 2.17}, 'swellPeriod': {'dwd': 11.87, 'icon': 13.18, 'meteo': 11.19, 'noaa': 13.03, 'sg': 11.19}, 'time': '2022-03-02T09:00:00+00:00', 'waveDirection': {'icon': 296.28, 'meteo': 299.1, 'noaa': 320.06, 'sg': 299.1}, 'windSpeed': {'icon': 12.05, 'noaa': 3.24, 'sg': 12.05}}, {'airTemperature': {'dwd': 12.38, 'noaa': 11.06, 'sg': 12.38}, 'swellDirection': {'dwd': 314.7, 'icon': 305.5, 'meteo': 321.08, 'noaa': 323.24, 'sg': 321.08}, 'swellHeight': {'dwd': 2.6, 'icon': 2.65, 'meteo': 2.14, 'noaa': 1.69, 'sg': 2.14}, 'swellPeriod': {'dwd': 11.55, 'icon': 12.5, 'meteo': 10.98, 'noaa': 12.94, 'sg': 10.98}, 'time': '2022-03-02T10:00:00+00:00', 'waveDirection': {'icon': 297.21, 'meteo': 
    299.13, 'noaa': 320.57, 'sg': 299.13}, 'windSpeed': {'icon': 10.64, 'noaa': 3.29, 'sg': 10.64}}, {'airTemperature': {'dwd': 12.77, 'noaa': 11.88, 'sg': 12.77}, 'swellDirection': {'dwd': 313.08, 'icon': 303.23, 'meteo': 321.05, 'noaa': 323.4, 'sg': 321.05}, 'swellHeight': {'dwd': 2.63, 'icon': 2.78, 'meteo': 2.11, 'noaa': 1.66, 'sg': 2.11}, 'swellPeriod': {'dwd': 11.02, 'icon': 11.81, 'meteo': 10.76, 'noaa': 12.85, 'sg': 10.76}, 'time': '2022-03-02T11:00:00+00:00', 'waveDirection': {'icon': 298.13, 'meteo': 299.16, 'noaa': 321.09, 'sg': 299.16}, 'windSpeed': {'icon': 9.22, 'noaa': 3.35, 'sg': 9.22}}, {'airTemperature': {'dwd': 13.43, 'noaa': 12.69, 'sg': 13.43}, 'swellDirection': {'dwd': 312.68, 'icon': 300.96, 'meteo': 321.01, 'noaa': 323.56, 'sg': 321.01}, 'swellHeight': {'dwd': 2.56, 'icon': 2.9, 'meteo': 2.08, 'noaa': 1.64, 'sg': 2.08}, 'swellPeriod': {'dwd': 10.87, 'icon': 11.13, 'meteo': 10.55, 'noaa': 12.76, 'sg': 10.55}, 'time': '2022-03-02T12:00:00+00:00', 'waveDirection': {'icon': 299.06, 'meteo': 299.19, 'noaa': 321.6, 'sg': 299.19}, 'windSpeed': {'icon': 7.81, 'noaa': 3.4, 'sg': 7.81}}, {'airTemperature': {'dwd': 13.4, 'noaa': 12.98, 'sg': 13.4}, 'swellDirection': {'dwd': 313.25, 'icon': 301.25, 'meteo': 321.74, 'noaa': 315.59, 'sg': 321.74}, 'swellHeight': {'dwd': 2.44, 'icon': 2.82, 'meteo': 1.99, 'noaa': 1.53, 'sg': 1.99}, 'swellPeriod': {'dwd': 10.98, 'icon': 11.07, 'meteo': 10.4, 'noaa': 12.48, 'sg': 10.4}, 'time': '2022-03-02T13:00:00+00:00', 'waveDirection': {'icon': 299.99, 'meteo': 299.19, 'noaa': 321.83, 'sg': 299.19}, 'windSpeed': {'icon': 7.03, 'noaa': 2.89, 'sg': 7.03}}, {'airTemperature': {'dwd': 13.05, 'noaa': 13.26, 'sg': 13.05}, 'swellDirection': {'dwd': 313.91, 'icon': 301.54, 'meteo': 322.48, 'noaa': 307.62, 'sg': 322.48}, 'swellHeight': {'dwd': 2.33, 'icon': 2.75, 'meteo': 1.91, 'noaa': 1.42, 'sg': 1.91}, 'swellPeriod': {'dwd': 11.1, 'icon': 11.01, 'meteo': 10.24, 'noaa': 12.2, 'sg': 10.24}, 'time': '2022-03-02T14:00:00+00:00', 'waveDirection': {'icon': 300.92, 'meteo': 299.18, 'noaa': 322.07, 'sg': 299.18}, 'windSpeed': {'icon': 6.25, 'noaa': 2.38, 'sg': 6.25}}, {'airTemperature': {'dwd': 12.82, 'noaa': 13.54, 'sg': 12.82}, 'swellDirection': {'dwd': 314.37, 'icon': 301.83, 'meteo': 323.21, 'noaa': 299.65, 'sg': 323.21}, 'swellHeight': {'dwd': 2.24, 'icon': 2.67, 'meteo': 1.82, 'noaa': 1.31, 'sg': 1.82}, 'swellPeriod': {'dwd': 11.14, 'icon': 10.95, 'meteo': 10.09, 'noaa': 11.92, 'sg': 10.09}, 'time': '2022-03-02T15:00:00+00:00', 'waveDirection': {'icon': 301.85, 'meteo': 299.18, 'noaa': 322.3, 'sg': 299.18}, 'windSpeed': {'icon': 5.47, 'noaa': 1.87, 'sg': 5.47}}, {'airTemperature': {'dwd': 12.57, 'noaa': 12.45, 'sg': 12.57}, 'swellDirection': {'dwd': 314.62, 'icon': 302.01, 'meteo': 309.53, 'noaa': 307.63, 'sg': 309.53}, 'swellHeight': {'dwd': 2.17, 'icon': 2.6, 'meteo': 1.85, 'noaa': 1.35, 'sg': 1.85}, 'swellPeriod': {'dwd': 11.07, 'icon': 10.87, 'meteo': 9.28, 'noaa': 12.01, 'sg': 9.28}, 'time': '2022-03-02T16:00:00+00:00', 'waveDirection': {'icon': 302.03, 'meteo': 298.88, 'noaa': 321.09, 'sg': 298.88}, 'windSpeed': {'icon': 3.98, 'noaa': 1.66, 'sg': 3.98}}, {'airTemperature': {'dwd': 12.26, 'noaa': 11.36, 'sg': 12.26}, 'swellDirection': {'dwd': 314.66, 'icon': 302.2, 'meteo': 295.86, 'noaa': 315.61, 'sg': 295.86}, 'swellHeight': {'dwd': 2.12, 'icon': 2.54, 'meteo': 1.88, 'noaa': 1.4, 'sg': 1.88}, 'swellPeriod': {'dwd': 10.94, 'icon': 10.8, 'meteo': 8.48, 'noaa': 12.11, 'sg': 8.48}, 'time': '2022-03-02T17:00:00+00:00', 'waveDirection': {'icon': 302.2, 'meteo': 298.59, 'noaa': 319.87, 'sg': 298.59}, 'windSpeed': {'icon': 2.5, 'noaa': 1.44, 'sg': 2.5}}, {'airTemperature': {'dwd': 12.02, 'noaa': 10.27, 'sg': 12.02}, 'swellDirection': {'dwd': 314.46, 'icon': 302.38, 'meteo': 282.18, 'noaa': 323.59, 'sg': 282.18}, 'swellHeight': {'dwd': 2.07, 'icon': 2.47, 'meteo': 1.91, 'noaa': 1.44, 'sg': 1.91}, 'swellPeriod': {'dwd': 10.8, 'icon': 10.72, 'meteo': 7.67, 'noaa': 12.2, 'sg': 7.67}, 'time': '2022-03-02T18:00:00+00:00', 'waveDirection': {'icon': 302.38, 'meteo': 298.29, 'noaa': 318.66, 'sg': 298.29}, 'windSpeed': {'icon': 1.01, 'noaa': 1.23, 'sg': 1.01}}, {'airTemperature': {'dwd': 11.78, 'noaa': 10.18, 'sg': 11.78}, 'swellDirection': {'dwd': 
    314.03, 'icon': 302.17, 'meteo': 281.73, 'noaa': 308.65, 'sg': 281.73}, 'swellHeight': {'dwd': 2.02, 'icon': 2.4, 'meteo': 1.85, 'noaa': 1.12, 'sg': 1.85}, 'swellPeriod': {'dwd': 10.68, 'icon': 10.63, 'meteo': 7.61, 'noaa': 12.15, 'sg': 7.61}, 'time': '2022-03-02T19:00:00+00:00', 'waveDirection': {'icon': 302.17, 'meteo': 298.09, 'noaa': 318.87, 'sg': 
    298.09}, 'windSpeed': {'icon': 1.95, 'noaa': 1.31, 'sg': 1.95}}, {'airTemperature': {'dwd': 11.8, 'noaa': 10.1, 'sg': 11.8}, 'swellDirection': {'dwd': 313.52, 'icon': 301.96, 'meteo': 281.28, 'noaa': 293.7, 'sg': 281.28}, 'swellHeight': {'dwd': 1.97, 'icon': 2.34, 'meteo': 1.79, 'noaa': 0.79, 'sg': 1.79}, 'swellPeriod': {'dwd': 10.58, 'icon': 10.55, 'meteo': 7.54, 'noaa': 12.1, 'sg': 7.54}, 'time': '2022-03-02T20:00:00+00:00', 'waveDirection': {'icon': 301.96, 'meteo': 297.89, 'noaa': 319.07, 'sg': 297.89}, 'windSpeed': {'icon': 2.88, 'noaa': 1.38, 'sg': 2.88}}, {'airTemperature': {'dwd': 11.96, 'noaa': 10.02, 'sg': 11.96}, 'swellDirection': {'dwd': 313.07, 'icon': 301.75, 'meteo': 280.83, 'noaa': 278.76, 'sg': 280.83}, 'swellHeight': {'dwd': 1.91, 'icon': 2.27, 'meteo': 1.73, 'noaa': 0.47, 'sg': 1.73}, 'swellPeriod': {'dwd': 10.48, 'icon': 10.46, 'meteo': 7.48, 'noaa': 12.05, 'sg': 7.48}, 'time': '2022-03-02T21:00:00+00:00', 'waveDirection': {'icon': 301.75, 'meteo': 297.69, 'noaa': 319.28, 'sg': 297.69}, 'windSpeed': {'icon': 3.82, 'noaa': 1.46, 'sg': 3.82}}, {'airTemperature': {'dwd': 12.1, 'noaa': 10.1, 'sg': 12.1}, 'swellDirection': {'dwd': 312.62, 'icon': 301.12, 'meteo': 282.92, 'noaa': 290.13, 'sg': 282.92}, 'swellHeight': {'dwd': 1.85, 'icon': 2.22, 'meteo': 1.65, 'noaa': 0.83, 'sg': 1.65}, 'swellPeriod': {'dwd': 10.39, 'icon': 10.36, 'meteo': 7.58, 'noaa': 11.93, 'sg': 7.58}, 'time': '2022-03-02T22:00:00+00:00', 'waveDirection': {'icon': 301.12, 'meteo': 297.16, 'noaa': 319.51, 'sg': 297.16}, 'windSpeed': {'icon': 3.41, 'noaa': 1.52, 'sg': 3.41}}, {'airTemperature': {'dwd': 11.87, 'noaa': 10.19, 'sg': 11.87}, 'swellDirection': {'dwd': 312.06, 'icon': 300.48, 'meteo': 285.0, 'noaa': 301.5, 'sg': 285.0}, 'swellHeight': {'dwd': 1.79, 'icon': 2.16, 'meteo': 1.57, 'noaa': 1.2, 'sg': 1.57}, 'swellPeriod': {'dwd': 10.3, 'icon': 10.25, 'meteo': 7.67, 'noaa': 11.8, 'sg': 7.67}, 'time': '2022-03-02T23:00:00+00:00', 'waveDirection': {'icon': 300.48, 'meteo': 296.63, 'noaa': 319.73, 'sg': 296.63}, 'windSpeed': {'icon': 2.99, 'noaa': 1.57, 'sg': 2.99}}, {'airTemperature': {'dwd': 11.63, 'noaa': 10.27, 'sg': 11.63}, 'swellDirection': {'dwd': 311.37, 'icon': 299.85, 'meteo': 287.09, 'noaa': 312.87, 'sg': 287.09}, 'swellHeight': {'dwd': 1.74, 'icon': 2.11, 'meteo': 1.49, 'noaa': 1.56, 'sg': 1.49}, 'swellPeriod': {'dwd': 10.23, 'icon': 10.15, 'meteo': 7.77, 'noaa': 11.68, 'sg': 7.77}, 'time': '2022-03-03T00:00:00+00:00', 'waveDirection': {'icon': 299.85, 'meteo': 296.1, 'noaa': 319.96, 'sg': 296.1}, 'windSpeed': {'icon': 2.58, 'noaa': 1.63, 'sg': 2.58}}, {'airTemperature': {'dwd': 11.87, 'noaa': 10.2, 'sg': 11.87}, 'swellDirection': {'dwd': 310.63, 'icon': 298.97, 'meteo': 287.41, 'noaa': 312.11, 'sg': 287.41}, 'swellHeight': {'dwd': 1.69, 'icon': 2.07, 'meteo': 1.35, 'noaa': 1.52, 'sg': 
    1.35}, 'swellPeriod': {'dwd': 10.19, 'icon': 10.09, 'meteo': 8.31, 'noaa': 11.61, 'sg': 8.31}, 'time': '2022-03-03T01:00:00+00:00', 'waveDirection': {'icon': 298.97, 'meteo': 294.98, 'noaa': 319.54, 'sg': 294.98}, 'windSpeed': {'icon': 2.33, 'noaa': 1.46, 'sg': 2.33}}, {'airTemperature': {'dwd': 11.84, 'noaa': 10.12, 'sg': 11.84}, 'swellDirection': {'dwd': 309.96, 'icon': 298.1, 'meteo': 287.72, 'noaa': 311.34, 'sg': 287.72}, 'swellHeight': {'dwd': 1.64, 'icon': 2.02, 'meteo': 1.21, 'noaa': 1.49, 'sg': 1.21}, 'swellPeriod': {'dwd': 10.17, 'icon': 10.02, 'meteo': 8.84, 'noaa': 11.54, 'sg': 8.84}, 'time': '2022-03-03T02:00:00+00:00', 'waveDirection': {'icon': 298.1, 'meteo': 293.86, 'noaa': 319.13, 'sg': 293.86}, 'windSpeed': {'icon': 2.08, 'noaa': 1.29, 'sg': 2.08}}, {'airTemperature': {'dwd': 11.84, 'noaa': 10.05, 'sg': 11.84}, 'swellDirection': {'dwd': 309.41, 'icon': 297.22, 'meteo': 288.04, 'noaa': 310.58, 'sg': 288.04}, 'swellHeight': {'dwd': 1.58, 'icon': 1.98, 'meteo': 1.07, 'noaa': 1.45, 'sg': 1.07}, 'swellPeriod': {'dwd': 10.18, 'icon': 9.96, 'meteo': 9.38, 'noaa': 11.47, 'sg': 9.38}, 'time': '2022-03-03T03:00:00+00:00', 'waveDirection': {'icon': 297.22, 'meteo': 292.74, 'noaa': 318.71, 'sg': 292.74}, 'windSpeed': {'icon': 1.83, 'noaa': 1.12, 'sg': 1.83}}, {'airTemperature': {'dwd': 12.06, 'noaa': 9.73, 'sg': 12.06}, 'swellDirection': {'dwd': 310.0, 'icon': 297.16, 'meteo': 286.8, 'noaa': 306.42, 'sg': 286.8}, 'swellHeight': {'dwd': 1.48, 'icon': 1.88, 'meteo': 1.09, 'noaa': 1.03, 'sg': 1.09}, 'swellPeriod': {'dwd': 10.57, 'icon': 10.27, 'meteo': 9.36, 'noaa': 12.86, 'sg': 9.36}, 'time': '2022-03-03T04:00:00+00:00', 'waveDirection': {'icon': 295.62, 'meteo': 292.55, 'noaa': 318.24, 'sg': 292.55}, 'windSpeed': {'icon': 4.63, 'noaa': 
    2.35, 'sg': 4.63}}, {'airTemperature': {'dwd': 12.0, 'noaa': 9.41, 'sg': 12.0}, 'swellDirection': {'dwd': 309.5, 'icon': 297.1, 'meteo': 285.57, 'noaa': 302.26, 'sg': 285.57}, 'swellHeight': {'dwd': 1.44, 'icon': 1.79, 'meteo': 1.12, 'noaa': 0.62, 'sg': 1.12}, 'swellPeriod': {'dwd': 10.66, 'icon': 10.58, 'meteo': 9.35, 'noaa': 14.25, 'sg': 9.35}, 'time': '2022-03-03T05:00:00+00:00', 'waveDirection': {'icon': 294.01, 'meteo': 292.35, 'noaa': 317.78, 'sg': 292.35}, 'windSpeed': {'icon': 7.43, 'noaa': 3.59, 'sg': 7.43}}, {'airTemperature': {'dwd': 11.32, 'noaa': 9.09, 'sg': 11.32}, 'swellDirection': {'dwd': 309.83, 'icon': 297.04, 'meteo': 284.33, 'noaa': 298.1, 'sg': 284.33}, 'swellHeight': {'dwd': 1.44, 'icon': 1.69, 'meteo': 1.14, 'noaa': 0.2, 'sg': 1.14}, 'swellPeriod': {'dwd': 10.5, 'icon': 10.89, 'meteo': 9.33, 'noaa': 15.64, 'sg': 9.33}, 'time': '2022-03-03T06:00:00+00:00', 'waveDirection': {'icon': 292.41, 'meteo': 292.16, 'noaa': 317.31, 'sg': 292.16}, 'windSpeed': {'icon': 10.23, 'noaa': 4.82, 'sg': 10.23}}, {'airTemperature': {'dwd': 11.1, 'noaa': 8.49, 'sg': 11.1}, 'swellDirection': {'dwd': 308.56, 'icon': 295.27, 'meteo': 285.21, 'noaa': 303.73, 'sg': 285.21}, 'swellHeight': {'dwd': 1.64, 'icon': 1.74, 'meteo': 1.38, 'noaa': 0.16, 'sg': 1.38}, 'swellPeriod': {'dwd': 9.3, 'icon': 10.77, 'meteo': 8.88, 'noaa': 18.12, 'sg': 8.88}, 'time': '2022-03-03T07:00:00+00:00', 'waveDirection': {'icon': 292.64, 'meteo': 293.23, 'noaa': 316.57, 'sg': 293.23}, 'windSpeed': {'icon': 9.88, 'noaa': 3.95, 'sg': 9.88}}, {'airTemperature': {'dwd': 10.7, 'noaa': 7.9, 'sg': 10.7}, 'swellDirection': {'dwd': 308.05, 'icon': 293.5, 'meteo': 286.1, 'noaa': 309.35, 'sg': 286.1}, 'swellHeight': {'dwd': 1.62, 'icon': 1.78, 'meteo': 1.63, 'noaa': 0.11, 'sg': 1.63}, 'swellPeriod': {'dwd': 9.32, 'icon': 10.64, 'meteo': 8.43, 'noaa': 20.6, 'sg': 8.43}, 'time': '2022-03-03T08:00:00+00:00', 'waveDirection': {'icon': 292.86, 'meteo': 294.31, 'noaa': 315.83, 'sg': 294.31}, 'windSpeed': {'icon': 9.52, 'noaa': 3.08, 'sg': 9.52}}, {'airTemperature': {'dwd': 10.5, 'noaa': 7.3, 'sg': 10.5}, 'swellDirection': {'dwd': 306.45, 'icon': 291.73, 'meteo': 286.98, 'noaa': 314.98, 'sg': 286.98}, 'swellHeight': {'dwd': 1.63, 'icon': 1.83, 'meteo': 1.87, 'noaa': 0.07, 'sg': 1.87}, 'swellPeriod': {'dwd': 9.33, 'icon': 10.52, 'meteo': 7.98, 'noaa': 23.08, 'sg': 7.98}, 'time': '2022-03-03T09:00:00+00:00', 'waveDirection': {'icon': 293.09, 'meteo': 295.38, 'noaa': 315.09, 'sg': 295.38}, 'windSpeed': {'icon': 9.17, 'noaa': 2.21, 'sg': 9.17}}, {'airTemperature': {'dwd': 10.39, 'noaa': 7.76, 'sg': 10.39}, 'swellDirection': {'dwd': 306.4, 'icon': 292.31, 'meteo': 287.04, 'noaa': 314.2, 'sg': 287.04}, 'swellHeight': {'dwd': 1.68, 'icon': 1.94, 'meteo': 1.96, 'noaa': 0.12, 'sg': 1.96}, 'swellPeriod': {'dwd': 9.18, 'icon': 10.43, 'meteo': 8.29, 'noaa': 22.55, 'sg': 8.29}, 'time': '2022-03-03T10:00:00+00:00', 'waveDirection': {'icon': 294.49, 'meteo': 296.57, 'noaa': 308.37, 'sg': 296.57}, 'windSpeed': {'icon': 8.72, 'noaa': 3.03, 'sg': 8.72}}, {'airTemperature': {'dwd': 10.46, 'noaa': 8.22, 'sg': 10.46}, 'swellDirection': {'dwd': 307.45, 'icon': 292.88, 'meteo': 287.11, 'noaa': 313.43, 'sg': 287.11}, 'swellHeight': {'dwd': 1.76, 'icon': 2.05, 'meteo': 2.05, 'noaa': 0.18, 'sg': 2.05}, 'swellPeriod': {'dwd': 9.07, 'icon': 10.33, 'meteo': 8.6, 'noaa': 22.02, 'sg': 8.6}, 'time': '2022-03-03T11:00:00+00:00', 'waveDirection': {'icon': 295.9, 'meteo': 297.77, 'noaa': 301.65, 'sg': 297.77}, 'windSpeed': {'icon': 8.27, 'noaa': 3.85, 'sg': 
    8.27}}, {'airTemperature': {'dwd': 10.38, 'noaa': 8.68, 'sg': 10.38}, 'swellDirection': {'dwd': 308.36, 'icon': 293.46, 'meteo': 287.17, 'noaa': 312.65, 'sg': 287.17}, 'swellHeight': {'dwd': 1.84, 'icon': 2.16, 'meteo': 2.14, 'noaa': 0.23, 'sg': 2.14}, 'swellPeriod': {'dwd': 9.12, 'icon': 10.24, 'meteo': 8.91, 'noaa': 21.49, 'sg': 8.91}, 'time': '2022-03-03T12:00:00+00:00', 'waveDirection': {'icon': 297.3, 'meteo': 298.96, 'noaa': 294.93, 'sg': 298.96}, 'windSpeed': {'icon': 7.82, 'noaa': 4.67, 'sg': 7.82}}, {'airTemperature': {'dwd': 11.28, 'noaa': 8.21, 'sg': 11.28}, 'swellDirection': {'dwd': 308.65, 'icon': 294.04, 'meteo': 287.46, 'noaa': 312.82, 'sg': 287.46}, 'swellHeight': {'dwd': 1.86, 'icon': 2.23, 'meteo': 2.23, 'noaa': 0.34, 'sg': 2.23}, 'swellPeriod': {'dwd': 9.67, 'icon': 10.6, 'meteo': 9.09, 'noaa': 21.01, 'sg': 9.09}, 'time': '2022-03-03T13:00:00+00:00', 'waveDirection': {'icon': 297.71, 'meteo': 299.51, 'noaa': 296.54, 'sg': 299.51}, 'windSpeed': {'icon': 7.97, 'noaa': 5.0, 'sg': 7.97}}, {'airTemperature': {'dwd': 10.81, 'noaa': 7.74, 'sg': 10.81}, 'swellDirection': {'dwd': 309.63, 'icon': 294.62, 'meteo': 287.76, 'noaa': 313.0, 'sg': 287.76}, 'swellHeight': {'dwd': 1.95, 'icon': 2.3, 'meteo': 2.31, 'noaa': 0.46, 'sg': 2.31}, 'swellPeriod': {'dwd': 9.84, 'icon': 10.96, 'meteo': 9.28, 'noaa': 20.52, 'sg': 9.28}, 'time': '2022-03-03T14:00:00+00:00', 'waveDirection': {'icon': 298.13, 'meteo': 300.07, 'noaa': 298.16, 'sg': 300.07}, 'windSpeed': {'icon': 8.11, 'noaa': 5.34, 'sg': 8.11}}, {'airTemperature': {'dwd': 10.95, 'noaa': 7.26, 'sg': 10.95}, 'swellDirection': {'dwd': 309.83, 'icon': 295.2, 'meteo': 288.05, 'noaa': 313.17, 'sg': 288.05}, 'swellHeight': {'dwd': 2.02, 'icon': 2.37, 'meteo': 2.4, 'noaa': 0.57, 'sg': 2.4}, 'swellPeriod': {'dwd': 10.17, 'icon': 11.32, 'meteo': 9.46, 'noaa': 20.04, 'sg': 9.46}, 'time': '2022-03-03T15:00:00+00:00', 'waveDirection': {'icon': 298.54, 'meteo': 300.62, 'noaa': 299.77, 'sg': 300.62}, 'windSpeed': {'icon': 8.26, 'noaa': 5.67, 'sg': 8.26}}, {'airTemperature': {'dwd': 11.09, 'noaa': 7.32, 'sg': 11.09}, 'swellDirection': {'dwd': 310.09, 'icon': 295.92, 'meteo': 287.91, 'noaa': 314.35, 'sg': 287.91}, 'swellHeight': {'dwd': 2.08, 'icon': 2.49, 'meteo': 2.46, 'noaa': 0.7, 'sg': 2.46}, 'swellPeriod': {'dwd': 10.56, 'icon': 11.51, 'meteo': 9.48, 'noaa': 19.58, 'sg': 9.48}, 'time': '2022-03-03T16:00:00+00:00', 'waveDirection': {'icon': 298.68, 'meteo': 300.94, 'noaa': 305.43, 'sg': 300.94}, 'windSpeed': {'icon': 8.01, 'noaa': 5.2, 'sg': 8.01}}, {'airTemperature': {'dwd': 10.62, 'noaa': 7.37, 'sg': 10.62}, 'swellDirection': {'dwd': 310.52, 'icon': 296.64, 'meteo': 287.78, 'noaa': 315.53, 'sg': 287.78}, 'swellHeight': {'dwd': 2.14, 'icon': 2.6, 'meteo': 2.52, 'noaa': 0.82, 'sg': 2.52}, 'swellPeriod': {'dwd': 11.07, 'icon': 11.71, 'meteo': 9.49, 'noaa': 19.12, 'sg': 9.49}, 'time': '2022-03-03T17:00:00+00:00', 'waveDirection': {'icon': 298.83, 'meteo': 301.26, 'noaa': 311.08, 'sg': 301.26}, 'windSpeed': {'icon': 7.77, 'noaa': 4.72, 'sg': 7.77}}, {'airTemperature': {'dwd': 9.8, 'noaa': 7.43, 'sg': 9.8}, 'swellDirection': {'dwd': 310.86, 'icon': 297.36, 'meteo': 287.64, 'noaa': 316.71, 'sg': 287.64}, 'swellHeight': {'dwd': 2.25, 'icon': 2.72, 'meteo': 2.58, 'noaa': 0.95, 'sg': 2.58}, 'swellPeriod': {'dwd': 11.23, 'icon': 11.9, 'meteo': 9.51, 'noaa': 18.66, 'sg': 
    9.51}, 'time': '2022-03-03T18:00:00+00:00', 'waveDirection': {'icon': 298.97, 'meteo': 301.58, 'noaa': 316.74, 'sg': 301.58}, 'windSpeed': {'icon': 7.52, 'noaa': 4.25, 'sg': 7.52}}, {'airTemperature': {'dwd': 9.46, 'noaa': 7.36, 'sg': 9.46}, 'swellDirection': {'dwd': 311.2, 'icon': 297.65, 'meteo': 287.94, 'noaa': 316.32, 'sg': 287.94}, 'swellHeight': 
    {'dwd': 2.32, 'icon': 2.82, 'meteo': 2.58, 'noaa': 1.12, 'sg': 2.58}, 'swellPeriod': {'dwd': 11.62, 'icon': 12.08, 'meteo': 9.37, 'noaa': 18.21, 'sg': 9.37}, 'time': '2022-03-03T19:00:00+00:00', 'waveDirection': {'icon': 299.22, 'meteo': 301.91, 'noaa': 315.79, 'sg': 301.91}, 'windSpeed': {'icon': 7.48, 'noaa': 4.21, 'sg': 7.48}}, {'airTemperature': {'dwd': 9.31, 'noaa': 7.29, 'sg': 9.31}, 'swellDirection': {'dwd': 311.09, 'icon': 297.93, 'meteo': 288.24, 'noaa': 315.93, 'sg': 288.24}, 'swellHeight': {'dwd': 2.41, 'icon': 2.93, 'meteo': 2.59, 'noaa': 1.28, 'sg': 2.59}, 'swellPeriod': {'dwd': 11.82, 'icon': 12.27, 'meteo': 9.22, 'noaa': 17.75, 'sg': 9.22}, 'time': '2022-03-03T20:00:00+00:00', 'waveDirection': {'icon': 299.46, 'meteo': 302.23, 'noaa': 314.85, 'sg': 302.23}, 'windSpeed': {'icon': 7.43, 'noaa': 4.16, 'sg': 7.43}}, {'airTemperature': {'dwd': 9.24, 'noaa': 7.22, 'sg': 9.24}, 'swellDirection': {'dwd': 311.3, 'icon': 298.22, 'meteo': 288.54, 'noaa': 315.54, 'sg': 288.54}, 'swellHeight': {'dwd': 2.49, 'icon': 3.03, 'meteo': 2.59, 'noaa': 
    1.45, 'sg': 2.59}, 'swellPeriod': {'dwd': 12.07, 'icon': 12.45, 'meteo': 9.08, 'noaa': 17.3, 'sg': 9.08}, 'time': '2022-03-03T21:00:00+00:00', 'waveDirection': {'icon': 299.71, 
    'meteo': 302.56, 'noaa': 313.9, 'sg': 302.56}, 'windSpeed': {'icon': 7.39, 'noaa': 4.12, 'sg': 7.39}}, {'airTemperature': {'dwd': 9.24, 'noaa': 6.94, 'sg': 9.24}, 'swellDirection': {'dwd': 311.49, 'icon': 298.55, 'meteo': 290.66, 'noaa': 316.57, 'sg': 290.66}, 'swellHeight': {'dwd': 2.59, 'icon': 3.13, 'meteo': 2.96, 'noaa': 1.56, 'sg': 2.96}, 'swellPeriod': {'dwd': 12.21, 'icon': 12.55, 'meteo': 9.87, 'noaa': 17.0, 'sg': 9.87}, 'time': '2022-03-03T22:00:00+00:00', 'waveDirection': {'icon': 300.33, 'meteo': 302.65, 'noaa': 313.88, 'sg': 302.65}, 'windSpeed': {'icon': 7.54, 'noaa': 3.89, 'sg': 7.54}}, {'airTemperature': {'dwd': 9.27, 'noaa': 6.66, 'sg': 9.27}, 'swellDirection': {'dwd': 311.88, 'icon': 298.88, 'meteo': 292.78, 'noaa': 317.59, 'sg': 292.78}, 'swellHeight': {'dwd': 2.72, 'icon': 3.24, 'meteo': 3.34, 'noaa': 1.67, 'sg': 3.34}, 'swellPeriod': {'dwd': 12.18, 'icon': 12.64, 'meteo': 10.66, 'noaa': 16.71, 'sg': 10.66}, 'time': '2022-03-03T23:00:00+00:00', 'waveDirection': {'icon': 300.96, 'meteo': 302.73, 'noaa': 313.85, 'sg': 302.73}, 'windSpeed': {'icon': 7.7, 'noaa': 3.65, 'sg': 7.7}}], 'meta': {'cost': 1, 'dailyQuota': 10, 'end': '2022-03-03 23:00', 'lat': 43.5777, 'lng': -5.9619, 'params': ['airTemperature', 'windSpeed', 'waveDirection', 'swellPeriod', 'swellHeight', 'swellDirection'], 'requestCount': 4, 'start': '2022-03-01 23:00'}} 
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
    
    print("----------")
    print(MSN)
    TABLA2= tabulate( data2 , headers=["hora","Periodo oleaje" , "Altura de ola"]  ) 

   
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
    print("----------")
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
    #while True:
    #    aux=0






def cambioI(update):
    global MSN,AUX
    MSN1=MSN
    print("---")
    
    print(MSN1)
    print("<<<<<<<<<<<<<<<<<<<<<<<")
    print(threading.get_ident())
    bot=telegram.Bot(TOKEN)
    bot.editMessageText(text=TABLA1,
                                    reply_markup= InlineKeyboardMarkup([
                        [buttonI , buttonD ]
                    ]),
                    chat_id=CHAT,
                    message_id=MSN1
    )


def cambioD(update):
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
