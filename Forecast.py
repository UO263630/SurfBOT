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

import os
import json
def busqueda(nombre,provincia,x,y):
    print()
    s="JSON"+nombre+"_"+provincia+".json"

    print(s)
    file = open(s,"w")

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
        'lat': x,
        'lng': y,
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
    
    json_data = {'hours': [{'airTemperature': {'dwd': 11.4, 'noaa': 6.75, 'sg': 11.4}, 'swellDirection': {'dwd': 323.98, 'icon': 290.11, 'meteo': 288.3, 'noaa': 304.27, 'sg': 288.3}, 'swellHeight': {'dwd': 2.78, 'icon': 4.77, 'meteo': 5.84, 'noaa': 3.17, 'sg': 5.84}, 'swellPeriod': {'dwd': 14.84, 'icon': 14.58, 'meteo': 12.82, 'noaa': 16.69, 'sg': 12.82}, 'time': '2022-03-11T23:00:00+00:00', 'waveDirection': {'icon': 289.23, 'meteo': 287.16, 'noaa': 309.21, 'sg': 287.16}, 'windSpeed': 
    {'icon': 8.21, 'noaa': 1.86, 'sg': 8.21}}, {'airTemperature': {'dwd': 11.1, 'noaa': 6.5, 'sg': 11.1}, 'swellDirection': {'dwd': 324.49, 'icon': 290.19, 'meteo': 288.36, 'noaa': 306.16, 'sg': 288.36}, 'swellHeight': {'dwd': 2.75, 'icon': 
    4.81, 'meteo': 5.83, 'noaa': 3.06, 'sg': 5.83}, 'swellPeriod': {'dwd': 14.98, 'icon': 14.58, 'meteo': 12.76, 'noaa': 16.73, 'sg': 12.76}, 'time': '2022-03-12T00:00:00+00:00', 'waveDirection': {'icon': 289.54, 'meteo': 287.44, 'noaa': 309.15, 'sg': 287.44}, 'windSpeed': {'icon': 7.67, 'noaa': 1.71, 'sg': 7.67}}, {'airTemperature': {'dwd': 10.79, 'noaa': 6.29, 'sg': 10.79}, 'swellDirection': {'dwd': 324.91, 'icon': 290.39, 'meteo': 288.52, 'noaa': 306.93, 'sg': 288.52}, 'swellHeight': {'dwd': 2.72, 'icon': 4.79, 'meteo': 5.77, 'noaa': 3.04, 'sg': 5.77}, 'swellPeriod': {'dwd': 15.09, 'icon': 14.6, 'meteo': 12.7, 'noaa': 16.72, 'sg': 12.7}, 'time': '2022-03-12T01:00:00+00:00', 'waveDirection': {'icon': 289.94, 'meteo': 287.81, 'noaa': 309.62, 'sg': 287.81}, 'windSpeed': {'icon': 6.63, 'noaa': 1.78, 'sg': 6.63}}, {'airTemperature': {'dwd': 10.43, 'noaa': 6.07, 'sg': 10.43}, 'swellDirection': {'dwd': 325.24, 'icon': 290.6, 'meteo': 288.69, 
    'noaa': 307.7, 'sg': 288.69}, 'swellHeight': {'dwd': 2.71, 'icon': 4.78, 'meteo': 5.71, 'noaa': 3.02, 'sg': 5.71}, 'swellPeriod': {'dwd': 15.17, 'icon': 14.62, 'meteo': 12.64, 'noaa': 16.71, 'sg': 12.64}, 'time': '2022-03-12T02:00:00+00:00', 'waveDirection': {'icon': 290.35, 'meteo': 288.17, 'noaa': 310.08, 'sg': 288.17}, 'windSpeed': {'icon': 5.58, 'noaa': 1.84, 'sg': 5.58}}, {'airTemperature': {'dwd': 10.45, 'noaa': 5.85, 'sg': 10.45}, 'swellDirection': {'dwd': 325.55, 'icon': 290.8, 'meteo': 288.85, 'noaa': 308.47, 'sg': 288.85}, 'swellHeight': {'dwd': 2.7, 'icon': 4.76, 'meteo': 5.65, 'noaa': 3.0, 'sg': 5.65}, 'swellPeriod': {'dwd': 15.23, 'icon': 14.64, 'meteo': 12.58, 'noaa': 16.7, 'sg': 12.58}, 
    'time': '2022-03-12T03:00:00+00:00', 'waveDirection': {'icon': 290.75, 'meteo': 288.54, 'noaa': 310.55, 'sg': 288.54}, 'windSpeed': {'icon': 4.54, 'noaa': 1.91, 'sg': 4.54}}, {'airTemperature': {'dwd': 10.45, 'noaa': 5.67, 'sg': 10.45}, 
    'swellDirection': {'dwd': 325.83, 'icon': 291.23, 'meteo': 289.16, 'noaa': 309.06, 'sg': 289.16}, 'swellHeight': {'dwd': 2.69, 'icon': 4.72, 'meteo': 5.56, 'noaa': 2.99, 'sg': 5.56}, 'swellPeriod': {'dwd': 15.27, 'icon': 14.67, 'meteo': 
    12.55, 'noaa': 16.63, 'sg': 12.55}, 'time': '2022-03-12T04:00:00+00:00', 'waveDirection': {'icon': 291.2, 'meteo': 288.94, 'noaa': 310.94, 'sg': 288.94}, 'windSpeed': {'icon': 4.37, 'noaa': 1.97, 'sg': 4.37}}, {'airTemperature': {'dwd': 
    10.43, 'noaa': 5.49, 'sg': 10.43}, 'swellDirection': {'dwd': 326.09, 'icon': 291.67, 'meteo': 289.48, 'noaa': 309.64, 'sg': 289.48}, 'swellHeight': {'dwd': 2.68, 'icon': 4.69, 'meteo': 5.48, 'noaa': 2.99, 'sg': 5.48}, 'swellPeriod': {'dwd': 15.31, 'icon': 14.71, 'meteo': 12.53, 'noaa': 16.56, 'sg': 12.53}, 'time': '2022-03-12T05:00:00+00:00', 'waveDirection': {'icon': 291.65, 'meteo': 289.34, 'noaa': 311.34, 'sg': 289.34}, 'windSpeed': {'icon': 4.2, 'noaa': 2.03, 'sg': 
    4.2}}, {'airTemperature': {'dwd': 10.6, 'noaa': 5.3, 'sg': 10.6}, 'swellDirection': {'dwd': 326.33, 'icon': 292.1, 'meteo': 289.79, 'noaa': 310.23, 'sg': 289.79}, 'swellHeight': {'dwd': 2.68, 'icon': 4.65, 'meteo': 5.39, 'noaa': 2.98, 'sg': 5.39}, 'swellPeriod': {'dwd': 15.33, 'icon': 14.74, 'meteo': 12.5, 'noaa': 16.49, 'sg': 12.5}, 'time': '2022-03-12T06:00:00+00:00', 'waveDirection': {'icon': 292.1, 'meteo': 289.74, 'noaa': 311.73, 'sg': 289.74}, 'windSpeed': {'icon': 4.03, 'noaa': 2.09, 'sg': 4.03}}, {'airTemperature': {'dwd': 10.01, 'noaa': 6.75, 'sg': 10.01}, 'swellDirection': {'dwd': 326.55, 'icon': 292.51, 'meteo': 290.12, 'noaa': 310.59, 'sg': 290.12}, 'swellHeight': {'dwd': 2.68, 'icon': 4.6, 'meteo': 5.27, 'noaa': 2.97, 'sg': 5.27}, 'swellPeriod': {'dwd': 15.33, 'icon': 14.72, 'meteo': 12.47, 'noaa': 16.43, 'sg': 12.47}, 'time': '2022-03-12T07:00:00+00:00', 'waveDirection': {'icon': 292.51, 'meteo': 290.01, 'noaa': 312.29, 
    'sg': 290.01}, 'windSpeed': {'icon': 4.34, 'noaa': 2.15, 'sg': 4.34}}, {'airTemperature': {'dwd': 9.81, 'noaa': 8.19, 'sg': 9.81}, 'swellDirection': {'dwd': 326.72, 'icon': 292.92, 'meteo': 290.44, 'noaa': 310.95, 'sg': 290.44}, 'swellHeight': {'dwd': 2.67, 'icon': 4.54, 'meteo': 5.15, 'noaa': 2.95, 'sg': 5.15}, 'swellPeriod': {'dwd': 15.32, 'icon': 14.69, 'meteo': 12.43, 'noaa': 16.38, 'sg': 12.43}, 'time': '2022-03-12T08:00:00+00:00', 'waveDirection': {'icon': 292.92, 'meteo': 290.28, 'noaa': 312.85, 'sg': 290.28}, 'windSpeed': {'icon': 4.65, 'noaa': 2.21, 'sg': 4.65}}, {'airTemperature': {'dwd': 10.61, 'noaa': 9.64, 'sg': 10.61}, 'swellDirection': {'dwd': 326.86, 'icon': 293.33, 'meteo': 290.77, 'noaa': 311.31, 'sg': 290.77}, 'swellHeight': {'dwd': 2.66, 'icon': 4.49, 'meteo': 5.03, 'noaa': 2.94, 'sg': 5.03}, 'swellPeriod': {'dwd': 15.29, 'icon': 14.67, 'meteo': 12.4, 'noaa': 16.32, 'sg': 12.4}, 'time': '2022-03-12T09:00:00+00:00', 'waveDirection': {'icon': 293.33, 'meteo': 290.55, 'noaa': 313.41, 'sg': 290.55}, 'windSpeed': {'icon': 4.96, 'noaa': 2.27, 'sg': 4.96}}, {'airTemperature': {'dwd': 11.62, 'noaa': 10.95, 'sg': 11.62}, 'swellDirection': {'dwd': 326.96, 'icon': 293.68, 'meteo': 290.92, 'noaa': 311.52, 'sg': 290.92}, 'swellHeight': {'dwd': 2.64, 'icon': 4.41, 'meteo': 4.88, 'noaa': 2.88, 'sg': 4.88}, 'swellPeriod': {'dwd': 15.25, 'icon': 14.6, 'meteo': 12.33, 'noaa': 16.11, 'sg': 12.33}, 
    'time': '2022-03-12T10:00:00+00:00', 'waveDirection': {'icon': 293.68, 'meteo': 290.72, 'noaa': 313.09, 'sg': 290.72}, 'windSpeed': {'icon': 4.94, 'noaa': 1.97, 'sg': 4.94}}, {'airTemperature': {'dwd': 12.0, 'noaa': 12.26, 'sg': 12.0}, 'swellDirection': {'dwd': 327.03, 'icon': 294.04, 'meteo': 291.08, 'noaa': 311.72, 'sg': 291.08}, 'swellHeight': {'dwd': 2.61, 'icon': 4.33, 'meteo': 4.73, 'noaa': 2.82, 'sg': 4.73}, 'swellPeriod': {'dwd': 15.19, 'icon': 14.53, 'meteo': 12.26, 'noaa': 15.89, 'sg': 12.26}, 'time': '2022-03-12T11:00:00+00:00', 'waveDirection': {'icon': 294.04, 'meteo': 290.9, 'noaa': 312.78, 'sg': 290.9}, 'windSpeed': {'icon': 4.93, 'noaa': 1.67, 'sg': 4.93}}, {'airTemperature': {'dwd': 12.11, 'noaa': 13.58, 'sg': 12.11}, 'swellDirection': {'dwd': 327.08, 'icon': 294.39, 'meteo': 291.23, 'noaa': 311.93, 'sg': 291.23}, 'swellHeight': {'dwd': 2.56, 'icon': 4.25, 'meteo': 4.58, 'noaa': 2.76, 'sg': 4.58}, 'swellPeriod': {'dwd': 15.11, 'icon': 14.46, 'meteo': 12.19, 'noaa': 15.68, 'sg': 12.19}, 'time': '2022-03-12T12:00:00+00:00', 'waveDirection': {'icon': 294.39, 'meteo': 291.07, 'noaa': 312.46, 'sg': 291.07}, 'windSpeed': {'icon': 4.91, 'noaa': 1.37, 'sg': 
    4.91}}, {'airTemperature': {'dwd': 12.56, 'noaa': 14.18, 'sg': 12.56}, 'swellDirection': {'dwd': 327.2, 'icon': 294.5, 'meteo': 291.16, 'noaa': 311.99, 'sg': 291.16}, 'swellHeight': {'dwd': 2.51, 'icon': 4.14, 'meteo': 4.44, 'noaa': 2.67, 'sg': 4.44}, 'swellPeriod': {'dwd': 15.0, 'icon': 14.32, 'meteo': 12.08, 'noaa': 15.55, 'sg': 12.08}, 'time': '2022-03-12T13:00:00+00:00', 'waveDirection': {'icon': 294.5, 'meteo': 291.03, 'noaa': 312.58, 'sg': 291.03}, 'windSpeed': {'icon': 4.24, 'noaa': 1.71, 'sg': 4.24}}, {'airTemperature': {'dwd': 12.6, 'noaa': 14.78, 'sg': 12.6}, 'swellDirection': {'dwd': 327.54, 'icon': 294.6, 'meteo': 291.08, 'noaa': 312.06, 'sg': 291.08}, 'swellHeight': {'dwd': 2.44, 'icon': 4.02, 'meteo': 4.31, 'noaa': 2.59, 'sg': 4.31}, 'swellPeriod': {'dwd': 14.82, 'icon': 14.17, 'meteo': 11.97, 'noaa': 15.43, 'sg': 11.97}, 'time': '2022-03-12T14:00:00+00:00', 'waveDirection': {'icon': 294.6, 'meteo': 291.0, 'noaa': 312.7, 'sg': 291.0}, 'windSpeed': {'icon': 3.57, 'noaa': 2.06, 'sg': 3.57}}, {'airTemperature': {'dwd': 12.87, 'noaa': 15.38, 'sg': 12.87}, 'swellDirection': {'dwd': 327.99, 'icon': 294.71, 'meteo': 291.01, 'noaa': 312.12, 'sg': 291.01}, 'swellHeight': {'dwd': 2.38, 'icon': 3.91, 'meteo': 4.17, 'noaa': 2.5, 'sg': 4.17}, 'swellPeriod': {'dwd': 14.6, 'icon': 14.03, 'meteo': 11.86, 'noaa': 15.3, 'sg': 11.86}, 'time': '2022-03-12T15:00:00+00:00', 'waveDirection': {'icon': 294.71, 'meteo': 290.96, 'noaa': 312.82, 'sg': 290.96}, 'windSpeed': {'icon': 2.9, 'noaa': 2.4, 'sg': 2.9}}, {'airTemperature': {'dwd': 12.69, 'noaa': 13.71, 'sg': 12.69}, 'swellDirection': {'dwd': 328.25, 'icon': 294.35, 'meteo': 290.72, 'noaa': 307.9, 'sg': 290.72}, 'swellHeight': {'dwd': 2.32, 'icon': 3.84, 'meteo': 4.14, 'noaa': 2.66, 'sg': 4.14}, 'swellPeriod': {'dwd': 14.41, 'icon': 13.87, 'meteo': 11.75, 'noaa': 15.07, 'sg': 11.75}, 'time': '2022-03-12T16:00:00+00:00', 
    'waveDirection': {'icon': 294.35, 'meteo': 290.7, 'noaa': 312.54, 'sg': 290.7}, 'windSpeed': {'icon': 2.5, 'noaa': 2.33, 'sg': 2.5}}, {'airTemperature': {'dwd': 12.75, 'noaa': 12.03, 'sg': 12.75}, 'swellDirection': {'dwd': 328.18, 'icon': 294.0, 'meteo': 290.42, 'noaa': 303.68, 'sg': 290.42}, 'swellHeight': {'dwd': 2.27, 'icon': 3.76, 'meteo': 4.1, 'noaa': 2.82, 'sg': 4.1}, 'swellPeriod': {'dwd': 14.3, 'icon': 13.7, 'meteo': 11.63, 'noaa': 14.85, 'sg': 11.63}, 'time': '2022-03-12T17:00:00+00:00', 'waveDirection': {'icon': 294.0, 'meteo': 290.44, 'noaa': 312.27, 'sg': 290.44}, 'windSpeed': {'icon': 2.09, 'noaa': 2.27, 'sg': 2.09}}, {'airTemperature': {'dwd': 12.12, 'noaa': 10.36, 'sg': 12.12}, 'swellDirection': {'dwd': 327.92, 'icon': 293.64, 'meteo': 290.13, 'noaa': 299.46, 'sg': 290.13}, 'swellHeight': {'dwd': 2.22, 'icon': 3.69, 'meteo': 4.07, 'noaa': 2.98, 'sg': 4.07}, 'swellPeriod': {'dwd': 14.25, 'icon': 13.54, 'meteo': 11.52, 'noaa': 14.62, 'sg': 11.52}, 'time': '2022-03-12T18:00:00+00:00', 'waveDirection': {'icon': 293.64, 'meteo': 290.18, 'noaa': 311.99, 'sg': 290.18}, 'windSpeed': {'icon': 1.69, 'noaa': 2.2, 'sg': 1.69}}, {'airTemperature': {'dwd': 11.22, 'noaa': 9.89, 'sg': 11.22}, 'swellDirection': {'dwd': 327.78, 'icon': 293.68, 'meteo': 290.58, 'noaa': 302.34, 'sg': 290.58}, 'swellHeight': {'dwd': 2.19, 'icon': 3.65, 'meteo': 4.08, 'noaa': 2.8, 'sg': 4.08}, 'swellPeriod': {'dwd': 14.27, 'icon': 13.51, 'meteo': 11.54, 'noaa': 14.54, 'sg': 11.54}, 'time': '2022-03-12T19:00:00+00:00', 'waveDirection': {'icon': 293.21, 'meteo': 289.53, 'noaa': 312.16, 'sg': 289.53}, 'windSpeed': {'icon': 4.24, 'noaa': 1.75, 'sg': 4.24}}, {'airTemperature': {'dwd': 11.49, 'noaa': 9.42, 'sg': 11.49}, 'swellDirection': {'dwd': 326.95, 'icon': 293.73, 'meteo': 291.04, 'noaa': 305.21, 'sg': 291.04}, 'swellHeight': {'dwd': 2.21, 'icon': 3.6, 'meteo': 4.1, 'noaa': 2.63, 'sg': 4.1}, 'swellPeriod': {'dwd': 14.03, 'icon': 13.49, 'meteo': 11.57, 'noaa': 14.45, 'sg': 11.57}, 'time': '2022-03-12T20:00:00+00:00', 'waveDirection': {'icon': 292.78, 'meteo': 288.88, 'noaa': 312.34, 'sg': 288.88}, 'windSpeed': {'icon': 6.79, 'noaa': 1.29, 'sg': 6.79}}, {'airTemperature': {'dwd': 11.17, 'noaa': 8.95, 'sg': 11.17}, 'swellDirection': {'dwd': 326.08, 'icon': 293.77, 'meteo': 291.49, 'noaa': 308.09, 'sg': 291.49}, 'swellHeight': {'dwd': 2.22, 'icon': 3.56, 'meteo': 4.11, 'noaa': 2.45, 'sg': 4.11}, 'swellPeriod': {'dwd': 13.84, 'icon': 13.46, 'meteo': 11.59, 'noaa': 14.37, 'sg': 11.59}, 'time': '2022-03-12T21:00:00+00:00', 'waveDirection': {'icon': 292.35, 'meteo': 288.23, 'noaa': 312.51, 'sg': 288.23}, 'windSpeed': {'icon': 9.34, 'noaa': 0.84, 'sg': 9.34}}, {'airTemperature': {'dwd': 11.26, 'noaa': 8.85, 'sg': 11.26}, 'swellDirection': {'dwd': 325.14, 'icon': 294.76, 'meteo': 292.15, 'noaa': 314.6, 'sg': 292.15}, 'swellHeight': {'dwd': 2.24, 'icon': 3.47, 'meteo': 4.13, 'noaa': 2.28, 'sg': 4.13}, 'swellPeriod': {'dwd': 13.58, 'icon': 13.55, 'meteo': 11.62, 'noaa': 13.18, 'sg': 11.62}, 'time': '2022-03-12T22:00:00+00:00', 'waveDirection': {'icon': 291.75, 'meteo': 288.33, 'noaa': 312.71, 'sg': 288.33}, 'windSpeed': {'icon': 10.25, 'noaa': 1.82, 'sg': 10.25}}, {'airTemperature': {'dwd': 11.29, 'noaa': 8.75, 'sg': 11.29}, 'swellDirection': {'dwd': 324.4, 'icon': 295.76, 'meteo': 292.8, 'noaa': 321.12, 'sg': 292.8}, 'swellHeight': {'dwd': 2.25, 'icon': 3.39, 'meteo': 4.16, 'noaa': 2.12, 'sg': 4.16}, 'swellPeriod': {'dwd': 13.41, 'icon': 13.63, 'meteo': 11.65, 'noaa': 11.99, 'sg': 11.65}, 'time': '2022-03-12T23:00:00+00:00', 
    'waveDirection': {'icon': 291.16, 'meteo': 288.43, 'noaa': 312.92, 'sg': 288.43}, 'windSpeed': {'icon': 11.17, 'noaa': 2.81, 'sg': 11.17}}, {'airTemperature': {'dwd': 11.32, 'noaa': 8.65, 'sg': 11.32}, 'swellDirection': {'dwd': 323.57, 'icon': 296.75, 'meteo': 293.46, 'noaa': 327.63, 'sg': 293.46}, 'swellHeight': {'dwd': 2.27, 'icon': 3.3, 'meteo': 4.18, 'noaa': 1.95, 'sg': 4.18}, 'swellPeriod': {'dwd': 13.19, 'icon': 13.72, 'meteo': 11.68, 'noaa': 10.8, 'sg': 11.68}, 'time': '2022-03-13T00:00:00+00:00', 'waveDirection': {'icon': 290.56, 'meteo': 288.53, 'noaa': 313.12, 'sg': 288.53}, 'windSpeed': {'icon': 12.08, 'noaa': 3.79, 'sg': 12.08}}, {'airTemperature': {'dwd': 11.01, 'noaa': 8.15, 'sg': 11.01}, 'swellDirection': {'dwd': 322.55, 'icon': 296.67, 'meteo': 294.02, 'noaa': 318.69, 'sg': 294.02}, 'swellHeight': {'dwd': 2.31, 'icon': 3.38, 'meteo': 4.24, 'noaa': 2.38, 'sg': 4.24}, 'swellPeriod': {'dwd': 12.87, 'icon': 13.38, 'meteo': 11.64, 'noaa': 11.74, 'sg': 11.64}, 'time': '2022-03-13T01:00:00+00:00', 'waveDirection': {'icon': 290.8, 'meteo': 288.81, 'noaa': 312.97, 'sg': 288.81}, 'windSpeed': {'icon': 11.46, 'noaa': 3.95, 'sg': 11.46}}, {'airTemperature': {'dwd': 10.84, 'noaa': 7.65, 'sg': 10.84}, 'swellDirection': {'dwd': 321.49, 'icon': 296.59, 'meteo': 294.58, 'noaa': 309.76, 'sg': 294.58}, 'swellHeight': {'dwd': 2.36, 'icon': 3.45, 'meteo': 4.31, 'noaa': 2.82, 'sg': 4.31}, 'swellPeriod': {'dwd': 12.48, 'icon': 13.03, 'meteo': 11.6, 'noaa': 12.67, 'sg': 11.6}, 'time': '2022-03-13T02:00:00+00:00', 'waveDirection': {'icon': 291.03, 'meteo': 289.1, 'noaa': 312.82, 'sg': 289.1}, 'windSpeed': {'icon': 10.84, 'noaa': 4.11, 'sg': 10.84}}, {'airTemperature': {'dwd': 10.43, 'noaa': 7.15, 'sg': 10.43}, 'swellDirection': {'dwd': 320.88, 'icon': 296.51, 'meteo': 295.14, 'noaa': 300.82, 'sg': 295.14}, 'swellHeight': {'dwd': 2.39, 'icon': 3.53, 'meteo': 4.37, 'noaa': 3.25, 'sg': 4.37}, 'swellPeriod': {'dwd': 12.27, 'icon': 12.69, 'meteo': 11.56, 'noaa': 13.61, 'sg': 11.56}, 'time': '2022-03-13T03:00:00+00:00', 'waveDirection': {'icon': 291.27, 'meteo': 289.38, 'noaa': 312.67, 'sg': 289.38}, 'windSpeed': {'icon': 10.22, 'noaa': 4.27, 'sg': 10.22}}, {'airTemperature': {'dwd': 9.9, 'noaa': 6.43, 'sg': 9.9}, 'swellDirection': {'dwd': 320.26, 'icon': 296.1, 'meteo': 295.18, 'noaa': 304.26, 'sg': 295.18}, 'swellHeight': {'dwd': 2.43, 'icon': 3.61, 'meteo': 4.48, 'noaa': 3.32, 'sg': 4.48}, 'swellPeriod': {'dwd': 12.08, 'icon': 12.46, 'meteo': 11.4, 'noaa': 13.73, 'sg': 11.4}, 'time': '2022-03-13T04:00:00+00:00', 'waveDirection': {'icon': 292.34, 'meteo': 290.05, 'noaa': 313.42, 'sg': 290.05}, 'windSpeed': {'icon': 8.96, 'noaa': 3.64, 'sg': 8.96}}, {'airTemperature': {'dwd': 9.43, 'noaa': 5.7, 'sg': 9.43}, 'swellDirection': {'dwd': 320.07, 'icon': 295.69, 'meteo': 295.21, 'noaa': 307.7, 'sg': 295.21}, 'swellHeight': {'dwd': 2.45, 'icon': 3.69, 'meteo': 4.59, 'noaa': 3.39, 'sg': 4.59}, 'swellPeriod': {'dwd': 12.05, 'icon': 12.22, 'meteo': 11.23, 'noaa': 13.85, 'sg': 11.23}, 'time': '2022-03-13T05:00:00+00:00', 'waveDirection': {'icon': 293.41, 'meteo': 290.72, 'noaa': 314.18, 'sg': 290.72}, 'windSpeed': {'icon': 7.7, 'noaa': 3.01, 'sg': 7.7}}, {'airTemperature': {'dwd': 9.2, 'noaa': 4.97, 'sg': 9.2}, 'swellDirection': {'dwd': 320.22, 'icon': 295.28, 'meteo': 295.25, 'noaa': 311.14, 'sg': 295.25}, 'swellHeight': {'dwd': 2.46, 'icon': 3.77, 'meteo': 4.7, 'noaa': 3.46, 'sg': 4.7}, 'swellPeriod': {'dwd': 12.15, 'icon': 11.99, 'meteo': 11.07, 'noaa': 13.97, 'sg': 11.07}, 'time': '2022-03-13T06:00:00+00:00', 'waveDirection': {'icon': 294.48, 'meteo': 291.39, 'noaa': 314.93, 'sg': 291.39}, 'windSpeed': {'icon': 6.44, 'noaa': 2.38, 'sg': 6.44}}, {'airTemperature': {'dwd': 9.14, 'noaa': 6.06, 'sg': 9.14}, 'swellDirection': {'dwd': 320.53, 'icon': 296.0, 'meteo': 295.25, 'noaa': 311.73, 'sg': 295.25}, 'swellHeight': {'dwd': 2.47, 'icon': 3.79, 'meteo': 4.75, 'noaa': 3.46, 'sg': 4.75}, 'swellPeriod': {'dwd': 12.3, 'icon': 12.1, 'meteo': 10.91, 'noaa': 13.98, 'sg': 10.91}, 'time': '2022-03-13T07:00:00+00:00', 'waveDirection': {'icon': 295.46, 'meteo': 292.05, 'noaa': 315.0, 'sg': 292.05}, 'windSpeed': {'icon': 5.13, 'noaa': 2.04, 'sg': 5.13}}, {'airTemperature': {'dwd': 9.54, 'noaa': 7.16, 'sg': 9.54}, 'swellDirection': {'dwd': 320.99, 'icon': 296.71, 'meteo': 295.24, 'noaa': 312.33, 'sg': 295.24}, 'swellHeight': {'dwd': 2.51, 'icon': 3.82, 'meteo': 4.79, 'noaa': 3.45, 'sg': 4.79}, 'swellPeriod': {'dwd': 12.47, 'icon': 12.2, 'meteo': 10.76, 'noaa': 13.98, 'sg': 10.76}, 'time': '2022-03-13T08:00:00+00:00', 'waveDirection': {'icon': 296.45, 'meteo': 292.72, 'noaa': 315.08, 'sg': 292.72}, 'windSpeed': {'icon': 3.82, 'noaa': 1.7, 'sg': 3.82}}, {'airTemperature': {'dwd': 10.32, 'noaa': 8.26, 'sg': 10.32}, 'swellDirection': {'dwd': 321.61, 'icon': 297.43, 'meteo': 295.24, 'noaa': 312.92, 'sg': 295.24}, 'swellHeight': {'dwd': 2.56, 'icon': 3.84, 'meteo': 4.84, 'noaa': 3.45, 'sg': 4.84}, 'swellPeriod': {'dwd': 12.66, 
    'icon': 12.31, 'meteo': 10.6, 'noaa': 13.99, 'sg': 10.6}, 'time': '2022-03-13T09:00:00+00:00', 'waveDirection': {'icon': 297.43, 'meteo': 293.38, 'noaa': 315.15, 'sg': 293.38}, 'windSpeed': {'icon': 2.51, 'noaa': 1.36, 'sg': 2.51}}, {'airTemperature': {'dwd': 11.16, 'noaa': 9.5, 'sg': 11.16}, 'swellDirection': {'dwd': 322.3, 'icon': 298.21, 'meteo': 295.26, 'noaa': 313.41, 'sg': 295.26}, 'swellHeight': {'dwd': 2.61, 'icon': 3.87, 'meteo': 4.79, 'noaa': 3.39, 'sg': 4.79}, 'swellPeriod': {'dwd': 12.85, 'icon': 12.42, 'meteo': 10.52, 'noaa': 13.93, 'sg': 10.52}, 'time': '2022-03-13T10:00:00+00:00', 'waveDirection': {'icon': 298.21, 'meteo': 294.02, 'noaa': 315.13, 'sg': 294.02}, 'windSpeed': {'icon': 2.64, 'noaa': 2.04, 'sg': 2.64}}, {'airTemperature': {'dwd': 11.8, 'noaa': 10.75, 'sg': 11.8}, 'swellDirection': {'dwd': 322.91, 'icon': 298.99, 'meteo': 295.28, 'noaa': 313.91, 'sg': 295.28}, 'swellHeight': {'dwd': 2.65, 'icon': 3.89, 'meteo': 4.73, 'noaa': 3.32, 'sg': 4.73}, 'swellPeriod': {'dwd': 12.99, 'icon': 12.53, 'meteo': 10.43, 'noaa': 13.86, 'sg': 10.43}, 'time': '2022-03-13T11:00:00+00:00', 'waveDirection': {'icon': 298.99, 'meteo': 294.66, 'noaa': 315.12, 'sg': 
    294.66}, 'windSpeed': {'icon': 2.77, 'noaa': 2.71, 'sg': 2.77}}, {'airTemperature': {'dwd': 12.24, 'noaa': 11.99, 'sg': 12.24}, 'swellDirection': {'dwd': 323.33, 'icon': 299.77, 'meteo': 295.3, 'noaa': 314.4, 'sg': 295.3}, 'swellHeight': {'dwd': 2.67, 'icon': 3.92, 'meteo': 4.68, 'noaa': 3.26, 'sg': 4.68}, 'swellPeriod': {'dwd': 13.06, 'icon': 12.64, 'meteo': 10.35, 'noaa': 13.8, 'sg': 10.35}, 'time': '2022-03-13T12:00:00+00:00', 'waveDirection': {'icon': 299.77, 'meteo': 295.3, 'noaa': 315.1, 'sg': 295.3}, 'windSpeed': {'icon': 2.9, 'noaa': 3.39, 'sg': 2.9}}, {'airTemperature': {'dwd': 11.55, 'noaa': 11.54, 'sg': 11.55}, 'swellDirection': {'dwd': 323.55, 'icon': 300.28, 'meteo': 295.7, 'noaa': 314.7, 
    'sg': 295.7}, 'swellHeight': {'dwd': 2.66, 'icon': 3.91, 'meteo': 4.56, 'noaa': 3.15, 'sg': 4.56}, 'swellPeriod': {'dwd': 13.06, 'icon': 12.66, 'meteo': 10.3, 'noaa': 13.68, 'sg': 10.3}, 'time': '2022-03-13T13:00:00+00:00', 'waveDirection': {'icon': 300.29, 'meteo': 295.7, 'noaa': 315.27, 'sg': 295.7}, 'windSpeed': {'icon': 4.77, 'noaa': 3.46, 'sg': 4.77}}, {'airTemperature': {'dwd': 11.84, 'noaa': 11.08, 'sg': 11.84}, 'swellDirection': {'dwd': 323.6, 'icon': 300.79, 'meteo': 296.09, 'noaa': 314.99, 'sg': 296.09}, 'swellHeight': {'dwd': 2.61, 'icon': 3.89, 'meteo': 4.44, 'noaa': 3.04, 'sg': 4.44}, 'swellPeriod': {'dwd': 13.02, 'icon': 12.69, 'meteo': 10.26, 'noaa': 13.56, 'sg': 10.26}, 'time': '2022-03-13T14:00:00+00:00', 'waveDirection': {'icon': 300.82, 'meteo': 296.1, 'noaa': 315.44, 'sg': 296.1}, 'windSpeed': {'icon': 6.65, 'noaa': 3.52, 'sg': 6.65}}, {'airTemperature': {'dwd': 12.11, 'noaa': 10.63, 'sg': 12.11}, 'swellDirection': {'dwd': 323.59, 'icon': 301.3, 'meteo': 296.49, 'noaa': 315.29, 'sg': 296.49}, 'swellHeight': {'dwd': 2.57, 'icon': 3.88, 'meteo': 4.32, 'noaa': 2.93, 'sg': 4.32}, 'swellPeriod': {'dwd': 12.95, 'icon': 12.71, 'meteo': 10.21, 'noaa': 13.44, 'sg': 10.21}, 'time': '2022-03-13T15:00:00+00:00', 'waveDirection': {'icon': 301.34, 'meteo': 296.5, 'noaa': 315.61, 'sg': 296.5}, 'windSpeed': {'icon': 8.52, 'noaa': 3.59, 'sg': 8.52}}, {'airTemperature': {'dwd': 12.19, 'noaa': 9.85, 'sg': 12.19}, 'swellDirection': {'dwd': 323.61, 'icon': 301.56, 'meteo': 296.58, 'noaa': 315.54, 'sg': 296.58}, 'swellHeight': {'dwd': 2.52, 'icon': 3.82, 'meteo': 4.19, 'noaa': 2.84, 'sg': 4.19}, 'swellPeriod': {'dwd': 12.86, 'icon': 
    12.64, 'meteo': 10.13, 'noaa': 13.28, 'sg': 10.13}, 'time': '2022-03-13T16:00:00+00:00', 'waveDirection': {'icon': 301.94, 'meteo': 296.61, 'noaa': 315.77, 'sg': 296.61}, 'windSpeed': {'icon': 8.75, 'noaa': 3.1, 'sg': 8.75}}, {'airTemperature': {'dwd': 12.24, 'noaa': 9.07, 'sg': 12.24}, 'swellDirection': {'dwd': 323.61, 'icon': 301.81, 'meteo': 296.68, 'noaa': 315.78, 'sg': 296.68}, 'swellHeight': {'dwd': 2.45, 'icon': 3.76, 'meteo': 4.06, 'noaa': 2.75, 'sg': 4.06}, 'swellPeriod': {'dwd': 12.75, 'icon': 12.58, 'meteo': 10.04, 'noaa': 13.11, 'sg': 10.04}, 'time': '2022-03-13T17:00:00+00:00', 'waveDirection': {'icon': 302.55, 'meteo': 296.71, 'noaa': 315.92, 'sg': 296.71}, 'windSpeed': {'icon': 8.97, 'noaa': 2.62, 'sg': 8.97}}, {'airTemperature': {'dwd': 12.2, 'noaa': 8.3, 'sg': 12.2}, 'swellDirection': {'dwd': 323.65, 'icon': 302.07, 'meteo': 296.77, 'noaa': 316.03, 'sg': 296.77}, 'swellHeight': {'dwd': 2.38, 'icon': 3.7, 'meteo': 3.93, 'noaa': 2.66, 'sg': 3.93}, 'swellPeriod': {'dwd': 12.64, 'icon': 12.51, 'meteo': 9.96, 'noaa': 12.95, 'sg': 9.96}, 'time': '2022-03-13T18:00:00+00:00', 'waveDirection': {'icon': 303.15, 'meteo': 296.82, 'noaa': 316.08, 'sg': 296.82}, 'windSpeed': {'icon': 9.2, 'noaa': 2.13, 'sg': 9.2}}, {'airTemperature': {'dwd': 12.15, 'noaa': 7.58, 'sg': 12.15}, 'swellDirection': {'dwd': 323.75, 'icon': 303.37, 'meteo': 296.77, 'noaa': 316.36, 'sg': 296.77}, 'swellHeight': {'dwd': 2.32, 'icon': 3.67, 'meteo': 3.81, 'noaa': 2.61, 'sg': 3.81}, 'swellPeriod': {'dwd': 12.53, 'icon': 12.16, 'meteo': 9.88, 'noaa': 12.82, 'sg': 9.88}, 'time': '2022-03-13T19:00:00+00:00', 'waveDirection': {'icon': 304.4, 'meteo': 296.99, 'noaa': 316.11, 'sg': 296.99}, 'windSpeed': {'icon': 8.09, 'noaa': 2.0, 'sg': 8.09}}, {'airTemperature': {'dwd': 12.07, 'noaa': 6.87, 'sg': 12.07}, 'swellDirection': {'dwd': 324.11, 'icon': 304.68, 'meteo': 296.76, 'noaa': 316.7, 'sg': 296.76}, 'swellHeight': {'dwd': 2.28, 'icon': 3.65, 'meteo': 3.68, 'noaa': 2.55, 'sg': 3.68}, 'swellPeriod': {'dwd': 12.36, 'icon': 11.81, 'meteo': 9.79, 'noaa': 12.68, 'sg': 9.79}, 'time': '2022-03-13T20:00:00+00:00', 'waveDirection': {'icon': 305.66, 'meteo': 297.17, 'noaa': 316.13, 'sg': 297.17}, 'windSpeed': {'icon': 6.99, 'noaa': 1.87, 'sg': 6.99}}, {'airTemperature': {'dwd': 12.06, 'noaa': 6.15, 'sg': 12.06}, 'swellDirection': {'dwd': 324.43, 'icon': 305.98, 'meteo': 296.76, 'noaa': 317.03, 'sg': 296.76}, 'swellHeight': {'dwd': 2.24, 'icon': 3.62, 'meteo': 3.56, 'noaa': 2.5, 'sg': 3.56}, 'swellPeriod': {'dwd': 12.22, 'icon': 11.46, 'meteo': 9.71, 'noaa': 12.55, 'sg': 9.71}, 'time': '2022-03-13T21:00:00+00:00', 'waveDirection': {'icon': 306.91, 'meteo': 297.34, 'noaa': 316.16, 'sg': 297.34}, 'windSpeed': {'icon': 5.88, 'noaa': 1.74, 'sg': 5.88}}, {'airTemperature': {'dwd': 11.9, 'noaa': 5.75, 'sg': 11.9}, 'swellDirection': {'dwd': 
    324.97, 'icon': 306.71, 'meteo': 296.81, 'noaa': 317.1, 'sg': 296.81}, 'swellHeight': {'dwd': 2.2, 'icon': 3.55, 'meteo': 3.45, 'noaa': 2.43, 'sg': 3.45}, 'swellPeriod': {'dwd': 12.06, 'icon': 11.32, 'meteo': 9.65, 'noaa': 12.41, 'sg': 9.65}, 'time': '2022-03-13T22:00:00+00:00', 'waveDirection': {'icon': 307.33, 'meteo': 297.6, 'noaa': 316.29, 'sg': 297.6}, 'windSpeed': {'icon': 4.55, 'noaa': 1.91, 'sg': 4.55}}, {'airTemperature': {'dwd': 11.51, 'noaa': 5.35, 'sg': 11.51}, 'swellDirection': {'dwd': 325.61, 'icon': 307.45, 'meteo': 296.87, 'noaa': 317.18, 'sg': 296.87}, 'swellHeight': {'dwd': 2.16, 'icon': 3.48, 'meteo': 3.33, 'noaa': 2.36, 'sg': 3.33}, 'swellPeriod': {'dwd': 11.91, 'icon': 11.17, 'meteo': 9.59, 'noaa': 12.27, 'sg': 9.59}, 'time': '2022-03-13T23:00:00+00:00', 'waveDirection': {'icon': 307.76, 'meteo': 297.86, 'noaa': 316.42, 'sg': 297.86}, 'windSpeed': {'icon': 3.22, 'noaa': 2.07, 'sg': 3.22}}], 'meta': {'cost': 1, 'dailyQuota': 10, 'end': '2022-03-13 23:00', 'lat': 43.5423, 'lng': -5.6592, 'params': ['airTemperature', 'windSpeed', 'waveDirection', 'swellPeriod', 'swellHeight', 'swellDirection'], 'requestCount': 5, 'start': '2022-03-11 23:00'}}       
    {'Nombre': 'San Lorenzo', 'Provincia': 'Melilla', 'CX': '35,2867', 'CY': '-2,9373'}
 

    #json.dump(json.loads(json_data) , file)
    json.dump(json_data , file)
    #file.write(json_data)
    file.close()





