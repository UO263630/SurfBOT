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
    json_data =  {'hours': [{'airTemperature': {'dwd': 12.44, 'noaa': 11.62, 'sg': 12.44}, 'swellDirection': {'dwd': 330.05, 'icon': 298.43, 'meteo': 296.56, 'noaa': 315.46, 'sg': 296.56}, 'swellHeight': {'dwd': 2.51, 'icon': 3.94, 'meteo': 3.85, 'noaa': 2.49, 'sg': 3.85}, 'swellPeriod': {'dwd': 15.75, 'icon': 14.93, 'meteo': 12.1, 'noaa': 14.98, 'sg': 12.1}, 'time': '2022-02-28T23:00:00+00:00', 'waveDirection': {'icon': 298.43, 'meteo': 296.59, 'noaa': 317.41, 'sg': 296.59}, 'windSpeed': {'icon': 1.89, 'noaa': 1.24, 'sg': 1.89}}, {'airTemperature': {'dwd': 12.92, 'noaa': 12.44, 'sg': 12.92}, 'swellDirection': {'dwd': 330.6, 'icon': 298.76, 'meteo': 296.35, 'noaa': 314.86, 'sg': 296.35}, 'swellHeight': {'dwd': 2.59, 'icon': 4.03, 'meteo': 3.92, 'noaa': 2.46, 'sg': 3.92}, 'swellPeriod': {'dwd': 15.9, 'icon': 15.07, 'meteo': 12.07, 'noaa': 14.84, 'sg': 12.07}, 'time': '2022-03-01T00:00:00+00:00', 'waveDirection': {'icon': 298.76, 'meteo': 296.38, 'noaa': 316.4, 'sg': 296.38}, 'windSpeed': {'icon': 2.13, 'noaa': 1.29, 'sg': 2.13}}, {'airTemperature': {'dwd': 12.88, 'noaa': 12.06, 'sg': 12.88}, 'swellDirection': {'dwd': 331.17, 'icon': 299.22, 'meteo': 297.38, 'noaa': 314.93, 'sg': 297.38}, 'swellHeight': {'dwd': 2.66, 'icon': 4.09, 'meteo': 4.03, 'noaa': 2.39, 'sg': 4.03}, 
    'swellPeriod': {'dwd': 16.04, 'icon': 15.14, 'meteo': 12.16, 'noaa': 14.94, 'sg': 12.16}, 'time': '2022-03-01T01:00:00+00:00', 'waveDirection': {'icon': 299.22, 'meteo': 297.41, 'noaa': 316.25, 'sg': 297.41}, 'windSpeed': {'icon': 2.31, 'noaa': 1.28, 'sg': 2.31}}, {'airTemperature': {'dwd': 12.79, 'noaa': 11.67, 'sg': 12.79}, 'swellDirection': {'dwd': 331.75, 'icon': 299.68, 'meteo': 298.42, 'noaa': 315.01, 'sg': 298.42}, 'swellHeight': {'dwd': 2.73, 'icon': 4.15, 'meteo': 4.13, 'noaa': 2.31, 'sg': 4.13}, 'swellPeriod': {'dwd': 16.15, 'icon': 15.2, 'meteo': 12.26, 'noaa': 15.03, 'sg': 12.26}, 'time': '2022-03-01T02:00:00+00:00', 'waveDirection': {'icon': 299.68, 'meteo': 298.45, 'noaa': 316.1, 'sg': 298.45}, 'windSpeed': {'icon': 2.5, 'noaa': 1.26, 'sg': 2.5}}, {'airTemperature': {'dwd': 12.69, 'noaa': 11.28, 'sg': 12.69}, 'swellDirection': {'dwd': 332.3, 'icon': 300.14, 'meteo': 299.45, 'noaa': 315.08, 'sg': 299.45}, 'swellHeight': {'dwd': 2.79, 'icon': 4.21, 'meteo': 4.24, 'noaa': 2.24, 'sg': 4.24}, 'swellPeriod': {'dwd': 16.23, 'icon': 15.27, 'meteo': 12.35, 'noaa': 15.13, 'sg': 12.35}, 'time': '2022-03-01T03:00:00+00:00', 'waveDirection': {'icon': 300.14, 'meteo': 299.48, 'noaa': 315.95, 'sg': 299.48}, 'windSpeed': {'icon': 2.68, 'noaa': 1.25, 'sg': 
    2.68}}, {'airTemperature': {'dwd': 12.72, 'noaa': 11.49, 'sg': 12.72}, 'swellDirection': {'dwd': 332.79, 'icon': 300.59, 'meteo': 299.99, 'noaa': 316.25, 'sg': 299.99}, 'swellHeight': {'dwd': 2.85, 'icon': 4.23, 'meteo': 4.21, 'noaa': 2.39, 'sg': 4.21}, 'swellPeriod': {'dwd': 16.28, 'icon': 15.26, 'meteo': 12.3, 'noaa': 15.2, 'sg': 12.3}, 'time': '2022-03-01T04:00:00+00:00', 'waveDirection': {'icon': 300.59, 'meteo': 300.02, 'noaa': 317.46, 'sg': 300.02}, 'windSpeed': {'icon': 2.26, 'noaa': 1.25, 'sg': 2.26}}, {'airTemperature': {'dwd': 12.67, 'noaa': 11.69, 'sg': 12.67}, 'swellDirection': {'dwd': 333.23, 'icon': 301.03, 'meteo': 300.53, 'noaa': 317.43, 'sg': 300.53}, 'swellHeight': {'dwd': 2.9, 'icon': 4.24, 'meteo': 
    4.19, 'noaa': 2.55, 'sg': 4.19}, 'swellPeriod': {'dwd': 16.29, 'icon': 15.24, 'meteo': 12.25, 'noaa': 15.28, 'sg': 12.25}, 'time': '2022-03-01T05:00:00+00:00', 'waveDirection': {'icon': 301.03, 'meteo': 300.55, 'noaa': 318.96, 'sg': 300.55}, 'windSpeed': {'icon': 1.85, 'noaa': 1.25, 'sg': 1.85}}, {'airTemperature': {'dwd': 12.44, 'noaa': 11.89, 'sg': 12.44}, 'swellDirection': {'dwd': 333.56, 'icon': 301.48, 'meteo': 301.07, 'noaa': 318.6, 'sg': 301.07}, 'swellHeight': {'dwd': 2.94, 'icon': 4.26, 'meteo': 4.16, 'noaa': 2.7, 'sg': 4.16}, 'swellPeriod': {'dwd': 16.25, 'icon': 15.23, 'meteo': 12.2, 'noaa': 15.35, 'sg': 12.2}, 'time': '2022-03-01T06:00:00+00:00', 'waveDirection': {'icon': 301.48, 'meteo': 301.09, 'noaa': 320.47, 'sg': 301.09}, 'windSpeed': {'icon': 1.43, 'noaa': 1.25, 'sg': 1.43}}, {'airTemperature': {'dwd': 12.3, 'noaa': 12.67, 'sg': 12.3}, 'swellDirection': {'dwd': 333.79, 'icon': 301.87, 'meteo': 301.52, 'noaa': 319.16, 'sg': 301.52}, 'swellHeight': {'dwd': 2.96, 'icon': 4.24, 'meteo': 4.09, 'noaa': 2.7, 'sg': 4.09}, 'swellPeriod': {'dwd': 16.19, 'icon': 15.17, 'meteo': 12.13, 'noaa': 15.22, 'sg': 12.13}, 'time': '2022-03-01T07:00:00+00:00', 'waveDirection': {'icon': 301.87, 'meteo': 301.54, 'noaa': 320.65, 'sg': 301.54}, 'windSpeed': {'icon': 1.9, 'noaa': 1.35, 'sg': 1.9}}, {'airTemperature': {'dwd': 12.05, 'noaa': 13.45, 'sg': 12.05}, 'swellDirection': {'dwd': 334.01, 'icon': 302.27, 'meteo': 301.97, 'noaa': 319.71, 'sg': 301.97}, 'swellHeight': {'dwd': 2.93, 'icon': 4.21, 'meteo': 4.03, 'noaa': 2.69, 'sg': 4.03}, 'swellPeriod': {'dwd': 16.13, 'icon': 15.11, 'meteo': 12.07, 'noaa': 15.09, 'sg': 12.07}, 'time': '2022-03-01T08:00:00+00:00', 'waveDirection': {'icon': 302.27, 'meteo': 301.99, 'noaa': 320.82, 'sg': 301.99}, 'windSpeed': {'icon': 2.36, 'noaa': 1.46, 'sg': 2.36}}, {'airTemperature': {'dwd': 12.0, 'noaa': 14.22, 'sg': 12.0}, 'swellDirection': {'dwd': 334.15, 'icon': 302.66, 'meteo': 302.42, 'noaa': 320.27, 'sg': 302.42}, 'swellHeight': {'dwd': 2.91, 'icon': 4.19, 'meteo': 3.96, 'noaa': 2.69, 'sg': 3.96}, 'swellPeriod': {'dwd': 16.05, 'icon': 15.05, 'meteo': 12.0, 'noaa': 14.96, 'sg': 12.0}, 'time': '2022-03-01T09:00:00+00:00', 'waveDirection': {'icon': 302.66, 'meteo': 302.44, 'noaa': 321.0, 'sg': 302.44}, 'windSpeed': {'icon': 2.83, 'noaa': 1.56, 'sg': 2.83}}, {'airTemperature': {'dwd': 12.35, 'noaa': 14.44, 'sg': 12.35}, 'swellDirection': {'dwd': 334.25, 'icon': 303.01, 'meteo': 301.18, 'noaa': 320.59, 'sg': 301.18}, 'swellHeight': {'dwd': 2.9, 'icon': 4.14, 'meteo': 3.76, 'noaa': 2.64, 'sg': 3.76}, 'swellPeriod': {'dwd': 15.95, 'icon': 14.97, 'meteo': 11.74, 'noaa': 14.85, 'sg': 11.74}, 'time': '2022-03-01T10:00:00+00:00', 'waveDirection': {'icon': 303.01, 'meteo': 302.84, 'noaa': 321.05, 'sg': 302.84}, 'windSpeed': {'icon': 2.89, 'noaa': 1.86, 'sg': 2.89}}, {'airTemperature': {'dwd': 12.43, 'noaa': 14.66, 'sg': 12.43}, 'swellDirection': {'dwd': 334.35, 'icon': 303.37, 'meteo': 299.93, 'noaa': 320.91, 'sg': 299.93}, 'swellHeight': {'dwd': 2.86, 'icon': 4.1, 'meteo': 3.56, 'noaa': 2.6, 'sg': 3.56}, 'swellPeriod': {'dwd': 15.85, 'icon': 14.88, 'meteo': 11.49, 'noaa': 14.73, 'sg': 11.49}, 'time': '2022-03-01T11:00:00+00:00', 'waveDirection': {'icon': 303.37, 'meteo': 303.24, 'noaa': 321.09, 
    'sg': 303.24}, 'windSpeed': {'icon': 2.95, 'noaa': 2.16, 'sg': 2.95}}, {'airTemperature': {'dwd': 12.43, 'noaa': 14.88, 'sg': 12.43}, 'swellDirection': {'dwd': 334.42, 'icon': 303.72, 'meteo': 298.69, 'noaa': 321.23, 'sg': 298.69}, 'swellHeight': {'dwd': 2.83, 'icon': 4.05, 'meteo': 3.36, 'noaa': 2.55, 'sg': 3.36}, 'swellPeriod': {'dwd': 15.75, 'icon': 14.8, 'meteo': 11.23, 'noaa': 14.62, 'sg': 11.23}, 'time': '2022-03-01T12:00:00+00:00', 'waveDirection': {'icon': 303.72, 'meteo': 303.64, 'noaa': 321.14, 'sg': 303.64}, 'windSpeed': {'icon': 3.01, 'noaa': 2.46, 'sg': 3.01}}, {'airTemperature': {'dwd': 12.53, 'noaa': 14.22, 'sg': 12.53}, 'swellDirection': {'dwd': 334.47, 'icon': 304.03, 'meteo': 303.57, 'noaa': 320.74, 'sg': 303.57}, 'swellHeight': {'dwd': 2.79, 'icon': 3.99, 'meteo': 3.25, 'noaa': 2.45, 'sg': 3.25}, 'swellPeriod': {'dwd': 15.66, 'icon': 14.71, 'meteo': 11.46, 'noaa': 14.49, 'sg': 11.46}, 'time': '2022-03-01T13:00:00+00:00', 'waveDirection': {'icon': 304.03, 'meteo': 303.98, 'noaa': 321.89, 'sg': 303.98}, 'windSpeed': {'icon': 2.52, 'noaa': 2.08, 'sg': 2.52}}, 
    {'airTemperature': {'dwd': 12.55, 'noaa': 13.55, 'sg': 12.55}, 'swellDirection': {'dwd': 334.52, 'icon': 304.33, 'meteo': 308.45, 'noaa': 320.24, 'sg': 308.45}, 'swellHeight': {'dwd': 2.76, 'icon': 3.94, 'meteo': 3.14, 'noaa': 2.35, 'sg': 3.14}, 'swellPeriod': {'dwd': 15.56, 'icon': 14.63, 'meteo': 11.69, 'noaa': 14.35, 'sg': 11.69}, 'time': '2022-03-01T14:00:00+00:00', 'waveDirection': {'icon': 304.33, 'meteo': 304.33, 'noaa': 322.64, 'sg': 304.33}, 'windSpeed': {'icon': 2.03, 'noaa': 1.69, 'sg': 2.03}}, {'airTemperature': {'dwd': 12.59, 'noaa': 12.89, 'sg': 12.59}, 'swellDirection': {'dwd': 334.56, 'icon': 304.64, 'meteo': 313.33, 'noaa': 319.75, 'sg': 313.33}, 'swellHeight': {'dwd': 2.72, 'icon': 3.88, 'meteo': 3.03, 'noaa': 2.25, 'sg': 3.03}, 'swellPeriod': {'dwd': 15.46, 'icon': 14.54, 'meteo': 11.92, 'noaa': 14.22, 'sg': 11.92}, 'time': '2022-03-01T15:00:00+00:00', 'waveDirection': {'icon': 
    304.64, 'meteo': 304.67, 'noaa': 323.39, 'sg': 304.67}, 'windSpeed': {'icon': 1.54, 'noaa': 1.31, 'sg': 1.54}}, {'airTemperature': {'dwd': 12.76, 'noaa': 12.51, 'sg': 12.76}, 'swellDirection': {'dwd': 334.59, 'icon': 304.82, 'meteo': 313.72, 'noaa': 320.71, 'sg': 313.72}, 'swellHeight': {'dwd': 2.69, 'icon': 3.81, 'meteo': 2.96, 'noaa': 2.23, 'sg': 2.96}, 'swellPeriod': {'dwd': 15.36, 'icon': 14.44, 'meteo': 11.83, 'noaa': 14.27, 'sg': 11.83}, 'time': '2022-03-01T16:00:00+00:00', 'waveDirection': {'icon': 304.82, 'meteo': 304.84, 'noaa': 324.17, 'sg': 304.84}, 'windSpeed': {'icon': 1.95, 'noaa': 1.54, 'sg': 1.95}}, {'airTemperature': {'dwd': 12.56, 'noaa': 12.13, 'sg': 12.56}, 'swellDirection': {'dwd': 334.6, 'icon': 305.01, 'meteo': 314.12, 'noaa': 321.66, 'sg': 314.12}, 'swellHeight': {'dwd': 2.69, 'icon': 3.75, 'meteo': 2.9, 'noaa': 2.22, 'sg': 2.9}, 'swellPeriod': {'dwd': 15.26, 'icon': 14.34, 'meteo': 11.73, 'noaa': 14.31, 'sg': 11.73}, 'time': '2022-03-01T17:00:00+00:00', 'waveDirection': {'icon': 305.01, 'meteo': 305.0, 'noaa': 324.96, 'sg': 305.0}, 'windSpeed': {'icon': 2.36, 'noaa': 1.78, 'sg': 2.36}}, {'airTemperature': {'dwd': 12.38, 'noaa': 11.75, 'sg': 12.38}, 'swellDirection': {'dwd': 334.48, 'icon': 305.19, 'meteo': 314.51, 'noaa': 322.62, 'sg': 314.51}, 'swellHeight': {'dwd': 2.58, 'icon': 3.68, 'meteo': 2.83, 'noaa': 2.2, 'sg': 2.83}, 'swellPeriod': {'dwd': 15.14, 'icon': 14.24, 'meteo': 11.64, 'noaa': 14.36, 'sg': 
    11.64}, 'time': '2022-03-01T18:00:00+00:00', 'waveDirection': {'icon': 305.19, 'meteo': 305.17, 'noaa': 325.74, 'sg': 305.17}, 'windSpeed': {'icon': 2.77, 'noaa': 2.01, 'sg': 2.77}}, {'airTemperature': {'dwd': 12.35, 'noaa': 11.34, 'sg': 12.35}, 'swellDirection': {'dwd': 334.34, 'icon': 305.21, 'meteo': 315.0, 'noaa': 323.17, 'sg': 315.0}, 'swellHeight': {'dwd': 2.52, 'icon': 3.61, 'meteo': 2.76, 'noaa': 2.16, 'sg': 2.76}, 'swellPeriod': {'dwd': 15.01, 'icon': 14.12, 'meteo': 11.57, 'noaa': 14.23, 'sg': 11.57}, 'time': '2022-03-01T19:00:00+00:00', 'waveDirection': {'icon': 305.21, 'meteo': 305.16, 'noaa': 325.16, 'sg': 305.16}, 'windSpeed': {'icon': 2.2, 'noaa': 1.82, 'sg': 2.2}}, {'airTemperature': {'dwd': 12.35, 'noaa': 10.92, 'sg': 12.35}, 'swellDirection': {'dwd': 334.19, 'icon': 305.24, 'meteo': 315.5, 'noaa': 323.73, 'sg': 315.5}, 'swellHeight': {'dwd': 2.48, 'icon': 3.54, 'meteo': 2.69, 'noaa': 2.11, 'sg': 2.69}, 'swellPeriod': {'dwd': 14.88, 'icon': 14.0, 'meteo': 11.5, 'noaa': 14.1, 'sg': 11.5}, 'time': '2022-03-01T20:00:00+00:00', 'waveDirection': {'icon': 305.24, 'meteo': 305.14, 'noaa': 324.57, 'sg': 305.14}, 'windSpeed': {'icon': 1.64, 'noaa': 1.63, 'sg': 1.64}}, {'airTemperature': {'dwd': 12.27, 'noaa': 10.51, 'sg': 12.27}, 'swellDirection': {'dwd': 333.99, 'icon': 305.26, 'meteo': 315.99, 'noaa': 324.28, 'sg': 315.99}, 'swellHeight': {'dwd': 2.42, 'icon': 3.47, 'meteo': 2.62, 'noaa': 2.07, 'sg': 2.62}, 'swellPeriod': 
    {'dwd': 14.74, 'icon': 13.88, 'meteo': 11.43, 'noaa': 13.97, 'sg': 11.43}, 'time': '2022-03-01T21:00:00+00:00', 'waveDirection': {'icon': 305.26, 'meteo': 305.13, 'noaa': 323.99, 'sg': 305.13}, 'windSpeed': {'icon': 1.07, 'noaa': 1.44, 'sg': 1.07}}, {'airTemperature': {'dwd': 12.25, 'noaa': 10.43, 'sg': 12.25}, 'swellDirection': {'dwd': 333.78, 'icon': 305.19, 'meteo': 316.34, 'noaa': 324.03, 'sg': 316.34}, 'swellHeight': {'dwd': 2.36, 'icon': 3.4, 'meteo': 2.57, 'noaa': 2.03, 'sg': 2.57}, 'swellPeriod': {'dwd': 14.61, 'icon': 13.75, 'meteo': 11.33, 'noaa': 13.88, 'sg': 11.33}, 'time': '2022-03-01T22:00:00+00:00', 'waveDirection': {'icon': 305.12, 'meteo': 305.18, 'noaa': 323.7, 'sg': 305.18}, 'windSpeed': {'icon': 3.17, 'noaa': 1.05, 'sg': 3.17}}, {'airTemperature': {'dwd': 12.15, 'noaa': 10.34, 'sg': 12.15}, 'swellDirection': {'dwd': 333.6, 'icon': 305.12, 'meteo': 316.68, 'noaa': 323.77, 'sg': 
    316.68}, 'swellHeight': {'dwd': 2.3, 'icon': 3.34, 'meteo': 2.51, 'noaa': 1.98, 'sg': 2.51}, 'swellPeriod': {'dwd': 14.48, 'icon': 13.62, 'meteo': 11.24, 'noaa': 13.78, 'sg': 11.24}, 'time': '2022-03-01T23:00:00+00:00', 'waveDirection': {'icon': 304.98, 'meteo': 305.22, 'noaa': 323.42, 'sg': 305.22}, 'windSpeed': {'icon': 5.26, 'noaa': 0.67, 'sg': 5.26}}, {'airTemperature': {'dwd': 12.2, 'noaa': 10.26, 'sg': 12.2}, 'swellDirection': {'dwd': 333.41, 'icon': 305.05, 'meteo': 317.03, 'noaa': 323.52, 'sg': 317.03}, 'swellHeight': {'dwd': 2.24, 
    'icon': 3.27, 'meteo': 2.46, 'noaa': 1.94, 'sg': 2.46}, 'swellPeriod': {'dwd': 14.36, 'icon': 13.49, 'meteo': 11.14, 'noaa': 13.69, 'sg': 11.14}, 'time': '2022-03-02T00:00:00+00:00', 'waveDirection': {'icon': 304.84, 'meteo': 305.27, 'noaa': 323.13, 'sg': 305.27}, 'windSpeed': {'icon': 7.36, 'noaa': 0.28, 'sg': 7.36}}, {'airTemperature': {'dwd': 12.68, 'noaa': 9.96, 'sg': 12.68}, 'swellDirection': {'dwd': 333.16, 'icon': 304.9, 'meteo': 317.35, 'noaa': 323.59, 'sg': 317.35}, 'swellHeight': {'dwd': 2.19, 'icon': 3.22, 'meteo': 2.41, 'noaa': 
    1.9, 'sg': 2.41}, 'swellPeriod': {'dwd': 14.22, 'icon': 13.3, 'meteo': 11.05, 'noaa': 13.65, 'sg': 11.05}, 'time': '2022-03-02T01:00:00+00:00', 'waveDirection': {'icon': 303.93, 'meteo': 305.19, 'noaa': 324.02, 'sg': 305.19}, 'windSpeed': {'icon': 7.49, 'noaa': 0.89, 'sg': 7.49}}, {'airTemperature': {'dwd': 11.9, 'noaa': 9.66, 'sg': 11.9}, 'swellDirection': {'dwd': 332.64, 'icon': 304.76, 'meteo': 317.67, 'noaa': 323.67, 'sg': 317.67}, 'swellHeight': {'dwd': 2.15, 'icon': 3.17, 'meteo': 2.35, 'noaa': 1.85, 'sg': 2.35}, 'swellPeriod': {'dwd': 14.02, 'icon': 13.12, 'meteo': 10.97, 'noaa': 13.61, 'sg': 10.97}, 'time': '2022-03-02T02:00:00+00:00', 'waveDirection': {'icon': 303.02, 'meteo': 305.11, 'noaa': 324.9, 'sg': 305.11}, 'windSpeed': {'icon': 7.61, 'noaa': 1.51, 'sg': 7.61}}, {'airTemperature': {'dwd': 11.73, 'noaa': 9.36, 'sg': 11.73}, 'swellDirection': {'dwd': 331.96, 'icon': 304.61, 'meteo': 
    317.99, 'noaa': 323.74, 'sg': 317.99}, 'swellHeight': {'dwd': 2.11, 'icon': 3.12, 'meteo': 2.3, 'noaa': 1.81, 'sg': 2.3}, 'swellPeriod': {'dwd': 13.75, 'icon': 12.93, 'meteo': 10.88, 'noaa': 13.57, 'sg': 10.88}, 'time': '2022-03-02T03:00:00+00:00', 'waveDirection': {'icon': 302.11, 'meteo': 305.03, 'noaa': 325.79, 'sg': 305.03}, 'windSpeed': {'icon': 7.74, 'noaa': 2.12, 'sg': 7.74}}, {'airTemperature': {'dwd': 11.74, 'noaa': 9.56, 'sg': 11.74}, 'swellDirection': {'dwd': 331.3, 'icon': 303.98, 'meteo': 318.35, 'noaa': 324.87, 'sg': 318.35}, 
    'swellHeight': {'dwd': 2.08, 'icon': 3.09, 'meteo': 2.24, 'noaa': 1.75, 'sg': 2.24}, 'swellPeriod': {'dwd': 13.46, 'icon': 12.71, 'meteo': 10.83, 'noaa': 13.51, 'sg': 10.83}, 'time': '2022-03-02T04:00:00+00:00', 'waveDirection': {'icon': 301.82, 'meteo': 304.27, 'noaa': 326.56, 'sg': 304.27}, 'windSpeed': {'icon': 7.4, 'noaa': 2.84, 'sg': 7.4}}, {'airTemperature': {'dwd': 11.7, 'noaa': 9.75, 'sg': 11.7}, 'swellDirection': {'dwd': 330.8, 'icon': 303.36, 'meteo': 318.71, 'noaa': 326.0, 'sg': 318.71}, 'swellHeight': {'dwd': 2.05, 'icon': 3.06, 'meteo': 2.19, 'noaa': 1.7, 'sg': 2.19}, 'swellPeriod': {'dwd': 13.24, 'icon': 12.49, 'meteo': 10.78, 'noaa': 13.45, 'sg': 10.78}, 'time': '2022-03-02T05:00:00+00:00', 'waveDirection': {'icon': 301.53, 'meteo': 303.5, 'noaa': 327.33, 'sg': 303.5}, 'windSpeed': {'icon': 7.06, 'noaa': 3.56, 'sg': 7.06}}, {'airTemperature': {'dwd': 11.65, 'noaa': 9.95, 'sg': 11.65}, 'swellDirection': {'dwd': 330.5, 'icon': 302.73, 'meteo': 319.07, 'noaa': 327.13, 'sg': 319.07}, 'swellHeight': {'dwd': 2.0, 'icon': 3.03, 'meteo': 2.13, 'noaa': 1.64, 'sg': 2.13}, 'swellPeriod': {'dwd': 13.1, 'icon': 12.27, 'meteo': 10.73, 'noaa': 13.39, 'sg': 10.73}, 'time': '2022-03-02T06:00:00+00:00', 'waveDirection': {'icon': 301.24, 'meteo': 302.74, 'noaa': 328.1, 'sg': 302.74}, 'windSpeed': {'icon': 6.72, 'noaa': 4.28, 'sg': 6.72}}, {'airTemperature': {'dwd': 11.65, 'noaa': 9.87, 'sg': 11.65}, 'swellDirection': {'dwd': 330.22, 'icon': 303.66, 'meteo': 319.03, 'noaa': 327.77, 'sg': 319.03}, 'swellHeight': {'dwd': 1.96, 'icon': 2.93, 'meteo': 2.1, 'noaa': 1.59, 'sg': 2.1}, 'swellPeriod': {'dwd': 13.01, 'icon': 
    12.4, 'meteo': 10.66, 'noaa': 13.35, 'sg': 10.66}, 'time': '2022-03-02T07:00:00+00:00', 'waveDirection': {'icon': 299.5, 'meteo': 298.31, 'noaa': 327.39, 'sg': 298.31}, 'windSpeed': 
    {'icon': 8.01, 'noaa': 3.71, 'sg': 8.01}}, {'airTemperature': {'dwd': 11.73, 'noaa': 9.8, 'sg': 11.73}, 'swellDirection': {'dwd': 329.51, 'icon': 304.59, 'meteo': 319.0, 'noaa': 328.42, 'sg': 319.0}, 'swellHeight': {'dwd': 1.92, 'icon': 2.84, 'meteo': 2.06, 'noaa': 1.53, 'sg': 2.06}, 'swellPeriod': {'dwd': 12.83, 'icon': 12.52, 'meteo': 10.58, 'noaa': 13.3, 'sg': 10.58}, 'time': '2022-03-02T08:00:00+00:00', 'waveDirection': {'icon': 297.75, 'meteo': 293.88, 'noaa': 326.69, 'sg': 293.88}, 'windSpeed': {'icon': 9.29, 'noaa': 3.15, 'sg': 9.29}}, {'airTemperature': {'dwd': 11.91, 'noaa': 9.72, 'sg': 11.91}, 'swellDirection': {'dwd': 328.13, 'icon': 305.52, 'meteo': 318.96, 'noaa': 329.06, 'sg': 318.96}, 'swellHeight': {'dwd': 1.93, 'icon': 2.74, 'meteo': 2.03, 'noaa': 1.48, 'sg': 2.03}, 'swellPeriod': {'dwd': 12.45, 'icon': 12.65, 'meteo': 10.51, 'noaa': 13.26, 'sg': 10.51}, 'time': '2022-03-02T09:00:00+00:00', 'waveDirection': {'icon': 296.01, 'meteo': 289.45, 'noaa': 325.98, 'sg': 289.45}, 'windSpeed': {'icon': 10.58, 'noaa': 2.58, 'sg': 10.58}}, {'airTemperature': {'dwd': 12.11, 'noaa': 11.2, 'sg': 12.11}, 'swellDirection': {'dwd': 326.46, 'icon': 303.47, 'meteo': 318.99, 'noaa': 328.91, 'sg': 318.99}, 'swellHeight': {'dwd': 1.95, 'icon': 2.79, 'meteo': 1.97, 'noaa': 1.46, 'sg': 1.97}, 'swellPeriod': {'dwd': 11.97, 'icon': 12.23, 'meteo': 10.56, 'noaa': 13.13, 'sg': 10.56}, 'time': '2022-03-02T10:00:00+00:00', 'waveDirection': {'icon': 296.08, 'meteo': 289.74, 'noaa': 325.93, 'sg': 289.74}, 'windSpeed': {'icon': 9.87, 'noaa': 2.98, 'sg': 9.87}}, {'airTemperature': {'dwd': 12.7, 'noaa': 12.67, 'sg': 12.7}, 'swellDirection': {'dwd': 324.67, 'icon': 301.42, 'meteo': 319.02, 'noaa': 328.77, 'sg': 319.02}, 'swellHeight': {'dwd': 1.99, 'icon': 2.85, 'meteo': 1.91, 'noaa': 1.45, 'sg': 1.91}, 'swellPeriod': {'dwd': 11.46, 'icon': 11.81, 'meteo': 10.61, 'noaa': 12.99, 'sg': 10.61}, 'time': '2022-03-02T11:00:00+00:00', 'waveDirection': {'icon': 296.15, 'meteo': 290.02, 'noaa': 325.89, 'sg': 290.02}, 'windSpeed': {'icon': 9.17, 'noaa': 3.38, 'sg': 9.17}}, {'airTemperature': {'dwd': 13.28, 'noaa': 14.15, 'sg': 13.28}, 'swellDirection': {'dwd': 324.26, 'icon': 299.37, 'meteo': 319.05, 'noaa': 328.62, 'sg': 319.05}, 'swellHeight': {'dwd': 1.97, 'icon': 2.9, 'meteo': 1.85, 'noaa': 1.43, 'sg': 1.85}, 'swellPeriod': {'dwd': 11.26, 'icon': 11.39, 'meteo': 10.66, 'noaa': 12.86, 'sg': 10.66}, 'time': '2022-03-02T12:00:00+00:00', 'waveDirection': {'icon': 296.22, 'meteo': 290.31, 'noaa': 325.84, 'sg': 290.31}, 'windSpeed': {'icon': 8.46, 'noaa': 3.78, 'sg': 8.46}}, {'airTemperature': {'dwd': 13.27, 'noaa': 14.1, 'sg': 13.27}, 'swellDirection': {'dwd': 324.85, 'icon': 299.46, 'meteo': 319.26, 'noaa': 328.38, 'sg': 319.26}, 'swellHeight': {'dwd': 1.9, 'icon': 2.86, 'meteo': 1.84, 'noaa': 1.42, 'sg': 1.84}, 'swellPeriod': {'dwd': 11.35, 'icon': 11.22, 'meteo': 10.5, 'noaa': 12.78, 'sg': 10.5}, 'time': '2022-03-02T13:00:00+00:00', 'waveDirection': {'icon': 297.38, 'meteo': 292.4, 'noaa': 326.19, 'sg': 292.4}, 'windSpeed': {'icon': 7.31, 'noaa': 3.45, 'sg': 7.31}}, {'airTemperature': {'dwd': 12.94, 'noaa': 14.04, 'sg': 12.94}, 'swellDirection': {'dwd': 325.34, 'icon': 299.56, 'meteo': 319.47, 'noaa': 328.15, 'sg': 319.47}, 'swellHeight': {'dwd': 1.83, 'icon': 2.82, 'meteo': 1.82, 'noaa': 1.4, 'sg': 1.82}, 'swellPeriod': {'dwd': 11.34, 'icon': 11.06, 'meteo': 10.33, 'noaa': 12.69, 'sg': 10.33}, 'time': '2022-03-02T14:00:00+00:00', 'waveDirection': {'icon': 298.53, 'meteo': 294.49, 'noaa': 326.53, 'sg': 294.49}, 'windSpeed': {'icon': 6.16, 'noaa': 3.11, 'sg': 6.16}}, {'airTemperature': {'dwd': 12.73, 'noaa': 13.99, 'sg': 12.73}, 'swellDirection': {'dwd': 326.14, 'icon': 299.65, 'meteo': 319.68, 'noaa': 327.91, 'sg': 319.68}, 'swellHeight': {'dwd': 1.75, 'icon': 2.78, 'meteo': 1.81, 'noaa': 1.39, 'sg': 1.81}, 'swellPeriod': {'dwd': 11.45, 'icon': 10.89, 'meteo': 10.17, 'noaa': 12.61, 'sg': 10.17}, 'time': '2022-03-02T15:00:00+00:00', 'waveDirection': {'icon': 
    299.69, 'meteo': 296.58, 'noaa': 326.88, 'sg': 296.58}, 'windSpeed': {'icon': 5.01, 'noaa': 2.78, 'sg': 5.01}}, {'airTemperature': {'dwd': 12.67, 'noaa': 12.89, 'sg': 12.67}, 'swellDirection': {'dwd': 326.62, 'icon': 300.09, 'meteo': 317.9, 'noaa': 328.14, 'sg': 317.9}, 'swellHeight': {'dwd': 1.69, 'icon': 2.7, 'meteo': 1.75, 'noaa': 1.35, 'sg': 1.75}, 'swellPeriod': {'dwd': 11.51, 'icon': 10.89, 'meteo': 9.96, 'noaa': 12.51, 'sg': 9.96}, 'time': '2022-03-02T16:00:00+00:00', 'waveDirection': {'icon': 300.12, 'meteo': 297.73, 'noaa': 326.08, 'sg': 297.73}, 'windSpeed': {'icon': 3.94, 'noaa': 2.2, 'sg': 3.94}}, {'airTemperature': {'dwd': 12.47, 'noaa': 11.79, 'sg': 12.47}, 'swellDirection': {'dwd': 326.81, 'icon': 300.54, 'meteo': 316.13, 'noaa': 328.37, 'sg': 316.13}, 'swellHeight': {'dwd': 1.64, 'icon': 2.62, 'meteo': 1.7, 'noaa': 1.31, 'sg': 1.7}, 'swellPeriod': {'dwd': 11.49, 'icon': 10.89, 'meteo': 9.75, 'noaa': 12.4, 'sg': 9.75}, 'time': '2022-03-02T17:00:00+00:00', 'waveDirection': {'icon': 300.55, 'meteo': 298.87, 'noaa': 325.28, 'sg': 298.87}, 'windSpeed': {'icon': 2.87, 'noaa': 1.61, 'sg': 2.87}}, {'airTemperature': {'dwd': 12.35, 'noaa': 10.69, 'sg': 12.35}, 'swellDirection': {'dwd': 326.74, 'icon': 300.98, 'meteo': 314.35, 'noaa': 328.6, 'sg': 
    314.35}, 'swellHeight': {'dwd': 1.6, 'icon': 2.54, 'meteo': 1.64, 'noaa': 1.27, 'sg': 1.64}, 'swellPeriod': {'dwd': 11.44, 'icon': 10.89, 'meteo': 9.54, 'noaa': 12.3, 'sg': 9.54}, 'time': '2022-03-02T18:00:00+00:00', 'waveDirection': {'icon': 300.98, 'meteo': 300.02, 'noaa': 324.48, 'sg': 300.02}, 'windSpeed': {'icon': 1.8, 'noaa': 1.03, 'sg': 1.8}}, {'airTemperature': {'dwd': 12.36, 'noaa': 10.67, 'sg': 12.36}, 'swellDirection': {'dwd': 326.58, 'icon': 301.02, 'meteo': 302.15, 'noaa': 313.07, 'sg': 302.15}, 'swellHeight': {'dwd': 1.55, 'icon': 2.47, 'meteo': 1.57, 'noaa': 1.04, 'sg': 1.57}, 'swellPeriod': {'dwd': 11.36, 'icon': 10.84, 'meteo': 8.88, 'noaa': 12.14, 'sg': 8.88}, 'time': '2022-03-02T19:00:00+00:00', 'waveDirection': {'icon': 301.02, 'meteo': 300.22, 'noaa': 324.04, 'sg': 300.22}, 'windSpeed': {'icon': 2.61, 'noaa': 1.03, 'sg': 2.61}}, {'airTemperature': {'dwd': 12.37, 'noaa': 10.65, 'sg': 12.37}, 'swellDirection': {'dwd': 326.41, 'icon': 301.06, 'meteo': 289.96, 'noaa': 297.55, 'sg': 289.96}, 'swellHeight': {'dwd': 1.51, 'icon': 2.39, 'meteo': 1.5, 'noaa': 0.81, 'sg': 1.5}, 'swellPeriod': {'dwd': 11.29, 'icon': 10.8, 'meteo': 8.22, 'noaa': 11.97, 'sg': 8.22}, 'time': '2022-03-02T20:00:00+00:00', 'waveDirection': {'icon': 301.06, 'meteo': 300.41, 'noaa': 323.59, 'sg': 300.41}, 'windSpeed': {'icon': 3.42, 'noaa': 1.04, 'sg': 3.42}}, {'airTemperature': {'dwd': 12.33, 'noaa': 10.63, 'sg': 12.33}, 'swellDirection': {'dwd': 326.25, 'icon': 301.1, 'meteo': 277.76, 'noaa': 282.02, 'sg': 277.76}, 'swellHeight': {'dwd': 1.46, 'icon': 2.32, 'meteo': 1.43, 'noaa': 0.58, 'sg': 1.43}, 'swellPeriod': {'dwd': 11.23, 'icon': 10.75, 'meteo': 7.56, 'noaa': 11.81, 'sg': 7.56}, 'time': '2022-03-02T21:00:00+00:00', 'waveDirection': {'icon': 301.1, 'meteo': 300.61, 'noaa': 323.15, 'sg': 300.61}, 'windSpeed': {'icon': 4.22, 'noaa': 1.04, 'sg': 4.22}}, {'airTemperature': {'dwd': 12.36, 'noaa': 10.55, 'sg': 12.36}, 'swellDirection': {'dwd': 326.03, 'icon': 300.69, 'meteo': 277.94, 'noaa': 294.67, 'sg': 277.94}, 'swellHeight': {'dwd': 1.41, 'icon': 2.26, 'meteo': 1.43, 'noaa': 0.85, 'sg': 1.43}, 'swellPeriod': {'dwd': 11.16, 'icon': 10.67, 'meteo': 7.49, 'noaa': 11.79, 'sg': 7.49}, 'time': '2022-03-02T22:00:00+00:00', 'waveDirection': {'icon': 300.69, 'meteo': 299.61, 'noaa': 323.32, 'sg': 299.61}, 'windSpeed': {'icon': 3.68, 'noaa': 1.02, 'sg': 3.68}}, {'airTemperature': {'dwd': 12.35, 'noaa': 10.48, 'sg': 12.35}, 'swellDirection': {'dwd': 325.68, 'icon': 300.28, 'meteo': 278.12, 'noaa': 307.33, 'sg': 278.12}, 'swellHeight': {'dwd': 1.36, 'icon': 2.2, 'meteo': 1.44, 'noaa': 1.12, 'sg': 1.44}, 'swellPeriod': {'dwd': 11.08, 'icon': 10.6, 'meteo': 7.41, 'noaa': 11.77, 'sg': 7.41}, 'time': '2022-03-02T23:00:00+00:00', 'waveDirection': {'icon': 300.28, 'meteo': 298.62, 'noaa': 323.49, 'sg': 298.62}, 'windSpeed': {'icon': 3.13, 'noaa': 1.0, 'sg': 3.13}}], 'meta': {'cost': 1, 'dailyQuota': 10, 'end': '2022-03-02 23:00', 'lat': 43.5423, 'lng': -5.6592, 'params': ['airTemperature', 'windSpeed', 'waveDirection', 'swellPeriod', 'swellHeight', 'swellDirection'], 'requestCount': 2, 'start': '2022-02-28 23:00'}}
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
    aux=0
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
