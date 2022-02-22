from telegram import ChatAction,InlineKeyboardMarkup, InlineKeyboardButton, InlineQueryResultPhoto
import telegram
from telegram.ext import CallbackQueryHandler
import arrow
import requests
from tabulate import tabulate


from uuid import uuid4

TABLA1=[]
TABLA2=[]
TABLA3=[]
TABLA4=[]
GRADOS=[]

buttonI = InlineKeyboardButton(
        text= "<--",
        callback_data='BI'
)
buttonD = InlineKeyboardButton(
        text= "--->",
        callback_data='BD'
)

buttonG= InlineKeyboardButton(
        text= "Graficas",
        callback_data='BG'
)

buttonI2 = InlineKeyboardButton(
        text= "<--",
        callback_data='BI2'
)
buttonD2 = InlineKeyboardButton(
        text= "--->",
        callback_data='BD2'
)

buttonG2= InlineKeyboardButton(
        text= "Graficas2",
        callback_data='BG2'
)

def Forecast(update,lat,lon):

    la = lat
    lo = lon
    tz='UTC+1'
    global TABLA1,TABLA2,TABLA3,TABLA4,GRADOS
    

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
    json_data = {'hours': [{'airTemperature': {'dwd': 12.33, 'noaa': 10.32, 'sg': 12.33}, 'swellDirection': {'dwd': 306.31, 'icon': 301.41, 'meteo': 304.61, 'noaa': 307.6, 'sg': 304.61}, 'swellHeight': {'dwd': 2.21, 'icon': 2.37, 'meteo': 2.58, 'noaa': 
    2.01, 'sg': 2.58}, 'swellPeriod': {'dwd': 9.06, 'icon': 9.42, 'meteo': 8.09, 'noaa': 9.95, 'sg': 8.09}, 'time': '2022-02-15T23:00:00+00:00', 'waveDirection': {'icon': 294.65, 'meteo': 291.51, 'noaa': 313.94, 'sg': 291.51}, 'windSpeed': {'icon': 8.7, 'noaa': 2.76, 'sg': 8.7}}, {'airTemperature': {'dwd': 12.41, 'noaa': 10.78, 'sg': 12.41}, 'swellDirection': {'dwd': 305.85, 'icon': 300.77, 'meteo': 304.08, 'noaa': 306.86, 'sg': 304.08}, 'swellHeight': {'dwd': 2.24, 'icon': 2.37, 'meteo': 2.56, 'noaa': 2.06, 'sg': 2.56}, 'swellPeriod': {'dwd': 9.16, 'icon': 9.45, 'meteo': 8.12, 'noaa': 9.84, 'sg': 8.12}, 'time': '2022-02-16T00:00:00+00:00', 'waveDirection': {'icon': 293.72, 'meteo': 291.02, 'noaa': 312.75, 'sg': 291.02}, 'windSpeed': {'icon': 8.73, 'noaa': 2.9, 'sg': 8.73}}, {'airTemperature': {'dwd': 12.82, 'noaa': 11.14, 'sg': 12.82}, 'swellDirection': {'dwd': 305.69, 'icon': 300.78, 'meteo': 306.23, 'noaa': 306.76, 'sg': 306.23}, 'swellHeight': {'dwd': 2.26, 'icon': 2.38, 'meteo': 2.48, 'noaa': 2.13, 'sg': 2.48}, 'swellPeriod': {'dwd': 9.32, 'icon': 9.59, 'meteo': 8.33, 'noaa': 9.9, 'sg': 8.33}, 'time': '2022-02-16T01:00:00+00:00', 'waveDirection': {'icon': 293.16, 'meteo': 290.16, 'noaa': 312.45, 'sg': 290.16}, 'windSpeed': {'icon': 8.87, 'noaa': 3.02, 'sg': 8.87}}, {'airTemperature': {'dwd': 13.1, 'noaa': 11.49, 'sg': 13.1}, 'swellDirection': {'dwd': 305.61, 'icon': 300.79, 'meteo': 308.38, 'noaa': 306.65, 'sg': 308.38}, 'swellHeight': {'dwd': 2.28, 'icon': 2.4, 'meteo': 2.39, 'noaa': 2.21, 'sg': 2.39}, 'swellPeriod': {'dwd': 9.47, 'icon': 9.72, 'meteo': 8.55, 'noaa': 9.95, 'sg': 8.55}, 'time': '2022-02-16T02:00:00+00:00', 'waveDirection': {'icon': 292.61, 'meteo': 289.31, 'noaa': 312.15, 'sg': 289.31}, 'windSpeed': {'icon': 9.01, 'noaa': 3.14, 'sg': 9.01}}, {'airTemperature': {'dwd': 13.16, 'noaa': 11.84, 'sg': 13.16}, 'swellDirection': {'dwd': 305.5, 'icon': 300.8, 'meteo': 310.53, 'noaa': 306.55, 'sg': 310.53}, 'swellHeight': {'dwd': 2.31, 'icon': 2.41, 'meteo': 2.31, 'noaa': 2.28, 'sg': 2.31}, 'swellPeriod': {'dwd': 9.59, 'icon': 9.86, 'meteo': 8.76, 'noaa': 10.01, 'sg': 8.76}, 'time': '2022-02-16T03:00:00+00:00', 'waveDirection': {'icon': 292.05, 'meteo': 288.45, 'noaa': 311.85, 'sg': 288.45}, 'windSpeed': {'icon': 9.15, 'noaa': 3.26, 'sg': 9.15}}, {'airTemperature': {'dwd': 13.21, 'noaa': 11.9, 'sg': 13.21}, 'swellDirection': {'dwd': 305.54, 'icon': 301.25, 'meteo': 309.94, 'noaa': 306.42, 'sg': 309.94}, 'swellHeight': {'dwd': 2.35, 'icon': 2.44, 'meteo': 2.43, 'noaa': 2.36, 'sg': 2.43}, 'swellPeriod': {'dwd': 9.69, 'icon': 10.03, 'meteo': 8.81, 'noaa': 
    10.2, 'sg': 8.81}, 'time': '2022-02-16T04:00:00+00:00', 'waveDirection': {'icon': 292.16, 'meteo': 288.76, 'noaa': 311.12, 'sg': 288.76}, 'windSpeed': {'icon': 9.49, 'noaa': 3.34, 'sg': 9.49}}, {'airTemperature': {'dwd': 13.63, 'noaa': 11.96, 'sg': 13.63}, 'swellDirection': {'dwd': 305.69, 'icon': 301.7, 'meteo': 309.35, 'noaa': 306.29, 'sg': 309.35}, 'swellHeight': {'dwd': 2.37, 'icon': 2.47, 'meteo': 2.56, 'noaa': 2.43, 'sg': 2.56}, 'swellPeriod': {'dwd': 9.82, 'icon': 10.19, 'meteo': 8.86, 'noaa': 10.4, 'sg': 8.86}, 'time': '2022-02-16T05:00:00+00:00', 'waveDirection': {'icon': 292.28, 'meteo': 289.08, 'noaa': 310.39, 'sg': 289.08}, 'windSpeed': {'icon': 9.84, 'noaa': 3.43, 'sg': 9.84}}, {'airTemperature': {'dwd': 13.88, 'noaa': 12.03, 'sg': 13.88}, 'swellDirection': {'dwd': 305.91, 'icon': 302.15, 'meteo': 308.76, 'noaa': 306.16, 'sg': 308.76}, 'swellHeight': {'dwd': 2.39, 'icon': 2.5, 'meteo': 2.68, 'noaa': 2.51, 'sg': 2.68}, 'swellPeriod': {'dwd': 9.97, 'icon': 10.36, 'meteo': 8.91, 'noaa': 10.59, 'sg': 8.91}, 'time': '2022-02-16T06:00:00+00:00', 'waveDirection': {'icon': 292.39, 'meteo': 289.39, 'noaa': 309.66, 'sg': 289.39}, 'windSpeed': {'icon': 10.18, 'noaa': 3.51, 'sg': 10.18}}, {'airTemperature': {'dwd': 13.89, 'noaa': 12.62, 'sg': 13.89}, 'swellDirection': {'dwd': 305.86, 'icon': 302.3, 'meteo': 308.19, 'noaa': 306.45, 'sg': 308.19}, 'swellHeight': {'dwd': 2.43, 'icon': 2.55, 'meteo': 2.77, 'noaa': 2.56, 'sg': 2.77}, 'swellPeriod': {'dwd': 10.06, 'icon': 10.45, 'meteo': 8.98, 'noaa': 10.75, 'sg': 8.98}, 'time': '2022-02-16T07:00:00+00:00', 'waveDirection': {'icon': 292.81, 'meteo': 289.87, 'noaa': 310.34, 'sg': 289.87}, 'windSpeed': {'icon': 10.09, 'noaa': 3.65, 'sg': 10.09}}, {'airTemperature': {'dwd': 13.99, 'noaa': 13.21, 'sg': 13.99}, 'swellDirection': {'dwd': 305.89, 'icon': 302.45, 'meteo': 307.62, 'noaa': 306.74, 'sg': 307.62}, 'swellHeight': {'dwd': 2.47, 'icon': 2.59, 'meteo': 2.87, 'noaa': 2.61, 'sg': 2.87}, 'swellPeriod': {'dwd': 10.16, 'icon': 10.55, 'meteo': 9.04, 'noaa': 10.92, 'sg': 9.04}, 'time': '2022-02-16T08:00:00+00:00', 'waveDirection': {'icon': 293.23, 'meteo': 
    290.36, 'noaa': 311.02, 'sg': 290.36}, 'windSpeed': {'icon': 10.0, 'noaa': 3.8, 'sg': 10.0}}, {'airTemperature': {'dwd': 14.35, 'noaa': 13.79, 'sg': 14.35}, 'swellDirection': {'dwd': 306.02, 'icon': 302.6, 'meteo': 307.05, 'noaa': 307.03, 'sg': 307.05}, 'swellHeight': {'dwd': 2.51, 'icon': 2.64, 'meteo': 2.96, 'noaa': 2.66, 'sg': 2.96}, 'swellPeriod': {'dwd': 10.26, 'icon': 10.64, 'meteo': 9.11, 'noaa': 11.08, 'sg': 9.11}, 'time': '2022-02-16T09:00:00+00:00', 'waveDirection': {'icon': 293.65, 'meteo': 290.84, 'noaa': 311.7, 'sg': 290.84}, 'windSpeed': {'icon': 9.92, 'noaa': 3.94, 'sg': 9.92}}, {'airTemperature': {'dwd': 14.77, 'noaa': 14.66, 'sg': 14.77}, 'swellDirection': {'dwd': 306.33, 'icon': 302.44, 'meteo': 306.27, 'noaa': 313.65, 'sg': 306.27}, 'swellHeight': {'dwd': 2.56, 'icon': 2.68, 'meteo': 2.92, 'noaa': 2.25, 'sg': 2.92}, 'swellPeriod': {'dwd': 10.39, 'icon': 10.7, 'meteo': 9.1, 'noaa': 11.8, 'sg': 9.1}, 'time': '2022-02-16T10:00:00+00:00', 'waveDirection': {'icon': 294.44, 'meteo': 291.7, 'noaa': 312.81, 'sg': 291.7}, 'windSpeed': {'icon': 9.58, 'noaa': 3.87, 'sg': 9.58}}, {'airTemperature': {'dwd': 14.96, 'noaa': 15.52, 'sg': 14.96}, 'swellDirection': 
    {'dwd': 306.66, 'icon': 302.29, 'meteo': 305.49, 'noaa': 320.28, 'sg': 305.49}, 'swellHeight': {'dwd': 2.6, 'icon': 2.73, 'meteo': 2.89, 'noaa': 1.84, 'sg': 2.89}, 'swellPeriod': {'dwd': 10.51, 'icon': 10.75, 'meteo': 9.1, 'noaa': 12.51, 'sg': 9.1}, 'time': '2022-02-16T11:00:00+00:00', 'waveDirection': {'icon': 295.24, 'meteo': 292.55, 'noaa': 313.93, 'sg': 292.55}, 'windSpeed': {'icon': 9.24, 'noaa': 3.79, 'sg': 9.24}}, {'airTemperature': {'dwd': 15.64, 'noaa': 16.38, 
    'sg': 15.64}, 'swellDirection': {'dwd': 307.08, 'icon': 302.13, 'meteo': 304.71, 'noaa': 326.9, 'sg': 304.71}, 'swellHeight': {'dwd': 2.63, 'icon': 2.77, 'meteo': 2.85, 'noaa': 1.43, 'sg': 2.85}, 'swellPeriod': {'dwd': 10.64, 'icon': 10.81, 'meteo': 9.09, 'noaa': 13.23, 'sg': 9.09}, 'time': '2022-02-16T12:00:00+00:00', 'waveDirection': {'icon': 296.03, 'meteo': 293.41, 'noaa': 315.04, 'sg': 293.41}, 'windSpeed': {'icon': 8.9, 'noaa': 3.72, 'sg': 8.9}}, {'airTemperature': {'dwd': 16.33, 'noaa': 16.5, 'sg': 16.33}, 'swellDirection': {'dwd': 307.3, 'icon': 302.12, 'meteo': 308.06, 'noaa': 321.86, 'sg': 308.06}, 'swellHeight': {'dwd': 2.65, 'icon': 2.77, 'meteo': 2.77, 'noaa': 1.8, 'sg': 2.77}, 'swellPeriod': {'dwd': 10.73, 'icon': 10.93, 'meteo': 9.51, 'noaa': 13.25, 'sg': 9.51}, 'time': '2022-02-16T13:00:00+00:00', 'waveDirection': {'icon': 296.85, 'meteo': 293.7, 'noaa': 317.35, 'sg': 293.7}, 'windSpeed': {'icon': 9.03, 'noaa': 3.67, 'sg': 9.03}}, {'airTemperature': {'dwd': 15.65, 'noaa': 16.62, 'sg': 15.65}, 'swellDirection': {'dwd': 307.68, 'icon': 302.11, 'meteo': 311.4, 'noaa': 316.81, 'sg': 311.4}, 'swellHeight': {'dwd': 2.65, 'icon': 2.77, 'meteo': 2.7, 'noaa': 
    2.18, 'sg': 2.7}, 'swellPeriod': {'dwd': 10.86, 'icon': 11.04, 'meteo': 9.92, 'noaa': 13.27, 'sg': 9.92}, 'time': '2022-02-16T14:00:00+00:00', 'waveDirection': {'icon': 297.67, 'meteo': 294.0, 'noaa': 319.66, 'sg': 294.0}, 'windSpeed': {'icon': 9.15, 'noaa': 3.62, 'sg': 9.15}}, {'airTemperature': {'dwd': 14.75, 'noaa': 16.74, 'sg': 14.75}, 'swellDirection': {'dwd': 308.02, 'icon': 302.1, 'meteo': 314.75, 'noaa': 311.77, 'sg': 314.75}, 'swellHeight': {'dwd': 2.65, 'icon': 2.77, 'meteo': 2.62, 'noaa': 2.55, 'sg': 2.62}, 'swellPeriod': {'dwd': 10.94, 'icon': 11.16, 'meteo': 10.34, 'noaa': 13.29, 'sg': 10.34}, 'time': '2022-02-16T15:00:00+00:00', 'waveDirection': {'icon': 298.49, 'meteo': 294.29, 'noaa': 321.97, 'sg': 294.29}, 'windSpeed': {'icon': 9.28, 'noaa': 3.57, 'sg': 9.28}}, {'airTemperature': {'dwd': 14.46, 'noaa': 15.45, 'sg': 14.46}, 'swellDirection': {'dwd': 308.3, 'icon': 303.66, 'meteo': 316.75, 'noaa': 311.81, 'sg': 316.75}, 'swellHeight': {'dwd': 2.68, 'icon': 2.71, 'meteo': 2.47, 'noaa': 2.6, 'sg': 2.47}, 'swellPeriod': {'dwd': 10.9, 'icon': 11.43, 'meteo': 10.61, 'noaa': 13.13, 'sg': 10.61}, 'time': '2022-02-16T16:00:00+00:00', 'waveDirection': {'icon': 
    298.63, 'meteo': 294.26, 'noaa': 320.87, 'sg': 294.26}, 'windSpeed': {'icon': 9.89, 'noaa': 2.95, 'sg': 9.89}}, {'airTemperature': {'dwd': 14.08, 'noaa': 14.16, 'sg': 14.08}, 'swellDirection': {'dwd': 308.71, 'icon': 305.21, 'meteo': 318.76, 'noaa': 311.85, 'sg': 318.76}, 'swellHeight': {'dwd': 2.71, 'icon': 2.64, 'meteo': 2.31, 'noaa': 2.66, 'sg': 2.31}, 'swellPeriod': {'dwd': 10.87, 'icon': 11.69, 'meteo': 10.88, 'noaa': 12.96, 'sg': 10.88}, 'time': '2022-02-16T17:00:00+00:00', 'waveDirection': {'icon': 298.76, 'meteo': 294.22, 'noaa': 319.77, 'sg': 294.22}, 'windSpeed': {'icon': 10.5, 'noaa': 2.32, 'sg': 10.5}}, {'airTemperature': {'dwd': 13.52, 'noaa': 12.86, 'sg': 13.52}, 'swellDirection': {'dwd': 308.92, 'icon': 306.77, 'meteo': 320.76, 'noaa': 311.89, 'sg': 320.76}, 'swellHeight': {'dwd': 2.77, 'icon': 2.58, 'meteo': 2.16, 'noaa': 2.71, 'sg': 2.16}, 'swellPeriod': {'dwd': 10.72, 'icon': 11.96, 'meteo': 11.15, 'noaa': 12.8, 'sg': 11.15}, 'time': '2022-02-16T18:00:00+00:00', 'waveDirection': {'icon': 298.9, 'meteo': 294.19, 'noaa': 318.67, 'sg': 294.19}, 'windSpeed': {'icon': 11.11, 'noaa': 1.7, 'sg': 11.11}}, {'airTemperature': {'dwd': 13.46, 'noaa': 11.79, 'sg': 13.46}, 'swellDirection': {'dwd': 309.01, 'icon': 305.83, 'meteo': 318.75, 'noaa': 310.8, 'sg': 318.75}, 'swellHeight': {'dwd': 2.82, 'icon': 2.7, 'meteo': 2.41, 'noaa': 2.78, 'sg': 2.41}, 'swellPeriod': {'dwd': 10.62, 'icon': 11.69, 
    'meteo': 10.94, 'noaa': 12.77, 'sg': 10.94}, 'time': '2022-02-16T19:00:00+00:00', 'waveDirection': {'icon': 299.37, 'meteo': 294.74, 'noaa': 318.25, 'sg': 294.74}, 'windSpeed': {'icon': 10.36, 'noaa': 1.83, 'sg': 10.36}}, {'airTemperature': {'dwd': 13.43, 'noaa': 10.72, 'sg': 13.43}, 'swellDirection': {'dwd': 309.14, 'icon': 304.9, 'meteo': 316.74, 'noaa': 309.72, 'sg': 316.74}, 'swellHeight': {'dwd': 2.84, 'icon': 2.83, 'meteo': 2.65, 'noaa': 2.84, 'sg': 2.65}, 'swellPeriod': {'dwd': 10.66, 'icon': 11.43, 'meteo': 10.74, 'noaa': 12.74, 'sg': 10.74}, 'time': '2022-02-16T20:00:00+00:00', 'waveDirection': {'icon': 299.83, 'meteo': 295.29, 'noaa': 317.83, 'sg': 295.29}, 'windSpeed': {'icon': 9.62, 'noaa': 1.95, 'sg': 9.62}}, {'airTemperature': {'dwd': 13.21, 'noaa': 9.65, 'sg': 13.21}, 'swellDirection': {'dwd': 309.27, 'icon': 303.96, 'meteo': 314.73, 'noaa': 308.63, 'sg': 314.73}, 'swellHeight': {'dwd': 2.82, 'icon': 2.95, 'meteo': 2.9, 'noaa': 2.91, 'sg': 2.9}, 'swellPeriod': {'dwd': 10.8, 'icon': 11.16, 'meteo': 10.53, 'noaa': 12.71, 'sg': 10.53}, 'time': '2022-02-16T21:00:00+00:00', 'waveDirection': {'icon': 300.3, 'meteo': 295.84, 'noaa': 317.41, 'sg': 295.84}, 'windSpeed': {'icon': 8.88, 'noaa': 2.08, 'sg': 8.88}}, {'airTemperature': {'dwd': 13.39, 'noaa': 9.47, 'sg': 13.39}, 'swellDirection': {'dwd': 309.43, 'icon': 304.07, 'meteo': 313.43, 'noaa': 309.4, 'sg': 313.43}, 'swellHeight': {'dwd': 2.79, 'icon': 2.97, 'meteo': 3.05, 'noaa': 2.94, 'sg': 3.05}, 'swellPeriod': {'dwd': 10.97, 'icon': 11.2, 'meteo': 10.4, 'noaa': 12.79, 'sg': 10.4}, 'time': '2022-02-16T22:00:00+00:00', 'waveDirection': {'icon': 300.73, 'meteo': 296.66, 'noaa': 317.32, 'sg': 296.66}, 'windSpeed': {'icon': 8.53, 'noaa': 1.96, 'sg': 8.53}}, {'airTemperature': {'dwd': 13.19, 'noaa': 9.3, 'sg': 13.19}, 'swellDirection': {'dwd': 309.63, 'icon': 304.19, 'meteo': 312.13, 'noaa': 310.16, 'sg': 312.13}, 'swellHeight': {'dwd': 2.77, 'icon': 2.99, 'meteo': 3.21, 'noaa': 2.98, 'sg': 3.21}, 'swellPeriod': {'dwd': 11.1, 'icon': 11.23, 'meteo': 10.26, 'noaa': 12.87, 'sg': 10.26}, 'time': '2022-02-16T23:00:00+00:00', 'waveDirection': {'icon': 301.15, 'meteo': 297.49, 'noaa': 317.24, 'sg': 297.49}, 'windSpeed': {'icon': 8.19, 'noaa': 1.85, 'sg': 8.19}}, {'airTemperature': {'dwd': 13.12, 'noaa': 9.13, 'sg': 13.12}, 'swellDirection': {'dwd': 309.86, 'icon': 304.3, 'meteo': 310.83, 'noaa': 310.93, 'sg': 310.83}, 'swellHeight': {'dwd': 2.78, 'icon': 3.01, 'meteo': 3.36, 'noaa': 3.01, 'sg': 3.36}, 'swellPeriod': {'dwd': 11.2, 'icon': 11.27, 'meteo': 10.13, 'noaa': 12.95, 'sg': 10.13}, 'time': '2022-02-17T00:00:00+00:00', 'waveDirection': {'icon': 301.58, 'meteo': 298.31, 'noaa': 317.15, 'sg': 298.31}, 'windSpeed': {'icon': 7.84, 'noaa': 1.73, 'sg': 7.84}}, {'airTemperature': {'dwd': 13.17, 'noaa': 8.9, 'sg': 13.17}, 'swellDirection': {'dwd': 310.15, 'icon': 304.52, 'meteo': 309.87, 'noaa': 311.74, 'sg': 309.87}, 'swellHeight': {'dwd': 2.79, 'icon': 3.02, 'meteo': 3.46, 'noaa': 3.04, 'sg': 3.46}, 'swellPeriod': {'dwd': 11.33, 'icon': 11.38, 'meteo': 10.07, 'noaa': 13.28, 'sg': 10.07}, 'time': '2022-02-17T01:00:00+00:00', 'waveDirection': {'icon': 301.88, 'meteo': 299.61, 'noaa': 318.26, 'sg': 299.61}, 'windSpeed': {'icon': 7.78, 'noaa': 1.81, 'sg': 7.78}}, {'airTemperature': {'dwd': 13.17, 'noaa': 8.67, 'sg': 13.17}, 'swellDirection': {'dwd': 310.38, 'icon': 304.75, 'meteo': 308.9, 'noaa': 312.55, 'sg': 308.9}, 'swellHeight': {'dwd': 2.79, 'icon': 3.04, 'meteo': 3.57, 'noaa': 3.07, 'sg': 3.57}, 'swellPeriod': {'dwd': 11.49, 'icon': 11.49, 'meteo': 10.02, 'noaa': 13.61, 'sg': 10.02}, 'time': '2022-02-17T02:00:00+00:00', 'waveDirection': {'icon': 302.18, 'meteo': 300.91, 'noaa': 319.37, 'sg': 300.91}, 'windSpeed': {'icon': 7.73, 'noaa': 1.88, 'sg': 7.73}}, {'airTemperature': {'dwd': 12.53, 'noaa': 8.43, 'sg': 12.53}, 'swellDirection': {'dwd': 310.6, 'icon': 304.97, 'meteo': 307.94, 'noaa': 313.36, 'sg': 307.94}, 'swellHeight': {'dwd': 2.79, 'icon': 3.05, 'meteo': 3.67, 'noaa': 3.1, 'sg': 3.67}, 'swellPeriod': {'dwd': 11.65, 'icon': 11.6, 'meteo': 9.96, 'noaa': 13.94, 'sg': 9.96}, 'time': '2022-02-17T03:00:00+00:00', 'waveDirection': {'icon': 302.48, 'meteo': 302.21, 'noaa': 320.48, 'sg': 302.21}, 'windSpeed': {'icon': 7.67, 'noaa': 1.96, 'sg': 7.67}}, {'airTemperature': {'dwd': 11.85, 'noaa': 8.15, 'sg': 11.85}, 'swellDirection': {'dwd': 310.83, 'icon': 304.87, 'meteo': 307.85, 'noaa': 313.9, 'sg': 307.85}, 'swellHeight': {'dwd': 2.8, 'icon': 3.09, 'meteo': 3.72, 'noaa': 3.11, 'sg': 3.72}, 'swellPeriod': {'dwd': 11.79, 'icon': 11.64, 'meteo': 10.0, 'noaa': 13.98, 'sg': 10.0}, 'time': '2022-02-17T04:00:00+00:00', 'waveDirection': {'icon': 303.0, 'meteo': 303.17, 'noaa': 320.23, 'sg': 303.17}, 'windSpeed': {'icon': 7.08, 'noaa': 1.96, 'sg': 7.08}}, {'airTemperature': {'dwd': 11.34, 'noaa': 7.86, 'sg': 11.34}, 'swellDirection': {'dwd': 311.03, 'icon': 304.77, 'meteo': 307.76, 'noaa': 314.43, 'sg': 307.76}, 'swellHeight': {'dwd': 2.8, 'icon': 3.13, 'meteo': 3.76, 'noaa': 3.12, 'sg': 3.76}, 'swellPeriod': {'dwd': 11.91, 'icon': 11.69, 'meteo': 10.03, 'noaa': 14.01, 'sg': 10.03}, 'time': '2022-02-17T05:00:00+00:00', 'waveDirection': {'icon': 303.53, 'meteo': 304.13, 'noaa': 319.99, 'sg': 304.13}, 'windSpeed': {'icon': 6.48, 'noaa': 1.97, 'sg': 6.48}}, {'airTemperature': {'dwd': 10.2, 'noaa': 7.57, 'sg': 10.2}, 'swellDirection': {'dwd': 311.21, 'icon': 304.67, 'meteo': 307.67, 'noaa': 314.97, 'sg': 307.67}, 'swellHeight': {'dwd': 2.81, 'icon': 3.17, 'meteo': 3.81, 'noaa': 3.13, 'sg': 3.81}, 'swellPeriod': {'dwd': 12.03, 'icon': 11.73, 'meteo': 10.07, 'noaa': 14.05, 'sg': 10.07}, 'time': '2022-02-17T06:00:00+00:00', 'waveDirection': {'icon': 304.05, 'meteo': 305.09, 'noaa': 319.74, 'sg': 305.09}, 'windSpeed': {'icon': 5.89, 'noaa': 1.97, 'sg': 5.89}}, {'airTemperature': {'dwd': 9.38, 'noaa': 8.62, 'sg': 9.38}, 'swellDirection': {'dwd': 311.38, 'icon': 304.86, 'meteo': 307.66, 'noaa': 315.13, 'sg': 307.66}, 'swellHeight': {'dwd': 2.82, 'icon': 3.2, 'meteo': 3.84, 'noaa': 3.13, 'sg': 3.84}, 'swellPeriod': {'dwd': 12.14, 'icon': 11.86, 'meteo': 10.11, 'noaa': 14.14, 'sg': 10.11}, 'time': '2022-02-17T07:00:00+00:00', 'waveDirection': {'icon': 304.44, 'meteo': 305.52, 'noaa': 319.68, 'sg': 305.52}, 'windSpeed': {'icon': 4.46, 'noaa': 1.71, 'sg': 4.46}}, {'airTemperature': {'dwd': 9.79, 'noaa': 9.67, 'sg': 9.79}, 'swellDirection': {'dwd': 311.55, 'icon': 305.04, 'meteo': 307.66, 'noaa': 315.29, 'sg': 307.66}, 'swellHeight': {'dwd': 2.83, 'icon': 3.23, 'meteo': 3.87, 'noaa': 3.12, 'sg': 3.87}, 'swellPeriod': {'dwd': 12.24, 'icon': 12.0, 'meteo': 10.16, 'noaa': 14.23, 'sg': 10.16}, 'time': '2022-02-17T08:00:00+00:00', 'waveDirection': {'icon': 304.84, 'meteo': 305.95, 'noaa': 319.63, 'sg': 305.95}, 'windSpeed': {'icon': 3.02, 'noaa': 1.46, 'sg': 3.02}}, {'airTemperature': {'dwd': 10.97, 'noaa': 10.72, 'sg': 
    10.97}, 'swellDirection': {'dwd': 311.67, 'icon': 305.23, 'meteo': 307.65, 'noaa': 315.45, 'sg': 307.65}, 'swellHeight': {'dwd': 2.86, 'icon': 3.26, 'meteo': 3.9, 'noaa': 3.12, 'sg': 3.9}, 'swellPeriod': {'dwd': 12.34, 'icon': 12.13, 'meteo': 10.2, 'noaa': 14.32, 'sg': 10.2}, 'time': '2022-02-17T09:00:00+00:00', 'waveDirection': {'icon': 305.23, 'meteo': 306.38, 'noaa': 319.57, 'sg': 306.38}, 'windSpeed': {'icon': 1.59, 'noaa': 1.2, 'sg': 1.59}}, {'airTemperature': {'dwd': 13.15, 'noaa': 12.69, 'sg': 13.15}, 'swellDirection': {'dwd': 311.79, 'icon': 305.5, 'meteo': 307.45, 'noaa': 315.33, 'sg': 307.45}, 'swellHeight': {'dwd': 2.91, 'icon': 3.31, 'meteo': 3.9, 'noaa': 3.12, 'sg': 3.9}, 'swellPeriod': {'dwd': 12.44, 'icon': 12.31, 'meteo': 10.25, 'noaa': 14.37, 'sg': 10.25}, 'time': '2022-02-17T10:00:00+00:00', 'waveDirection': {'icon': 305.5, 'meteo': 306.44, 'noaa': 319.11, 'sg': 306.44}, 'windSpeed': {'icon': 1.85, 'noaa': 1.29, 'sg': 1.85}}, {'airTemperature': {'dwd': 14.42, 'noaa': 14.65, 'sg': 14.42}, 'swellDirection': {'dwd': 311.92, 'icon': 305.76, 'meteo': 307.25, 'noaa': 315.2, 'sg': 307.25}, 'swellHeight': {'dwd': 2.95, 'icon': 3.37, 'meteo': 3.91, 'noaa': 3.11, 'sg': 3.91}, 'swellPeriod': {'dwd': 12.57, 'icon': 12.5, 'meteo': 10.29, 'noaa': 14.41, 'sg': 10.29}, 'time': '2022-02-17T11:00:00+00:00', 'waveDirection': {'icon': 305.76, 'meteo': 306.49, 'noaa': 318.65, 'sg': 306.49}, 'windSpeed': {'icon': 2.1, 'noaa': 1.38, 'sg': 2.1}}, {'airTemperature': {'dwd': 15.08, 'noaa': 16.62, 'sg': 15.08}, 'swellDirection': {'dwd': 312.1, 'icon': 306.03, 'meteo': 307.05, 'noaa': 315.08, 'sg': 307.05}, 'swellHeight': {'dwd': 2.96, 'icon': 3.42, 'meteo': 3.91, 'noaa': 3.11, 'sg': 3.91}, 'swellPeriod': {'dwd': 12.71, 'icon': 12.68, 'meteo': 10.34, 'noaa': 14.46, 'sg': 10.34}, 'time': '2022-02-17T12:00:00+00:00', 'waveDirection': {'icon': 306.03, 'meteo': 306.55, 'noaa': 
    318.19, 'sg': 306.55}, 'windSpeed': {'icon': 2.36, 'noaa': 1.47, 'sg': 2.36}}, {'airTemperature': {'dwd': 14.74, 'noaa': 16.7, 'sg': 14.74}, 'swellDirection': {'dwd': 312.31, 'icon': 306.16, 'meteo': 306.77, 'noaa': 314.96, 'sg': 306.77}, 'swellHeight': {'dwd': 3.01, 'icon': 3.49, 'meteo': 3.93, 'noaa': 3.11, 'sg': 3.93}, 'swellPeriod': {'dwd': 12.88, 'icon': 12.86, 'meteo': 10.43, 'noaa': 14.45, 'sg': 10.43}, 'time': '2022-02-17T13:00:00+00:00', 'waveDirection': {'icon': 306.16, 'meteo': 306.43, 'noaa': 317.85, 'sg': 306.43}, 'windSpeed': {'icon': 2.1, 'noaa': 1.69, 'sg': 2.1}}, {'airTemperature': {'dwd': 14.96, 'noaa': 16.78, 'sg': 14.96}, 'swellDirection': {'dwd': 312.53, 'icon': 306.28, 'meteo': 306.48, 'noaa': 314.85, 'sg': 306.48}, 'swellHeight': {'dwd': 3.07, 'icon': 3.57, 'meteo': 3.94, 'noaa': 3.1, 'sg': 3.94}, 'swellPeriod': {'dwd': 13.05, 'icon': 13.04, 'meteo': 10.53, 'noaa': 14.44, 'sg': 10.53}, 'time': '2022-02-17T14:00:00+00:00', 'waveDirection': {'icon': 306.28, 'meteo': 306.31, 'noaa': 317.5, 'sg': 306.31}, 'windSpeed': {'icon': 1.83, 'noaa': 1.92, 'sg': 1.83}}, {'airTemperature': {'dwd': 15.1, 'noaa': 16.86, 'sg': 15.1}, 'swellDirection': {'dwd': 312.76, 'icon': 306.41, 'meteo': 306.2, 'noaa': 314.73, 'sg': 306.2}, 'swellHeight': {'dwd': 3.19, 'icon': 3.64, 'meteo': 3.96, 'noaa': 3.1, 'sg': 3.96}, 'swellPeriod': {'dwd': 13.23, 'icon': 13.22, 'meteo': 10.62, 'noaa': 14.43, 'sg': 10.62}, 'time': '2022-02-17T15:00:00+00:00', 'waveDirection': {'icon': 306.41, 'meteo': 306.19, 'noaa': 317.16, 'sg': 306.19}, 'windSpeed': {'icon': 1.57, 'noaa': 2.14, 'sg': 1.57}}, {'airTemperature': {'dwd': 14.87, 'noaa': 14.82, 'sg': 14.87}, 'swellDirection': {'dwd': 312.96, 'icon': 306.3, 'meteo': 306.0, 'noaa': 314.74, 'sg': 306.0}, 'swellHeight': {'dwd': 3.24, 'icon': 3.7, 'meteo': 4.03, 'noaa': 3.1, 'sg': 4.03}, 'swellPeriod': {'dwd': 13.38, 'icon': 13.33, 'meteo': 10.77, 'noaa': 14.42, 'sg': 10.77}, 'time': '2022-02-17T16:00:00+00:00', 'waveDirection': {'icon': 306.3, 'meteo': 305.99, 'noaa': 316.83, 'sg': 305.99}, 'windSpeed': {'icon': 1.2, 'noaa': 1.61, 'sg': 1.2}}, {'airTemperature': {'dwd': 14.03, 'noaa': 12.78, 'sg': 14.03}, 'swellDirection': {'dwd': 313.1, 'icon': 306.2, 'meteo': 305.79, 'noaa': 314.76, 'sg': 305.79}, 'swellHeight': {'dwd': 3.28, 'icon': 3.75, 'meteo': 4.09, 'noaa': 3.11, 'sg': 4.09}, 'swellPeriod': {'dwd': 13.51, 'icon': 13.43, 'meteo': 10.92, 'noaa': 14.41, 'sg': 10.92}, 'time': '2022-02-17T17:00:00+00:00', 'waveDirection': {'icon': 306.2, 'meteo': 305.79, 'noaa': 316.49, 'sg': 305.79}, 'windSpeed': {'icon': 0.84, 'noaa': 1.09, 'sg': 0.84}}, {'airTemperature': {'dwd': 12.8, 'noaa': 10.73, 'sg': 12.8}, 'swellDirection': {'dwd': 313.12, 'icon': 306.09, 'meteo': 305.59, 'noaa': 314.77, 'sg': 305.59}, 'swellHeight': {'dwd': 3.32, 'icon': 3.81, 'meteo': 4.16, 'noaa': 3.11, 
    'sg': 4.16}, 'swellPeriod': {'dwd': 13.61, 'icon': 13.54, 'meteo': 11.07, 'noaa': 14.4, 'sg': 11.07}, 'time': '2022-02-17T18:00:00+00:00', 'waveDirection': {'icon': 306.09, 'meteo': 305.59, 'noaa': 316.16, 'sg': 305.59}, 'windSpeed': {'icon': 0.47, 'noaa': 0.56, 'sg': 0.47}}, {'airTemperature': {'dwd': 11.94, 'noaa': 10.31, 'sg': 11.94}, 'swellDirection': {'dwd': 313.06, 'icon': 305.77, 'meteo': 305.11, 'noaa': 314.65, 'sg': 305.11}, 'swellHeight': {'dwd': 3.36, 'icon': 3.82, 'meteo': 4.2, 'noaa': 3.1, 'sg': 4.2}, 'swellPeriod': {'dwd': 13.67, 'icon': 13.55, 'meteo': 11.12, 'noaa': 14.39, 'sg': 11.12}, 'time': '2022-02-17T19:00:00+00:00', 'waveDirection': {'icon': 305.77, 'meteo': 305.11, 'noaa': 315.83, 'sg': 305.11}, 'windSpeed': {'icon': 0.54, 'noaa': 0.88, 'sg': 0.54}}, {'airTemperature': {'dwd': 11.51, 'noaa': 9.89, 'sg': 11.51}, 'swellDirection': {'dwd': 312.92, 'icon': 305.44, 'meteo': 304.63, 'noaa': 314.53, 'sg': 304.63}, 'swellHeight': {'dwd': 3.39, 'icon': 3.83, 'meteo': 4.24, 'noaa': 3.1, 'sg': 4.24}, 'swellPeriod': {'dwd': 13.7, 'icon': 13.57, 'meteo': 11.16, 'noaa': 14.37, 'sg': 11.16}, 'time': '2022-02-17T20:00:00+00:00', 'waveDirection': {'icon': 305.44, 'meteo': 304.63, 'noaa': 315.51, 'sg': 304.63}, 'windSpeed': {'icon': 0.61, 'noaa': 1.2, 'sg': 0.61}}, {'airTemperature': {'dwd': 11.4, 'noaa': 9.47, 'sg': 11.4}, 'swellDirection': {'dwd': 312.71, 'icon': 305.12, 'meteo': 304.15, 'noaa': 314.41, 'sg': 304.15}, 'swellHeight': {'dwd': 3.39, 'icon': 3.84, 'meteo': 4.28, 'noaa': 3.09, 'sg': 4.28}, 'swellPeriod': {'dwd': 13.69, 'icon': 13.58, 'meteo': 11.21, 'noaa': 14.36, 'sg': 11.21}, 'time': '2022-02-17T21:00:00+00:00', 'waveDirection': {'icon': 305.12, 'meteo': 304.15, 'noaa': 315.18, 'sg': 304.15}, 'windSpeed': {'icon': 0.68, 'noaa': 1.52, 'sg': 0.68}}, {'airTemperature': {'dwd': 11.29, 'noaa': 9.27, 'sg': 11.29}, 'swellDirection': {'dwd': 312.41, 
    'icon': 304.73, 'meteo': 303.51, 'noaa': 313.98, 'sg': 303.51}, 'swellHeight': {'dwd': 3.41, 'icon': 3.82, 'meteo': 4.25, 'noaa': 3.05, 'sg': 4.25}, 'swellPeriod': {'dwd': 13.65, 'icon': 13.54, 'meteo': 11.18, 'noaa': 14.31, 'sg': 11.18}, 'time': '2022-02-17T22:00:00+00:00', 'waveDirection': {'icon': 304.73, 'meteo': 303.51, 'noaa': 314.55, 'sg': 303.51}, 'windSpeed': {'icon': 0.76, 'noaa': 1.5, 'sg': 0.76}}, {'airTemperature': {'dwd': 11.23, 'noaa': 9.06, 'sg': 11.23}, 'swellDirection': {'dwd': 312.1, 'icon': 304.33, 'meteo': 302.88, 'noaa': 313.55, 'sg': 302.88}, 'swellHeight': {'dwd': 3.36, 'icon': 3.79, 'meteo': 4.21, 'noaa': 3.01, 'sg': 4.21}, 'swellPeriod': {'dwd': 13.57, 'icon': 13.49, 'meteo': 
    11.14, 'noaa': 14.26, 'sg': 11.14}, 'time': '2022-02-17T23:00:00+00:00', 'waveDirection': {'icon': 304.33, 'meteo': 302.86, 'noaa': 313.92, 'sg': 302.86}, 'windSpeed': {'icon': 0.85, 'noaa': 1.49, 'sg': 0.85}}], 'meta': {'cost': 1, 'dailyQuota': 10, 'end': '2022-02-17 23:00', 'lat': 43.5777, 'lng': -5.9619, 'params': ['airTemperature', 'windSpeed', 'waveDirection', 'swellPeriod', 'swellHeight', 'swellDirection'], 'requestCount': 1, 'start': '2022-02-15 23:00'}}
    

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
                GRADOS.append(sD)
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
        x=x+1
        
    
 
    
    TABLA1=tabulate( data , headers=["hora","Temperatura" , "Velocidad viento"]  ) 
    update.message.reply_text( 
        text= tabulate( data , headers=["hora","Temperatura" , "Velocidad viento"]  ) ,
        reply_markup= InlineKeyboardMarkup([
                        [buttonI , buttonD , buttonG]
                    ])
    )
    #ID=update.message.message_id
    TABLA2= tabulate( data2 , headers=["hora","Periodo oleaje" , "Altura de ola"]  ) 

   
    from PIL import Image
    img = Image.open("Ejemplo.png")
    img.show()
    
    import numpy
    update.message.reply_photo(photo=numpy.array(img))

    print("Al dia siguiente")
    update.message.reply_text("Al dia siguiente")

    TABLA3=tabulate( data3 , headers=["hora","Temperatura" , "Velocidad viento"]  ) 
    update.message.reply_text( 
        text= tabulate( data3 , headers=["hora","Temperatura" , "Velocidad viento"]  )  ,
        reply_markup= InlineKeyboardMarkup([
                        [buttonI2 , buttonD2 , buttonG2]
                    ])
    )

    TABLA4=tabulate( data4 , headers=["hora","Periodo oleaje" , "Altura de ola"]  )



    print(GRADOS)






def cambioI(update):
    update.callback_query.edit_message_text(text=TABLA1,
                                    reply_markup= InlineKeyboardMarkup([
                        [buttonI , buttonD , buttonG]
                    ])
    )


def cambioD(update):
    update.callback_query.edit_message_text(text=TABLA2,
                                    reply_markup= InlineKeyboardMarkup([
                        [buttonI , buttonD , buttonG]
                    ])
    )


def cambioG(update):

    update.callback_query.edit_message_text(text=TABLA4,
                                    reply_markup= InlineKeyboardMarkup([
                                    [buttonI2 , buttonD2 , buttonG2]
                                    ])
    )


def cambioI2(update):
    
    update.callback_query.edit_message_text(text=TABLA3,
                                    reply_markup= InlineKeyboardMarkup([
                                    [buttonI2 , buttonD2 , buttonG2]
                                    ])
    )


def cambioD2(update):
    update.callback_query.edit_message_text(text=TABLA4,
                                    reply_markup= InlineKeyboardMarkup([
                                    [buttonI2 , buttonD2 , buttonG2]
                                    ])
    )

    