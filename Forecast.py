from telegram import InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto
import telegram

import arrow

from tabulate import tabulate




import Graficas
import os
import json
    


   
DIC=[]
TOKEN=""

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
        
        json_data = {'hours': [{'airTemperature': {'dwd': 11.22, 'noaa': 7.3, 'sg': 11.22}, 'swellDirection': {'dwd': 347.05, 'icon': 311.88, 'meteo': 303.92, 'noaa': 322.15, 'sg': 303.92}, 'swellHeight': {'dwd': 2.59, 'icon': 3.42, 'meteo': 3.16, 'noaa': 1.9, 'sg': 3.16}, 'swellPeriod': {'dwd': 12.29, 'icon': 13.07, 'meteo': 11.61, 'noaa': 14.4, 'sg': 11.61}, 'time': '2022-03-17T23:00:00+00:00', 'waveDirection': {'icon': 316.73, 'meteo': 313.13, 'noaa': 323.56, 'sg': 313.13}, 'windSpeed': {'icon': 8.88, 'noaa': 2.86, 'sg': 8.88}}, {'airTemperature': {'dwd': 11.18, 'noaa': 8.05, 'sg': 11.18}, 'swellDirection': {'dwd': 348.94, 'icon': 312.17, 'meteo': 303.91, 'noaa': 322.24, 'sg': 303.91}, 'swellHeight': {'dwd': 2.58, 'icon': 3.35, 'meteo': 3.08, 'noaa': 1.87, 'sg': 3.08}, 'swellPeriod': {'dwd': 11.99, 'icon': 12.92, 'meteo': 11.56, 'noaa': 14.36, 'sg': 11.56}, 'time': '2022-03-18T00:00:00+00:00', 'waveDirection': {'icon': 318.34, 'meteo': 313.8, 'noaa': 323.85, 'sg': 313.8}, 'windSpeed': {'icon': 9.44, 'noaa': 2.97, 'sg': 9.44}}, {'airTemperature': {'dwd': 11.25, 'noaa': 7.62, 'sg': 11.25}, 'swellDirection': {'dwd': 351.28, 'icon': 313.76, 'meteo': 303.57, 'noaa': 322.24, 'sg': 303.57}, 'swellHeight': {'dwd': 2.57, 'icon': 3.34, 'meteo': 3.0, 'noaa': 1.85, 'sg': 3.0}, 'swellPeriod': {'dwd': 11.66, 'icon': 12.74, 'meteo': 11.46, 'noaa': 14.3, 'sg': 11.46}, 'time': '2022-03-18T01:00:00+00:00', 'waveDirection': {'icon': 319.3, 'meteo': 316.53, 'noaa': 323.98, 'sg': 316.53}, 'windSpeed': {'icon': 8.94, 'noaa': 2.75, 'sg': 8.94}}, {'airTemperature': {'dwd': 11.09, 'noaa': 7.18, 'sg': 11.09}, 'swellDirection': {'dwd': 352.66, 'icon': 315.35, 'meteo': 303.23, 'noaa': 322.24, 'sg': 303.23}, 'swellHeight': {'dwd': 2.56, 'icon': 3.34, 'meteo': 2.92, 'noaa': 1.83, 'sg': 
        2.92}, 'swellPeriod': {'dwd': 11.49, 'icon': 12.56, 'meteo': 11.37, 'noaa': 14.23, 'sg': 11.37}, 'time': '2022-03-18T02:00:00+00:00', 'waveDirection': {'icon': 320.27, 'meteo': 
        319.26, 'noaa': 324.1, 'sg': 319.26}, 'windSpeed': {'icon': 8.44, 'noaa': 2.52, 'sg': 8.44}}, {'airTemperature': {'dwd': 10.86, 'noaa': 6.75, 'sg': 10.86}, 'swellDirection': {'dwd': 353.42, 'icon': 316.94, 'meteo': 302.89, 'noaa': 322.24, 'sg': 302.89}, 'swellHeight': {'dwd': 2.53, 'icon': 3.33, 'meteo': 2.84, 'noaa': 1.81, 'sg': 2.84}, 'swellPeriod': 
        {'dwd': 11.4, 'icon': 12.38, 'meteo': 11.27, 'noaa': 14.17, 'sg': 11.27}, 'time': '2022-03-18T03:00:00+00:00', 'waveDirection': {'icon': 321.23, 'meteo': 321.99, 'noaa': 324.23, 'sg': 321.99}, 'windSpeed': {'icon': 7.94, 'noaa': 2.3, 'sg': 7.94}}, {'airTemperature': {'dwd': 10.91, 'noaa': 6.6, 'sg': 10.91}, 'swellDirection': {'dwd': 353.99, 'icon': 317.4, 'meteo': 303.01, 'noaa': 322.2, 'sg': 303.01}, 'swellHeight': {'dwd': 2.51, 'icon': 3.31, 'meteo': 2.81, 'noaa': 1.8, 'sg': 2.81}, 'swellPeriod': {'dwd': 11.33, 'icon': 12.35, 'meteo': 11.26, 'noaa': 14.02, 'sg': 11.26}, 'time': '2022-03-18T04:00:00+00:00', 'waveDirection': {'icon': 321.87, 'meteo': 322.23, 'noaa': 323.23, 'sg': 322.23}, 'windSpeed': {'icon': 8.15, 'noaa': 2.18, 'sg': 8.15}}, {'airTemperature': {'dwd': 11.08, 'noaa': 6.45, 'sg': 11.08}, 'swellDirection': {'dwd': 354.47, 'icon': 317.86, 'meteo': 303.12, 'noaa': 322.16, 'sg': 303.12}, 'swellHeight': {'dwd': 2.49, 'icon': 3.29, 'meteo': 2.79, 'noaa': 1.79, 'sg': 2.79}, 'swellPeriod': {'dwd': 11.27, 'icon': 12.31, 'meteo': 11.25, 'noaa': 13.86, 'sg': 11.25}, 'time': '2022-03-18T05:00:00+00:00', 'waveDirection': {'icon': 322.51, 'meteo': 322.48, 'noaa': 322.22, 'sg': 322.48}, 'windSpeed': {'icon': 8.35, 'noaa': 2.05, 'sg': 8.35}}, {'airTemperature': {'dwd': 11.19, 'noaa': 6.3, 'sg': 11.19}, 'swellDirection': {'dwd': 354.85, 'icon': 318.32, 'meteo': 303.24, 'noaa': 322.12, 'sg': 303.24}, 'swellHeight': {'dwd': 2.47, 'icon': 3.27, 'meteo': 2.76, 'noaa': 1.78, 'sg': 2.76}, 'swellPeriod': {'dwd': 11.24, 'icon': 12.28, 'meteo': 11.24, 'noaa': 13.71, 'sg': 11.24}, 'time': '2022-03-18T06:00:00+00:00', 'waveDirection': {'icon': 323.15, 'meteo': 322.72, 'noaa': 321.22, 'sg': 322.72}, 'windSpeed': {'icon': 8.56, 'noaa': 1.93, 'sg': 8.56}}, {'airTemperature': {'dwd': 11.3, 'noaa': 7.29, 'sg': 11.3}, 'swellDirection': {'dwd': 355.17, 'icon': 316.92, 'meteo': 303.54, 'noaa': 322.06, 'sg': 303.54}, 'swellHeight': {'dwd': 2.46, 'icon': 3.22, 'meteo': 2.75, 'noaa': 1.76, 'sg': 2.75}, 'swellPeriod': {'dwd': 11.21, 'icon': 12.42, 'meteo': 11.26, 'noaa': 13.64, 'sg': 11.26}, 'time': '2022-03-18T07:00:00+00:00', 'waveDirection': {'icon': 324.18, 'meteo': 323.24, 'noaa': 321.27, 'sg': 323.24}, 'windSpeed': {'icon': 9.0, 'noaa': 2.15, 'sg': 9.0}}, {'airTemperature': {'dwd': 11.37, 'noaa': 8.28, 'sg': 11.37}, 'swellDirection': {'dwd': 355.23, 'icon': 315.53, 'meteo': 303.84, 'noaa': 322.01, 'sg': 303.84}, 'swellHeight': {'dwd': 2.45, 'icon': 3.17, 'meteo': 2.74, 'noaa': 1.75, 'sg': 2.74}, 'swellPeriod': {'dwd': 11.22, 'icon': 12.56, 'meteo': 11.29, 'noaa': 13.56, 'sg': 11.29}, 'time': '2022-03-18T08:00:00+00:00', 'waveDirection': {'icon': 325.22, 'meteo': 323.75, 'noaa': 321.31, 'sg': 323.75}, 'windSpeed': {'icon': 9.43, 'noaa': 2.37, 'sg': 9.43}}, {'airTemperature': {'dwd': 11.34, 'noaa': 9.28, 'sg': 11.34}, 'swellDirection': {'dwd': 353.69, 'icon': 314.13, 'meteo': 304.14, 'noaa': 321.95, 'sg': 304.14}, 'swellHeight': {'dwd': 2.42, 'icon': 3.12, 'meteo': 2.73, 'noaa': 1.73, 'sg': 2.73}, 'swellPeriod': {'dwd': 11.4, 'icon': 12.7, 'meteo': 11.31, 'noaa': 13.49, 'sg': 11.31}, 'time': '2022-03-18T09:00:00+00:00', 'waveDirection': {'icon': 326.25, 'meteo': 324.27, 'noaa': 321.36, 'sg': 324.27}, 'windSpeed': {'icon': 9.87, 'noaa': 2.59, 'sg': 9.87}}, {'airTemperature': {'dwd': 11.28, 'noaa': 10.09, 'sg': 11.28}, 'swellDirection': {'dwd': 353.25, 'icon': 315.06, 'meteo': 304.68, 'noaa': 322.06, 'sg': 304.68}, 'swellHeight': {'dwd': 2.41, 'icon': 3.14, 'meteo': 2.73, 'noaa': 1.71, 'sg': 2.73}, 'swellPeriod': {'dwd': 11.47, 'icon': 12.68, 'meteo': 11.37, 'noaa': 13.46, 'sg': 11.37}, 'time': '2022-03-18T10:00:00+00:00', 'waveDirection': {'icon': 327.67, 'meteo': 324.96, 'noaa': 321.38, 'sg': 324.96}, 'windSpeed': {'icon': 9.89, 'noaa': 3.32, 'sg': 9.89}}, {'airTemperature': {'dwd': 11.29, 'noaa': 10.9, 'sg': 11.29}, 'swellDirection': {'dwd': 353.45, 'icon': 315.99, 'meteo': 305.21, 'noaa': 322.16, 'sg': 305.21}, 'swellHeight': {'dwd': 2.42, 'icon': 3.16, 'meteo': 2.73, 'noaa': 1.69, 'sg': 2.73}, 'swellPeriod': {'dwd': 11.5, 'icon': 12.66, 'meteo': 11.43, 'noaa': 13.44, 'sg': 11.43}, 'time': '2022-03-18T11:00:00+00:00', 'waveDirection': {'icon': 329.08, 'meteo': 325.65, 'noaa': 321.4, 'sg': 325.65}, 'windSpeed': {'icon': 9.9, 'noaa': 4.04, 'sg': 9.9}}, {'airTemperature': {'dwd': 11.36, 'noaa': 11.72, 'sg': 11.36}, 'swellDirection': {'dwd': 354.62, 'icon': 316.92, 'meteo': 305.75, 'noaa': 322.27, 'sg': 305.75}, 'swellHeight': {'dwd': 2.46, 'icon': 3.18, 'meteo': 2.73, 'noaa': 1.67, 'sg': 2.73}, 'swellPeriod': {'dwd': 11.45, 'icon': 12.64, 'meteo': 11.49, 'noaa': 13.41, 'sg': 11.49}, 'time': '2022-03-18T12:00:00+00:00', 'waveDirection': {'icon': 330.5, 'meteo': 326.34, 'noaa': 321.42, 'sg': 326.34}, 'windSpeed': {'icon': 9.92, 'noaa': 4.77, 'sg': 9.92}}, {'airTemperature': {'dwd': 11.48, 'noaa': 11.58, 'sg': 11.48}, 'swellDirection': {'dwd': 356.49, 'icon': 319.22, 'meteo': 306.37, 'noaa': 321.9, 'sg': 306.37}, 'swellHeight': {'dwd': 2.51, 'icon': 3.23, 'meteo': 2.74, 'noaa': 1.63, 'sg': 2.74}, 'swellPeriod': {'dwd': 11.36, 'icon': 12.55, 'meteo': 11.56, 'noaa': 13.46, 'sg': 11.56}, 'time': '2022-03-18T13:00:00+00:00', 'waveDirection': {'icon': 330.84, 'meteo': 326.62, 'noaa': 321.55, 'sg': 326.62}, 'windSpeed': {'icon': 9.69, 'noaa': 4.62, 'sg': 9.69}}, {'airTemperature': {'dwd': 11.37, 'noaa': 11.43, 'sg': 11.37}, 'swellDirection': {'dwd': 356.06, 'icon': 321.51, 'meteo': 306.99, 'noaa': 321.53, 'sg': 306.99}, 'swellHeight': {'dwd': 2.53, 'icon': 3.29, 'meteo': 2.74, 'noaa': 1.6, 'sg': 2.74}, 'swellPeriod': {'dwd': 11.53, 'icon': 12.46, 'meteo': 11.62, 'noaa': 13.51, 'sg': 11.62}, 'time': '2022-03-18T14:00:00+00:00', 'waveDirection': {'icon': 331.19, 'meteo': 326.91, 'noaa': 321.69, 'sg': 326.91}, 'windSpeed': {'icon': 9.46, 'noaa': 4.47, 'sg': 9.46}}, {'airTemperature': {'dwd': 11.22, 'noaa': 11.29, 'sg': 11.22}, 'swellDirection': {'dwd': 357.75, 'icon': 323.81, 'meteo': 307.61, 'noaa': 321.16, 'sg': 307.61}, 'swellHeight': {'dwd': 2.59, 'icon': 3.34, 'meteo': 2.75, 'noaa': 1.56, 'sg': 2.75}, 'swellPeriod': {'dwd': 11.49, 'icon': 12.37, 'meteo': 11.69, 'noaa': 13.56, 'sg': 11.69}, 'time': '2022-03-18T15:00:00+00:00', 'waveDirection': {'icon': 331.53, 'meteo': 327.19, 'noaa': 321.82, 'sg': 327.19}, 'windSpeed': {'icon': 9.23, 'noaa': 4.32, 'sg': 9.23}}, {'airTemperature': {'dwd': 11.32, 'noaa': 10.58, 'sg': 11.32}, 'swellDirection': {'dwd': 358.41, 'icon': 324.44, 'meteo': 308.07, 'noaa': 331.71, 'sg': 308.07}, 'swellHeight': {'dwd': 2.63, 'icon': 3.35, 'meteo': 2.75, 'noaa': 1.23, 'sg': 2.75}, 'swellPeriod': {'dwd': 11.55, 'icon': 12.4, 'meteo': 11.73, 'noaa': 14.27, 'sg': 11.73}, 'time': '2022-03-18T16:00:00+00:00', 'waveDirection': {'icon': 331.35, 'meteo': 327.09, 'noaa': 323.69, 'sg': 327.09}, 'windSpeed': {'icon': 9.05, 'noaa': 3.84, 'sg': 9.05}}, {'airTemperature': {'dwd': 11.53, 'noaa': 9.87, 'sg': 11.53}, 'swellDirection': {'dwd': 358.53, 'icon': 325.07, 'meteo': 308.54, 'noaa': 342.27, 'sg': 308.54}, 'swellHeight': {'dwd': 2.65, 'icon': 3.36, 'meteo': 2.74, 'noaa': 0.89, 'sg': 2.74}, 'swellPeriod': {'dwd': 11.65, 'icon': 12.42, 'meteo': 11.77, 'noaa': 14.98, 'sg': 11.77}, 'time': '2022-03-18T17:00:00+00:00', 'waveDirection': {'icon': 331.18, 'meteo': 326.98, 'noaa': 325.56, 'sg': 326.98}, 'windSpeed': {'icon': 8.86, 'noaa': 3.36, 'sg': 8.86}}, {'airTemperature': {'dwd': 11.55, 'noaa': 9.16, 'sg': 11.55}, 'swellDirection': {'dwd': 358.12, 'icon': 325.7, 'meteo': 309.0, 'noaa': 352.82, 'sg': 309.0}, 'swellHeight': {'dwd': 2.66, 'icon': 3.37, 'meteo': 2.74, 'noaa': 0.56, 'sg': 2.74}, 'swellPeriod': {'dwd': 11.78, 'icon': 12.45, 'meteo': 11.81, 'noaa': 15.69, 'sg': 11.81}, 'time': '2022-03-18T18:00:00+00:00', 'waveDirection': {'icon': 331.0, 'meteo': 326.88, 'noaa': 327.43, 'sg': 326.88}, 'windSpeed': {'icon': 8.68, 'noaa': 2.88, 'sg': 8.68}}, {'airTemperature': {'dwd': 11.56, 'noaa': 8.32, 'sg': 11.56}, 'swellDirection': {'dwd': 358.31, 'icon': 325.92, 'meteo': 309.23, 'noaa': 343.3, 'sg': 309.23}, 'swellHeight': {'dwd': 2.66, 'icon': 3.36, 'meteo': 2.72, 'noaa': 0.98, 'sg': 2.72}, 'swellPeriod': {'dwd': 11.8, 'icon': 12.44, 'meteo': 11.82, 'noaa': 15.16, 'sg': 11.82}, 'time': '2022-03-18T19:00:00+00:00', 'waveDirection': {'icon': 330.56, 'meteo': 327.01, 'noaa': 326.44, 'sg': 327.01}, 'windSpeed': {'icon': 8.38, 'noaa': 2.71, 'sg': 8.38}}, {'airTemperature': {'dwd': 11.63, 'noaa': 7.48, 'sg': 11.63}, 'swellDirection': {'dwd': 358.21, 'icon': 326.14, 'meteo': 309.46, 'noaa': 333.78, 'sg': 309.46}, 'swellHeight': {'dwd': 2.65, 'icon': 3.34, 'meteo': 2.69, 'noaa': 1.39, 'sg': 2.69}, 'swellPeriod': {'dwd': 11.81, 'icon': 12.44, 'meteo': 11.83, 'noaa': 14.64, 'sg': 11.83}, 'time': '2022-03-18T20:00:00+00:00', 'waveDirection': {'icon': 330.11, 'meteo': 327.15, 'noaa': 325.46, 'sg': 327.15}, 'windSpeed': {'icon': 8.08, 'noaa': 2.55, 'sg': 8.08}}, {'airTemperature': {'dwd': 11.7, 'noaa': 6.65, 'sg': 11.7}, 'swellDirection': {'dwd': 358.05, 'icon': 326.36, 'meteo': 309.69, 'noaa': 324.26, 'sg': 309.69}, 'swellHeight': {'dwd': 2.63, 'icon': 3.33, 'meteo': 2.67, 'noaa': 1.81, 'sg': 2.67}, 'swellPeriod': {'dwd': 11.81, 'icon': 12.43, 'meteo': 11.84, 'noaa': 14.11, 'sg': 11.84}, 'time': '2022-03-18T21:00:00+00:00', 'waveDirection': {'icon': 329.67, 'meteo': 327.28, 'noaa': 324.47, 'sg': 327.28}, 'windSpeed': {'icon': 7.78, 'noaa': 2.38, 'sg': 7.78}}, {'airTemperature': {'dwd': 11.62, 'noaa': 6.58, 'sg': 11.62}, 'swellDirection': {'dwd': 357.76, 'icon': 326.33, 'meteo': 309.75, 'noaa': 348.15, 'sg': 
        309.75}, 'swellHeight': {'dwd': 2.59, 'icon': 3.28, 'meteo': 2.62, 'noaa': 1.39, 'sg': 2.62}, 'swellPeriod': {'dwd': 11.78, 'icon': 12.38, 'meteo': 11.81, 'noaa': 11.86, 'sg': 11.81}, 'time': '2022-03-18T22:00:00+00:00', 'waveDirection': {'icon': 328.98, 'meteo': 327.14, 'noaa': 324.03, 'sg': 327.14}, 'windSpeed': {'icon': 7.33, 'noaa': 2.19, 'sg': 7.33}}, {'airTemperature': {'dwd': 11.49, 'noaa': 6.52, 'sg': 11.49}, 'swellDirection': {'dwd': 357.05, 'icon': 326.29, 'meteo': 309.8, 'noaa': 12.04, 'sg': 309.8}, 'swellHeight': 
        {'dwd': 2.54, 'icon': 3.24, 'meteo': 2.58, 'noaa': 0.98, 'sg': 2.58}, 'swellPeriod': {'dwd': 11.77, 'icon': 12.32, 'meteo': 11.77, 'noaa': 9.62, 'sg': 11.77}, 'time': '2022-03-18T23:00:00+00:00', 'waveDirection': {'icon': 328.3, 'meteo': 327.01, 'noaa': 323.59, 'sg': 327.01}, 'windSpeed': {'icon': 6.89, 'noaa': 2.0, 'sg': 6.89}}, {'airTemperature': {'dwd': 11.21, 'noaa': 6.45, 'sg': 11.21}, 'swellDirection': {'dwd': 356.29, 'icon': 326.26, 'meteo': 309.86, 'noaa': 35.93, 'sg': 309.86}, 'swellHeight': {'dwd': 2.48, 'icon': 3.19, 'meteo': 2.53, 'noaa': 0.56, 'sg': 2.53}, 'swellPeriod': {'dwd': 11.75, 'icon': 12.27, 'meteo': 11.74, 'noaa': 7.37, 'sg': 11.74}, 'time': '2022-03-19T00:00:00+00:00', 'waveDirection': {'icon': 327.61, 'meteo': 326.87, 'noaa': 323.15, 'sg': 326.87}, 'windSpeed': {'icon': 6.44, 'noaa': 1.81, 'sg': 6.44}}, {'airTemperature': {'dwd': 11.09, 'noaa': 6.56, 'sg': 11.09}, 'swellDirection': {'dwd': 355.49, 'icon': 325.86, 'meteo': 309.74, 'noaa': 35.16, 'sg': 309.74}, 'swellHeight': {'dwd': 2.41, 'icon': 3.12, 'meteo': 2.46, 'noaa': 0.54, 'sg': 2.46}, 'swellPeriod': {'dwd': 11.71, 'icon': 12.2, 'meteo': 11.68, 'noaa': 7.29, 'sg': 11.68}, 'time': '2022-03-19T01:00:00+00:00', 'waveDirection': {'icon': 326.84, 'meteo': 326.22, 'noaa': 322.88, 'sg': 326.22}, 'windSpeed': {'icon': 5.86, 'noaa': 1.73, 'sg': 5.86}}, {'airTemperature': {'dwd': 10.98, 'noaa': 6.66, 'sg': 10.98}, 'swellDirection': {'dwd': 354.66, 'icon': 325.46, 'meteo': 309.62, 'noaa': 34.38, 'sg': 309.62}, 'swellHeight': {'dwd': 2.33, 'icon': 3.04, 'meteo': 2.4, 'noaa': 0.53, 'sg': 2.4}, 'swellPeriod': {'dwd': 11.67, 'icon': 12.14, 'meteo': 11.62, 'noaa': 7.2, 'sg': 11.62}, 'time': '2022-03-19T02:00:00+00:00', 'waveDirection': {'icon': 326.06, 'meteo': 325.57, 'noaa': 322.6, 'sg': 325.57}, 'windSpeed': {'icon': 5.28, 'noaa': 1.65, 'sg': 5.28}}, {'airTemperature': {'dwd': 10.57, 'noaa': 6.77, 'sg': 10.57}, 'swellDirection': {'dwd': 353.82, 
        'icon': 325.06, 'meteo': 309.5, 'noaa': 33.61, 'sg': 309.5}, 'swellHeight': {'dwd': 2.25, 'icon': 2.97, 'meteo': 2.33, 'noaa': 0.51, 'sg': 2.33}, 'swellPeriod': {'dwd': 11.62, 'icon': 12.07, 'meteo': 11.56, 'noaa': 7.12, 'sg': 11.56}, 'time': '2022-03-19T03:00:00+00:00', 'waveDirection': {'icon': 325.29, 'meteo': 324.92, 'noaa': 322.33, 'sg': 324.92}, 
        'windSpeed': {'icon': 4.7, 'noaa': 1.57, 'sg': 4.7}}, {'airTemperature': {'dwd': 9.95, 'noaa': 7.09, 'sg': 9.95}, 'swellDirection': {'dwd': 353.01, 'icon': 324.68, 'meteo': 309.43, 'noaa': 34.21, 'sg': 309.43}, 'swellHeight': {'dwd': 2.17, 'icon': 2.89, 'meteo': 2.26, 'noaa': 0.47, 'sg': 2.26}, 'swellPeriod': {'dwd': 11.56, 'icon': 12.01, 'meteo': 11.48, 'noaa': 7.02, 'sg': 11.48}, 'time': '2022-03-19T04:00:00+00:00', 'waveDirection': {'icon': 324.83, 'meteo': 324.08, 'noaa': 322.1, 'sg': 324.08}, 'windSpeed': {'icon': 3.97, 
        'noaa': 1.67, 'sg': 3.97}}, {'airTemperature': {'dwd': 9.36, 'noaa': 7.42, 'sg': 9.36}, 'swellDirection': {'dwd': 352.38, 'icon': 324.3, 'meteo': 309.35, 'noaa': 34.8, 'sg': 309.35}, 'swellHeight': {'dwd': 2.1, 'icon': 2.8, 'meteo': 2.18, 'noaa': 0.44, 'sg': 2.18}, 'swellPeriod': {'dwd': 11.49, 'icon': 11.96, 'meteo': 11.4, 'noaa': 6.92, 'sg': 11.4}, 'time': '2022-03-19T05:00:00+00:00', 'waveDirection': {'icon': 324.38, 'meteo': 323.24, 'noaa': 321.86, 'sg': 323.24}, 'windSpeed': {'icon': 3.24, 'noaa': 1.78, 'sg': 3.24}}, {'airTemperature': {'dwd': 9.16, 'noaa': 7.74, 'sg': 9.16}, 'swellDirection': {'dwd': 352.05, 'icon': 323.92, 'meteo': 309.28, 'noaa': 35.4, 'sg': 309.28}, 'swellHeight': {'dwd': 2.03, 'icon': 2.72, 'meteo': 2.11, 'noaa': 0.4, 'sg': 2.11}, 'swellPeriod': {'dwd': 11.4, 'icon': 11.9, 'meteo': 11.32, 'noaa': 6.82, 'sg': 11.32}, 'time': '2022-03-19T06:00:00+00:00', 'waveDirection': {'icon': 323.92, 'meteo': 322.4, 'noaa': 321.63, 'sg': 322.4}, 'windSpeed': {'icon': 2.51, 'noaa': 1.88, 'sg': 2.51}}, {'airTemperature': {'dwd': 9.44, 'noaa': 9.97, 'sg': 9.44}, 'swellDirection': {'dwd': 352.07, 'icon': 324.23, 'meteo': 309.22, 'noaa': 34.86, 'sg': 309.22}, 'swellHeight': {'dwd': 1.96, 'icon': 2.64, 'meteo': 2.04, 'noaa': 0.39, 'sg': 2.04}, 'swellPeriod': {'dwd': 11.29, 'icon': 11.81, 'meteo': 11.24, 'noaa': 6.73, 'sg': 11.24}, 'time': '2022-03-19T07:00:00+00:00', 'waveDirection': {'icon': 324.23, 'meteo': 322.19, 'noaa': 320.55, 'sg': 322.19}, 'windSpeed': {'icon': 2.28, 'noaa': 1.69, 'sg': 2.28}}, {'airTemperature': {'dwd': 10.06, 'noaa': 12.2, 'sg': 10.06}, 'swellDirection': {'dwd': 352.46, 'icon': 324.53, 'meteo': 309.15, 'noaa': 34.33, 'sg': 309.15}, 'swellHeight': {'dwd': 1.91, 'icon': 2.56, 'meteo': 1.96, 'noaa': 0.37, 'sg': 1.96}, 'swellPeriod': {'dwd': 11.18, 'icon': 11.72, 'meteo': 11.17, 'noaa': 6.64, 'sg': 11.17}, 'time': '2022-03-19T08:00:00+00:00', 'waveDirection': {'icon': 324.53, 'meteo': 
        321.98, 'noaa': 319.47, 'sg': 321.98}, 'windSpeed': {'icon': 2.05, 'noaa': 1.51, 'sg': 2.05}}, {'airTemperature': {'dwd': 10.99, 'noaa': 14.43, 'sg': 10.99}, 'swellDirection': {'dwd': 353.32, 'icon': 324.84, 'meteo': 309.09, 'noaa': 33.79, 'sg': 309.09}, 'swellHeight': {'dwd': 1.86, 'icon': 2.48, 'meteo': 1.89, 'noaa': 0.36, 'sg': 1.89}, 'swellPeriod': {'dwd': 11.04, 'icon': 11.63, 'meteo': 11.09, 'noaa': 6.55, 'sg': 11.09}, 'time': '2022-03-19T09:00:00+00:00', 'waveDirection': {'icon': 324.84, 'meteo': 321.77, 'noaa': 318.39, 'sg': 321.77}, 'windSpeed': {'icon': 1.82, 'noaa': 1.32, 'sg': 1.82}}, {'airTemperature': {'dwd': 11.68, 'noaa': 15.63, 'sg': 11.68}, 'swellDirection': {'dwd': 354.65, 'icon': 325.89, 'meteo': 309.04, 'noaa': 33.05, 'sg': 309.04}, 'swellHeight': {'dwd': 1.82, 'icon': 2.42, 'meteo': 1.83, 'noaa': 0.37, 'sg': 1.83}, 'swellPeriod': {'dwd': 10.89, 'icon': 11.52, 'meteo': 11.04, 'noaa': 6.7, 'sg': 11.04}, 'time': '2022-03-19T10:00:00+00:00', 'waveDirection': {'icon': 325.89, 'meteo': 322.33, 'noaa': 318.46, 'sg': 322.33}, 'windSpeed': {'icon': 1.85, 'noaa': 1.64, 'sg': 1.85}}, {'airTemperature': {'dwd': 11.78, 'noaa': 16.83, 'sg': 11.78}, 'swellDirection': {'dwd': 356.29, 'icon': 326.95, 'meteo': 308.98, 'noaa': 32.3, 'sg': 308.98}, 'swellHeight': {'dwd': 1.79, 'icon': 2.35, 'meteo': 1.77, 'noaa': 0.38, 'sg': 1.77}, 'swellPeriod': {'dwd': 10.74, 'icon': 11.4, 'meteo': 10.98, 
        'noaa': 6.85, 'sg': 10.98}, 'time': '2022-03-19T11:00:00+00:00', 'waveDirection': {'icon': 326.95, 'meteo': 322.89, 'noaa': 318.54, 'sg': 322.89}, 'windSpeed': {'icon': 1.88, 'noaa': 1.96, 'sg': 1.88}}, {'airTemperature': {'dwd': 11.88, 'noaa': 18.03, 'sg': 11.88}, 'swellDirection': {'dwd': 357.93, 'icon': 328.0, 'meteo': 308.93, 'noaa': 31.56, 'sg': 308.93}, 'swellHeight': {'dwd': 1.75, 'icon': 2.29, 'meteo': 1.71, 'noaa': 0.39, 'sg': 1.71}, 'swellPeriod': {'dwd': 10.6, 'icon': 11.29, 'meteo': 10.93, 'noaa': 7.0, 'sg': 10.93}, 'time': '2022-03-19T12:00:00+00:00', 'waveDirection': {'icon': 328.0, 'meteo': 323.45, 'noaa': 318.61, 'sg': 323.45}, 'windSpeed': {'icon': 1.91, 'noaa': 2.28, 'sg': 1.91}}, 
        {'airTemperature': {'dwd': 11.84, 'noaa': 16.88, 'sg': 11.84}, 'swellDirection': {'dwd': 359.34, 'icon': 329.15, 'meteo': 308.89, 'noaa': 8.1, 'sg': 308.89}, 'swellHeight': {'dwd': 1.72, 'icon': 2.23, 'meteo': 1.66, 'noaa': 0.61, 'sg': 1.66}, 'swellPeriod': {'dwd': 10.48, 'icon': 11.2, 'meteo': 10.9, 'noaa': 8.85, 'sg': 10.9}, 'time': '2022-03-19T13:00:00+00:00', 'waveDirection': {'icon': 329.16, 'meteo': 323.85, 'noaa': 318.98, 'sg': 323.85}, 'windSpeed': {'icon': 2.44, 'noaa': 2.19, 'sg': 2.44}}, {'airTemperature': {'dwd': 
        11.99, 'noaa': 15.74, 'sg': 11.99}, 'swellDirection': {'dwd': 0.37, 'icon': 330.31, 'meteo': 308.85, 'noaa': 344.65, 'sg': 308.85}, 'swellHeight': {'dwd': 1.68, 'icon': 2.17, 'meteo': 1.62, 'noaa': 0.82, 'sg': 1.62}, 'swellPeriod': {'dwd': 10.39, 'icon': 11.11, 'meteo': 10.88, 'noaa': 10.7, 'sg': 10.88}, 'time': '2022-03-19T14:00:00+00:00', 'waveDirection': {'icon': 330.32, 'meteo': 324.24, 'noaa': 319.35, 'sg': 324.24}, 'windSpeed': {'icon': 2.98, 'noaa': 2.1, 'sg': 2.98}}, {'airTemperature': {'dwd': 12.18, 'noaa': 14.59, 'sg': 12.18}, 'swellDirection': {'dwd': 1.0, 'icon': 331.46, 'meteo': 308.81, 'noaa': 321.19, 'sg': 308.81}, 'swellHeight': {'dwd': 1.63, 'icon': 2.11, 'meteo': 1.57, 'noaa': 1.04, 'sg': 1.57}, 'swellPeriod': {'dwd': 10.34, 'icon': 11.02, 'meteo': 10.85, 'noaa': 12.55, 'sg': 10.85}, 'time': '2022-03-19T15:00:00+00:00', 'waveDirection': {'icon': 331.48, 'meteo': 324.64, 'noaa': 319.72, 'sg': 324.64}, 'windSpeed': {'icon': 3.51, 'noaa': 2.01, 'sg': 3.51}}, {'airTemperature': {'dwd': 12.3, 'noaa': 14.2, 'sg': 12.3}, 'swellDirection': {'dwd': 1.28, 'icon': 331.95, 'meteo': 308.66, 'noaa': 339.32, 'sg': 308.66}, 'swellHeight': {'dwd': 1.58, 'icon': 2.05, 'meteo': 1.54, 'noaa': 0.76, 'sg': 1.54}, 'swellPeriod': {'dwd': 10.31, 'icon': 10.98, 'meteo': 10.85, 'noaa': 12.02, 'sg': 10.85}, 'time': '2022-03-19T16:00:00+00:00', 'waveDirection': {'icon': 331.96, 'meteo': 324.35, 'noaa': 319.31, 'sg': 324.35}, 'windSpeed': {'icon': 3.15, 'noaa': 2.16, 'sg': 3.15}}, {'airTemperature': {'dwd': 12.44, 'noaa': 13.82, 'sg': 12.44}, 'swellDirection': {'dwd': 1.35, 'icon': 332.44, 'meteo': 308.5, 'noaa': 357.44, 'sg': 308.5}, 'swellHeight': {'dwd': 1.53, 'icon': 2.0, 'meteo': 1.5, 'noaa': 0.49, 'sg': 1.5}, 'swellPeriod': {'dwd': 10.3, 'icon': 
        10.94, 'meteo': 10.85, 'noaa': 11.5, 'sg': 10.85}, 'time': '2022-03-19T17:00:00+00:00', 'waveDirection': {'icon': 332.45, 'meteo': 324.05, 'noaa': 318.91, 'sg': 324.05}, 'windSpeed': {'icon': 2.79, 'noaa': 2.31, 'sg': 2.79}}, {'airTemperature': {'dwd': 12.55, 'noaa': 13.43, 'sg': 12.55}, 'swellDirection': {'dwd': 1.31, 'icon': 332.93, 'meteo': 308.35, 
        'noaa': 15.57, 'sg': 308.35}, 'swellHeight': {'dwd': 1.48, 'icon': 1.94, 'meteo': 1.47, 'noaa': 0.21, 'sg': 1.47}, 'swellPeriod': {'dwd': 10.3, 'icon': 10.9, 'meteo': 10.85, 'noaa': 10.97, 'sg': 10.85}, 'time': '2022-03-19T18:00:00+00:00', 'waveDirection': {'icon': 332.93, 'meteo': 323.76, 'noaa': 318.5, 'sg': 323.76}, 'windSpeed': {'icon': 2.43, 'noaa': 2.46, 'sg': 2.43}}, {'airTemperature': {'dwd': 12.67, 'noaa': 12.46, 'sg': 12.67}, 'swellDirection': {'dwd': 1.23, 'icon': 332.08, 'meteo': 307.99, 'noaa': 0.45, 'sg': 307.99}, 'swellHeight': {'dwd': 1.43, 'icon': 1.9, 'meteo': 1.45, 'noaa': 0.3, 'sg': 1.45}, 'swellPeriod': {'dwd': 10.32, 'icon': 10.96, 'meteo': 10.86, 'noaa': 12.31, 'sg': 10.86}, 'time': '2022-03-19T19:00:00+00:00', 'waveDirection': {'icon': 332.08, 'meteo': 322.48, 'noaa': 318.42, 'sg': 322.48}, 'windSpeed': {'icon': 2.24, 'noaa': 2.34, 'sg': 2.24}}, {'airTemperature': {'dwd': 12.75, 'noaa': 11.49, 'sg': 12.75}, 'swellDirection': {'dwd': 1.1, 'icon': 331.23, 'meteo': 307.62, 'noaa': 345.32, 'sg': 307.62}, 'swellHeight': {'dwd': 1.38, 'icon': 1.85, 'meteo': 1.43, 'noaa': 0.39, 'sg': 1.43}, 'swellPeriod': {'dwd': 10.35, 'icon': 11.01, 'meteo': 10.86, 'noaa': 13.65, 'sg': 10.86}, 'time': '2022-03-19T20:00:00+00:00', 'waveDirection': {'icon': 331.23, 'meteo': 321.2, 'noaa': 318.34, 'sg': 321.2}, 'windSpeed': {'icon': 2.06, 'noaa': 2.22, 'sg': 2.06}}, {'airTemperature': {'dwd': 12.78, 'noaa': 10.51, 'sg': 12.78}, 'swellDirection': {'dwd': 0.89, 'icon': 330.38, 'meteo': 307.26, 'noaa': 330.2, 'sg': 307.26}, 'swellHeight': {'dwd': 1.34, 'icon': 1.81, 'meteo': 1.41, 'noaa': 0.48, 'sg': 1.41}, 'swellPeriod': {'dwd': 10.4, 'icon': 11.07, 'meteo': 10.87, 'noaa': 14.99, 'sg': 10.87}, 'time': '2022-03-19T21:00:00+00:00', 'waveDirection': {'icon': 330.38, 'meteo': 319.92, 'noaa': 318.26, 'sg': 319.92}, 'windSpeed': {'icon': 1.87, 'noaa': 2.1, 'sg': 1.87}}, {'airTemperature': {'dwd': 12.65, 'noaa': 10.37, 'sg': 12.65}, 'swellDirection': {'dwd': 0.53, 'icon': 327.94, 'meteo': 305.46, 'noaa': 329.7, 'sg': 305.46}, 'swellHeight': {'dwd': 1.3, 'icon': 1.8, 'meteo': 1.36, 'noaa': 0.51, 'sg': 1.36}, 'swellPeriod': {'dwd': 10.46, 'icon': 11.24, 'meteo': 10.72, 'noaa': 14.74, 'sg': 10.72}, 'time': '2022-03-19T22:00:00+00:00', 'waveDirection': {'icon': 327.94, 'meteo': 317.31, 'noaa': 319.09, 'sg': 317.31}, 'windSpeed': {'icon': 1.35, 'noaa': 2.22, 'sg': 1.35}}, {'airTemperature': {'dwd': 12.26, 'noaa': 10.23, 'sg': 12.26}, 'swellDirection': {'dwd': 0.71, 'icon': 325.51, 'meteo': 303.66, 'noaa': 329.19, 'sg': 303.66}, 'swellHeight': {'dwd': 1.27, 'icon': 1.79, 'meteo': 1.3, 'noaa': 0.55, 'sg': 1.3}, 'swellPeriod': {'dwd': 10.5, 'icon': 11.4, 'meteo': 10.56, 'noaa': 14.5, 'sg': 10.56}, 'time': '2022-03-19T23:00:00+00:00', 'waveDirection': {'icon': 325.51, 'meteo': 314.69, 'noaa': 319.93, 'sg': 314.69}, 'windSpeed': {'icon': 0.82, 'noaa': 2.33, 'sg': 0.82}}], 'meta': {'cost': 1, 'dailyQuota': 10, 'end': '2022-03-19 23:00', 'lat': 43.5423, 'lng': -5.6592, 'params': ['airTemperature', 'windSpeed', 'waveDirection', 'swellPeriod', 'swellHeight', 'swellDirection'], 'requestCount': 2, 'start': '2022-03-17 23:00'}}
        

        #json.dump(json.loads(json_data) , file)
        json.dump(json_data , file)
        #file.write(json_data)
        file.close()

