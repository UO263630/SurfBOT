from telegram import ChatAction,InlineKeyboardMarkup, InlineKeyboardButton, InlineQueryResultPhoto, InputMedia, InputMediaPhoto
import telegram
from telegram.ext import CallbackQueryHandler
import arrow
import requests
from tabulate import tabulate


from uuid import uuid4

#import telepot

import Graficas

TABLA1=[]
TABLA2=[]
TABLA3=[]
TABLA4=[]
DIRV=[]
DIRS=[]
DIRV2=[]
DIRS2=[]


buttonI = InlineKeyboardButton(
        text= "<--",
        callback_data='BI'
)
buttonD = InlineKeyboardButton(
        text= "--->",
        callback_data='BD'
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
        callback_data='BI2'
)
buttonD2 = InlineKeyboardButton(
        text= "--->",
        callback_data='BD2'
)

buttonGV2= InlineKeyboardButton(
        text= "Grafica de viento",
        callback_data='BGV2'
)

buttonGS2= InlineKeyboardButton(
        text= "Grafica de oleaje",
        callback_data='BGS2'
)

def Forecast(update,lat,lon,BOT_TOKEN,chat_id):

    la = lat
    lo = lon
    tz='UTC+1'
    global TABLA1,TABLA2,TABLA3,TABLA4,DIRV,DIRS,DIRV2,DIRS2


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
    json_data = {'hours': [{'airTemperature': {'dwd': 8.35, 'noaa': 4.48, 'sg': 8.35}, 'swellDirection': {'dwd': 317.9, 'icon': 309.31, 'meteo': 308.46, 'noaa': 319.98, 'sg': 308.46}, 'swellHeight': {'dwd': 2.97, 'icon': 3.32, 'meteo': 3.2, 'noaa': 2.44, 'sg': 3.2}, 'swellPeriod': {'dwd': 13.44, 'icon': 13.14, 'meteo': 10.68, 'noaa': 13.75, 'sg': 10.68}, 'time': '2022-02-22T23:00:00+00:00', 'waveDirection': {'icon': 309.31, 'meteo': 308.46, 'noaa': 318.78, 'sg': 308.46}, 'windSpeed': {'icon': 3.26, 'noaa': 1.62, 'sg': 3.26}}, {'airTemperature': {'dwd': 8.61, 'noaa': 4.47, 'sg': 8.61}, 'swellDirection': {'dwd': 317.59, 'icon': 308.89, 'meteo': 308.13, 'noaa': 319.54, 'sg': 308.13}, 'swellHeight': {'dwd': 2.9, 'icon': 3.24, 'meteo': 3.13, 'noaa': 2.4, 'sg': 3.13}, 'swellPeriod': {'dwd': 13.34, 'icon': 13.05, 'meteo': 10.65, 'noaa': 13.72, 'sg': 10.65}, 'time': '2022-02-23T00:00:00+00:00', 'waveDirection': {'icon': 308.89, 'meteo': 308.13, 'noaa': 318.36, 'sg': 308.13}, 'windSpeed': {'icon': 4.03, 'noaa': 1.63, 'sg': 4.03}}, {'airTemperature': {'dwd': 8.13, 'noaa': 4.39, 'sg': 8.13}, 'swellDirection': {'dwd': 317.23, 'icon': 308.39, 'meteo': 307.88, 'noaa': 319.27, 'sg': 307.88}, 'swellHeight': {'dwd': 2.83, 'icon': 3.2, 'meteo': 3.13, 'noaa': 2.43, 'sg': 3.13}, 'swellPeriod': {'dwd': 13.25, 'icon': 13.01, 'meteo': 10.68, 'noaa': 13.73, 'sg': 10.68}, 'time': '2022-02-23T01:00:00+00:00', 'waveDirection': {'icon': 308.39, 'meteo': 307.88, 'noaa': 318.24, 'sg': 307.88}, 'windSpeed': {'icon': 4.2, 'noaa': 1.53, 'sg': 4.2}}, {'airTemperature': {'dwd': 8.65, 'noaa': 4.31, 'sg': 8.65}, 'swellDirection': {'dwd': 316.83, 'icon': 307.88, 'meteo': 307.62, 'noaa': 318.99, 'sg': 307.62}, 'swellHeight': {'dwd': 2.79, 'icon': 3.17, 'meteo': 3.12, 'noaa': 2.45, 'sg': 3.12}, 
    'swellPeriod': {'dwd': 13.19, 'icon': 12.98, 'meteo': 10.72, 'noaa': 13.74, 'sg': 10.72}, 'time': '2022-02-23T02:00:00+00:00', 'waveDirection': {'icon': 307.89, 'meteo': 307.63, 'noaa': 318.13, 'sg': 307.63}, 'windSpeed': {'icon': 4.38, 'noaa': 1.43, 'sg': 4.38}}, {'airTemperature': {'dwd': 8.16, 'noaa': 4.23, 'sg': 8.16}, 'swellDirection': {'dwd': 316.4, 'icon': 307.38, 'meteo': 307.37, 'noaa': 318.72, 'sg': 307.37}, 'swellHeight': {'dwd': 2.75, 'icon': 3.13, 'meteo': 3.12, 'noaa': 2.48, 'sg': 3.12}, 'swellPeriod': {'dwd': 13.14, 'icon': 12.94, 'meteo': 10.75, 'noaa': 13.75, 'sg': 10.75}, 'time': '2022-02-23T03:00:00+00:00', 'waveDirection': {'icon': 307.39, 'meteo': 307.38, 'noaa': 318.01, 'sg': 307.38}, 'windSpeed': {'icon': 4.55, 'noaa': 1.33, 'sg': 4.55}}, {'airTemperature': {'dwd': 7.34, 'noaa': 4.06, 'sg': 7.34}, 'swellDirection': {'dwd': 315.94, 'icon': 306.85, 'meteo': 307.04, 'noaa': 318.34, 'sg': 307.04}, 'swellHeight': {'dwd': 2.73, 'icon': 3.13, 'meteo': 3.16, 'noaa': 2.53, 'sg': 3.16}, 'swellPeriod': {'dwd': 13.12, 'icon': 12.95, 'meteo': 10.82, 'noaa': 13.78, 'sg': 10.82}, 'time': '2022-02-23T04:00:00+00:00', 'waveDirection': {'icon': 306.87, 'meteo': 307.12, 'noaa': 317.61, 'sg': 307.12}, 'windSpeed': {'icon': 4.42, 'noaa': 1.35, 'sg': 4.42}}, {'airTemperature': {'dwd': 6.5, 'noaa': 3.89, 'sg': 6.5}, 'swellDirection': {'dwd': 315.47, 'icon': 306.33, 'meteo': 306.72, 'noaa': 317.96, 'sg': 306.72}, 'swellHeight': {'dwd': 2.72, 'icon': 3.13, 'meteo': 3.19, 'noaa': 2.57, 'sg': 3.19}, 'swellPeriod': {'dwd': 13.1, 'icon': 12.96, 'meteo': 10.88, 'noaa': 13.81, 'sg': 10.88}, 'time': '2022-02-23T05:00:00+00:00', 'waveDirection': {'icon': 306.34, 'meteo': 306.86, 'noaa': 317.21, 'sg': 306.86}, 'windSpeed': {'icon': 4.3, 'noaa': 1.38, 
    'sg': 4.3}}, {'airTemperature': {'dwd': 5.89, 'noaa': 3.71, 'sg': 5.89}, 'swellDirection': {'dwd': 315.0, 'icon': 305.8, 'meteo': 306.39, 'noaa': 317.58, 'sg': 306.39}, 'swellHeight': {'dwd': 2.72, 'icon': 3.13, 'meteo': 3.23, 'noaa': 2.62, 'sg': 3.23}, 'swellPeriod': {'dwd': 13.1, 'icon': 12.97, 'meteo': 10.95, 'noaa': 13.84, 'sg': 10.95}, 'time': '2022-02-23T06:00:00+00:00', 'waveDirection': {'icon': 305.82, 'meteo': 306.6, 'noaa': 316.81, 'sg': 306.6}, 'windSpeed': {'icon': 4.17, 'noaa': 1.4, 'sg': 4.17}}, {'airTemperature': {'dwd': 5.57, 'noaa': 5.17, 'sg': 5.57}, 'swellDirection': {'dwd': 314.54, 'icon': 305.35, 'meteo': 306.08, 'noaa': 317.06, 'sg': 306.08}, 'swellHeight': {'dwd': 2.73, 'icon': 3.14, 'meteo': 3.27, 'noaa': 2.61, 'sg': 3.27}, 'swellPeriod': {'dwd': 13.11, 'icon': 12.99, 'meteo': 11.01, 'noaa': 13.81, 'sg': 11.01}, 'time': '2022-02-23T07:00:00+00:00', 
    'waveDirection': {'icon': 305.4, 'meteo': 306.29, 'noaa': 316.17, 'sg': 306.29}, 'windSpeed': {'icon': 4.42, 'noaa': 1.21, 'sg': 4.42}}, {'airTemperature': {'dwd': 5.85, 'noaa': 6.63, 'sg': 5.85}, 'swellDirection': {'dwd': 314.1, 'icon': 304.9, 'meteo': 305.76, 'noaa': 316.54, 'sg': 305.76}, 'swellHeight': {'dwd': 2.73, 'icon': 3.16, 'meteo': 3.31, 'noaa': 2.6, 'sg': 3.31}, 'swellPeriod': {'dwd': 13.12, 'icon': 13.0, 'meteo': 11.07, 'noaa': 13.78, 'sg': 11.07}, 'time': '2022-02-23T08:00:00+00:00', 'waveDirection': {'icon': 304.99, 'meteo': 305.99, 'noaa': 315.53, 'sg': 305.99}, 'windSpeed': {'icon': 4.67, 'noaa': 1.03, 'sg': 4.67}}, {'airTemperature': {'dwd': 7.73, 'noaa': 8.09, 'sg': 7.73}, 'swellDirection': {'dwd': 313.72, 'icon': 304.45, 'meteo': 305.45, 'noaa': 316.02, 'sg': 305.45}, 'swellHeight': {'dwd': 2.74, 'icon': 3.17, 'meteo': 3.35, 'noaa': 2.59, 'sg': 3.35}, 'swellPeriod': {'dwd': 13.14, 'icon': 13.02, 'meteo': 11.13, 'noaa': 13.75, 'sg': 11.13}, 'time': '2022-02-23T09:00:00+00:00', 'waveDirection': {'icon': 304.57, 'meteo': 305.68, 
    'noaa': 314.89, 'sg': 305.68}, 'windSpeed': {'icon': 4.92, 'noaa': 0.84, 'sg': 4.92}}, {'airTemperature': {'dwd': 10.11, 'noaa': 9.77, 'sg': 10.11}, 'swellDirection': {'dwd': 313.41, 'icon': 304.18, 'meteo': 305.29, 'noaa': 315.63, 'sg': 305.29}, 'swellHeight': {'dwd': 2.74, 'icon': 3.18, 'meteo': 3.37, 'noaa': 2.55, 'sg': 3.37}, 'swellPeriod': {'dwd': 13.15, 'icon': 13.01, 'meteo': 11.16, 'noaa': 13.72, 'sg': 11.16}, 'time': '2022-02-23T10:00:00+00:00', 'waveDirection': {'icon': 304.48, 'meteo': 305.55, 'noaa': 314.13, 'sg': 305.55}, 'windSpeed': {'icon': 5.25, 'noaa': 1.03, 'sg': 5.25}}, {'airTemperature': {'dwd': 11.46, 'noaa': 11.44, 'sg': 11.46}, 'swellDirection': {'dwd': 313.16, 'icon': 303.91, 'meteo': 305.14, 'noaa': 315.25, 'sg': 305.14}, 'swellHeight': {'dwd': 2.74, 'icon': 3.2, 'meteo': 3.39, 'noaa': 2.51, 'sg': 3.39}, 'swellPeriod': {'dwd': 13.16, 'icon': 13.01, 'meteo': 11.19, 'noaa': 13.68, 'sg': 11.19}, 'time': '2022-02-23T11:00:00+00:00', 'waveDirection': {'icon': 304.38, 'meteo': 305.43, 'noaa': 313.36, 'sg': 305.43}, 'windSpeed': {'icon': 5.59, 'noaa': 1.23, 'sg': 5.59}}, {'airTemperature': {'dwd': 12.04, 'noaa': 13.12, 'sg': 12.04}, 'swellDirection': {'dwd': 312.98, 'icon': 303.64, 'meteo': 304.98, 'noaa': 314.86, 'sg': 304.98}, 'swellHeight': {'dwd': 2.74, 'icon': 3.21, 'meteo': 3.41, 'noaa': 2.47, 'sg': 3.41}, 'swellPeriod': {'dwd': 13.17, 'icon': 13.0, 'meteo': 11.22, 'noaa': 13.65, 'sg': 11.22}, 'time': '2022-02-23T12:00:00+00:00', 'waveDirection': {'icon': 304.29, 'meteo': 305.3, 'noaa': 312.6, 'sg': 305.3}, 'windSpeed': {'icon': 5.92, 'noaa': 1.42, 'sg': 5.92}}, {'airTemperature': {'dwd': 12.24, 'noaa': 13.04, 'sg': 12.24}, 'swellDirection': {'dwd': 312.86, 'icon': 303.65, 'meteo': 304.96, 'noaa': 314.79, 'sg': 304.96}, 'swellHeight': {'dwd': 2.74, 'icon': 3.22, 'meteo': 3.42, 'noaa': 2.44, 'sg': 3.42}, 'swellPeriod': {'dwd': 13.17, 'icon': 12.95, 'meteo': 11.22, 'noaa': 13.63, 'sg': 11.22}, 'time': '2022-02-23T13:00:00+00:00', 'waveDirection': {'icon': 304.46, 'meteo': 305.28, 'noaa': 311.77, 'sg': 305.28}, 'windSpeed': {'icon': 6.03, 'noaa': 1.5, 'sg': 6.03}}, 
    {'airTemperature': {'dwd': 12.07, 'noaa': 12.95, 'sg': 12.07}, 'swellDirection': {'dwd': 312.78, 'icon': 303.66, 'meteo': 304.93, 'noaa': 314.72, 'sg': 304.93}, 'swellHeight': {'dwd': 2.74, 'icon': 3.24, 'meteo': 3.42, 'noaa': 2.4, 'sg': 3.42}, 'swellPeriod': {'dwd': 13.18, 'icon': 12.91, 'meteo': 11.23, 'noaa': 13.62, 'sg': 11.23}, 'time': '2022-02-23T14:00:00+00:00', 'waveDirection': {'icon': 304.62, 'meteo': 305.26, 'noaa': 310.95, 'sg': 305.26}, 'windSpeed': {'icon': 6.13, 'noaa': 1.57, 'sg': 6.13}}, {'airTemperature': {'dwd': 11.91, 'noaa': 12.87, 'sg': 11.91}, 'swellDirection': {'dwd': 312.72, 'icon': 303.67, 'meteo': 304.91, 'noaa': 314.65, 'sg': 304.91}, 'swellHeight': {'dwd': 2.73, 'icon': 
    3.25, 'meteo': 3.43, 'noaa': 2.37, 'sg': 3.43}, 'swellPeriod': {'dwd': 13.18, 'icon': 12.86, 'meteo': 11.23, 'noaa': 13.6, 'sg': 11.23}, 'time': '2022-02-23T15:00:00+00:00', 'waveDirection': {'icon': 304.79, 'meteo': 305.24, 'noaa': 310.12, 'sg': 305.24}, 'windSpeed': {'icon': 6.24, 'noaa': 1.65, 'sg': 6.24}}, {'airTemperature': {'dwd': 11.79, 'noaa': 
    11.26, 'sg': 11.79}, 'swellDirection': {'dwd': 312.69, 'icon': 303.8, 'meteo': 303.94, 'noaa': 314.36, 'sg': 303.94}, 'swellHeight': {'dwd': 2.72, 'icon': 3.26, 'meteo': 3.36, 'noaa': 2.33, 'sg': 3.36}, 'swellPeriod': {'dwd': 13.18, 'icon': 12.82, 'meteo': 11.09, 'noaa': 13.56, 'sg': 11.09}, 'time': '2022-02-23T16:00:00+00:00', 'waveDirection': {'icon': 304.7, 'meteo': 305.26, 'noaa': 309.67, 'sg': 305.26}, 'windSpeed': {'icon': 6.0, 'noaa': 1.26, 'sg': 6.0}}, {'airTemperature': {'dwd': 11.52, 'noaa': 9.64, 'sg': 11.52}, 'swellDirection': {'dwd': 312.67, 'icon': 303.94, 'meteo': 302.97, 'noaa': 314.08, 'sg': 302.97}, 'swellHeight': {'dwd': 2.72, 'icon': 3.26, 'meteo': 3.28, 'noaa': 2.29, 'sg': 3.28}, 'swellPeriod': {'dwd': 13.19, 'icon': 12.77, 'meteo': 10.95, 'noaa': 13.53, 'sg': 10.95}, 'time': '2022-02-23T17:00:00+00:00', 'waveDirection': {'icon': 304.62, 'meteo': 305.28, 'noaa': 309.23, 'sg': 305.28}, 'windSpeed': {'icon': 5.77, 'noaa': 0.86, 'sg': 5.77}}, {'airTemperature': {'dwd': 10.8, 'noaa': 8.03, 'sg': 10.8}, 'swellDirection': {'dwd': 312.64, 'icon': 304.07, 'meteo': 302.0, 'noaa': 313.79, 'sg': 302.0}, 'swellHeight': {'dwd': 2.71, 'icon': 3.27, 'meteo': 3.21, 'noaa': 2.25, 'sg': 3.21}, 'swellPeriod': {'dwd': 
    13.2, 'icon': 12.73, 'meteo': 10.81, 'noaa': 13.49, 'sg': 10.81}, 'time': '2022-02-23T18:00:00+00:00', 'waveDirection': {'icon': 304.53, 'meteo': 305.3, 'noaa': 308.78, 'sg': 305.3}, 'windSpeed': {'icon': 5.53, 'noaa': 0.47, 'sg': 5.53}}, {'airTemperature': {'dwd': 10.3, 'noaa': 7.55, 'sg': 10.3}, 'swellDirection': {'dwd': 312.64, 'icon': 303.94, 'meteo': 302.01, 'noaa': 313.66, 'sg': 302.01}, 'swellHeight': {'dwd': 2.71, 'icon': 3.26, 'meteo': 3.2, 'noaa': 2.22, 'sg': 3.2}, 'swellPeriod': {'dwd': 13.21, 'icon': 12.74, 'meteo': 10.79, 'noaa': 13.46, 'sg': 10.79}, 'time': '2022-02-23T19:00:00+00:00', 'waveDirection': {'icon': 304.25, 'meteo': 305.27, 'noaa': 308.77, 'sg': 305.27}, 'windSpeed': {'icon': 4.76, 'noaa': 0.58, 'sg': 4.76}}, {'airTemperature': {'dwd': 10.18, 'noaa': 7.08, 'sg': 10.18}, 'swellDirection': {'dwd': 312.63, 'icon': 303.82, 'meteo': 302.01, 'noaa': 313.52, 'sg': 302.01}, 'swellHeight': {'dwd': 2.71, 'icon': 3.26, 'meteo': 3.18, 'noaa': 2.2, 'sg': 3.18}, 'swellPeriod': {'dwd': 13.21, 'icon': 12.74, 'meteo': 10.78, 'noaa': 13.43, 'sg': 10.78}, 'time': '2022-02-23T20:00:00+00:00', 'waveDirection': {'icon': 303.97, 'meteo': 305.25, 'noaa': 308.77, 'sg': 305.25}, 'windSpeed': {'icon': 3.99, 'noaa': 0.7, 
    'sg': 3.99}}, {'airTemperature': {'dwd': 9.95, 'noaa': 6.61, 'sg': 9.95}, 'swellDirection': {'dwd': 312.61, 'icon': 303.69, 'meteo': 302.02, 'noaa': 313.39, 'sg': 302.02}, 'swellHeight': {'dwd': 2.73, 'icon': 3.25, 'meteo': 3.17, 'noaa': 2.17, 'sg': 3.17}, 'swellPeriod': {'dwd': 13.23, 'icon': 12.75, 'meteo': 10.76, 'noaa': 13.4, 'sg': 10.76}, 'time': 
    '2022-02-23T21:00:00+00:00', 'waveDirection': {'icon': 303.69, 'meteo': 305.22, 'noaa': 308.76, 'sg': 305.22}, 'windSpeed': {'icon': 3.22, 'noaa': 0.81, 'sg': 3.22}}, {'airTemperature': {'dwd': 9.91, 'noaa': 6.39, 'sg': 9.91}, 'swellDirection': {'dwd': 312.76, 'icon': 303.52, 'meteo': 302.13, 'noaa': 314.03, 'sg': 302.13}, 'swellHeight': {'dwd': 2.69, 
    'icon': 3.24, 'meteo': 3.17, 'noaa': 2.21, 'sg': 3.17}, 'swellPeriod': {'dwd': 13.22, 'icon': 12.8, 'meteo': 10.76, 'noaa': 13.42, 'sg': 10.76}, 'time': '2022-02-23T22:00:00+00:00', 'waveDirection': {'icon': 303.52, 'meteo': 305.22, 'noaa': 308.95, 'sg': 305.22}, 'windSpeed': {'icon': 2.56, 'noaa': 0.96, 'sg': 2.56}}, {'airTemperature': {'dwd': 9.94, 'noaa': 6.17, 'sg': 9.94}, 'swellDirection': {'dwd': 312.81, 'icon': 303.35, 'meteo': 302.23, 'noaa': 314.67, 'sg': 302.23}, 'swellHeight': {'dwd': 2.69, 'icon': 3.24, 'meteo': 3.18, 'noaa': 2.24, 'sg': 3.18}, 'swellPeriod': {'dwd': 13.23, 'icon': 12.85, 'meteo': 10.75, 'noaa': 13.43, 'sg': 10.75}, 'time': '2022-02-23T23:00:00+00:00', 'waveDirection': {'icon': 303.35, 'meteo': 305.23, 'noaa': 309.14, 'sg': 305.23}, 'windSpeed': {'icon': 1.91, 'noaa': 1.11, 'sg': 1.91}}, {'airTemperature': {'dwd': 9.72, 'noaa': 5.95, 'sg': 9.72}, 'swellDirection': {'dwd': 312.86, 'icon': 303.18, 'meteo': 302.34, 'noaa': 315.31, 'sg': 302.34}, 'swellHeight': {'dwd': 2.69, 'icon': 3.23, 'meteo': 3.18, 'noaa': 2.28, 'sg': 3.18}, 'swellPeriod': {'dwd': 13.24, 'icon': 12.9, 'meteo': 10.75, 'noaa': 13.45, 'sg': 10.75}, 'time': '2022-02-24T00:00:00+00:00', 'waveDirection': {'icon': 303.18, 'meteo': 305.23, 'noaa': 309.33, 'sg': 305.23}, 'windSpeed': {'icon': 1.25, 'noaa': 1.26, 'sg': 1.25}}, {'airTemperature': {'dwd': 9.7, 'noaa': 5.93, 'sg': 9.7}, 'swellDirection': {'dwd': 312.94, 'icon': 303.29, 'meteo': 303.42, 'noaa': 315.11, 'sg': 303.42}, 'swellHeight': {'dwd': 2.7, 'icon': 3.25, 'meteo': 3.26, 'noaa': 2.26, 'sg': 3.26}, 'swellPeriod': {'dwd': 13.26, 'icon': 13.02, 'meteo': 10.9, 'noaa': 13.44, 'sg': 10.9}, 'time': '2022-02-24T01:00:00+00:00', 'waveDirection': {'icon': 303.29, 'meteo': 305.39, 'noaa': 309.91, 'sg': 305.39}, 'windSpeed': {'icon': 1.03, 'noaa': 1.31, 'sg': 1.03}}, {'airTemperature': {'dwd': 9.4, 'noaa': 5.9, 'sg': 9.4}, 'swellDirection': {'dwd': 313.04, 'icon': 303.4, 'meteo': 304.51, 'noaa': 314.91, 'sg': 304.51}, 'swellHeight': {'dwd': 2.71, 'icon': 3.26, 'meteo': 3.33, 'noaa': 2.23, 'sg': 3.33}, 'swellPeriod': {'dwd': 13.3, 'icon': 13.13, 'meteo': 11.06, 'noaa': 13.42, 'sg': 11.06}, 'time': '2022-02-24T02:00:00+00:00', 'waveDirection': {'icon': 303.4, 'meteo': 305.56, 'noaa': 310.49, 'sg': 305.56}, 'windSpeed': {'icon': 0.82, 'noaa': 1.36, 'sg': 0.82}}, {'airTemperature': {'dwd': 9.4, 'noaa': 5.88, 'sg': 9.4}, 'swellDirection': {'dwd': 313.2, 'icon': 303.51, 'meteo': 305.59, 'noaa': 314.71, 'sg': 305.59}, 'swellHeight': {'dwd': 2.72, 'icon': 3.28, 'meteo': 3.41, 'noaa': 2.21, 'sg': 3.41}, 'swellPeriod': {'dwd': 13.37, 'icon': 13.25, 'meteo': 11.21, 'noaa': 13.41, 'sg': 11.21}, 'time': '2022-02-24T03:00:00+00:00', 'waveDirection': {'icon': 303.51, 'meteo': 305.72, 'noaa': 311.07, 'sg': 305.72}, 'windSpeed': {'icon': 0.6, 'noaa': 1.41, 'sg': 0.6}}, {'airTemperature': {'dwd': 9.39, 'noaa': 6.18, 'sg': 9.39}, 'swellDirection': {'dwd': 313.44, 'icon': 304.03, 'meteo': 305.91, 'noaa': 306.07, 'sg': 305.91}, 'swellHeight': {'dwd': 2.76, 'icon': 3.36, 'meteo': 3.45, 'noaa': 1.87, 'sg': 3.45}, 'swellPeriod': {'dwd': 13.49, 'icon': 13.5, 'meteo': 11.29, 'noaa': 13.62, 'sg': 11.29}, 'time': '2022-02-24T04:00:00+00:00', 'waveDirection': {'icon': 304.03, 'meteo': 306.03, 'noaa': 311.42, 'sg': 306.03}, 'windSpeed': {'icon': 0.92, 'noaa': 1.5, 'sg': 0.92}}, {'airTemperature': {'dwd': 9.59, 'noaa': 6.49, 'sg': 9.59}, 'swellDirection': {'dwd': 313.76, 'icon': 304.54, 'meteo': 306.23, 'noaa': 297.42, 'sg': 306.23}, 'swellHeight': {'dwd': 2.8, 'icon': 3.43, 'meteo': 3.5, 'noaa': 1.54, 'sg': 3.5}, 'swellPeriod': {'dwd': 13.65, 'icon': 13.76, 'meteo': 11.37, 'noaa': 13.84, 'sg': 11.37}, 'time': '2022-02-24T05:00:00+00:00', 'waveDirection': {'icon': 304.54, 'meteo': 306.33, 'noaa': 311.76, 'sg': 306.33}, 'windSpeed': {'icon': 1.24, 'noaa': 1.58, 'sg': 1.24}}, {'airTemperature': {'dwd': 9.75, 'noaa': 6.79, 'sg': 9.75}, 'swellDirection': {'dwd': 314.19, 'icon': 305.06, 'meteo': 306.55, 'noaa': 288.78, 'sg': 306.55}, 'swellHeight': {'dwd': 2.87, 'icon': 3.51, 'meteo': 3.54, 'noaa': 1.2, 'sg': 3.54}, 'swellPeriod': {'dwd': 13.86, 'icon': 14.01, 'meteo': 11.45, 'noaa': 14.05, 'sg': 11.45}, 'time': '2022-02-24T06:00:00+00:00', 'waveDirection': {'icon': 305.06, 'meteo': 306.64, 'noaa': 312.11, 'sg': 306.64}, 'windSpeed': {'icon': 1.56, 'noaa': 1.67, 'sg': 1.56}}, {'airTemperature': {'dwd': 9.33, 'noaa': 7.34, 'sg': 9.33}, 'swellDirection': {'dwd': 314.7, 'icon': 305.7, 'meteo': 306.88, 'noaa': 299.23, 'sg': 306.88}, 'swellHeight': {'dwd': 2.96, 'icon': 3.64, 'meteo': 3.62, 'noaa': 1.62, 'sg': 3.62}, 
    'swellPeriod': {'dwd': 14.13, 'icon': 14.31, 'meteo': 11.6, 'noaa': 14.91, 'sg': 11.6}, 'time': '2022-02-24T07:00:00+00:00', 'waveDirection': {'icon': 305.7, 'meteo': 307.09, 'noaa': 316.06, 'sg': 307.09}, 'windSpeed': {'icon': 2.48, 'noaa': 1.48, 'sg': 2.48}}, {'airTemperature': {'dwd': 9.33, 'noaa': 7.89, 'sg': 9.33}, 'swellDirection': {'dwd': 315.26, 'icon': 306.34, 'meteo': 307.22, 'noaa': 309.69, 'sg': 307.22}, 'swellHeight': {'dwd': 3.07, 'icon': 3.77, 'meteo': 3.69, 'noaa': 2.05, 'sg': 3.69}, 'swellPeriod': {'dwd': 14.41, 'icon': 14.6, 'meteo': 11.74, 'noaa': 15.76, 'sg': 11.74}, 'time': '2022-02-24T08:00:00+00:00', 'waveDirection': {'icon': 306.34, 'meteo': 307.53, 'noaa': 320.0, 'sg': 307.53}, 'windSpeed': {'icon': 3.39, 'noaa': 1.3, 'sg': 3.39}}, {'airTemperature': {'dwd': 10.31, 'noaa': 8.44, 'sg': 10.31}, 'swellDirection': {'dwd': 315.82, 'icon': 306.98, 'meteo': 307.55, 'noaa': 320.14, 'sg': 307.55}, 'swellHeight': {'dwd': 3.19, 'icon': 3.9, 'meteo': 3.77, 'noaa': 2.47, 'sg': 3.77}, 'swellPeriod': {'dwd': 14.7, 'icon': 14.9, 'meteo': 11.89, 'noaa': 16.62, 'sg': 11.89}, 'time': '2022-02-24T09:00:00+00:00', 'waveDirection': {'icon': 306.98, 'meteo': 307.98, 'noaa': 323.95, 'sg': 307.98}, 'windSpeed': {'icon': 4.31, 'noaa': 1.11, 'sg': 4.31}}, {'airTemperature': {'dwd': 11.04, 'noaa': 9.53, 'sg': 11.04}, 'swellDirection': {'dwd': 316.34, 'icon': 307.41, 'meteo': 307.96, 'noaa': 320.33, 'sg': 307.96}, 'swellHeight': {'dwd': 3.32, 'icon': 4.03, 'meteo': 3.89, 'noaa': 2.75, 'sg': 3.89}, 'swellPeriod': {'dwd': 14.97, 'icon': 15.1, 'meteo': 11.98, 'noaa': 16.74, 'sg': 11.98}, 'time': '2022-02-24T10:00:00+00:00', 'waveDirection': {'icon': 307.41, 'meteo': 308.25, 'noaa': 323.96, 'sg': 308.25}, 'windSpeed': {'icon': 4.33, 'noaa': 1.44, 'sg': 4.33}}, {'airTemperature': {'dwd': 11.46, 'noaa': 10.62, 'sg': 11.46}, 'swellDirection': {'dwd': 316.8, 'icon': 307.83, 'meteo': 308.36, 'noaa': 320.53, 'sg': 308.36}, 'swellHeight': {'dwd': 3.46, 'icon': 4.15, 'meteo': 4.02, 'noaa': 3.02, 'sg': 4.02}, 'swellPeriod': {'dwd': 15.21, 'icon': 15.3, 'meteo': 12.06, 'noaa': 16.87, 'sg': 12.06}, 'time': '2022-02-24T11:00:00+00:00', 'waveDirection': {'icon': 307.83, 'meteo': 308.51, 'noaa': 323.97, 'sg': 308.51}, 'windSpeed': {'icon': 4.35, 'noaa': 1.78, 'sg': 4.35}}, {'airTemperature': {'dwd': 11.75, 'noaa': 11.71, 'sg': 11.75}, 'swellDirection': {'dwd': 317.17, 'icon': 308.26, 'meteo': 308.77, 'noaa': 320.72, 'sg': 308.77}, 'swellHeight': {'dwd': 3.58, 'icon': 4.28, 'meteo': 4.14, 'noaa': 3.3, 'sg': 4.14}, 'swellPeriod': {'dwd': 15.4, 'icon': 15.5, 'meteo': 12.15, 'noaa': 16.99, 'sg': 12.15}, 'time': '2022-02-24T12:00:00+00:00', 'waveDirection': {'icon': 308.26, 'meteo': 308.78, 'noaa': 323.98, 'sg': 308.78}, 'windSpeed': {'icon': 4.37, 'noaa': 2.11, 'sg': 4.37}}, {'airTemperature': {'dwd': 12.11, 'noaa': 11.69, 'sg': 12.11}, 'swellDirection': {'dwd': 317.47, 'icon': 308.52, 'meteo': 308.93, 'noaa': 320.87, 'sg': 308.93}, 'swellHeight': {'dwd': 3.7, 'icon': 4.38, 'meteo': 4.23, 'noaa': 3.43, 'sg': 4.23}, 'swellPeriod': {'dwd': 15.56, 'icon': 15.61, 'meteo': 12.28, 'noaa': 16.82, 'sg': 12.28}, 'time': '2022-02-24T13:00:00+00:00', 'waveDirection': {'icon': 308.52, 'meteo': 309.06, 'noaa': 323.71, 'sg': 309.06}, 'windSpeed': {'icon': 4.25, 'noaa': 2.19, 'sg': 4.25}}, {'airTemperature': {'dwd': 12.41, 'noaa': 11.67, 'sg': 12.41}, 'swellDirection': {'dwd': 317.73, 'icon': 308.77, 'meteo': 309.1, 'noaa': 321.03, 'sg': 309.1}, 'swellHeight': {'dwd': 3.8, 'icon': 4.47, 'meteo': 4.33, 'noaa': 3.55, 
    'sg': 4.33}, 'swellPeriod': {'dwd': 15.69, 'icon': 15.72, 'meteo': 12.4, 'noaa': 16.66, 'sg': 12.4}, 'time': '2022-02-24T14:00:00+00:00', 'waveDirection': {'icon': 308.77, 'meteo': 309.33, 'noaa': 323.45, 'sg': 309.33}, 'windSpeed': {'icon': 4.14, 'noaa': 2.26, 'sg': 4.14}}, {'airTemperature': {'dwd': 12.44, 'noaa': 11.65, 'sg': 12.44}, 'swellDirection': {'dwd': 317.97, 'icon': 309.03, 'meteo': 309.26, 'noaa': 321.18, 'sg': 309.26}, 'swellHeight': {'dwd': 3.9, 'icon': 4.57, 'meteo': 4.42, 'noaa': 3.68, 'sg': 4.42}, 'swellPeriod': {'dwd': 15.81, 'icon': 15.83, 'meteo': 12.53, 'noaa': 16.49, 'sg': 12.53}, 'time': '2022-02-24T15:00:00+00:00', 'waveDirection': {'icon': 309.03, 'meteo': 309.61, 'noaa': 323.18, 'sg': 309.61}, 'windSpeed': {'icon': 4.02, 'noaa': 2.34, 'sg': 4.02}}, {'airTemperature': {'dwd': 12.03, 'noaa': 10.41, 'sg': 12.03}, 'swellDirection': {'dwd': 318.21, 'icon': 309.31, 'meteo': 309.62, 'noaa': 320.91, 'sg': 309.62}, 'swellHeight': {'dwd': 3.99, 'icon': 4.65, 'meteo': 4.52, 'noaa': 3.62, 'sg': 4.52}, 'swellPeriod': {'dwd': 15.93, 
    'icon': 15.87, 'meteo': 12.56, 'noaa': 16.43, 'sg': 12.56}, 'time': '2022-02-24T16:00:00+00:00', 'waveDirection': {'icon': 309.34, 'meteo': 310.34, 'noaa': 322.66, 'sg': 310.34}, 'windSpeed': {'icon': 4.73, 'noaa': 2.04, 'sg': 4.73}}, {'airTemperature': {'dwd': 11.26, 'noaa': 9.17, 'sg': 11.26}, 'swellDirection': {'dwd': 318.47, 'icon': 309.58, 'meteo': 309.99, 'noaa': 320.65, 'sg': 309.99}, 'swellHeight': {'dwd': 4.08, 'icon': 4.72, 'meteo': 4.62, 'noaa': 3.56, 'sg': 4.62}, 'swellPeriod': {'dwd': 16.05, 'icon': 15.92, 'meteo': 12.58, 'noaa': 16.36, 'sg': 12.58}, 'time': '2022-02-24T17:00:00+00:00', 'waveDirection': {'icon': 309.64, 'meteo': 311.08, 'noaa': 322.14, 'sg': 311.08}, 'windSpeed': {'icon': 5.44, 'noaa': 1.74, 'sg': 5.44}}, {'airTemperature': {'dwd': 10.93, 'noaa': 7.94, 'sg': 10.93}, 'swellDirection': {'dwd': 318.75, 'icon': 309.86, 'meteo': 310.35, 'noaa': 320.38, 'sg': 310.35}, 'swellHeight': {'dwd': 4.17, 'icon': 4.8, 'meteo': 4.72, 'noaa': 3.5, 'sg': 4.72}, 'swellPeriod': {'dwd': 16.16, 'icon': 15.96, 'meteo': 12.61, 'noaa': 16.3, 'sg': 12.61}, 'time': '2022-02-24T18:00:00+00:00', 'waveDirection': {'icon': 309.95, 'meteo': 311.81, 'noaa': 321.62, 'sg': 311.81}, 'windSpeed': {'icon': 6.15, 'noaa': 1.44, 'sg': 6.15}}, {'airTemperature': {'dwd': 10.88, 'noaa': 8.0, 'sg': 10.88}, 'swellDirection': {'dwd': 319.09, 'icon': 310.31, 'meteo': 310.35, 'noaa': 321.52, 'sg': 310.35}, 'swellHeight': {'dwd': 4.27, 'icon': 4.89, 'meteo': 4.78, 'noaa': 3.85, 'sg': 4.78}, 'swellPeriod': {'dwd': 16.22, 'icon': 15.91, 'meteo': 12.39, 'noaa': 16.81, 'sg': 12.39}, 'time': '2022-02-24T19:00:00+00:00', 'waveDirection': {'icon': 310.45, 'meteo': 312.38, 'noaa': 322.08, 'sg': 312.38}, 'windSpeed': {'icon': 6.28, 'noaa': 1.83, 'sg': 6.28}}, {'airTemperature': {'dwd': 10.81, 'noaa': 8.07, 'sg': 10.81}, 'swellDirection': {'dwd': 319.52, 'icon': 310.77, 'meteo': 310.35, 'noaa': 322.67, 'sg': 310.35}, 'swellHeight': {'dwd': 4.39, 'icon': 4.98, 'meteo': 4.85, 'noaa': 4.21, 'sg': 4.85}, 'swellPeriod': {'dwd': 16.22, 'icon': 15.87, 'meteo': 12.16, 'noaa': 17.32, 'sg': 12.16}, 'time': '2022-02-24T20:00:00+00:00', 'waveDirection': {'icon': 310.95, 'meteo': 312.96, 'noaa': 322.55, 'sg': 312.96}, 'windSpeed': {'icon': 6.41, 'noaa': 2.21, 'sg': 6.41}}, {'airTemperature': {'dwd': 10.6, 'noaa': 8.13, 'sg': 10.6}, 'swellDirection': {'dwd': 320.0, 'icon': 311.22, 'meteo': 310.35, 'noaa': 323.81, 'sg': 310.35}, 'swellHeight': {'dwd': 4.53, 'icon': 5.07, 'meteo': 4.91, 'noaa': 4.56, 'sg': 4.91}, 'swellPeriod': {'dwd': 16.13, 'icon': 15.82, 'meteo': 11.94, 'noaa': 17.83, 'sg': 11.94}, 'time': '2022-02-24T21:00:00+00:00', 'waveDirection': {'icon': 311.45, 'meteo': 313.53, 'noaa': 323.01, 'sg': 313.53}, 'windSpeed': {'icon': 6.54, 'noaa': 2.6, 'sg': 6.54}}, {'airTemperature': {'dwd': 10.44, 'noaa': 7.76, 'sg': 10.44}, 'swellDirection': {'dwd': 320.42, 'icon': 311.62, 'meteo': 310.92, 'noaa': 324.1, 'sg': 310.92}, 'swellHeight': {'dwd': 4.67, 'icon': 5.16, 'meteo': 5.05, 'noaa': 4.7, 'sg': 5.05}, 'swellPeriod': {'dwd': 16.0, 'icon': 15.77, 'meteo': 11.93, 'noaa': 17.8, 'sg': 11.93}, 'time': '2022-02-24T22:00:00+00:00', 'waveDirection': {'icon': 311.89, 'meteo': 313.73, 'noaa': 323.68, 'sg': 313.73}, 'windSpeed': {'icon': 6.7, 'noaa': 2.35, 'sg': 6.7}}, {'airTemperature': {'dwd': 10.42, 'noaa': 7.39, 'sg': 10.42}, 'swellDirection': {'dwd': 320.75, 'icon': 312.02, 'meteo': 311.49, 'noaa': 324.4, 'sg': 311.49}, 'swellHeight': {'dwd': 4.81, 'icon': 5.26, 'meteo': 5.18, 'noaa': 4.84, 'sg': 5.18}, 'swellPeriod': 
    {'dwd': 15.9, 'icon': 15.71, 'meteo': 11.93, 'noaa': 17.78, 'sg': 11.93}, 'time': '2022-02-24T23:00:00+00:00', 'waveDirection': {'icon': 312.33, 'meteo': 313.92, 'noaa': 324.34, 'sg': 313.92}, 'windSpeed': {'icon': 6.85, 'noaa': 2.1, 'sg': 6.85}}], 'meta': {'cost': 1, 'dailyQuota': 10, 'end': '2022-02-24 23:00', 'lat': 43.588, 'lng': -5.9391, 'params': ['airTemperature', 'windSpeed', 'waveDirection', 'swellPeriod', 'swellHeight', 'swellDirection'], 'requestCount': 1, 'start': '2022-02-22 23:00'}}
    
    x=1
    data= []
    data2= []
    data3= []
    data4 = []
    f=str(start).split("T")
    dia=f[0].split("-")
    print(int(dia[2]))
    
    wd = []

    for row in json_data['hours']:
        if(row['time'] >= str(start) and x%2!=0 ):
            dyh=row['time']
            fecha=dyh.split("T")
            di=fecha[0].split("-")
            print(int(di[2]))
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
            if(int(di[2]) > int(dia[2]) ):

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
        
    
 
    
    TABLA1=tabulate( data , headers=["hora","Temperatura" , "Velocidad viento"]  ) 
    update.message.reply_text( 
        text= tabulate( data , headers=["hora","Temperatura" , "Velocidad viento"]  ) ,
        reply_markup= InlineKeyboardMarkup([
                        [buttonI , buttonD]
                    ])
    )
    
    TABLA2= tabulate( data2 , headers=["hora","Periodo oleaje" , "Altura de ola"]  ) 

   
    Graficas.grafica1(DIRS,0)
    Graficas.grafica2(DIRV,0)

    update.message.reply_photo(
        photo=open('WindDirection.png','rb'),
        reply_markup= InlineKeyboardMarkup([
                    [buttonGV , buttonGS]
         ])   
    )

    

    print("Al dia siguiente")
    update.message.reply_text("Al dia siguiente")
   

    TABLA3=tabulate( data3 , headers=["hora","Temperatura" , "Velocidad viento"]  ) 
    update.message.reply_text( 
        text= tabulate( data3 , headers=["hora","Temperatura" , "Velocidad viento"]  )  ,
        reply_markup= InlineKeyboardMarkup([
                        [buttonI2 , buttonD2 ]
                    ])
    )


    TABLA4=tabulate( data4 , headers=["hora","Periodo oleaje" , "Altura de ola"]  )

    Graficas.grafica1(DIRS2,1)
    Graficas.grafica2(DIRV2,1)

    update.message.reply_photo(
        photo=open('WindDirection2.png','rb'),
        reply_markup= InlineKeyboardMarkup([
                    [buttonGV2 , buttonGS2]
         ])   
    )
    
    print(DIRS)