#def Forecast(lat,lon,BOT_TOKEN,chat_id):
def Forecast(BOT_TOKEN,chat_id,json_data):

    print("<<<<<<<<<<<<<<<<<<<<<<<")
    #print(threading.get_ident())

    #la = lat
    #lo = lon
    global TABLA1,TABLA2,TABLA3,TABLA4,DIRV,DIRS,DIRV2,DIRS2,MSN,TOKEN,CHAT,AUX
    TOKEN=BOT_TOKEN
    CHAT=chat_id
    
    # Get first hour of today
    start = arrow.now().floor('day')
    print(start)
    # Get last hour of today
    end = start.shift(days=+2)
    print(end)

    
    
     

    x=1
    data= []
    data2= []
    data3= []
    data4 = []
    tem1=[]
    tem2=[]
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
                tem1.append(wS)
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
                tem2.append(wS)
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
    Graficas.grafica1(DIRS,0,tem1)
    DIRS=[]
    Graficas.grafica2(DIRV,0,tem2)
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

    Graficas.grafica1(DIRS2,1,tem1)
    DIRS2=[]
    Graficas.grafica2(DIRV2,1,tem2)
    DIRV2=[]


    bot.sendPhoto(chat_id=CHAT,
        photo=open('WindDirection2.png','rb'),
        reply_markup= InlineKeyboardMarkup([
                    [buttonGV2 , buttonGS2]
         ])   
    )
    
    print(len(data))

    


"""


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


"""