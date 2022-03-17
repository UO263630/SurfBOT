from concurrent.futures import thread
from statistics import linear_regression
from telegram import ChatAction,InlineKeyboardMarkup, InlineKeyboardButton, InlineQueryResultPhoto, InputMedia, InputMediaPhoto
import telegram
from telegram.ext import CallbackQueryHandler, CommandHandler, Updater, ConversationHandler
import arrow
import requests
from tabulate import tabulate
import threading

from uuid import uuid4

import telepot

import Graficas
import os
import json
    
import threading

  
MSN=""
MSND=[]
TABLA1=[]
TABLA2=[]
TABLA3=[]
TABLA4=[]
#DIRV=[]
#DIRS=[]
#DIRV2=[]
#DIRS2=[]
    
DIC=[]
CHAT=""
AUX=0

def busqueda(nombre,provincia,x,y):
        print()
        s="JSON"+nombre+"_"+provincia+".json"

        if(os.path.isfile(s)):
            f = open(s,"r")
            linea= f.readlines()
            f.close()
            f = open(s,"w")
            for line in linea: 
                if line!="nickname_to_delete"+"\n": 
                    f.write(line)

            
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
        
        json_data = {'hours': [{'airTemperature': {'dwd': 11.29, 'noaa': 9.67, 'sg': 11.29}, 'swellDirection': {'dwd': 336.31, 'icon': 306.63, 'meteo': 308.07, 'noaa': 320.05, 'sg': 308.07}, 'swellHeight': {'dwd': 3.11, 'icon': 4.16, 'meteo': 4.0, 'noaa': 2.28, 'sg': 4.0}, 'swellPeriod': {'dwd': 15.63, 'icon': 15.04, 'meteo': 12.71, 'noaa': 15.35, 'sg': 12.71}, 'time': '2022-03-16T23:00:00+00:00', 'waveDirection': {'icon': 307.95, 'meteo': 307.96, 'noaa': 324.07, 'sg': 307.96}, 'windSpeed': {'icon': 7.24, 'noaa': 3.41, 'sg': 7.24}}, {'airTemperature': {'dwd': 11.78, 'noaa': 9.54, 'sg': 11.78}, 'swellDirection': {'dwd': 336.37, 'icon': 306.85, 'meteo': 305.82, 'noaa': 320.46, 'sg': 305.82}, 'swellHeight': {'dwd': 3.17, 
        'icon': 4.22, 'meteo': 4.22, 'noaa': 2.26, 'sg': 4.22}, 'swellPeriod': {'dwd': 15.64, 'icon': 15.04, 'meteo': 12.58, 'noaa': 15.35, 'sg': 12.58}, 'time': '2022-03-17T00:00:00+00:00', 'waveDirection': {'icon': 308.77, 'meteo': 308.36, 'noaa': 326.78, 'sg': 308.36}, 'windSpeed': {'icon': 8.32, 'noaa': 3.6, 'sg': 8.32}}, {'airTemperature': {'dwd': 11.57, 
        'noaa': 9.26, 'sg': 11.57}, 'swellDirection': {'dwd': 336.83, 'icon': 307.25, 'meteo': 305.59, 'noaa': 321.62, 'sg': 305.59}, 'swellHeight': {'dwd': 3.23, 'icon': 4.26, 'meteo': 4.28, 'noaa': 2.35, 'sg': 4.28}, 'swellPeriod': {'dwd': 15.48, 'icon': 14.98, 'meteo': 12.66, 'noaa': 15.62, 'sg': 12.66}, 'time': '2022-03-17T01:00:00+00:00', 'waveDirection': {'icon': 309.2, 'meteo': 308.14, 'noaa': 326.05, 'sg': 308.14}, 'windSpeed': {'icon': 8.12, 'noaa': 3.42, 'sg': 8.12}}, {'airTemperature': {'dwd': 11.36, 'noaa': 8.97, 'sg': 11.36}, 'swellDirection': {'dwd': 337.7, 'icon': 307.66, 'meteo': 305.35, 'noaa': 322.79, 'sg': 305.35}, 'swellHeight': {'dwd': 3.3, 'icon': 4.3, 'meteo': 4.33, 'noaa': 2.43, 'sg': 4.33}, 'swellPeriod': {'dwd': 15.26, 'icon': 14.91, 'meteo': 12.73, 'noaa': 15.88, 'sg': 12.73}, 'time': '2022-03-17T02:00:00+00:00', 'waveDirection': {'icon': 309.62, 'meteo': 307.93, 'noaa': 325.33, 'sg': 307.93}, 'windSpeed': {'icon': 7.92, 'noaa': 3.24, 'sg': 7.92}}, {'airTemperature': {'dwd': 11.17, 'noaa': 8.69, 'sg': 11.17}, 'swellDirection': 
        {'dwd': 338.45, 'icon': 308.06, 'meteo': 305.12, 'noaa': 323.95, 'sg': 305.12}, 'swellHeight': {'dwd': 3.34, 'icon': 4.34, 'meteo': 4.39, 'noaa': 2.52, 'sg': 4.39}, 'swellPeriod': {'dwd': 15.14, 'icon': 14.85, 'meteo': 12.81, 'noaa': 16.15, 'sg': 12.81}, 'time': '2022-03-17T03:00:00+00:00', 'waveDirection': {'icon': 310.05, 'meteo': 307.71, 'noaa': 324.6, 'sg': 307.71}, 'windSpeed': {'icon': 7.72, 'noaa': 3.06, 'sg': 7.72}}, {'airTemperature': {'dwd': 10.91, 'noaa': 8.56, 'sg': 10.91}, 'swellDirection': {'dwd': 338.86, 'icon': 308.52, 'meteo': 304.9, 'noaa': 324.49, 'sg': 304.9}, 'swellHeight': {'dwd': 3.35, 'icon': 4.33, 'meteo': 4.34, 'noaa': 2.59, 'sg': 4.34}, 'swellPeriod': {'dwd': 15.03, 'icon': 14.75, 'meteo': 12.76, 'noaa': 16.28, 'sg': 12.76}, 'time': '2022-03-17T04:00:00+00:00', 'waveDirection': {'icon': 310.15, 'meteo': 307.89, 'noaa': 325.21, 'sg': 307.89}, 'windSpeed': {'icon': 7.39, 'noaa': 3.05, 'sg': 7.39}}, {'airTemperature': {'dwd': 11.05, 'noaa': 8.43, 'sg': 11.05}, 'swellDirection': {'dwd': 339.44, 'icon': 308.97, 'meteo': 304.69, 'noaa': 325.02, 'sg': 304.69}, 'swellHeight': {'dwd': 3.32, 'icon': 4.32, 'meteo': 4.29, 'noaa': 2.66, 'sg': 4.29}, 'swellPeriod': {'dwd': 14.85, 'icon': 14.66, 'meteo': 12.7, 'noaa': 16.42, 'sg': 12.7}, 'time': '2022-03-17T05:00:00+00:00', 'waveDirection': {'icon': 310.25, 'meteo': 308.08, 'noaa': 325.82, 'sg': 308.08}, 'windSpeed': {'icon': 7.05, 'noaa': 3.04, 'sg': 7.05}}, {'airTemperature': {'dwd': 10.86, 'noaa': 8.3, 'sg': 10.86}, 'swellDirection': {'dwd': 339.49, 'icon': 309.43, 'meteo': 304.47, 'noaa': 325.56, 'sg': 304.47}, 'swellHeight': {'dwd': 3.27, 'icon': 4.31, 'meteo': 4.24, 'noaa': 2.73, 'sg': 4.24}, 'swellPeriod': {'dwd': 14.78, 'icon': 14.56, 'meteo': 12.65, 'noaa': 16.55, 'sg': 12.65}, 'time': '2022-03-17T06:00:00+00:00', 'waveDirection': {'icon': 310.35, 'meteo': 308.26, 'noaa': 326.43, 'sg': 308.26}, 'windSpeed': {'icon': 6.72, 'noaa': 3.03, 'sg': 6.72}}, {'airTemperature': {'dwd': 10.99, 'noaa': 8.42, 'sg': 10.99}, 'swellDirection': {'dwd': 339.57, 'icon': 309.59, 'meteo': 304.59, 'noaa': 335.57, 'sg': 304.59}, 'swellHeight': {'dwd': 3.23, 'icon': 4.28, 'meteo': 4.22, 'noaa': 2.04, 'sg': 4.22}, 'swellPeriod': {'dwd': 14.73, 'icon': 14.53, 'meteo': 12.56, 'noaa': 16.67, 'sg': 12.56}, 'time': '2022-03-17T07:00:00+00:00', 'waveDirection': {'icon': 310.45, 'meteo': 308.27, 'noaa': 326.24, 'sg': 308.27}, 'windSpeed': {'icon': 6.67, 'noaa': 2.95, 'sg': 6.67}}, {'airTemperature': {'dwd': 10.87, 'noaa': 8.54, 'sg': 10.87}, 'swellDirection': {'dwd': 339.58, 'icon': 309.75, 'meteo': 304.7, 'noaa': 345.58, 'sg': 304.7}, 'swellHeight': {'dwd': 3.2, 'icon': 4.26, 'meteo': 4.19, 'noaa': 1.36, 'sg': 4.19}, 'swellPeriod': {'dwd': 14.7, 'icon': 14.5, 'meteo': 12.46, 'noaa': 16.78, 'sg': 12.46}, 'time': '2022-03-17T08:00:00+00:00', 'waveDirection': {'icon': 310.54, 'meteo': 308.27, 'noaa': 326.04, 'sg': 308.27}, 'windSpeed': {'icon': 6.61, 'noaa': 2.87, 'sg': 6.61}}, {'airTemperature': {'dwd': 11.0, 'noaa': 8.66, 'sg': 11.0}, 'swellDirection': {'dwd': 339.66, 'icon': 309.91, 'meteo': 304.82, 'noaa': 355.59, 'sg': 304.82}, 'swellHeight': {'dwd': 3.17, 'icon': 4.23, 'meteo': 4.17, 'noaa': 0.67, 'sg': 4.17}, 'swellPeriod': {'dwd': 14.65, 'icon': 14.47, 'meteo': 12.37, 'noaa': 16.9, 'sg': 12.37}, 'time': '2022-03-17T09:00:00+00:00', 'waveDirection': {'icon': 310.64, 'meteo': 308.28, 'noaa': 325.85, 'sg': 308.28}, 'windSpeed': {'icon': 6.56, 'noaa': 2.79, 'sg': 6.56}}, {'airTemperature': {'dwd': 10.74, 'noaa': 9.43, 'sg': 10.74}, 'swellDirection': {'dwd': 339.68, 'icon': 309.97, 'meteo': 304.37, 'noaa': 346.17, 'sg': 304.37}, 'swellHeight': {'dwd': 3.14, 'icon': 4.18, 'meteo': 4.11, 'noaa': 1.3, 'sg': 4.11}, 'swellPeriod': {'dwd': 14.6, 'icon': 14.42, 'meteo': 12.35, 'noaa': 16.44, 'sg': 12.35}, 'time': '2022-03-17T10:00:00+00:00', 'waveDirection': {'icon': 310.71, 'meteo': 308.46, 'noaa': 325.62, 'sg': 308.46}, 'windSpeed': {'icon': 6.58, 'noaa': 3.08, 'sg': 6.58}}, {'airTemperature': {'dwd': 10.72, 'noaa': 10.19, 'sg': 10.72}, 'swellDirection': {'dwd': 339.7, 'icon': 310.02, 'meteo': 303.93, 'noaa': 336.74, 'sg': 303.93}, 'swellHeight': {'dwd': 3.1, 'icon': 4.14, 'meteo': 4.04, 'noaa': 1.94, 'sg': 4.04}, 'swellPeriod': {'dwd': 14.54, 'icon': 14.36, 'meteo': 12.34, 'noaa': 15.99, 'sg': 12.34}, 'time': '2022-03-17T11:00:00+00:00', 'waveDirection': {'icon': 310.79, 'meteo': 308.63, 'noaa': 325.4, 'sg': 308.63}, 'windSpeed': {'icon': 6.59, 'noaa': 3.36, 'sg': 6.59}}, {'airTemperature': {'dwd': 10.93, 'noaa': 10.95, 'sg': 10.93}, 'swellDirection': {'dwd': 339.88, 'icon': 310.08, 'meteo': 303.48, 'noaa': 327.32, 'sg': 303.48}, 'swellHeight': {'dwd': 3.06, 'icon': 4.09, 'meteo': 3.98, 'noaa': 2.57, 'sg': 3.98}, 'swellPeriod': {'dwd': 14.42, 'icon': 14.31, 'meteo': 12.32, 'noaa': 15.53, 'sg': 12.32}, 'time': '2022-03-17T12:00:00+00:00', 'waveDirection': {'icon': 310.86, 'meteo': 308.81, 'noaa': 325.17, 'sg': 308.81}, 'windSpeed': {'icon': 6.61, 'noaa': 3.65, 'sg': 6.61}}, {'airTemperature': {'dwd': 11.12, 'noaa': 10.94, 'sg': 11.12}, 'swellDirection': {'dwd': 340.0, 'icon': 310.11, 'meteo': 303.51, 'noaa': 325.73, 'sg': 303.51}, 'swellHeight': {'dwd': 3.01, 'icon': 4.03, 'meteo': 3.92, 'noaa': 2.47, 'sg': 3.92}, 'swellPeriod': {'dwd': 14.3, 'icon': 14.23, 'meteo': 12.26, 'noaa': 15.44, 'sg': 12.26}, 'time': '2022-03-17T13:00:00+00:00', 'waveDirection': {'icon': 311.0, 'meteo': 308.93, 'noaa': 325.42, 'sg': 308.93}, 'windSpeed': {'icon': 6.78, 'noaa': 3.83, 'sg': 6.78}}, {'airTemperature': {'dwd': 11.15, 'noaa': 10.92, 'sg': 11.15}, 'swellDirection': {'dwd': 340.01, 'icon': 310.14, 'meteo': 303.53, 'noaa': 324.13, 'sg': 303.53}, 'swellHeight': {'dwd': 2.96, 'icon': 3.98, 'meteo': 3.86, 'noaa': 2.36, 'sg': 3.86}, 'swellPeriod': {'dwd': 14.19, 'icon': 14.14, 'meteo': 12.2, 'noaa': 15.34, 'sg': 12.2}, 'time': '2022-03-17T14:00:00+00:00', 'waveDirection': {'icon': 311.13, 'meteo': 309.04, 'noaa': 325.66, 'sg': 309.04}, 'windSpeed': {'icon': 6.96, 'noaa': 4.01, 'sg': 6.96}}, {'airTemperature': {'dwd': 10.97, 'noaa': 10.91, 'sg': 10.97}, 'swellDirection': {'dwd': 340.26, 'icon': 310.17, 'meteo': 303.56, 'noaa': 322.54, 'sg': 303.56}, 'swellHeight': {'dwd': 2.91, 'icon': 3.92, 'meteo': 3.8, 'noaa': 2.26, 'sg': 3.8}, 'swellPeriod': {'dwd': 14.04, 'icon': 14.06, 'meteo': 12.14, 'noaa': 15.25, 'sg': 12.14}, 'time': '2022-03-17T15:00:00+00:00', 'waveDirection': {'icon': 311.27, 'meteo': 309.16, 'noaa': 325.91, 'sg': 309.16}, 'windSpeed': {'icon': 7.13, 'noaa': 4.19, 'sg': 7.13}}, {'airTemperature': {'dwd': 11.03, 'noaa': 10.11, 'sg': 11.03}, 'swellDirection': {'dwd': 340.61, 'icon': 310.24, 'meteo': 303.64, 'noaa': 322.35, 'sg': 303.64}, 'swellHeight': {'dwd': 2.87, 'icon': 3.86, 'meteo': 3.73, 'noaa': 2.2, 'sg': 3.73}, 'swellPeriod': {'dwd': 13.88, 'icon': 13.96, 'meteo': 12.07, 'noaa': 15.1, 'sg': 12.07}, 'time': '2022-03-17T16:00:00+00:00', 'waveDirection': {'icon': 311.49, 'meteo': 309.38, 'noaa': 325.32, 'sg': 309.38}, 'windSpeed': {'icon': 7.18, 'noaa': 3.98, 'sg': 7.18}}, {'airTemperature': {'dwd': 10.98, 'noaa': 
        9.32, 'sg': 10.98}, 'swellDirection': {'dwd': 340.93, 'icon': 310.31, 'meteo': 303.71, 'noaa': 322.17, 'sg': 303.71}, 'swellHeight': {'dwd': 2.82, 'icon': 3.8, 'meteo': 3.67, 'noaa': 2.15, 'sg': 3.67}, 'swellPeriod': {'dwd': 13.73, 'icon': 13.86, 'meteo': 12.01, 'noaa': 14.94, 'sg': 12.01}, 'time': '2022-03-17T17:00:00+00:00', 'waveDirection': {'icon': 311.7, 'meteo': 309.59, 'noaa': 324.72, 'sg': 309.59}, 'windSpeed': {'icon': 7.24, 'noaa': 3.78, 'sg': 7.24}}, {'airTemperature': {'dwd': 11.1, 'noaa': 8.53, 'sg': 11.1}, 'swellDirection': {'dwd': 341.74, 'icon': 310.38, 'meteo': 303.79, 'noaa': 321.98, 'sg': 303.79}, 'swellHeight': {'dwd': 2.78, 'icon': 3.74, 'meteo': 3.6, 'noaa': 2.09, 'sg': 3.6}, 'swellPeriod': {'dwd': 13.52, 'icon': 13.76, 'meteo': 11.94, 'noaa': 14.79, 'sg': 11.94}, 'time': '2022-03-17T18:00:00+00:00', 'waveDirection': {'icon': 311.92, 'meteo': 309.81, 
        'noaa': 324.13, 'sg': 309.81}, 'windSpeed': {'icon': 7.29, 'noaa': 3.57, 'sg': 7.29}}, {'airTemperature': {'dwd': 11.11, 'noaa': 7.62, 'sg': 11.11}, 'swellDirection': {'dwd': 342.63, 'icon': 310.69, 'meteo': 303.84, 'noaa': 321.97, 'sg': 303.84}, 'swellHeight': {'dwd': 2.74, 'icon': 3.68, 'meteo': 3.51, 'noaa': 2.05, 'sg': 3.51}, 'swellPeriod': {'dwd': 13.31, 'icon': 13.63, 'meteo': 11.86, 'noaa': 14.68, 'sg': 11.86}, 'time': '2022-03-17T19:00:00+00:00', 'waveDirection': {'icon': 312.45, 'meteo': 310.47, 'noaa': 323.75, 'sg': 310.47}, 'windSpeed': {'icon': 7.44, 'noaa': 3.26, 'sg': 7.44}}, {'airTemperature': {'dwd': 10.88, 'noaa': 6.72, 'sg': 10.88}, 'swellDirection': {'dwd': 343.45, 'icon': 310.99, 'meteo': 303.9, 'noaa': 321.97, 'sg': 303.9}, 'swellHeight': {'dwd': 2.7, 'icon': 3.63, 'meteo': 3.42, 'noaa': 2.01, 'sg': 3.42}, 'swellPeriod': {'dwd': 13.13, 'icon': 13.5, 'meteo': 11.79, 'noaa': 14.58, 'sg': 11.79}, 'time': '2022-03-17T20:00:00+00:00', 'waveDirection': {'icon': 312.98, 'meteo': 311.14, 'noaa': 323.36, 'sg': 311.14}, 'windSpeed': {'icon': 7.6, 'noaa': 2.94, 'sg': 7.6}}, {'airTemperature': {'dwd': 10.99, 'noaa': 5.81, 'sg': 10.99}, 'swellDirection': {'dwd': 344.53, 'icon': 311.3, 'meteo': 303.95, 'noaa': 321.96, 'sg': 303.95}, 'swellHeight': {'dwd': 2.66, 'icon': 3.57, 'meteo': 3.33, 'noaa': 1.97, 'sg': 3.33}, 'swellPeriod': {'dwd': 12.91, 'icon': 13.37, 'meteo': 11.71, 'noaa': 14.47, 'sg': 11.71}, 'time': '2022-03-17T21:00:00+00:00', 'waveDirection': {'icon': 313.51, 'meteo': 311.8, 'noaa': 322.98, 'sg': 311.8}, 'windSpeed': {'icon': 7.75, 'noaa': 2.63, 'sg': 7.75}}, {'airTemperature': {'dwd': 11.19, 'noaa': 6.39, 'sg': 11.19}, 'swellDirection': {'dwd': 345.46, 'icon': 312.12, 'meteo': 303.94, 'noaa': 322.08, 'sg': 303.94}, 'swellHeight': {'dwd': 2.62, 'icon': 3.53, 'meteo': 3.25, 'noaa': 1.94, 'sg': 3.25}, 'swellPeriod': {'dwd': 12.72, 'icon': 13.21, 'meteo': 11.66, 'noaa': 14.43, 'sg': 11.66}, 'time': '2022-03-17T22:00:00+00:00', 'waveDirection': {'icon': 314.6, 'meteo': 312.47, 'noaa': 323.28, 'sg': 312.47}, 'windSpeed': {'icon': 7.95, 'noaa': 2.64, 'sg': 7.95}}, {'airTemperature': {'dwd': 11.22, 'noaa': 6.97, 'sg': 11.22}, 'swellDirection': {'dwd': 346.8, 'icon': 312.94, 'meteo': 303.92, 'noaa': 322.2, 'sg': 303.92}, 'swellHeight': {'dwd': 2.59, 'icon': 3.49, 'meteo': 3.16, 'noaa': 1.92, 'sg': 3.16}, 'swellPeriod': {'dwd': 12.46, 'icon': 13.05, 'meteo': 11.61, 'noaa': 14.4, 'sg': 11.61}, 'time': '2022-03-17T23:00:00+00:00', 'waveDirection': {'icon': 315.68, 'meteo': 313.13, 'noaa': 323.58, 'sg': 313.13}, 'windSpeed': {'icon': 8.16, 'noaa': 2.64, 'sg': 8.16}}, {'airTemperature': {'dwd': 11.38, 'noaa': 7.56, 'sg': 11.38}, 'swellDirection': {'dwd': 348.17, 'icon': 313.76, 'meteo': 303.91, 'noaa': 322.32, 'sg': 303.91}, 'swellHeight': {'dwd': 2.56, 'icon': 3.45, 'meteo': 3.08, 'noaa': 1.89, 'sg': 3.08}, 'swellPeriod': {'dwd': 12.21, 'icon': 12.89, 'meteo': 11.56, 'noaa': 14.36, 'sg': 11.56}, 'time': '2022-03-18T00:00:00+00:00', 'waveDirection': {'icon': 316.77, 'meteo': 313.8, 'noaa': 323.88, 'sg': 313.8}, 'windSpeed': {'icon': 8.36, 'noaa': 2.65, 'sg': 8.36}}, {'airTemperature': {'dwd': 10.99, 'noaa': 7.01, 'sg': 
        10.99}, 'swellDirection': {'dwd': 349.65, 'icon': 315.3, 'meteo': 304.16, 'noaa': 322.35, 'sg': 304.16}, 'swellHeight': {'dwd': 2.55, 'icon': 3.44, 'meteo': 3.02, 'noaa': 1.87, 
        'sg': 3.02}, 'swellPeriod': {'dwd': 11.98, 'icon': 12.7, 'meteo': 11.52, 'noaa': 14.3, 'sg': 11.52}, 'time': '2022-03-18T01:00:00+00:00', 'waveDirection': {'icon': 317.82, 'meteo': 315.06, 'noaa': 324.05, 'sg': 315.06}, 'windSpeed': {'icon': 7.83, 'noaa': 2.36, 'sg': 7.83}}, {'airTemperature': {'dwd': 10.22, 'noaa': 6.47, 'sg': 10.22}, 'swellDirection': {'dwd': 350.94, 'icon': 316.84, 'meteo': 304.42, 'noaa': 322.38, 'sg': 304.42}, 'swellHeight': {'dwd': 2.53, 'icon': 3.42, 'meteo': 2.96, 'noaa': 1.85, 'sg': 2.96}, 'swellPeriod': {'dwd': 11.8, 'icon': 12.52, 'meteo': 11.47, 'noaa': 14.25, 'sg': 11.47}, 'time': '2022-03-18T02:00:00+00:00', 'waveDirection': {'icon': 318.88, 'meteo': 316.31, 'noaa': 324.22, 'sg': 316.31}, 'windSpeed': {'icon': 7.3, 'noaa': 2.06, 'sg': 7.3}}, {'airTemperature': {'dwd': 9.93, 'noaa': 5.93, 'sg': 9.93}, 'swellDirection': {'dwd': 352.3, 'icon': 318.38, 'meteo': 304.67, 'noaa': 322.41, 'sg': 304.67}, 'swellHeight': {'dwd': 2.52, 'icon': 3.41, 'meteo': 2.9, 'noaa': 1.83, 'sg': 2.9}, 'swellPeriod': {'dwd': 11.65, 'icon': 12.33, 'meteo': 11.43, 'noaa': 14.19, 'sg': 11.43}, 'time': '2022-03-18T03:00:00+00:00', 'waveDirection': {'icon': 319.93, 'meteo': 317.57, 'noaa': 324.39, 'sg': 317.57}, 'windSpeed': {'icon': 6.77, 'noaa': 1.77, 'sg': 6.77}}, {'airTemperature': {'dwd': 9.89, 'noaa': 5.96, 'sg': 9.89}, 'swellDirection': {'dwd': 353.97, 'icon': 318.99, 'meteo': 304.82, 'noaa': 322.39, 'sg': 304.82}, 'swellHeight': {'dwd': 2.52, 'icon': 3.39, 'meteo': 2.87, 'noaa': 1.82, 'sg': 2.87}, 'swellPeriod': {'dwd': 11.49, 'icon': 12.28, 'meteo': 11.42, 'noaa': 14.03, 'sg': 11.42}, 'time': '2022-03-18T04:00:00+00:00', 'waveDirection': {'icon': 321.13, 'meteo': 318.95, 'noaa': 323.4, 'sg': 318.95}, 'windSpeed': {'icon': 7.09, 'noaa': 1.98, 'sg': 7.09}}, {'airTemperature': {'dwd': 9.91, 'noaa': 5.99, 'sg': 9.91}, 'swellDirection': {'dwd': 355.71, 'icon': 319.61, 'meteo': 304.96, 'noaa': 322.37, 'sg': 304.96}, 'swellHeight': {'dwd': 2.53, 'icon': 3.37, 'meteo': 2.83, 'noaa': 1.81, 'sg': 2.83}, 'swellPeriod': {'dwd': 11.33, 'icon': 12.24, 'meteo': 11.42, 'noaa': 13.88, 'sg': 11.42}, 'time': '2022-03-18T05:00:00+00:00', 'waveDirection': {'icon': 322.33, 'meteo': 320.34, 'noaa': 322.4, 'sg': 320.34}, 'windSpeed': {'icon': 7.41, 'noaa': 2.18, 'sg': 7.41}}, {'airTemperature': {'dwd': 10.15, 'noaa': 6.03, 'sg': 10.15}, 'swellDirection': {'dwd': 357.0, 'icon': 320.22, 'meteo': 305.11, 'noaa': 322.35, 'sg': 305.11}, 'swellHeight': {'dwd': 2.53, 'icon': 3.35, 'meteo': 2.8, 'noaa': 1.8, 'sg': 2.8}, 'swellPeriod': {'dwd': 11.21, 'icon': 12.19, 'meteo': 11.41, 'noaa': 13.72, 'sg': 11.41}, 'time': '2022-03-18T06:00:00+00:00', 'waveDirection': {'icon': 323.53, 'meteo': 321.72, 'noaa': 321.41, 'sg': 321.72}, 'windSpeed': {'icon': 7.73, 'noaa': 2.39, 'sg': 7.73}}, {'airTemperature': {'dwd': 11.07, 'noaa': 7.37, 'sg': 11.07}, 'swellDirection': {'dwd': 357.77, 'icon': 318.7, 'meteo': 305.31, 'noaa': 322.27, 'sg': 305.31}, 'swellHeight': {'dwd': 2.52, 'icon': 3.3, 
        'meteo': 2.78, 'noaa': 1.78, 'sg': 2.78}, 'swellPeriod': {'dwd': 11.15, 'icon': 12.33, 'meteo': 11.42, 'noaa': 13.64, 'sg': 11.42}, 'time': '2022-03-18T07:00:00+00:00', 'waveDirection': {'icon': 324.79, 'meteo': 322.52, 'noaa': 321.45, 'sg': 322.52}, 'windSpeed': {'icon': 8.38, 'noaa': 2.9, 'sg': 8.38}}, {'airTemperature': {'dwd': 11.53, 'noaa': 8.72, 
        'sg': 11.53}, 'swellDirection': {'dwd': 358.47, 'icon': 317.18, 'meteo': 305.5, 'noaa': 322.2, 'sg': 305.5}, 'swellHeight': {'dwd': 2.52, 'icon': 3.24, 'meteo': 2.76, 'noaa': 1.76, 'sg': 2.76}, 'swellPeriod': {'dwd': 11.09, 'icon': 12.47, 'meteo': 11.43, 'noaa': 13.57, 'sg': 11.43}, 'time': '2022-03-18T08:00:00+00:00', 'waveDirection': {'icon': 326.06, 'meteo': 323.31, 'noaa': 321.5, 'sg': 323.31}, 'windSpeed': {'icon': 9.02, 'noaa': 3.42, 'sg': 9.02}}, {'airTemperature': {'dwd': 11.39, 'noaa': 10.07, 'sg': 11.39}, 'swellDirection': {'dwd': 358.85, 'icon': 315.66, 'meteo': 305.7, 'noaa': 322.12, 'sg': 305.7}, 'swellHeight': {'dwd': 2.52, 'icon': 3.19, 'meteo': 2.74, 'noaa': 1.74, 'sg': 2.74}, 'swellPeriod': {'dwd': 11.06, 'icon': 12.61, 'meteo': 11.44, 'noaa': 13.49, 'sg': 11.44}, 'time': '2022-03-18T09:00:00+00:00', 'waveDirection': {'icon': 327.32, 'meteo': 324.11, 'noaa': 321.54, 'sg': 324.11}, 'windSpeed': {'icon': 9.67, 'noaa': 3.93, 'sg': 9.67}}, {'airTemperature': {'dwd': 11.3, 'noaa': 10.65, 'sg': 11.3}, 'swellDirection': {'dwd': 356.39, 
        'icon': 316.68, 'meteo': 305.98, 'noaa': 322.17, 'sg': 305.98}, 'swellHeight': {'dwd': 2.47, 'icon': 3.21, 'meteo': 2.73, 'noaa': 1.72, 'sg': 2.73}, 'swellPeriod': {'dwd': 11.35, 'icon': 12.56, 'meteo': 11.48, 'noaa': 13.46, 'sg': 11.48}, 'time': '2022-03-18T10:00:00+00:00', 'waveDirection': {'icon': 327.69, 'meteo': 324.7, 'noaa': 321.52, 'sg': 324.7}, 'windSpeed': {'icon': 9.55, 'noaa': 4.14, 'sg': 9.55}}, {'airTemperature': {'dwd': 11.47, 'noaa': 11.24, 'sg': 11.47}, 'swellDirection': {'dwd': 357.75, 'icon': 317.7, 'meteo': 306.27, 'noaa': 322.22, 'sg': 306.27}, 'swellHeight': {'dwd': 2.49, 'icon': 3.23, 'meteo': 2.73, 'noaa': 1.7, 'sg': 2.73}, 'swellPeriod': {'dwd': 11.25, 'icon': 12.52, 'meteo': 11.53, 'noaa': 13.43, 'sg': 11.53}, 'time': '2022-03-18T11:00:00+00:00', 'waveDirection': {'icon': 328.06, 'meteo': 325.29, 'noaa': 321.51, 'sg': 325.29}, 'windSpeed': {'icon': 9.43, 'noaa': 4.36, 'sg': 9.43}}, {'airTemperature': {'dwd': 11.56, 'noaa': 11.82, 'sg': 11.56}, 'swellDirection': {'dwd': 357.68, 'icon': 318.72, 'meteo': 306.55, 'noaa': 322.27, 'sg': 306.55}, 'swellHeight': {'dwd': 2.5, 'icon': 3.25, 'meteo': 2.72, 'noaa': 1.68, 'sg': 2.72}, 'swellPeriod': {'dwd': 11.3, 'icon': 12.47, 'meteo': 11.57, 'noaa': 13.4, 'sg': 11.57}, 'time': '2022-03-18T12:00:00+00:00', 'waveDirection': {'icon': 328.43, 'meteo': 325.88, 'noaa': 321.49, 'sg': 325.88}, 'windSpeed': {'icon': 9.31, 'noaa': 4.57, 'sg': 9.31}}, {'airTemperature': {'dwd': 11.63, 'noaa': 11.76, 'sg': 11.63}, 'swellDirection': {'dwd': 357.82, 'icon': 319.48, 'meteo': 306.92, 'noaa': 321.88, 'sg': 306.92}, 'swellHeight': {'dwd': 2.51, 'icon': 3.26, 'meteo': 2.72, 'noaa': 1.64, 'sg': 2.72}, 'swellPeriod': {'dwd': 11.34, 'icon': 12.47, 'meteo': 11.61, 'noaa': 13.45, 'sg': 11.61}, 'time': '2022-03-18T13:00:00+00:00', 'waveDirection': {'icon': 328.9, 'meteo': 326.1, 'noaa': 321.6, 'sg': 326.1}, 'windSpeed': {'icon': 9.27, 'noaa': 4.52, 'sg': 9.27}}, {'airTemperature': {'dwd': 11.49, 'noaa': 11.7, 'sg': 11.49}, 'swellDirection': {'dwd': 357.44, 'icon': 320.25, 'meteo': 307.3, 'noaa': 321.49, 'sg': 307.3}, 'swellHeight': {'dwd': 2.52, 'icon': 3.28, 'meteo': 2.72, 'noaa': 1.61, 'sg': 2.72}, 'swellPeriod': {'dwd': 11.44, 'icon': 12.46, 'meteo': 11.65, 'noaa': 13.5, 'sg': 11.65}, 'time': '2022-03-18T14:00:00+00:00', 'waveDirection': {'icon': 329.37, 'meteo': 326.33, 'noaa': 321.72, 'sg': 326.33}, 'windSpeed': {'icon': 9.23, 'noaa': 4.48, 'sg': 9.23}}, {'airTemperature': {'dwd': 11.62, 'noaa': 11.64, 'sg': 11.62}, 'swellDirection': {'dwd': 357.82, 'icon': 321.01, 'meteo': 307.67, 'noaa': 321.1, 'sg': 307.67}, 'swellHeight': {'dwd': 2.54, 'icon': 3.29, 'meteo': 
        2.72, 'noaa': 1.57, 'sg': 2.72}, 'swellPeriod': {'dwd': 11.47, 'icon': 12.46, 'meteo': 11.69, 'noaa': 13.55, 'sg': 11.69}, 'time': '2022-03-18T15:00:00+00:00', 'waveDirection': 
        {'icon': 329.84, 'meteo': 326.55, 'noaa': 321.83, 'sg': 326.55}, 'windSpeed': {'icon': 9.19, 'noaa': 4.43, 'sg': 9.19}}, {'airTemperature': {'dwd': 11.63, 'noaa': 10.67, 'sg': 11.63}, 'swellDirection': {'dwd': 358.17, 'icon': 321.88, 'meteo': 308.01, 'noaa': 322.08, 'sg': 308.01}, 'swellHeight': {'dwd': 2.57, 'icon': 3.3, 'meteo': 2.71, 'noaa': 1.65, 'sg': 2.71}, 'swellPeriod': {'dwd': 11.51, 'icon': 12.45, 'meteo': 11.7, 'noaa': 13.91, 'sg': 11.7}, 'time': '2022-03-18T16:00:00+00:00', 'waveDirection': {'icon': 330.54, 'meteo': 327.31, 'noaa': 323.69, 'sg': 327.31}, 'windSpeed': {'icon': 9.24, 'noaa': 3.98, 'sg': 9.24}}, {'airTemperature': {'dwd': 11.6, 'noaa': 9.7, 'sg': 11.6}, 'swellDirection': {'dwd': 357.99, 'icon': 322.76, 'meteo': 308.35, 'noaa': 323.05, 'sg': 308.35}, 'swellHeight': {'dwd': 2.58, 'icon': 3.3, 'meteo': 2.7, 'noaa': 1.74, 'sg': 2.7}, 'swellPeriod': {'dwd': 11.58, 'icon': 12.43, 'meteo': 11.72, 'noaa': 14.28, 'sg': 11.72}, 'time': '2022-03-18T17:00:00+00:00', 'waveDirection': {'icon': 331.23, 'meteo': 328.07, 'noaa': 325.55, 
        'sg': 328.07}, 'windSpeed': {'icon': 9.28, 'noaa': 3.53, 'sg': 9.28}}, {'airTemperature': {'dwd': 11.48, 'noaa': 8.72, 'sg': 11.48}, 'swellDirection': {'dwd': 358.52, 'icon': 323.63, 'meteo': 308.69, 'noaa': 324.03, 'sg': 308.69}, 'swellHeight': {'dwd': 2.59, 'icon': 3.31, 'meteo': 2.69, 'noaa': 1.82, 'sg': 2.69}, 'swellPeriod': {'dwd': 11.58, 'icon': 
        12.42, 'meteo': 11.73, 'noaa': 14.64, 'sg': 11.73}, 'time': '2022-03-18T18:00:00+00:00', 'waveDirection': {'icon': 331.93, 'meteo': 328.83, 'noaa': 327.41, 'sg': 328.83}, 'windSpeed': {'icon': 9.33, 'noaa': 3.08, 'sg': 9.33}}, {'airTemperature': {'dwd': 11.54, 'noaa': 7.98, 'sg': 11.54}, 'swellDirection': {'dwd': 0.11, 'icon': 325.01, 'meteo': 308.85, 
        'noaa': 324.17, 'sg': 308.85}, 'swellHeight': {'dwd': 2.62, 'icon': 3.31, 'meteo': 2.65, 'noaa': 1.82, 'sg': 2.65}, 'swellPeriod': {'dwd': 11.43, 'icon': 12.32, 'meteo': 11.7, 'noaa': 14.46, 'sg': 11.7}, 'time': '2022-03-18T19:00:00+00:00', 'waveDirection': {'icon': 331.81, 'meteo': 328.99, 'noaa': 326.48, 'sg': 328.99}, 'windSpeed': {'icon': 8.94, 'noaa': 2.9, 'sg': 8.94}}, {'airTemperature': {'dwd': 11.7, 'noaa': 7.23, 'sg': 11.7}, 'swellDirection': {'dwd': 1.08, 'icon': 326.38, 'meteo': 309.0, 'noaa': 324.31, 'sg': 309.0}, 'swellHeight': {'dwd': 2.63, 'icon': 3.3, 'meteo': 2.61, 'noaa': 1.83, 'sg': 2.61}, 'swellPeriod': {'dwd': 11.33, 'icon': 12.22, 'meteo': 11.68, 'noaa': 14.29, 'sg': 11.68}, 'time': '2022-03-18T20:00:00+00:00', 'waveDirection': {'icon': 331.7, 'meteo': 329.15, 'noaa': 325.56, 'sg': 329.15}, 'windSpeed': {'icon': 8.55, 'noaa': 2.73, 'sg': 8.55}}, {'airTemperature': {'dwd': 12.02, 'noaa': 6.48, 'sg': 12.02}, 'swellDirection': {'dwd': 0.58, 'icon': 327.76, 'meteo': 309.16, 'noaa': 324.45, 'sg': 309.16}, 'swellHeight': {'dwd': 2.59, 'icon': 3.3, 'meteo': 2.57, 'noaa': 1.83, 'sg': 2.57}, 'swellPeriod': {'dwd': 11.37, 'icon': 12.12, 'meteo': 11.65, 'noaa': 14.11, 'sg': 11.65}, 'time': '2022-03-18T21:00:00+00:00', 'waveDirection': {'icon': 331.58, 'meteo': 329.31, 'noaa': 324.63, 'sg': 329.31}, 'windSpeed': {'icon': 8.16, 'noaa': 2.55, 'sg': 8.16}}, {'airTemperature': {'dwd': 11.99, 'noaa': 6.45, 'sg': 11.99}, 'swellDirection': {'dwd': 0.46, 'icon': 328.23, 'meteo': 309.15, 'noaa': 347.9, 'sg': 309.15}, 'swellHeight': {'dwd': 2.56, 'icon': 3.25, 'meteo': 2.51, 'noaa': 1.43, 'sg': 2.51}, 'swellPeriod': {'dwd': 11.34, 'icon': 12.05, 'meteo': 11.6, 'noaa': 11.81, 'sg': 11.6}, 'time': '2022-03-18T22:00:00+00:00', 'waveDirection': {'icon': 331.45, 'meteo': 329.1, 'noaa': 324.25, 'sg': 329.1}, 'windSpeed': {'icon': 7.76, 'noaa': 2.29, 'sg': 7.76}}, {'airTemperature': {'dwd': 11.61, 'noaa': 6.42, 'sg': 11.61}, 'swellDirection': {'dwd': 0.38, 'icon': 328.71, 'meteo': 309.14, 'noaa': 11.34, 'sg': 309.14}, 'swellHeight': {'dwd': 2.51, 'icon': 3.2, 'meteo': 2.45, 'noaa': 1.02, 'sg': 
        2.45}, 'swellPeriod': {'dwd': 11.29, 'icon': 11.97, 'meteo': 11.54, 'noaa': 9.52, 'sg': 11.54}, 'time': '2022-03-18T23:00:00+00:00', 'waveDirection': {'icon': 331.32, 'meteo': 328.88, 'noaa': 323.88, 'sg': 328.88}, 'windSpeed': {'icon': 7.35, 'noaa': 2.03, 'sg': 7.35}}], 'meta': {'cost': 1, 'dailyQuota': 10, 'end': '2022-03-18 23:00', 'lat': 43.5423, 'lng': -5.6592, 'params': ['airTemperature', 'windSpeed', 'waveDirection', 'swellPeriod', 'swellHeight', 'swellDirection'], 'requestCount': 2, 'start': '2022-03-16 23:00'}}
        

        #json.dump(json.loads(json_data) , file)
        json.dump(json_data , file)
        #file.write(json_data)
        file.close()