def datos(id,chat):
    tipo=9
    json=[]
    global DIC
    print(id)
    print(chat)
    aux=0
    for x in DIC:
        print(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,INICIO,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,")
        print(x[0])
        print(x[3])
        if(x[0] ==id):
            #print(x[1])
            print(x[2])
            if(x[3] ==chat):
                if(x[2]<=3 and aux==0):
                    x[2]=x[2]+4
                    tipo=x[2]    
                    json=x[1]
                    aux=1
                    print(x[2])
                if(x[2]>=4 and x[2]<=7 and aux==0):
                    x[2]=x[2]-4
                    tipo=x[2]
                    json=x[1]
                    aux=1
                    print(x[2])
                if(x[2]>=8 and aux==0):
                    print("ERROR")

            print(tipo)
            #print(json)
            tabla=tablas(tipo,json)
            print(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,FIN,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,")
            #print(tabla)
            print(id)
            return tabla
            
    
    


def tablas(id,json_data):
    
    # Primera hora del dia
    start = arrow.now().floor('day')
    print(start)
    # Ultima hora del dia
    end = start.shift(days=+2)
    print(end)
    
    data= []
    data2= []
    data3= []
    data4 = []
    dirs=[]
    dirv=[]
    dirs2=[]
    dirv2=[]
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
                dirv.append(wD)
                dirs.append(sD)
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
                dirs2.append(sD)
                dirv2.append(wD)
                tem2.append(wS)
        x=x+1


    if(id==0):
        tabla1=tabulate( data , headers=["hora","Temperatura" , "Velocidad viento"]  )
        return tabla1
    if(id==1):
        Graficas.grafica1(dirs,0,tem1)
        #dirs=[]
        g="WindDirection.png"
        return g
    if(id==2):
        tabla3=tabulate( data3 , headers=["hora","Temperatura" , "Velocidad viento"]  )
        return tabla3
    if(id==3):
        Graficas.grafica1(dirs2,1,tem1)
        #dirs2=[]
        g="WindDirection2.png"
        return g
    if(id==4):
        tabla2= tabulate( data2 , headers=["hora","Periodo oleaje" , "Altura de ola"]  ) 
        return tabla2
    if(id==5):
        Graficas.grafica2(dirv,0,tem2)
        #dirv=[]
        g="SwellDirection.png"
        return g
    if(id==6):
        tabla4=tabulate( data4 , headers=["hora","Periodo oleaje" , "Altura de ola"]  )
        return tabla4
    if(id==7):
        Graficas.grafica2(dirv2,1,tem2)
        #dirv2=[]
        g="SwellDirection2.png"
        return g
        
    print()


def Forecast1(BOT_TOKEN,chat_id,json_data):
    print("<<<<<<<<<<<<<<<<<<<<<<<")

    global TOKEN,DIC
    TOKEN=BOT_TOKEN
    chat=chat_id


    
    # Primera hora del dia
    start = arrow.now().floor('day')
    print(start)
    # Ultima hora del dia
    end = start.shift(days=+2)
    print(end)

    x=1
    data= []
    data2= []
    data3= []
    data4 = []
    dirs=[]
    dirv=[]
    dirs2=[]
    dirv2=[]
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
                dirv.append(wD)
                dirs.append(sD)
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
                dirs2.append(sD)
                dirv2.append(wD)
                tem2.append(wS)
        x=x+1
        
    
    bot= telegram.Bot(BOT_TOKEN)
    



    tabla1=tabulate( data , headers=["hora","Temperatura" , "Velocidad viento"]  ) 
    
    
    tabla2= tabulate( data2 , headers=["hora","Periodo oleaje" , "Altura de ola"]  ) 
    
    
    
    f=bot.sendMessage( chat, tabla1,           
                    reply_markup=InlineKeyboardMarkup([
                        [buttonI , buttonD]])
                    )
    print(f)
    msn=f['message_id']
    d=[msn,json_data,0,chat_id]
    DIC.append(d)
    print("-----MSN-----")
    print(msn)
    
    #print(DIRS)
    Graficas.grafica1(dirs,0,tem1)
    #dirs=[]
    Graficas.grafica2(dirv,0,tem2)
    #dirv=[]

    n=bot.sendPhoto(chat_id=chat,
        photo=open('WindDirection.png','rb') ,
        reply_markup=InlineKeyboardMarkup([
                        [buttonGV , buttonGS]])
                    
    )
    print("----message_id------")
    print(n['message_id'])
    
    
    d=[n['message_id'],json_data,1,chat_id]

    DIC.append(d)

    print("Al dia siguiente")
    bot.sendMessage(chat,text="Al dia siguiente")


    tabla3=tabulate( data3 , headers=["hora","Temperatura" , "Velocidad viento"]  ) 

    tabla4=tabulate( data4 , headers=["hora","Periodo oleaje" , "Altura de ola"]  )

    
    n=bot.sendMessage( chat, tabla3 ,           
                    reply_markup=InlineKeyboardMarkup([
                        [buttonI , buttonD]])
                    )
    d=[n['message_id'],json_data,2,chat_id]

    DIC.append(d)
    

    Graficas.grafica1(dirs2,1,tem1)
    #dirs2=[]
    Graficas.grafica2(dirv2,1,tem2)
    #dirv2=[]

 
    n=bot.sendPhoto(chat_id=chat,
        photo=open('WindDirection2.png','rb'),
        reply_markup=InlineKeyboardMarkup([
                        [buttonGV , buttonGS]])
    )
    
    d=[n['message_id'],json_data,3,chat_id]

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
    tabla=datos(id,chat)
    #global MSN,AUX
    #MSN1=id
    #chat=chat
    #print(chat)
    print("<<<<<<<<<<<<<<<<<<<<<<<")
    #print(threading.get_ident())
    bot2=telegram.Bot(TOKEN)
    bot2.editMessageText(text=tabla,
                    chat_id=chat,
                    message_id=id,
                    reply_markup=InlineKeyboardMarkup([
                    [buttonI , buttonD]]
                    
                )
    )


def cambioGI(id,chat):
    tabla=datos(id,chat)
    #global MSN,AUX
    #MSN1=id
    #chat=chat
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
                            message_id=id
        )
