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

    """
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
    json_data = {'hours': [{'airTemperature': {'dwd': 9.24, 'noaa': 4.82, 'sg': 9.24}, 'swellDirection': {'dwd': 335.09, 'icon': 306.29, 'meteo': 303.39, 'noaa': 341.31, 'sg': 303.39}, 'swellHeight': {'dwd': 2.76, 'icon': 3.91, 'meteo': 3.91, 'noaa': 1.47, 'sg': 3.91}, 'swellPeriod': {'dwd': 14.72, 'icon': 14.2, 'meteo': 11.42, 'noaa': 9.55, 'sg': 11.42}, 'time': '2022-03-04T23:00:00+00:00', 'waveDirection': {'icon': 306.29, 'meteo': 303.39, 'noaa': 323.3, 'sg': 303.39}, 'windSpeed': {'icon': 1.53, 'noaa': 1.59, 'sg': 1.53}}, {'airTemperature': {'dwd': 9.22, 'noaa': 4.05, 'sg': 9.22}, 'swellDirection': {'dwd': 335.19, 'icon': 306.55, 'meteo': 303.79, 'noaa': 350.49, 'sg': 303.79}, 'swellHeight': {'dwd': 2.76, 'icon': 
    3.89, 'meteo': 3.84, 'noaa': 0.95, 'sg': 3.84}, 'swellPeriod': {'dwd': 14.79, 'icon': 14.24, 'meteo': 11.4, 'noaa': 6.81, 'sg': 11.4}, 'time': '2022-03-05T00:00:00+00:00', 'waveDirection': {'icon': 306.55, 'meteo': 303.79, 'noaa': 323.72, 'sg': 303.79}, 'windSpeed': {'icon': 1.2, 'noaa': 2.09, 'sg': 1.2}}, {'airTemperature': {'dwd': 9.2, 'noaa': 3.76, 'sg': 9.2}, 'swellDirection': {'dwd': 335.27, 'icon': 306.84, 'meteo': 304.21, 'noaa': 341.64, 'sg': 304.21}, 'swellHeight': {'dwd': 2.75, 'icon': 3.86, 'meteo': 3.76, 'noaa': 1.41, 'sg': 3.76}, 'swellPeriod': {'dwd': 14.85, 'icon': 14.24, 'meteo': 11.37, 'noaa': 9.53, 'sg': 11.37}, 'time': '2022-03-05T01:00:00+00:00', 'waveDirection': {'icon': 306.84, 'meteo': 304.22, 'noaa': 324.19, 'sg': 304.22}, 'windSpeed': {'icon': 1.26, 'noaa': 2.01, 'sg': 1.26}}, {'airTemperature': {'dwd': 8.97, 'noaa': 3.47, 'sg': 8.97}, 'swellDirection': {'dwd': 335.33, 'icon': 307.13, 'meteo': 304.64, 'noaa': 
    332.79, 'sg': 304.64}, 'swellHeight': {'dwd': 2.74, 'icon': 3.82, 'meteo': 3.67, 'noaa': 1.86, 'sg': 3.67}, 'swellPeriod': {'dwd': 14.88, 'icon': 14.23, 'meteo': 11.35, 'noaa': 12.24, 'sg': 11.35}, 'time': '2022-03-05T02:00:00+00:00', 'waveDirection': {'icon': 307.13, 'meteo': 304.64, 'noaa': 324.65, 'sg': 304.64}, 'windSpeed': {'icon': 1.33, 'noaa': 1.92, 'sg': 1.33}}, {'airTemperature': {'dwd': 8.42, 'noaa': 3.18, 'sg': 8.42}, 'swellDirection': {'dwd': 335.36, 'icon': 307.42, 'meteo': 305.06, 'noaa': 323.94, 'sg': 305.06}, 'swellHeight': {'dwd': 2.72, 'icon': 3.79, 'meteo': 3.59, 'noaa': 2.32, 'sg': 3.59}, 'swellPeriod': {'dwd': 14.88, 'icon': 14.23, 'meteo': 11.32, 'noaa': 14.96, 'sg': 11.32}, 'time': '2022-03-05T03:00:00+00:00', 'waveDirection': {'icon': 307.42, 'meteo': 305.07, 'noaa': 325.12, 'sg': 305.07}, 'windSpeed': {'icon': 1.39, 'noaa': 1.84, 'sg': 1.39}}, {'airTemperature': {'dwd': 8.18, 'noaa': 2.94, 'sg': 8.18}, 'swellDirection': {'dwd': 335.35, 'icon': 307.7, 'meteo': 305.45, 'noaa': 334.29, 'sg': 305.45}, 'swellHeight': {'dwd': 2.7, 'icon': 3.74, 'meteo': 3.49, 'noaa': 1.65, 'sg': 3.49}, 'swellPeriod': {'dwd': 14.86, 'icon': 14.18, 'meteo': 11.27, 'noaa': 15.14, 'sg': 11.27}, 'time': '2022-03-05T04:00:00+00:00', 'waveDirection': {'icon': 307.7, 'meteo': 305.51, 'noaa': 325.0, 'sg': 305.51}, 'windSpeed': {'icon': 1.7, 'noaa': 1.83, 'sg': 1.7}}, {'airTemperature': {'dwd': 8.15, 'noaa': 2.69, 'sg': 8.15}, 'swellDirection': {'dwd': 335.33, 'icon': 307.97, 'meteo': 305.83, 'noaa': 344.65, 'sg': 305.83}, 'swellHeight': {'dwd': 2.66, 'icon': 3.68, 'meteo': 3.39, 'noaa': 0.99, 'sg': 3.39}, 'swellPeriod': {'dwd': 14.82, 'icon': 14.14, 'meteo': 11.22, 'noaa': 15.33, 'sg': 11.22}, 'time': '2022-03-05T05:00:00+00:00', 'waveDirection': {'icon': 307.97, 'meteo': 305.96, 'noaa': 324.87, 'sg': 305.96}, 'windSpeed': {'icon': 2.01, 'noaa': 1.81, 'sg': 2.01}}, {'airTemperature': {'dwd': 8.26, 'noaa': 2.45, 'sg': 8.26}, 'swellDirection': {'dwd': 335.29, 'icon': 308.25, 'meteo': 306.22, 'noaa': 355.0, 'sg': 306.22}, 'swellHeight': {'dwd': 2.62, 'icon': 3.63, 'meteo': 3.29, 'noaa': 0.32, 'sg': 3.29}, 
    'swellPeriod': {'dwd': 14.76, 'icon': 14.09, 'meteo': 11.17, 'noaa': 15.51, 'sg': 11.17}, 'time': '2022-03-05T06:00:00+00:00', 'waveDirection': {'icon': 308.25, 'meteo': 306.4, 'noaa': 324.75, 'sg': 306.4}, 'windSpeed': {'icon': 2.32, 'noaa': 1.8, 'sg': 2.32}}, {'airTemperature': {'dwd': 8.27, 'noaa': 3.66, 'sg': 8.27}, 'swellDirection': {'dwd': 335.23, 'icon': 308.46, 'meteo': 306.6, 'noaa': 344.81, 'sg': 306.6}, 'swellHeight': {'dwd': 2.57, 'icon': 3.56, 'meteo': 3.18, 'noaa': 0.87, 'sg': 3.18}, 'swellPeriod': {'dwd': 14.67, 'icon': 14.0, 'meteo': 11.11, 'noaa': 15.16, 'sg': 11.11}, 'time': '2022-03-05T07:00:00+00:00', 'waveDirection': {'icon': 308.46, 'meteo': 306.89, 'noaa': 325.12, 'sg': 306.89}, 
    'windSpeed': {'icon': 2.75, 'noaa': 1.54, 'sg': 2.75}}, {'airTemperature': {'dwd': 8.24, 'noaa': 4.87, 'sg': 8.24}, 'swellDirection': {'dwd': 335.14, 'icon': 308.66, 'meteo': 306.98, 'noaa': 334.61, 'sg': 306.98}, 'swellHeight': {'dwd': 
    2.52, 'icon': 3.49, 'meteo': 3.08, 'noaa': 1.41, 'sg': 3.08}, 'swellPeriod': {'dwd': 14.57, 'icon': 13.91, 'meteo': 11.06, 'noaa': 14.8, 'sg': 11.06}, 'time': '2022-03-05T08:00:00+00:00', 'waveDirection': {'icon': 308.66, 'meteo': 307.38, 'noaa': 325.48, 'sg': 307.38}, 'windSpeed': {'icon': 3.18, 'noaa': 1.29, 'sg': 3.18}}, {'airTemperature': {'dwd': 8.46, 'noaa': 6.08, 'sg': 8.46}, 'swellDirection': {'dwd': 335.04, 'icon': 308.87, 'meteo': 307.36, 'noaa': 324.42, 'sg': 307.36}, 'swellHeight': {'dwd': 2.46, 'icon': 3.42, 'meteo': 2.97, 'noaa': 1.96, 'sg': 2.97}, 'swellPeriod': {'dwd': 14.45, 'icon': 13.82, 'meteo': 11.0, 'noaa': 14.45, 'sg': 11.0}, 'time': '2022-03-05T09:00:00+00:00', 'waveDirection': 
    {'icon': 308.87, 'meteo': 307.87, 'noaa': 325.85, 'sg': 307.87}, 'windSpeed': {'icon': 3.61, 'noaa': 1.03, 'sg': 3.61}}, {'airTemperature': {'dwd': 8.78, 'noaa': 7.14, 'sg': 8.78}, 'swellDirection': {'dwd': 334.91, 'icon': 308.85, 'meteo': 307.39, 'noaa': 324.85, 'sg': 307.39}, 'swellHeight': {'dwd': 2.39, 'icon': 3.35, 'meteo': 2.89, 'noaa': 1.91, 'sg': 2.89}, 'swellPeriod': {'dwd': 14.33, 'icon': 13.72, 'meteo': 11.0, 'noaa': 14.42, 'sg': 11.0}, 'time': '2022-03-05T10:00:00+00:00', 'waveDirection': {'icon': 308.85, 'meteo': 308.0, 'noaa': 326.23, 'sg': 308.0}, 'windSpeed': {'icon': 3.89, 'noaa': 1.69, 'sg': 3.89}}, {'airTemperature': {'dwd': 8.97, 'noaa': 8.21, 'sg': 8.97}, 'swellDirection': {'dwd': 
    334.75, 'icon': 308.82, 'meteo': 307.43, 'noaa': 325.29, 'sg': 307.43}, 'swellHeight': {'dwd': 2.33, 'icon': 3.28, 'meteo': 2.82, 'noaa': 1.86, 'sg': 2.82}, 'swellPeriod': {'dwd': 14.2, 'icon': 13.61, 'meteo': 11.0, 'noaa': 14.4, 'sg': 11.0}, 'time': '2022-03-05T11:00:00+00:00', 'waveDirection': {'icon': 308.84, 'meteo': 308.13, 'noaa': 326.6, 'sg': 308.13}, 'windSpeed': {'icon': 4.18, 'noaa': 2.36, 'sg': 4.18}}, {'airTemperature': {'dwd': 9.01, 'noaa': 9.28, 'sg': 9.01}, 'swellDirection': {'dwd': 334.51, 'icon': 308.8, 'meteo': 307.46, 'noaa': 325.72, 'sg': 307.46}, 'swellHeight': {'dwd': 2.27, 'icon': 3.21, 'meteo': 2.74, 'noaa': 1.81, 'sg': 2.74}, 'swellPeriod': {'dwd': 14.07, 'icon': 13.51, 'meteo': 11.0, 'noaa': 14.37, 'sg': 11.0}, 'time': '2022-03-05T12:00:00+00:00', 'waveDirection': {'icon': 308.82, 'meteo': 308.26, 'noaa': 326.98, 'sg': 308.26}, 'windSpeed': {'icon': 4.46, 'noaa': 3.02, 'sg': 4.46}}, {'airTemperature': {'dwd': 9.04, 'noaa': 9.08, 'sg': 9.04}, 'swellDirection': {'dwd': 334.2, 'icon': 308.35, 'meteo': 303.18, 'noaa': 326.17, 'sg': 303.18}, 'swellHeight': {'dwd': 2.22, 'icon': 3.18, 'meteo': 2.57, 'noaa': 1.81, 'sg': 2.57}, 'swellPeriod': {'dwd': 13.96, 'icon': 13.45, 'meteo': 11.49, 'noaa': 14.33, 'sg': 11.49}, 'time': '2022-03-05T13:00:00+00:00', 'waveDirection': {'icon': 308.38, 'meteo': 307.45, 'noaa': 327.28, 'sg': 307.45}, 'windSpeed': {'icon': 4.34, 'noaa': 3.07, 'sg': 4.34}}, {'airTemperature': {'dwd': 9.24, 'noaa': 8.89, 'sg': 9.24}, 'swellDirection': {'dwd': 333.91, 'icon': 307.89, 'meteo': 298.91, 'noaa': 326.62, 'sg': 298.91}, 'swellHeight': {'dwd': 2.18, 'icon': 3.14, 'meteo': 2.39, 'noaa': 1.8, 'sg': 2.39}, 'swellPeriod': {'dwd': 13.84, 'icon': 13.38, 'meteo': 11.99, 'noaa': 14.3, 'sg': 11.99}, 'time': '2022-03-05T14:00:00+00:00', 'waveDirection': {'icon': 307.93, 'meteo': 306.64, 'noaa': 327.59, 'sg': 306.64}, 'windSpeed': {'icon': 4.22, 'noaa': 3.11, 'sg': 4.22}}, {'airTemperature': {'dwd': 9.79, 'noaa': 8.69, 'sg': 9.79}, 'swellDirection': {'dwd': 333.71, 'icon': 307.44, 'meteo': 294.63, 'noaa': 327.07, 'sg': 294.63}, 'swellHeight': {'dwd': 2.15, 'icon': 3.11, 'meteo': 2.22, 'noaa': 1.8, 'sg': 2.22}, 'swellPeriod': {'dwd': 13.72, 'icon': 13.32, 'meteo': 12.48, 'noaa': 14.26, 'sg': 12.48}, 'time': '2022-03-05T15:00:00+00:00', 'waveDirection': {'icon': 307.49, 'meteo': 305.83, 'noaa': 327.89, 'sg': 305.83}, 'windSpeed': {'icon': 4.1, 'noaa': 3.16, 'sg': 4.1}}, {'airTemperature': {'dwd': 10.31, 'noaa': 7.88, 'sg': 10.31}, 'swellDirection': {'dwd': 333.35, 'icon': 306.61, 'meteo': 296.48, 'noaa': 326.86, 'sg': 296.48}, 'swellHeight': {'dwd': 2.14, 'icon': 3.13, 'meteo': 2.53, 'noaa': 1.86, 'sg': 2.53}, 'swellPeriod': {'dwd': 13.64, 'icon': 13.32, 'meteo': 12.29, 'noaa': 14.6, 'sg': 12.29}, 'time': '2022-03-05T16:00:00+00:00', 'waveDirection': {'icon': 306.8, 
    'meteo': 304.65, 'noaa': 325.22, 'sg': 304.65}, 'windSpeed': {'icon': 4.51, 'noaa': 2.97, 'sg': 4.51}}, {'airTemperature': {'dwd': 10.32, 'noaa': 7.07, 'sg': 10.32}, 'swellDirection': {'dwd': 333.06, 'icon': 305.79, 'meteo': 298.34, 'noaa': 326.65, 'sg': 298.34}, 'swellHeight': {'dwd': 2.15, 'icon': 3.14, 'meteo': 2.84, 'noaa': 1.92, 'sg': 2.84}, 'swellPeriod': {'dwd': 13.57, 'icon': 13.33, 'meteo': 12.1, 'noaa': 14.93, 'sg': 12.1}, 'time': '2022-03-05T17:00:00+00:00', 
    'waveDirection': {'icon': 306.12, 'meteo': 303.48, 'noaa': 322.56, 'sg': 303.48}, 'windSpeed': {'icon': 4.91, 'noaa': 2.78, 'sg': 4.91}}, {'airTemperature': {'dwd': 10.33, 'noaa': 6.25, 'sg': 10.33}, 'swellDirection': {'dwd': 332.92, 'icon': 304.96, 'meteo': 300.19, 'noaa': 326.44, 'sg': 300.19}, 'swellHeight': {'dwd': 2.16, 'icon': 3.16, 'meteo': 3.15, 'noaa': 1.98, 'sg': 3.15}, 'swellPeriod': {'dwd': 13.47, 'icon': 13.33, 'meteo': 11.91, 'noaa': 15.27, 'sg': 11.91}, 'time': '2022-03-05T18:00:00+00:00', 'waveDirection': {'icon': 305.43, 'meteo': 302.3, 'noaa': 319.89, 'sg': 302.3}, 'windSpeed': {'icon': 5.32, 'noaa': 2.59, 'sg': 5.32}}, {'airTemperature': {'dwd': 10.37, 'noaa': 6.23, 'sg': 10.37}, 'swellDirection': {'dwd': 332.4, 'icon': 304.23, 'meteo': 299.15, 'noaa': 324.92, 'sg': 299.15}, 'swellHeight': {'dwd': 2.17, 'icon': 3.2, 'meteo': 3.24, 'noaa': 2.02, 'sg': 3.24}, 'swellPeriod': {'dwd': 13.45, 'icon': 13.32, 'meteo': 11.94, 'noaa': 15.07, 'sg': 11.94}, 'time': '2022-03-05T19:00:00+00:00', 'waveDirection': {'icon': 304.63, 'meteo': 301.39, 'noaa': 319.1, 'sg': 301.39}, 'windSpeed': {'icon': 5.16, 'noaa': 2.34, 'sg': 5.16}}, {'airTemperature': {'dwd': 10.37, 'noaa': 6.21, 'sg': 10.37}, 'swellDirection': {'dwd': 331.53, 'icon': 303.5, 'meteo': 298.1, 'noaa': 323.4, 'sg': 298.1}, 'swellHeight': {'dwd': 2.18, 'icon': 3.23, 'meteo': 3.33, 'noaa': 2.05, 'sg': 3.33}, 'swellPeriod': {'dwd': 13.49, 'icon': 13.31, 'meteo': 11.98, 'noaa': 14.87, 'sg': 11.98}, 'time': '2022-03-05T20:00:00+00:00', 'waveDirection': {'icon': 303.83, 'meteo': 300.48, 'noaa': 318.32, 'sg': 300.48}, 'windSpeed': {'icon': 5.01, 'noaa': 2.08, 'sg': 5.01}}, 
    {'airTemperature': {'dwd': 9.95, 'noaa': 6.19, 'sg': 9.95}, 'swellDirection': {'dwd': 330.68, 'icon': 302.77, 'meteo': 297.06, 'noaa': 321.88, 'sg': 297.06}, 'swellHeight': {'dwd': 2.18, 'icon': 3.27, 'meteo': 3.42, 'noaa': 2.09, 'sg': 3.42}, 'swellPeriod': {'dwd': 13.52, 'icon': 13.3, 'meteo': 12.01, 'noaa': 14.67, 'sg': 12.01}, 'time': '2022-03-05T21:00:00+00:00', 'waveDirection': {'icon': 303.03, 'meteo': 299.57, 'noaa': 317.53, 'sg': 299.57}, 'windSpeed': {'icon': 4.85, 'noaa': 1.83, 'sg': 4.85}}, {'airTemperature': {'dwd': 9.86, 'noaa': 6.03, 'sg': 9.86}, 'swellDirection': {'dwd': 329.89, 'icon': 302.3, 'meteo': 296.53, 'noaa': 320.5, 'sg': 296.53}, 'swellHeight': {'dwd': 2.18, 'icon': 3.29, 'meteo': 3.43, 'noaa': 2.08, 'sg': 3.43}, 'swellPeriod': {'dwd': 13.52, 'icon': 13.25, 'meteo': 11.93, 'noaa': 14.56, 'sg': 11.93}, 'time': '2022-03-05T22:00:00+00:00', 'waveDirection': {'icon': 302.47, 'meteo': 298.98, 'noaa': 316.77, 'sg': 
    298.98}, 'windSpeed': {'icon': 4.15, 'noaa': 1.47, 'sg': 4.15}}, {'airTemperature': {'dwd': 9.9, 'noaa': 5.87, 'sg': 9.9}, 'swellDirection': {'dwd': 329.21, 'icon': 301.83, 'meteo': 296.0, 'noaa': 319.12, 'sg': 296.0}, 'swellHeight': {'dwd': 2.16, 'icon': 3.3, 'meteo': 3.43, 'noaa': 2.06, 'sg': 3.43}, 'swellPeriod': {'dwd': 13.5, 'icon': 13.19, 'meteo': 11.85, 'noaa': 14.46, 'sg': 11.85}, 'time': '2022-03-05T23:00:00+00:00', 'waveDirection': {'icon': 301.92, 'meteo': 298.4, 'noaa': 316.02, 'sg': 298.4}, 'windSpeed': {'icon': 3.46, 'noaa': 1.1, 'sg': 3.46}}, {'airTemperature': {'dwd': 9.42, 'noaa': 5.7, 'sg': 9.42}, 'swellDirection': {'dwd': 328.66, 'icon': 301.36, 'meteo': 295.47, 'noaa': 317.74, 'sg': 295.47}, 'swellHeight': {'dwd': 2.14, 'icon': 3.32, 'meteo': 3.44, 'noaa': 2.05, 'sg': 3.44}, 'swellPeriod': {'dwd': 13.43, 'icon': 13.14, 'meteo': 11.77, 'noaa': 14.35, 'sg': 11.77}, 'time': '2022-03-06T00:00:00+00:00', 'waveDirection': {'icon': 301.36, 'meteo': 297.81, 'noaa': 315.26, 'sg': 297.81}, 'windSpeed': {'icon': 2.76, 'noaa': 0.74, 'sg': 2.76}}, {'airTemperature': {'dwd': 9.16, 'noaa': 4.78, 'sg': 9.16}, 'swellDirection': {'dwd': 328.24, 'icon': 301.21, 'meteo': 294.83, 'noaa': 316.83, 'sg': 294.83}, 'swellHeight': {'dwd': 2.12, 'icon': 3.3, 'meteo': 3.36, 'noaa': 2.0, 'sg': 3.36}, 'swellPeriod': {'dwd': 13.33, 'icon': 13.03, 'meteo': 11.69, 'noaa': 14.23, 'sg': 11.69}, 'time': '2022-03-06T01:00:00+00:00', 'waveDirection': {'icon': 301.21, 'meteo': 297.54, 'noaa': 314.88, 'sg': 297.54}, 'windSpeed': {'icon': 2.2, 'noaa': 1.12, 'sg': 2.2}}, {'airTemperature': {'dwd': 9.02, 'noaa': 3.85, 'sg': 9.02}, 'swellDirection': {'dwd': 327.91, 'icon': 301.07, 'meteo': 294.2, 'noaa': 315.91, 'sg': 294.2}, 'swellHeight': {'dwd': 2.1, 'icon': 3.28, 'meteo': 3.28, 'noaa': 1.96, 'sg': 3.28}, 'swellPeriod': {'dwd': 13.21, 'icon': 12.93, 'meteo': 11.61, 'noaa': 14.12, 'sg': 11.61}, 'time': '2022-03-06T02:00:00+00:00', 'waveDirection': {'icon': 301.07, 'meteo': 297.28, 'noaa': 314.49, 'sg': 297.28}, 'windSpeed': {'icon': 1.63, 'noaa': 1.5, 'sg': 1.63}}, {'airTemperature': {'dwd': 8.64, 'noaa': 2.92, 'sg': 8.64}, 'swellDirection': {'dwd': 327.66, 'icon': 300.92, 'meteo': 293.56, 'noaa': 315.0, 'sg': 293.56}, 'swellHeight': {'dwd': 2.06, 'icon': 3.26, 'meteo': 3.2, 'noaa': 1.91, 'sg': 3.2}, 'swellPeriod': {'dwd': 13.05, 'icon': 12.82, 'meteo': 11.53, 'noaa': 14.0, 'sg': 11.53}, 'time': '2022-03-06T03:00:00+00:00', 'waveDirection': {'icon': 300.92, 'meteo': 297.01, 'noaa': 314.11, 'sg': 297.01}, 'windSpeed': {'icon': 1.07, 'noaa': 1.88, 'sg': 1.07}}, {'airTemperature': {'dwd': 8.46, 'noaa': 2.69, 'sg': 8.46}, 'swellDirection': {'dwd': 327.52, 'icon': 301.21, 'meteo': 293.25, 'noaa': 315.35, 'sg': 293.25}, 'swellHeight': {'dwd': 2.01, 'icon': 3.21, 'meteo': 3.09, 'noaa': 1.87, 'sg': 3.09}, 'swellPeriod': {'dwd': 12.86, 'icon': 12.66, 'meteo': 11.4, 'noaa': 13.85, 'sg': 11.4}, 'time': '2022-03-06T04:00:00+00:00', 'waveDirection': {'icon': 301.21, 'meteo': 297.65, 'noaa': 313.79, 'sg': 297.65}, 'windSpeed': {'icon': 0.81, 'noaa': 2.06, 'sg': 
    0.81}}, {'airTemperature': {'dwd': 7.7, 'noaa': 2.46, 'sg': 7.7}, 'swellDirection': {'dwd': 327.46, 'icon': 301.5, 'meteo': 292.93, 'noaa': 315.69, 'sg': 292.93}, 'swellHeight': {'dwd': 1.97, 'icon': 3.15, 'meteo': 2.98, 'noaa': 1.84, 'sg': 2.98}, 'swellPeriod': {'dwd': 12.66, 'icon': 12.49, 'meteo': 11.26, 'noaa': 13.69, 'sg': 11.26}, 'time': '2022-03-06T05:00:00+00:00', 'waveDirection': {'icon': 301.5, 'meteo': 298.28, 'noaa': 313.46, 'sg': 298.28}, 'windSpeed': {'icon': 0.56, 'noaa': 2.24, 'sg': 0.56}}, {'airTemperature': {'dwd': 7.34, 'noaa': 2.23, 'sg': 7.34}, 'swellDirection': {'dwd': 327.5, 'icon': 301.79, 'meteo': 292.62, 'noaa': 316.04, 'sg': 292.62}, 'swellHeight': {'dwd': 1.92, 'icon': 3.1, 
    'meteo': 2.87, 'noaa': 1.8, 'sg': 2.87}, 'swellPeriod': {'dwd': 12.42, 'icon': 12.33, 'meteo': 11.13, 'noaa': 13.54, 'sg': 11.13}, 'time': '2022-03-06T06:00:00+00:00', 'waveDirection': {'icon': 301.79, 'meteo': 298.92, 'noaa': 313.14, 'sg': 298.92}, 'windSpeed': {'icon': 0.31, 'noaa': 2.42, 'sg': 0.31}}, {'airTemperature': {'dwd': 7.31, 'noaa': 3.14, 'sg': 7.31}, 'swellDirection': {'dwd': 327.67, 'icon': 302.53, 'meteo': 292.5, 'noaa': 314.68, 'sg': 292.5}, 'swellHeight': {'dwd': 1.88, 'icon': 3.03, 'meteo': 2.76, 'noaa': 1.71, 'sg': 2.76}, 'swellPeriod': {'dwd': 12.19, 'icon': 12.14, 'meteo': 11.0, 'noaa': 13.41, 'sg': 11.0}, 'time': '2022-03-06T07:00:00+00:00', 'waveDirection': {'icon': 302.53, 'meteo': 299.56, 'noaa': 313.21, 'sg': 299.56}, 'windSpeed': {'icon': 0.3, 'noaa': 2.18, 'sg': 0.3}}, {'airTemperature': {'dwd': 7.27, 'noaa': 4.06, 'sg': 7.27}, 'swellDirection': {'dwd': 328.05, 'icon': 303.27, 'meteo': 292.38, 'noaa': 313.33, 'sg': 292.38}, 'swellHeight': {'dwd': 1.85, 'icon': 2.97, 'meteo': 2.64, 'noaa': 1.62, 'sg': 2.64}, 'swellPeriod': {'dwd': 11.94, 'icon': 11.95, 'meteo': 10.86, 'noaa': 13.29, 'sg': 10.86}, 'time': '2022-03-06T08:00:00+00:00', 'waveDirection': {'icon': 303.27, 'meteo': 300.21, 'noaa': 313.28, 'sg': 300.21}, 'windSpeed': {'icon': 0.3, 'noaa': 1.95, 'sg': 0.3}}, {'airTemperature': {'dwd': 7.25, 'noaa': 4.97, 'sg': 7.25}, 'swellDirection': {'dwd': 328.65, 'icon': 304.01, 'meteo': 292.26, 'noaa': 311.97, 'sg': 292.26}, 'swellHeight': {'dwd': 1.81, 'icon': 2.9, 'meteo': 2.53, 'noaa': 1.53, 'sg': 2.53}, 'swellPeriod': {'dwd': 11.69, 'icon': 11.76, 'meteo': 10.73, 'noaa': 13.16, 'sg': 10.73}, 'time': '2022-03-06T09:00:00+00:00', 'waveDirection': {'icon': 304.01, 'meteo': 300.85, 'noaa': 313.35, 'sg': 300.85}, 'windSpeed': {'icon': 0.29, 'noaa': 1.71, 'sg': 0.29}}, {'airTemperature': {'dwd': 7.87, 'noaa': 5.97, 'sg': 7.87}, 'swellDirection': {'dwd': 329.5, 'icon': 304.96, 'meteo': 292.26, 'noaa': 311.92, 'sg': 292.26}, 'swellHeight': {'dwd': 1.77, 'icon': 2.83, 'meteo': 2.42, 'noaa': 1.47, 'sg': 2.42}, 'swellPeriod': {'dwd': 11.41, 'icon': 11.58, 'meteo': 10.61, 'noaa': 12.99, 'sg': 10.61}, 'time': '2022-03-06T10:00:00+00:00', 'waveDirection': {'icon': 304.96, 'meteo': 302.01, 'noaa': 313.11, 'sg': 302.01}, 'windSpeed': {'icon': 0.84, 'noaa': 1.56, 'sg': 0.84}}, {'airTemperature': {'dwd': 8.39, 'noaa': 6.97, 'sg': 8.39}, 'swellDirection': {'dwd': 330.65, 'icon': 305.92, 'meteo': 292.26, 'noaa': 311.86, 'sg': 292.26}, 'swellHeight': {'dwd': 1.73, 'icon': 2.77, 'meteo': 2.31, 'noaa': 1.42, 'sg': 2.31}, 'swellPeriod': {'dwd': 11.11, 'icon': 11.41, 'meteo': 10.5, 'noaa': 12.81, 'sg': 10.5}, 'time': '2022-03-06T11:00:00+00:00', 'waveDirection': {'icon': 305.92, 'meteo': 303.16, 'noaa': 312.87, 'sg': 303.16}, 'windSpeed': {'icon': 1.38, 'noaa': 1.41, 'sg': 1.38}}, {'airTemperature': {'dwd': 8.61, 'noaa': 7.97, 'sg': 8.61}, 'swellDirection': {'dwd': 332.12, 'icon': 306.87, 'meteo': 292.26, 'noaa': 311.81, 'sg': 292.26}, 'swellHeight': {'dwd': 1.71, 'icon': 2.7, 'meteo': 2.2, 'noaa': 1.36, 'sg': 2.2}, 'swellPeriod': {'dwd': 10.81, 'icon': 11.23, 'meteo': 10.38, 'noaa': 12.64, 'sg': 10.38}, 'time': '2022-03-06T12:00:00+00:00', 'waveDirection': {'icon': 306.87, 'meteo': 304.32, 'noaa': 312.63, 'sg': 304.32}, 'windSpeed': {'icon': 1.93, 'noaa': 1.26, 'sg': 1.93}}, {'airTemperature': {'dwd': 8.75, 'noaa': 8.15, 'sg': 8.75}, 'swellDirection': {'dwd': 333.9, 'icon': 307.76, 'meteo': 293.12, 'noaa': 317.51, 'sg': 293.12}, 'swellHeight': {'dwd': 1.69, 'icon': 2.63, 'meteo': 2.05, 'noaa': 1.33, 'sg': 2.05}, 'swellPeriod': {'dwd': 10.5, 'icon': 11.09, 'meteo': 10.21, 'noaa': 11.68, 'sg': 10.21}, 'time': '2022-03-06T13:00:00+00:00', 'waveDirection': {'icon': 307.76, 'meteo': 305.93, 'noaa': 313.1, 'sg': 305.93}, 'windSpeed': {'icon': 2.36, 'noaa': 1.71, 'sg': 2.36}}, {'airTemperature': {'dwd': 8.87, 'noaa': 8.33, 'sg': 8.87}, 'swellDirection': {'dwd': 335.75, 'icon': 308.65, 'meteo': 293.97, 'noaa': 323.21, 'sg': 293.97}, 'swellHeight': {'dwd': 1.68, 'icon': 2.57, 'meteo': 1.91, 'noaa': 1.29, 'sg': 1.91}, 'swellPeriod': {'dwd': 10.2, 'icon': 10.95, 'meteo': 10.05, 'noaa': 10.72, 'sg': 10.05}, 'time': '2022-03-06T14:00:00+00:00', 'waveDirection': {'icon': 308.65, 'meteo': 307.54, 'noaa': 313.57, 'sg': 307.54}, 'windSpeed': {'icon': 2.8, 'noaa': 2.15, 'sg': 2.8}}, {'airTemperature': {'dwd': 9.17, 'noaa': 8.51, 'sg': 9.17}, 'swellDirection': {'dwd': 337.42, 'icon': 309.54, 'meteo': 294.83, 'noaa': 328.91, 'sg': 294.83}, 'swellHeight': {'dwd': 1.67, 'icon': 2.5, 'meteo': 1.76, 'noaa': 1.26, 'sg': 1.76}, 'swellPeriod': {'dwd': 9.96, 'icon': 10.81, 'meteo': 9.88, 'noaa': 9.76, 'sg': 9.88}, 'time': '2022-03-06T15:00:00+00:00', 'waveDirection': {'icon': 
    309.54, 'meteo': 309.15, 'noaa': 314.04, 'sg': 309.15}, 'windSpeed': {'icon': 3.23, 'noaa': 2.6, 'sg': 3.23}}, {'airTemperature': {'dwd': 9.29, 'noaa': 7.68, 'sg': 9.29}, 'swellDirection': {'dwd': 338.76, 'icon': 310.28, 'meteo': 293.9, 
    'noaa': 338.62, 'sg': 293.9}, 'swellHeight': {'dwd': 1.65, 'icon': 2.44, 'meteo': 1.73, 'noaa': 1.24, 'sg': 1.73}, 'swellPeriod': {'dwd': 9.76, 'icon': 10.7, 'meteo': 9.88, 'noaa': 8.91, 'sg': 9.88}, 'time': '2022-03-06T16:00:00+00:00', 
    'waveDirection': {'icon': 310.28, 'meteo': 310.61, 'noaa': 313.29, 'sg': 310.61}, 'windSpeed': {'icon': 3.28, 'noaa': 1.93, 'sg': 3.28}}, {'airTemperature': {'dwd': 9.19, 'noaa': 6.85, 'sg': 9.19}, 'swellDirection': {'dwd': 339.77, 'icon': 311.01, 'meteo': 292.97, 'noaa': 348.33, 'sg': 292.97}, 'swellHeight': {'dwd': 1.61, 'icon': 2.39, 'meteo': 1.71, 'noaa': 1.23, 'sg': 1.71}, 'swellPeriod': {'dwd': 9.61, 'icon': 10.6, 'meteo': 9.88, 'noaa': 8.07, 'sg': 9.88}, 'time': 
    '2022-03-06T17:00:00+00:00', 'waveDirection': {'icon': 311.01, 'meteo': 312.07, 'noaa': 312.54, 'sg': 312.07}, 'windSpeed': {'icon': 3.33, 'noaa': 1.27, 'sg': 3.33}}, {'airTemperature': {'dwd': 8.93, 'noaa': 6.02, 'sg': 8.93}, 'swellDirection': {'dwd': 340.48, 'icon': 311.75, 'meteo': 292.04, 'noaa': 358.04, 'sg': 292.04}, 'swellHeight': {'dwd': 1.58, 'icon': 2.33, 'meteo': 1.68, 'noaa': 1.21, 'sg': 1.68}, 'swellPeriod': {'dwd': 9.5, 'icon': 10.49, 'meteo': 9.88, 'noaa': 7.22, 'sg': 9.88}, 'time': '2022-03-06T18:00:00+00:00', 'waveDirection': {'icon': 311.75, 'meteo': 313.53, 'noaa': 311.79, 'sg': 313.53}, 'windSpeed': {'icon': 3.38, 'noaa': 0.6, 'sg': 3.38}}, {'airTemperature': {'dwd': 8.64, 'noaa': 5.21, 'sg': 8.64}, 'swellDirection': {'dwd': 340.97, 'icon': 312.41, 'meteo': 292.05, 'noaa': 346.05, 'sg': 292.05}, 'swellHeight': {'dwd': 1.55, 'icon': 2.28, 'meteo': 1.62, 'noaa': 1.0, 'sg': 1.62}, 'swellPeriod': {'dwd': 9.4, 'icon': 10.41, 'meteo': 9.81, 'noaa': 8.74, 'sg': 9.81}, 'time': '2022-03-06T19:00:00+00:00', 'waveDirection': {'icon': 312.41, 'meteo': 314.53, 'noaa': 312.32, 'sg': 314.53}, 'windSpeed': {'icon': 2.9, 'noaa': 0.98, 'sg': 2.9}}, {'airTemperature': {'dwd': 8.4, 'noaa': 4.4, 'sg': 8.4}, 'swellDirection': {'dwd': 341.28, 'icon': 313.06, 'meteo': 292.05, 'noaa': 334.07, 'sg': 292.05}, 'swellHeight': {'dwd': 1.52, 'icon': 2.24, 'meteo': 1.55, 'noaa': 0.79, 'sg': 1.55}, 'swellPeriod': {'dwd': 9.33, 'icon': 10.34, 'meteo': 9.75, 'noaa': 10.27, 'sg': 9.75}, 'time': '2022-03-06T20:00:00+00:00', 'waveDirection': {'icon': 313.06, 'meteo': 315.53, 'noaa': 312.85, 'sg': 315.53}, 'windSpeed': {'icon': 2.42, 'noaa': 1.35, 'sg': 2.42}}, {'airTemperature': {'dwd': 8.51, 'noaa': 3.6, 'sg': 8.51}, 'swellDirection': {'dwd': 341.52, 'icon': 313.72, 'meteo': 292.06, 'noaa': 322.08, 'sg': 292.06}, 'swellHeight': {'dwd': 1.51, 'icon': 2.19, 'meteo': 1.49, 'noaa': 0.58, 'sg': 1.49}, 'swellPeriod': {'dwd': 9.26, 'icon': 10.26, 'meteo': 9.68, 'noaa': 11.79, 'sg': 9.68}, 'time': '2022-03-06T21:00:00+00:00', 'waveDirection': {'icon': 313.72, 'meteo': 316.53, 'noaa': 313.38, 'sg': 316.53}, 'windSpeed': {'icon': 1.94, 'noaa': 1.73, 'sg': 1.94}}, {'airTemperature': {'dwd': 8.61, 'noaa': 3.37, 'sg': 8.61}, 'swellDirection': {'dwd': 341.7, 'icon': 314.28, 'meteo': 291.97, 'noaa': 333.8, 'sg': 291.97}, 'swellHeight': {'dwd': 1.49, 'icon': 2.15, 'meteo': 1.43, 'noaa': 0.73, 'sg': 1.43}, 'swellPeriod': {'dwd': 9.21, 'icon': 10.2, 'meteo': 9.62, 'noaa': 10.27, 'sg': 9.62}, 'time': '2022-03-06T22:00:00+00:00', 'waveDirection': {'icon': 314.28, 'meteo': 317.26, 'noaa': 313.02, 'sg': 317.26}, 'windSpeed': {'icon': 1.86, 'noaa': 1.7, 'sg': 1.86}}, {'airTemperature': {'dwd': 8.66, 'noaa': 3.15, 'sg': 8.66}, 'swellDirection': {'dwd': 341.87, 'icon': 314.85, 'meteo': 291.87, 'noaa': 345.52, 'sg': 291.87}, 'swellHeight': {'dwd': 1.48, 'icon': 2.12, 'meteo': 1.38, 'noaa': 0.89, 'sg': 1.38}, 'swellPeriod': {'dwd': 9.16, 'icon': 10.14, 'meteo': 9.56, 'noaa': 8.76, 'sg': 9.56}, 'time': '2022-03-06T23:00:00+00:00', 'waveDirection': {'icon': 314.85, 'meteo': 317.98, 'noaa': 312.65, 'sg': 317.98}, 'windSpeed': {'icon': 1.78, 'noaa': 1.67, 'sg': 1.78}}], 'meta': {'cost': 1, 'dailyQuota': 10, 'end': '2022-03-06 23:00', 'lat': 43.5423, 'lng': -5.6592, 'params': ['airTemperature', 'windSpeed', 'waveDirection', 'swellPeriod', 'swellHeight', 'swellDirection'], 'requestCount': 2, 'start': '2022-03-04 23:00'}}
   
     

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