def datos(id):
    tipo=9
    json=[]
    global DIC
    print(id)
    aux=0
    for x in DIC:
        print(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,")
        print(x[0])
        print(x[2])
        if(x[0] ==id):
            #print(x[1])
            #print(x[2])
            if(x[2]<=3):
                x[2]=x[2]+4
                tipo=x[2]
                
                json = x[1]
                
            if(x[2]>3 and x[2]<=7):
                x[2]=x[2]-4
                tipo=x[2]
                json=x[1]
                aux=1
            else:
                print("ERROR")

            #print(DIC)
            print(json)
            tabla=tablas(id,json)
            print(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,")
            print(tabla)
            return tabla
            print(id)
    
    


def tablas(id,json_data):
    
    # Get first hour of today
    start = arrow.now().floor('day')
    print(start)
    # Get last hour of today
    end = start.shift(days=+2)
    print(end)
    
    data= []
    data2= []
    data3= []
    data4 = []
    DIRS=[]
    DIRV=[]
    DIRS2=[]
    DIRV2=[]
    tem1=[]
    tem2=[]
    x=1


    f=str(start).split("T")
    dia=f[0].split("-")
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
                DIRV.append(wD)
                DIRS.append(sD)
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


    if(id==0):
        tabla1=tabulate( data , headers=["hora","Temperatura" , "Velocidad viento"]  )
        return tabla1
    if(id==1):
        Graficas.grafica1(DIRS,0,tem1)
        DIRS=[]
        g="WindDirection.png"
        return g
    if(id==2):
        tabla3=tabulate( data3 , headers=["hora","Temperatura" , "Velocidad viento"]  )
        return tabla3
    if(id==3):
        Graficas.grafica2(DIRV,0,tem2)
        DIRV=[]
        g="SwellDirection.png"
        return g
    if(id==4):
        tabla2= tabulate( data2 , headers=["hora","Periodo oleaje" , "Altura de ola"]  ) 
        return tabla2
    if(id==5):
        Graficas.grafica1(DIRS2,1,tem1)
        DIRS2=[]
        g="WindDirection2.png"
        return g
    if(id==6):
        tabla4=tabulate( data4 , headers=["hora","Periodo oleaje" , "Altura de ola"]  )
        return tabla4
    if(id==7):
        Graficas.grafica2(DIRV2,1,tem2)
        DIRV2=[]
        g="SwellDirection2.png"
        return g
        
    print()


def Forecast1(BOT_TOKEN,chat_id,json_data):
    print("<<<<<<<<<<<<<<<<<<<<<<<")

    global TABLA1,TABLA2,TABLA3,TABLA4,MSN,TOKEN,CHAT,DIC
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
    DIRS=[]
    DIRV=[]
    DIRS2=[]
    DIRV2=[]
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
                DIRV.append(wD)
                DIRS.append(sD)
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
    
    
    TABLA2= tabulate( data2 , headers=["hora","Periodo oleaje" , "Altura de ola"]  ) 
    
    T12 =TABLA1 +"\n" + "________________________" +"\n"+ TABLA2
    print(T12)
    f=bot.sendMessage( CHAT, TABLA1,           
                    reply_markup=InlineKeyboardMarkup([
                        [buttonI , buttonD]])
                    )
    
    MSN=f['message_id']
    d=[MSN,json_data,0]
    DIC.append(d)
    print("-----MSN-----")
    print(MSN)
    
    #print(DIRS)
    Graficas.grafica1(DIRS,0,tem1)
    DIRS=[]
    Graficas.grafica2(DIRV,0,tem2)
    DIRV=[]

    n=bot.sendPhoto(chat_id=CHAT,
        photo=open('WindDirection.png','rb') ,
        reply_markup=InlineKeyboardMarkup([
                        [buttonGV , buttonGS]])
                    
    )
    print("----message_id------")
    print(n['message_id'])
    
    
    d=[n['message_id'],json_data,1]

    DIC.append(d)

    print("Al dia siguiente")
    bot.sendMessage(CHAT,text="Al dia siguiente")


    TABLA3=tabulate( data3 , headers=["hora","Temperatura" , "Velocidad viento"]  ) 

    TABLA4=tabulate( data4 , headers=["hora","Periodo oleaje" , "Altura de ola"]  )

    T34 =TABLA3 +"\n" + "____________" +"\n"+ TABLA4
    print(T34)

    n=bot.sendMessage( CHAT, TABLA3 ,           
                    reply_markup=InlineKeyboardMarkup([
                        [buttonI , buttonD]])
                    )
    d=[n['message_id'],json_data,2]

    DIC.append(d)
    

    Graficas.grafica1(DIRS2,1,tem1)
    DIRS2=[]
    Graficas.grafica2(DIRV2,1,tem2)
    DIRV2=[]

 
    n=bot.sendPhoto(chat_id=CHAT,
        photo=open('WindDirection2.png','rb'),
        reply_markup=InlineKeyboardMarkup([
                        [buttonGV , buttonGS]])
    )
    
    d=[n['message_id'],json_data,3]

    DIC.append(d)

    #print(DIC)
    #while(True):
    #   True


buttonI = InlineKeyboardButton(
        text= "<---",
        callback_data='BI'
)
buttonD = InlineKeyboardButton(
        text= "--->",
        callback_data='BI'
)
buttonGV = InlineKeyboardButton(
        text= "<---",
        callback_data='BGV'
)
buttonGS = InlineKeyboardButton(
        text= "--->",
        callback_data='BGV'
)


def cambioI(id,chat):
    tabla=datos(id)
    global MSN,AUX,CHAT
    MSN1=id
    #CHAT=chat
    #print(chat)
    print("<<<<<<<<<<<<<<<<<<<<<<<")
    #print(threading.get_ident())
    bot2=telegram.Bot(TOKEN)
    bot2.editMessageText(text=tabla,
                    chat_id=chat,
                    message_id=MSN1,
                    reply_markup=InlineKeyboardMarkup([
                    [buttonI , buttonD]]
                    
                )
    )
"""
def cambioD(id,chat):
    tabla=datos(id)
    global MSN,AUX,CHAT
    MSN1=id
    #CHAT=chat
    #print(chat)
    print("<<<<<<<<<<<<<<<<<<<<<<<")
    #print(threading.get_ident())
    bot2=telegram.Bot(TOKEN)
    bot2.editMessageText(text=tabla,
                    chat_id=chat,
                    message_id=MSN1,
                    reply_markup=InlineKeyboardMarkup([
                    [buttonI, buttonD]]
                    
                )
    )
"""

def cambioGI(id,chat):
    tabla=datos(id)
    global MSN,AUX,CHAT
    MSN1=id
    #CHAT=chat
    #print(chat)
    print("<<<<<<<<<<<<<<<<<<<<<<<")
    #print(threading.get_ident())
    bot2=telegram.Bot(TOKEN)
    bot2.editMessageMedia(
                            media=InputMediaPhoto(media = open(tabla,'rb')),
                            reply_markup= InlineKeyboardMarkup([
                            [buttonGV , buttonGS]
                            ]),
                            chat_id=chat,
                            message_id=MSN1
        )
"""
def cambioGD(id,chat):
    tabla=datos(id)
    global MSN,AUX,CHAT
    MSN1=id
    #CHAT=chat
    #print(chat)
    print("<<<<<<<<<<<<<<<<<<<<<<<")
    #print(threading.get_ident())
    bot2=telegram.Bot(TOKEN)
    bot2.editMessageMedia(
                            media=InputMediaPhoto(media = open(tabla,'rb')),
                            reply_markup= InlineKeyboardMarkup([
                            [buttonGV , buttonGS]
                            ]),
                            chat_id=chat,
                            message_id=MSN1
        )
"""