def cambioI(update):
    update.callback_query.edit_message_text(text=TABLA1,
                                    reply_markup= InlineKeyboardMarkup([
                        [buttonI , buttonD ]
                    ])
    )


def cambioD(update):
    update.callback_query.edit_message_text(text=TABLA2,
                                    reply_markup= InlineKeyboardMarkup([
                        [buttonI , buttonD ]
                    ])
    )


def cambioGS(update):

    update.callback_query.edit_message_media(
                                    media=InputMediaPhoto(media = open('SwellDirection.png','rb')),
                                    reply_markup= InlineKeyboardMarkup([
                                    [buttonGV , buttonGS]
                                    ])
    )


def cambioGV(update):
    update.callback_query.edit_message_media(
                                    media=InputMediaPhoto(media = open('WindDirection.png','rb')),
                                    reply_markup= InlineKeyboardMarkup([
                                    [buttonGV , buttonGS]
                                    ])
    )



def cambioI2(update):
    
    update.callback_query.edit_message_text(text=TABLA3,
                                    reply_markup= InlineKeyboardMarkup([
                                    [buttonI2 , buttonD2 ]
                                    ])
    )


def cambioD2(update):
    update.callback_query.edit_message_text(text=TABLA4,
                                    reply_markup= InlineKeyboardMarkup([
                                    [buttonI2 , buttonD2 ]
                                    ])
    )

def cambioGS2(update):
        
   update.callback_query.edit_message_text(media=InputMediaPhoto(media = open('SwellDirection2.png','rb')),
                                   reply_markup= InlineKeyboardMarkup([
                                   [buttonGV2 , buttonGS2]
                                   ])
   )


def cambioGV2(update):
    update.callback_query.edit_message_text(media=InputMediaPhoto(media = open('WindDirection2.png','rb')),
                                    reply_markup= InlineKeyboardMarkup([
                                    [buttonGV2 , buttonGS2]
                                    ])
    )