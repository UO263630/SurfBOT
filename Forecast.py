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
    json_data = {'hours': [{'airTemperature': {'dwd': 8.54, 'noaa': 5.87, 'sg': 8.54}, 'swellDirection': {'dwd': 334.62, 'icon': 304.53, 'meteo': 298.49, 'noaa': 319.77, 'sg': 298.49}, 'swellHeight': {'dwd': 1.98, 'icon': 3.02, 'meteo': 2.78, 'noaa': 2.08, 'sg': 2.78}, 'swellPeriod': {'dwd': 12.03, 'icon': 12.56, 'meteo': 11.5, 'noaa': 14.46, 'sg': 11.5}, 'time': '2022-03-05T23:00:00+00:00', 'waveDirection': {'icon': 304.85, 'meteo': 303.96, 'noaa': 316.26, 'sg': 303.96}, 'windSpeed': {'icon': 3.95, 'noaa': 1.1, 'sg': 3.95}}, {'airTemperature': {'dwd': 8.36, 'noaa': 5.7, 'sg': 8.36}, 'swellDirection': {'dwd': 333.7, 'icon': 303.69, 'meteo': 297.14, 'noaa': 318.72, 'sg': 297.14}, 'swellHeight': {'dwd': 2.02, 'icon': 3.08, 'meteo': 2.88, 'noaa': 2.07, 'sg': 2.88}, 'swellPeriod': {'dwd': 12.21, 'icon': 12.6, 'meteo': 11.57, 'noaa': 14.36, 'sg': 11.57}, 'time': '2022-03-06T00:00:00+00:00', 'waveDirection': {'icon': 303.7, 'meteo': 302.34, 'noaa': 315.63, 'sg': 302.34}, 'windSpeed': {'icon': 3.23, 'noaa': 0.74, 'sg': 3.23}}, {'airTemperature': {'dwd': 8.06, 'noaa': 4.78, 'sg': 8.06}, 'swellDirection': {'dwd': 332.97, 'icon': 303.09, 'meteo': 296.34, 'noaa': 317.17, 'sg': 296.34}, 'swellHeight': {'dwd': 2.05, 'icon': 3.1, 'meteo': 2.9, 'noaa': 2.01, 'sg': 2.9}, 'swellPeriod': {'dwd': 12.28, 'icon': 12.58, 'meteo': 11.55, 'noaa': 14.24, 'sg': 11.55}, 'time': '2022-03-06T01:00:00+00:00', 'waveDirection': {'icon': 303.1, 'meteo': 301.7, 'noaa': 315.16, 'sg': 301.7}, 'windSpeed': {'icon': 2.92, 'noaa': 1.12, 'sg': 2.92}}, {'airTemperature': {'dwd': 7.94, 'noaa': 3.85, 'sg': 7.94}, 'swellDirection': {'dwd': 332.32, 'icon': 302.49, 'meteo': 295.55, 'noaa': 315.63, 'sg': 295.55}, 'swellHeight': {'dwd': 2.05, 'icon': 3.11, 'meteo': 2.93, 'noaa': 1.95, 'sg': 2.93}, 'swellPeriod': {'dwd': 12.29, 'icon': 12.57, 'meteo': 11.52, 'noaa': 14.13, 'sg': 11.52}, 'time': '2022-03-06T02:00:00+00:00', 'waveDirection': {'icon': 302.49, 'meteo': 301.05, 'noaa': 314.68, 'sg': 301.05}, 'windSpeed': {'icon': 2.6, 'noaa': 1.5, 'sg': 2.6}}, {'airTemperature': {'dwd': 8.04, 'noaa': 2.92, 'sg': 8.04}, 'swellDirection': {'dwd': 331.71, 'icon': 301.89, 'meteo': 294.75, 'noaa': 314.08, 'sg': 294.75}, 'swellHeight': {'dwd': 2.04, 'icon': 3.13, 'meteo': 2.95, 'noaa': 1.89, 'sg': 2.95}, 'swellPeriod': {'dwd': 12.25, 'icon': 12.55, 'meteo': 11.5, 'noaa': 14.01, 'sg': 11.5}, 'time': '2022-03-06T03:00:00+00:00', 'waveDirection': {'icon': 301.89, 'meteo': 300.41, 'noaa': 314.21, 'sg': 300.41}, 'windSpeed': {'icon': 2.29, 'noaa': 1.88, 'sg': 2.29}}, {'airTemperature': {'dwd': 8.03, 'noaa': 2.69, 'sg': 8.03}, 'swellDirection': {'dwd': 331.16, 'icon': 301.95, 'meteo': 294.36, 'noaa': 313.71, 'sg': 294.36}, 'swellHeight': {'dwd': 2.01, 'icon': 3.11, 'meteo': 2.9, 'noaa': 1.83, 'sg': 2.9}, 'swellPeriod': {'dwd': 12.18, 'icon': 12.44, 'meteo': 11.4, 'noaa': 13.85, 'sg': 11.4}, 'time': '2022-03-06T04:00:00+00:00', 'waveDirection': {'icon': 301.95, 'meteo': 300.35, 'noaa': 313.94, 'sg': 300.35}, 'windSpeed': {'icon': 1.72, 
    'noaa': 2.06, 'sg': 1.72}}, {'airTemperature': {'dwd': 7.9, 'noaa': 2.46, 'sg': 7.9}, 'swellDirection': {'dwd': 330.78, 'icon': 302.0, 'meteo': 293.97, 'noaa': 313.33, 'sg': 293.97}, 'swellHeight': {'dwd': 1.99, 'icon': 3.08, 'meteo': 2.84, 'noaa': 1.77, 'sg': 2.84}, 'swellPeriod': {'dwd': 12.07, 'icon': 12.34, 'meteo': 11.31, 'noaa': 13.7, 'sg': 11.31}, 'time': '2022-03-06T05:00:00+00:00', 'waveDirection': {'icon': 302.0, 'meteo': 300.3, 'noaa': 313.68, 'sg': 300.3}, 'windSpeed': {'icon': 1.14, 'noaa': 2.24, 'sg': 1.14}}, {'airTemperature': {'dwd': 7.86, 'noaa': 2.23, 'sg': 7.86}, 'swellDirection': {'dwd': 330.8, 'icon': 302.06, 'meteo': 293.58, 'noaa': 312.96, 'sg': 293.58}, 'swellHeight': {'dwd': 1.96, 'icon': 3.06, 'meteo': 2.79, 'noaa': 1.71, 'sg': 2.79}, 'swellPeriod': {'dwd': 11.87, 'icon': 12.23, 'meteo': 11.21, 'noaa': 13.54, 'sg': 11.21}, 'time': '2022-03-06T06:00:00+00:00', 'waveDirection': {'icon': 302.06, 'meteo': 300.24, 'noaa': 313.41, 'sg': 300.24}, 'windSpeed': {'icon': 0.57, 'noaa': 2.42, 'sg': 0.57}}, {'airTemperature': {'dwd': 7.68, 'noaa': 3.14, 'sg': 7.68}, 'swellDirection': {'dwd': 331.14, 'icon': 302.79, 'meteo': 293.22, 'noaa': 312.73, 'sg': 293.22}, 'swellHeight': {'dwd': 1.94, 'icon': 3.02, 'meteo': 2.7, 'noaa': 1.65, 'sg': 2.7}, 'swellPeriod': {'dwd': 11.63, 'icon': 12.06, 'meteo': 11.12, 'noaa': 13.41, 'sg': 11.12}, 'time': '2022-03-06T07:00:00+00:00', 'waveDirection': {'icon': 302.8, 'meteo': 301.01, 'noaa': 313.46, 'sg': 301.01}, 'windSpeed': {'icon': 1.52, 'noaa': 2.18, 'sg': 1.52}}, {'airTemperature': {'dwd': 7.5, 'noaa': 4.06, 'sg': 
    7.5}, 'swellDirection': {'dwd': 331.66, 'icon': 303.53, 'meteo': 292.85, 'noaa': 312.49, 'sg': 292.85}, 'swellHeight': {'dwd': 1.93, 'icon': 2.97, 'meteo': 2.6, 'noaa': 1.58, 'sg': 2.6}, 'swellPeriod': {'dwd': 11.38, 'icon': 11.89, 'meteo': 11.04, 'noaa': 13.29, 'sg': 11.04}, 'time': '2022-03-06T08:00:00+00:00', 'waveDirection': {'icon': 303.54, 'meteo': 301.79, 'noaa': 313.52, 'sg': 301.79}, 'windSpeed': {'icon': 2.48, 'noaa': 1.95, 'sg': 2.48}}, {'airTemperature': {'dwd': 7.59, 'noaa': 4.97, 'sg': 7.59}, 'swellDirection': {'dwd': 332.55, 'icon': 304.26, 'meteo': 292.49, 'noaa': 312.26, 'sg': 292.49}, 'swellHeight': {'dwd': 1.9, 'icon': 2.93, 'meteo': 2.51, 'noaa': 1.52, 'sg': 2.51}, 'swellPeriod': {'dwd': 11.11, 'icon': 11.72, 'meteo': 10.95, 'noaa': 13.16, 'sg': 10.95}, 'time': '2022-03-06T09:00:00+00:00', 'waveDirection': {'icon': 304.28, 'meteo': 302.56, 'noaa': 313.57, 'sg': 302.56}, 'windSpeed': {'icon': 3.43, 'noaa': 1.71, 'sg': 3.43}}, {'airTemperature': {'dwd': 7.82, 'noaa': 5.97, 'sg': 7.82}, 'swellDirection': {'dwd': 333.62, 'icon': 305.18, 'meteo': 292.36, 'noaa': 314.94, 'sg': 292.36}, 'swellHeight': {'dwd': 1.87, 'icon': 2.88, 'meteo': 2.41, 'noaa': 1.47, 'sg': 2.41}, 'swellPeriod': {'dwd': 10.86, 'icon': 11.57, 'meteo': 10.85, 'noaa': 12.54, 'sg': 10.85}, 'time': '2022-03-06T10:00:00+00:00', 'waveDirection': {'icon': 305.19, 'meteo': 304.15, 'noaa': 313.36, 'sg': 304.15}, 'windSpeed': {'icon': 2.95, 'noaa': 1.56, 'sg': 2.95}}, {'airTemperature': {'dwd': 8.14, 'noaa': 6.97, 'sg': 8.14}, 'swellDirection': {'dwd': 334.87, 'icon': 306.09, 'meteo': 292.22, 'noaa': 317.63, 'sg': 292.22}, 'swellHeight': {'dwd': 1.86, 'icon': 2.82, 'meteo': 2.32, 'noaa': 1.41, 'sg': 2.32}, 'swellPeriod': {'dwd': 10.62, 'icon': 11.41, 'meteo': 10.76, 'noaa': 11.92, 'sg': 10.76}, 'time': '2022-03-06T11:00:00+00:00', 'waveDirection': {'icon': 306.1, 'meteo': 305.73, 'noaa': 313.15, 'sg': 305.73}, 'windSpeed': {'icon': 2.47, 'noaa': 1.41, 'sg': 2.47}}, {'airTemperature': {'dwd': 8.34, 'noaa': 7.97, 'sg': 8.34}, 'swellDirection': {'dwd': 336.21, 'icon': 307.01, 'meteo': 292.09, 'noaa': 320.31, 'sg': 292.09}, 'swellHeight': {'dwd': 1.84, 'icon': 2.77, 'meteo': 2.22, 'noaa': 1.36, 'sg': 2.22}, 'swellPeriod': {'dwd': 10.39, 'icon': 11.26, 'meteo': 10.66, 'noaa': 11.3, 'sg': 10.66}, 'time': '2022-03-06T12:00:00+00:00', 'waveDirection': {'icon': 307.01, 'meteo': 307.32, 'noaa': 312.94, 'sg': 307.32}, 'windSpeed': {'icon': 1.99, 'noaa': 1.26, 'sg': 1.99}}, {'airTemperature': {'dwd': 8.55, 'noaa': 8.15, 'sg': 8.55}, 'swellDirection': {'dwd': 337.53, 'icon': 308.14, 'meteo': 292.02, 'noaa': 323.2, 'sg': 292.02}, 'swellHeight': {'dwd': 1.83, 'icon': 2.72, 'meteo': 2.13, 'noaa': 1.34, 'sg': 2.13}, 'swellPeriod': {'dwd': 10.19, 'icon': 11.12, 'meteo': 10.58, 'noaa': 10.82, 'sg': 10.58}, 'time': '2022-03-06T13:00:00+00:00', 'waveDirection': {'icon': 308.14, 'meteo': 309.03, 'noaa': 313.43, 'sg': 309.03}, 'windSpeed': {'icon': 2.34, 'noaa': 1.71, 'sg': 2.34}}, {'airTemperature': {'dwd': 8.74, 'noaa': 8.33, 'sg': 8.74}, 'swellDirection': {'dwd': 338.77, 'icon': 309.28, 'meteo': 291.95, 'noaa': 326.09, 'sg': 291.95}, 'swellHeight': {'dwd': 1.81, 'icon': 2.66, 'meteo': 2.04, 'noaa': 1.32, 'sg': 2.04}, 'swellPeriod': {'dwd': 10.01, 'icon': 10.97, 'meteo': 10.51, 'noaa': 10.35, 'sg': 10.51}, 'time': '2022-03-06T14:00:00+00:00', 'waveDirection': {'icon': 309.28, 'meteo': 310.73, 'noaa': 313.93, 'sg': 310.73}, 'windSpeed': {'icon': 2.69, 'noaa': 2.15, 'sg': 2.69}}, {'airTemperature': {'dwd': 9.04, 'noaa': 8.51, 'sg': 9.04}, 'swellDirection': {'dwd': 339.94, 'icon': 310.41, 'meteo': 291.88, 'noaa': 328.98, 'sg': 291.88}, 'swellHeight': {'dwd': 1.78, 'icon': 2.61, 'meteo': 1.95, 'noaa': 1.3, 'sg': 1.95}, 'swellPeriod': {'dwd': 9.85, 'icon': 10.83, 'meteo': 10.43, 'noaa': 9.87, 'sg': 10.43}, 'time': '2022-03-06T15:00:00+00:00', 'waveDirection': {'icon': 310.41, 'meteo': 312.44, 'noaa': 314.42, 'sg': 312.44}, 'windSpeed': {'icon': 3.04, 'noaa': 2.6, 'sg': 3.04}}, {'airTemperature': {'dwd': 9.17, 'noaa': 7.68, 'sg': 9.17}, 'swellDirection': {'dwd': 341.01, 'icon': 311.4, 'meteo': 292.78, 'noaa': 338.67, 'sg': 292.78}, 'swellHeight': {'dwd': 1.76, 'icon': 2.56, 'meteo': 1.84, 'noaa': 1.3, 'sg': 1.84}, 'swellPeriod': {'dwd': 9.7, 'icon': 10.72, 'meteo': 10.26, 'noaa': 9.08, 'sg': 10.26}, 'time': '2022-03-06T16:00:00+00:00', 'waveDirection': {'icon': 311.4, 'meteo': 313.59, 'noaa': 313.78, 'sg': 313.59}, 'windSpeed': {'icon': 2.92, 'noaa': 1.93, 'sg': 2.92}}, {'airTemperature': {'dwd': 9.24, 'noaa': 6.85, 'sg': 9.24}, 'swellDirection': {'dwd': 341.93, 'icon': 312.38, 'meteo': 293.67, 'noaa': 348.37, 'sg': 293.67}, 'swellHeight': {'dwd': 1.74, 'icon': 2.5, 'meteo': 1.73, 'noaa': 1.29, 'sg': 1.73}, 'swellPeriod': {'dwd': 9.57, 'icon': 10.61, 'meteo': 10.1, 'noaa': 8.28, 'sg': 10.1}, 'time': '2022-03-06T17:00:00+00:00', 'waveDirection': {'icon': 312.38, 'meteo': 314.73, 'noaa': 313.13, 'sg': 314.73}, 'windSpeed': {'icon': 2.8, 'noaa': 1.27, 'sg': 2.8}}, {'airTemperature': {'dwd': 9.19, 'noaa': 6.02, 'sg': 9.19}, 'swellDirection': {'dwd': 342.65, 'icon': 313.37, 'meteo': 294.57, 'noaa': 358.06, 'sg': 294.57}, 'swellHeight': {'dwd': 1.71, 'icon': 2.45, 'meteo': 1.62, 'noaa': 1.29, 'sg': 1.62}, 'swellPeriod': {'dwd': 9.45, 'icon': 10.5, 'meteo': 9.93, 'noaa': 7.49, 'sg': 9.93}, 'time': '2022-03-06T18:00:00+00:00', 'waveDirection': {'icon': 313.37, 'meteo': 315.88, 'noaa': 312.49, 'sg': 315.88}, 'windSpeed': {'icon': 2.68, 'noaa': 0.6, 'sg': 2.68}}, {'airTemperature': {'dwd': 9.08, 'noaa': 5.21, 'sg': 9.08}, 'swellDirection': {'dwd': 343.12, 'icon': 314.04, 'meteo': 293.6, 'noaa': 346.19, 'sg': 293.6}, 'swellHeight': {'dwd': 1.68, 'icon': 2.4, 'meteo': 1.6, 'noaa': 1.05, 'sg': 1.6}, 'swellPeriod': {'dwd': 9.36, 'icon': 10.42, 'meteo': 9.94, 'noaa': 8.91, 'sg': 9.94}, 'time': '2022-03-06T19:00:00+00:00', 'waveDirection': {'icon': 314.04, 'meteo': 316.36, 'noaa': 312.93, 'sg': 316.36}, 'windSpeed': {'icon': 2.1, 'noaa': 0.98, 'sg': 2.1}}, {'airTemperature': {'dwd': 8.98, 'noaa': 4.4, 'sg': 8.98}, 'swellDirection': {'dwd': 343.39, 'icon': 314.7, 'meteo': 292.63, 'noaa': 334.33, 'sg': 292.63}, 'swellHeight': {'dwd': 1.64, 'icon': 
    2.35, 'meteo': 1.57, 'noaa': 0.8, 'sg': 1.57}, 'swellPeriod': {'dwd': 9.28, 'icon': 10.34, 'meteo': 9.94, 'noaa': 10.32, 'sg': 9.94}, 'time': '2022-03-06T20:00:00+00:00', 'waveDirection': {'icon': 314.7, 'meteo': 316.84, 'noaa': 313.36, 'sg': 316.84}, 'windSpeed': {'icon': 1.53, 'noaa': 1.35, 'sg': 1.53}}, {'airTemperature': {'dwd': 8.94, 'noaa': 3.6, 
    'sg': 8.94}, 'swellDirection': {'dwd': 343.48, 'icon': 315.37, 'meteo': 291.66, 'noaa': 322.46, 'sg': 291.66}, 'swellHeight': {'dwd': 1.6, 'icon': 2.3, 'meteo': 1.55, 'noaa': 0.56, 'sg': 1.55}, 'swellPeriod': {'dwd': 9.22, 'icon': 10.26, 'meteo': 9.95, 'noaa': 11.74, 'sg': 9.95}, 'time': '2022-03-06T21:00:00+00:00', 'waveDirection': {'icon': 315.37, 'meteo': 317.32, 'noaa': 313.8, 'sg': 317.32}, 'windSpeed': {'icon': 0.95, 'noaa': 1.73, 'sg': 0.95}}, {'airTemperature': {'dwd': 8.86, 'noaa': 3.37, 'sg': 8.86}, 'swellDirection': {'dwd': 343.44, 'icon': 315.84, 'meteo': 291.53, 'noaa': 334.76, 'sg': 291.53}, 'swellHeight': {'dwd': 1.56, 'icon': 2.26, 'meteo': 1.49, 'noaa': 0.73, 'sg': 1.49}, 'swellPeriod': {'dwd': 9.16, 'icon': 10.2, 'meteo': 9.88, 'noaa': 10.22, 'sg': 9.88}, 'time': '2022-03-06T22:00:00+00:00', 'waveDirection': {'icon': 315.84, 'meteo': 317.57, 'noaa': 313.36, 'sg': 317.57}, 'windSpeed': {'icon': 0.92, 'noaa': 1.7, 'sg': 0.92}}, {'airTemperature': {'dwd': 8.77, 'noaa': 3.15, 'sg': 8.77}, 'swellDirection': {'dwd': 343.35, 'icon': 316.32, 'meteo': 291.4, 'noaa': 347.07, 'sg': 291.4}, 'swellHeight': {'dwd': 1.52, 'icon': 2.21, 'meteo': 1.44, 'noaa': 0.91, 'sg': 1.44}, 'swellPeriod': {'dwd': 9.12, 'icon': 10.14, 'meteo': 9.8, 'noaa': 8.69, 'sg': 9.8}, 'time': '2022-03-06T23:00:00+00:00', 'waveDirection': {'icon': 316.32, 'meteo': 317.81, 'noaa': 312.93, 'sg': 317.81}, 'windSpeed': {'icon': 0.89, 'noaa': 1.67, 'sg': 0.89}}, {'airTemperature': {'dwd': 8.5, 'noaa': 2.92, 'sg': 8.5}, 'swellDirection': {'dwd': 343.25, 'icon': 316.79, 'meteo': 291.27, 'noaa': 359.37, 'sg': 291.27}, 'swellHeight': {'dwd': 1.48, 'icon': 2.17, 'meteo': 1.38, 'noaa': 1.08, 'sg': 1.38}, 'swellPeriod': {'dwd': 9.08, 'icon': 10.08, 'meteo': 9.73, 'noaa': 7.17, 'sg': 9.73}, 'time': '2022-03-07T00:00:00+00:00', 'waveDirection': {'icon': 316.79, 'meteo': 318.06, 'noaa': 312.49, 'sg': 318.06}, 'windSpeed': {'icon': 0.86, 'noaa': 1.64, 'sg': 0.86}}, {'airTemperature': {'dwd': 8.21, 'noaa': 2.65, 'sg': 8.21}, 'swellDirection': {'dwd': 343.18, 'icon': 317.12, 'meteo': 291.15, 'noaa': 346.18, 'sg': 291.15}, 'swellHeight': {'dwd': 1.44, 'icon': 2.13, 'meteo': 1.33, 'noaa': 0.9, 'sg': 1.33}, 'swellPeriod': {'dwd': 9.04, 'icon': 10.03, 'meteo': 9.64, 'noaa': 8.61, 'sg': 9.64}, 'time': '2022-03-07T01:00:00+00:00', 'waveDirection': {'icon': 317.12, 'meteo': 318.54, 'noaa': 312.37, 'sg': 318.54}, 'windSpeed': {'icon': 0.92, 'noaa': 1.7, 'sg': 0.92}}, {'airTemperature': {'dwd': 7.88, 'noaa': 2.38, 'sg': 7.88}, 'swellDirection': {'dwd': 343.18, 'icon': 317.45, 'meteo': 291.03, 'noaa': 333.0, 'sg': 291.03}, 'swellHeight': {'dwd': 1.41, 'icon': 2.09, 'meteo': 1.29, 'noaa': 0.71, 'sg': 1.29}, 'swellPeriod': {'dwd': 9.01, 'icon': 9.99, 'meteo': 9.55, 'noaa': 10.06, 'sg': 9.55}, 'time': '2022-03-07T02:00:00+00:00', 'waveDirection': {'icon': 317.45, 'meteo': 319.01, 'noaa': 312.24, 'sg': 319.01}, 'windSpeed': {'icon': 0.98, 'noaa': 1.76, 'sg': 0.98}}, {'airTemperature': {'dwd': 7.5, 'noaa': 2.11, 'sg': 7.5}, 'swellDirection': {'dwd': 343.29, 'icon': 317.78, 'meteo': 290.91, 'noaa': 319.81, 'sg': 290.91}, 'swellHeight': {'dwd': 1.37, 'icon': 2.05, 'meteo': 1.24, 'noaa': 0.53, 'sg': 1.24}, 'swellPeriod': {'dwd': 8.97, 'icon': 9.94, 'meteo': 9.46, 'noaa': 11.5, 'sg': 9.46}, 'time': '2022-03-07T03:00:00+00:00', 'waveDirection': {'icon': 317.78, 'meteo': 319.49, 'noaa': 312.12, 'sg': 319.49}, 'windSpeed': {'icon': 1.04, 'noaa': 1.82, 'sg': 1.04}}, {'airTemperature': {'dwd': 7.1, 'noaa': 2.02, 'sg': 7.1}, 'swellDirection': {'dwd': 343.57, 'icon': 317.94, 'meteo': 293.98, 'noaa': 322.31, 'sg': 293.98}, 'swellHeight': {'dwd': 1.34, 'icon': 2.01, 'meteo': 1.2, 'noaa': 0.44, 'sg': 1.2}, 'swellPeriod': {'dwd': 8.94, 'icon': 9.91, 'meteo': 9.19, 'noaa': 12.27, 'sg': 9.19}, 'time': '2022-03-07T04:00:00+00:00', 'waveDirection': {'icon': 317.94, 'meteo': 320.56, 'noaa': 312.04, 'sg': 320.56}, 'windSpeed': {'icon': 1.24, 'noaa': 1.88, 'sg': 1.24}}, {'airTemperature': {'dwd': 6.55, 'noaa': 1.94, 'sg': 6.55}, 'swellDirection': {'dwd': 344.08, 'icon': 318.1, 'meteo': 297.04, 'noaa': 324.81, 'sg': 297.04}, 'swellHeight': {'dwd': 1.31, 'icon': 1.97, 'meteo': 1.16, 'noaa': 0.34, 'sg': 1.16}, 'swellPeriod': {'dwd': 8.89, 'icon': 9.87, 'meteo': 8.93, 'noaa': 13.03, 'sg': 8.93}, 'time': '2022-03-07T05:00:00+00:00', 'waveDirection': {'icon': 318.1, 'meteo': 321.62, 'noaa': 311.97, 'sg': 321.62}, 'windSpeed': 
    {'icon': 1.43, 'noaa': 1.94, 'sg': 1.43}}, {'airTemperature': {'dwd': 6.06, 'noaa': 1.85, 'sg': 6.06}, 'swellDirection': {'dwd': 344.89, 'icon': 318.26, 'meteo': 300.11, 'noaa': 327.31, 'sg': 300.11}, 'swellHeight': {'dwd': 1.29, 'icon': 1.93, 'meteo': 1.12, 'noaa': 0.25, 'sg': 1.12}, 'swellPeriod': {'dwd': 8.84, 'icon': 9.84, 'meteo': 8.66, 'noaa': 13.8, 'sg': 8.66}, 'time': '2022-03-07T06:00:00+00:00', 'waveDirection': {'icon': 318.26, 'meteo': 322.69, 'noaa': 311.89, 'sg': 322.69}, 'windSpeed': {'icon': 1.63, 'noaa': 2.0, 
    'sg': 1.63}}, {'airTemperature': {'dwd': 6.02, 'noaa': 3.39, 'sg': 6.02}, 'swellDirection': {'dwd': 346.0, 'icon': 318.27, 'meteo': 299.95, 'noaa': 327.31, 'sg': 299.95}, 'swellHeight': {'dwd': 1.28, 'icon': 1.89, 'meteo': 1.08, 'noaa': 0.22, 'sg': 1.08}, 'swellPeriod': {'dwd': 8.77, 'icon': 9.82, 'meteo': 8.59, 'noaa': 13.64, 'sg': 8.59}, 'time': '2022-03-07T07:00:00+00:00', 'waveDirection': {'icon': 318.27, 'meteo': 323.41, 'noaa': 311.53, 'sg': 323.41}, 'windSpeed': {'icon': 1.8, 'noaa': 1.67, 'sg': 1.8}}, {'airTemperature': {'dwd': 6.07, 'noaa': 4.92, 'sg': 6.07}, 'swellDirection': {'dwd': 347.28, 'icon': 318.29, 'meteo': 299.78, 'noaa': 327.3, 'sg': 299.78}, 'swellHeight': {'dwd': 1.26, 'icon': 1.86, 'meteo': 1.04, 'noaa': 0.2, 'sg': 1.04}, 'swellPeriod': {'dwd': 8.7, 'icon': 9.79, 'meteo': 8.53, 'noaa': 13.49, 'sg': 8.53}, 'time': '2022-03-07T08:00:00+00:00', 'waveDirection': {'icon': 318.29, 'meteo': 324.12, 'noaa': 311.17, 'sg': 324.12}, 'windSpeed': {'icon': 1.96, 'noaa': 1.34, 'sg': 1.96}}, {'airTemperature': {'dwd': 6.58, 'noaa': 6.46, 'sg': 6.58}, 'swellDirection': {'dwd': 348.44, 'icon': 318.3, 'meteo': 299.62, 'noaa': 327.3, 'sg': 299.62}, 'swellHeight': {'dwd': 1.25, 'icon': 1.82, 'meteo': 1.0, 'noaa': 0.17, 'sg': 1.0}, 'swellPeriod': {'dwd': 8.65, 'icon': 9.77, 'meteo': 8.46, 'noaa': 13.33, 'sg': 8.46}, 'time': '2022-03-07T09:00:00+00:00', 'waveDirection': {'icon': 318.3, 'meteo': 324.84, 'noaa': 310.81, 'sg': 324.84}, 'windSpeed': {'icon': 2.13, 'noaa': 1.01, 'sg': 2.13}}, {'airTemperature': {'dwd': 7.71, 'noaa': 7.93, 'sg': 7.71}, 'swellDirection': 
    {'dwd': 349.28, 'icon': 318.15, 'meteo': 296.02, 'noaa': 327.01, 'sg': 296.02}, 'swellHeight': {'dwd': 1.23, 'icon': 1.79, 'meteo': 0.97, 'noaa': 0.19, 'sg': 0.97}, 'swellPeriod': {'dwd': 8.62, 'icon': 9.77, 'meteo': 8.59, 'noaa': 13.22, 'sg': 8.59}, 'time': '2022-03-07T10:00:00+00:00', 'waveDirection': {'icon': 318.15, 'meteo': 324.99, 'noaa': 310.65, 'sg': 324.99}, 'windSpeed': {'icon': 2.54, 'noaa': 1.49, 'sg': 2.54}}, {'airTemperature': {'dwd': 8.47, 'noaa': 9.39, 'sg': 8.47}, 'swellDirection': {'dwd': 349.74, 'icon': 317.99, 'meteo': 292.43, 'noaa': 326.71, 'sg': 292.43}, 'swellHeight': {'dwd': 1.21, 'icon': 1.75, 'meteo': 0.94, 'noaa': 0.21, 'sg': 0.94}, 'swellPeriod': {'dwd': 8.62, 'icon': 9.77, 'meteo': 8.73, 'noaa': 13.11, 'sg': 8.73}, 'time': '2022-03-07T11:00:00+00:00', 'waveDirection': {'icon': 317.99, 'meteo': 325.15, 'noaa': 310.48, 'sg': 325.15}, 'windSpeed': {'icon': 2.94, 'noaa': 1.96, 'sg': 2.94}}, {'airTemperature': {'dwd': 9.15, 'noaa': 10.86, 'sg': 9.15}, 'swellDirection': {'dwd': 349.86, 'icon': 317.84, 'meteo': 288.83, 'noaa': 326.42, 'sg': 288.83}, 'swellHeight': {'dwd': 1.18, 'icon': 1.72, 'meteo': 0.91, 'noaa': 0.23, 'sg': 0.91}, 'swellPeriod': {'dwd': 8.66, 'icon': 9.77, 'meteo': 8.86, 'noaa': 13.0, 'sg': 8.86}, 'time': '2022-03-07T12:00:00+00:00', 'waveDirection': {'icon': 317.84, 'meteo': 325.3, 'noaa': 310.32, 'sg': 325.3}, 'windSpeed': {'icon': 3.35, 'noaa': 2.44, 'sg': 3.35}}, {'airTemperature': {'dwd': 9.69, 'noaa': 10.75, 'sg': 9.69}, 'swellDirection': {'dwd': 349.56, 'icon': 317.26, 'meteo': 288.51, 'noaa': 325.16, 'sg': 288.51}, 'swellHeight': {'dwd': 1.14, 'icon': 1.69, 'meteo': 0.88, 'noaa': 0.22, 'sg': 0.88}, 'swellPeriod': {'dwd': 8.75, 'icon': 9.82, 'meteo': 8.79, 'noaa': 13.26, 'sg': 8.79}, 'time': 
    '2022-03-07T13:00:00+00:00', 'waveDirection': {'icon': 317.95, 'meteo': 325.93, 'noaa': 310.21, 'sg': 325.93}, 'windSpeed': {'icon': 4.6, 'noaa': 2.65, 'sg': 4.6}}, {'airTemperature': {'dwd': 10.05, 'noaa': 10.65, 'sg': 10.05}, 'swellDirection': {'dwd': 348.87, 'icon': 316.68, 'meteo': 288.18, 'noaa': 323.91, 'sg': 288.18}, 'swellHeight': {'dwd': 1.11, 'icon': 1.65, 'meteo': 0.84, 'noaa': 0.21, 'sg': 0.84}, 'swellPeriod': {'dwd': 8.88, 'icon': 9.86, 'meteo': 8.72, 'noaa': 13.52, 'sg': 8.72}, 'time': '2022-03-07T14:00:00+00:00', 'waveDirection': {'icon': 318.05, 'meteo': 326.56, 'noaa': 310.1, 'sg': 326.56}, 'windSpeed': {'icon': 5.85, 'noaa': 2.85, 'sg': 5.85}}, {'airTemperature': {'dwd': 10.27, 'noaa': 10.54, 'sg': 10.27}, 'swellDirection': {'dwd': 348.77, 'icon': 316.1, 'meteo': 287.86, 'noaa': 322.65, 'sg': 287.86}, 'swellHeight': {'dwd': 1.09, 'icon': 1.62, 'meteo': 0.81, 'noaa': 0.2, 'sg': 0.81}, 'swellPeriod': {'dwd': 8.94, 'icon': 9.91, 'meteo': 8.65, 'noaa': 13.78, 'sg': 8.65}, 'time': '2022-03-07T15:00:00+00:00', 'waveDirection': {'icon': 318.16, 'meteo': 327.19, 'noaa': 309.99, 'sg': 327.19}, 'windSpeed': {'icon': 7.1, 'noaa': 3.06, 'sg': 7.1}}, {'airTemperature': {'dwd': 10.61, 'noaa': 9.37, 'sg': 10.61}, 'swellDirection': {'dwd': 352.52, 'icon': 316.57, 'meteo': 293.64, 'noaa': 321.5, 'sg': 293.64}, 'swellHeight': {'dwd': 1.11, 'icon': 1.6, 'meteo': 0.79, 'noaa': 0.22, 'sg': 0.79}, 'swellPeriod': {'dwd': 8.67, 'icon': 9.88, 'meteo': 9.87, 'noaa': 14.03, 'sg': 9.87}, 'time': '2022-03-07T16:00:00+00:00', 'waveDirection': {'icon': 322.42, 'meteo': 327.58, 'noaa': 309.46, 'sg': 327.58}, 'windSpeed': {'icon': 7.39, 'noaa': 2.92, 'sg': 7.39}}, {'airTemperature': {'dwd': 10.91, 'noaa': 8.2, 'sg': 10.91}, 'swellDirection': {'dwd': 357.72, 'icon': 317.04, 'meteo': 299.43, 'noaa': 320.35, 'sg': 299.43}, 'swellHeight': {'dwd': 1.14, 'icon': 1.58, 'meteo': 0.76, 'noaa': 0.25, 'sg': 0.76}, 'swellPeriod': {'dwd': 8.42, 'icon': 9.85, 'meteo': 11.09, 'noaa': 14.27, 'sg': 11.09}, 'time': '2022-03-07T17:00:00+00:00', 'waveDirection': {'icon': 326.67, 'meteo': 327.98, 'noaa': 308.94, 'sg': 327.98}, 'windSpeed': {'icon': 7.68, 'noaa': 2.77, 'sg': 7.68}}, {'airTemperature': {'dwd': 11.09, 'noaa': 7.03, 'sg': 11.09}, 'swellDirection': {'dwd': 6.45, 'icon': 317.51, 'meteo': 305.21, 'noaa': 319.2, 'sg': 305.21}, 'swellHeight': {'dwd': 1.2, 'icon': 1.56, 'meteo': 0.74, 'noaa': 0.27, 'sg': 0.74}, 'swellPeriod': {'dwd': 8.06, 'icon': 9.82, 'meteo': 
    12.31, 'noaa': 14.52, 'sg': 12.31}, 'time': '2022-03-07T18:00:00+00:00', 'waveDirection': {'icon': 330.93, 'meteo': 328.37, 'noaa': 308.41, 'sg': 328.37}, 'windSpeed': {'icon': 
    7.97, 'noaa': 2.63, 'sg': 7.97}}, {'airTemperature': {'dwd': 11.17, 'noaa': 6.48, 'sg': 11.17}, 'swellDirection': {'dwd': 12.13, 'icon': 319.56, 'meteo': 305.35, 'noaa': 320.19, 'sg': 305.35}, 'swellHeight': {'dwd': 1.24, 'icon': 1.56, 'meteo': 0.77, 'noaa': 0.29, 'sg': 0.77}, 'swellPeriod': {'dwd': 7.95, 'icon': 9.72, 'meteo': 12.22, 'noaa': 14.59, 'sg': 12.22}, 'time': '2022-03-07T19:00:00+00:00', 'waveDirection': {'icon': 334.15, 'meteo': 329.47, 'noaa': 316.03, 'sg': 329.47}, 'windSpeed': {'icon': 7.68, 'noaa': 2.39, 'sg': 7.68}}, {'airTemperature': {'dwd': 11.09, 'noaa': 5.94, 'sg': 11.09}, 'swellDirection': {'dwd': 20.39, 'icon': 321.62, 'meteo': 305.49, 'noaa': 321.19, 'sg': 305.49}, 'swellHeight': {'dwd': 1.3, 'icon': 1.55, 'meteo': 0.79, 'noaa': 0.3, 'sg': 0.79}, 'swellPeriod': {'dwd': 7.72, 'icon': 9.62, 'meteo': 12.14, 'noaa': 14.66, 'sg': 12.14}, 'time': '2022-03-07T20:00:00+00:00', 'waveDirection': {'icon': 337.36, 'meteo': 330.57, 'noaa': 323.66, 'sg': 330.57}, 'windSpeed': {'icon': 7.38, 'noaa': 2.16, 'sg': 7.38}}, {'airTemperature': {'dwd': 11.1, 'noaa': 5.39, 'sg': 11.1}, 'swellDirection': {'dwd': 25.54, 'icon': 323.67, 'meteo': 305.63, 'noaa': 322.18, 'sg': 305.63}, 'swellHeight': {'dwd': 1.35, 'icon': 1.55, 'meteo': 0.82, 'noaa': 0.32, 'sg': 0.82}, 'swellPeriod': {'dwd': 7.69, 'icon': 9.52, 'meteo': 12.05, 'noaa': 14.73, 'sg': 12.05}, 'time': '2022-03-07T21:00:00+00:00', 'waveDirection': {'icon': 340.58, 'meteo': 331.67, 'noaa': 331.28, 'sg': 331.67}, 'windSpeed': {'icon': 7.09, 'noaa': 1.92, 'sg': 7.09}}, {'airTemperature': {'dwd': 11.08, 'noaa': 
    5.99, 'sg': 11.08}, 'swellDirection': {'dwd': 27.78, 'icon': 328.17, 'meteo': 305.17, 'noaa': 317.46, 'sg': 305.17}, 'swellHeight': {'dwd': 1.35, 'icon': 1.57, 'meteo': 0.87, 'noaa': 0.36, 'sg': 0.87}, 'swellPeriod': {'dwd': 7.8, 'icon': 9.3, 'meteo': 11.74, 'noaa': 13.59, 'sg': 11.74}, 'time': '2022-03-07T22:00:00+00:00', 'waveDirection': {'icon': 339.72, 'meteo': 330.47, 'noaa': 328.22, 'sg': 330.47}, 'windSpeed': {'icon': 6.11, 'noaa': 1.95, 'sg': 6.11}}, {'airTemperature': {'dwd': 10.61, 'noaa': 6.6, 'sg': 10.61}, 'swellDirection': {'dwd': 28.6, 'icon': 332.68, 'meteo': 304.72, 'noaa': 312.75, 'sg': 304.72}, 'swellHeight': {'dwd': 1.33, 'icon': 1.58, 'meteo': 0.91, 'noaa': 0.41, 'sg': 0.91}, 'swellPeriod': {'dwd': 7.94, 'icon': 9.07, 'meteo': 11.44, 'noaa': 12.45, 'sg': 11.44}, 'time': '2022-03-07T23:00:00+00:00', 'waveDirection': {'icon': 338.85, 'meteo': 329.27, 'noaa': 325.16, 'sg': 329.27}, 'windSpeed': {'icon': 5.13, 'noaa': 1.99, 'sg': 5.13}}], 'meta': {'cost': 1, 'dailyQuota': 10, 'end': '2022-03-07 23:00', 'lat': 43.5694, 'lng': -5.722, 'params': ['airTemperature', 'windSpeed', 'waveDirection', 'swellPeriod', 'swellHeight', 'swellDirection'], 'requestCount': 2, 'start': '2022-03-05 23:00'}}
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
            print(x)
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

    print(DIRS)
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
    aux=0
    evento.set()
    while True:
        aux=0
    






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
