from telegram import ChatAction,InlineKeyboardMarkup, InlineKeyboardButton, InlineQueryResultPhoto, InputMedia, InputMediaPhoto
import telegram
from telegram.ext import CallbackQueryHandler
import arrow
import requests
from tabulate import tabulate


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
MSN2=""
MSN3=""
MSN4=""
TOKEN=""
CHAT=""

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

def Forecast(update,lat,lon,BOT_TOKEN,chat_id):

    la = lat
    lo = lon
    tz='UTC+1'
    global TABLA1,TABLA2,TABLA3,TABLA4,DIRV,DIRS,DIRV2,DIRS2,MSN,MSN2,MSN3,MSN4,TOKEN,CHAT 
    TOKEN=BOT_TOKEN
    CHAT=chat_id
    global buttonNUEVO
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
    json_data = {'hours': [{'airTemperature': {'dwd': 10.6, 'noaa': 8.17, 'sg': 10.6}, 'swellDirection': {'dwd': 321.02, 'icon': 311.47, 'meteo': 312.93, 'noaa': 324.16, 'sg': 312.93}, 'swellHeight': {'dwd': 5.59, 'icon': 5.58, 'meteo': 5.85, 'noaa': 4.66, 'sg': 5.85}, 'swellPeriod': {'dwd': 17.06, 'icon': 16.34, 'meteo': 13.05, 'noaa': 17.17, 'sg': 13.05}, 'time': '2022-02-24T23:00:00+00:00', 'waveDirection': {'icon': 311.77, 'meteo': 313.97, 'noaa': 323.48, 'sg': 313.97}, 'windSpeed': {'icon': 8.41, 'noaa': 2.2, 'sg': 8.41}}, {'airTemperature': {'dwd': 10.65, 'noaa': 8.09, 'sg': 10.65}, 'swellDirection': {'dwd': 321.1, 'icon': 311.74, 'meteo': 313.36, 'noaa': 324.39, 'sg': 313.36}, 'swellHeight': {'dwd': 5.65, 'icon': 5.66, 'meteo': 5.93, 'noaa': 4.91, 'sg': 5.93}, 'swellPeriod': {'dwd': 16.93, 'icon': 16.32, 'meteo': 13.03, 'noaa': 17.42, 'sg': 13.03}, 'time': '2022-02-25T00:00:00+00:00', 'waveDirection': {'icon': 312.14, 'meteo': 314.33, 'noaa': 323.6, 'sg': 314.33}, 'windSpeed': {'icon': 8.85, 'noaa': 2.15, 'sg': 8.85}}, {'airTemperature': {'dwd': 10.49, 'noaa': 7.94, 'sg': 10.49}, 'swellDirection': {'dwd': 321.14, 'icon': 311.97, 'meteo': 313.63, 'noaa': 324.55, 'sg': 313.63}, 'swellHeight': {'dwd': 5.68, 'icon': 5.7, 'meteo': 5.95, 'noaa': 4.97, 'sg': 5.95}, 'swellPeriod': {'dwd': 16.82, 'icon': 16.28, 'meteo': 13.0, 'noaa': 17.42, 'sg': 13.0}, 'time': '2022-02-25T01:00:00+00:00', 'waveDirection': {'icon': 312.41, 'meteo': 314.45, 'noaa': 324.04, 'sg': 314.45}, 'windSpeed': {'icon': 8.9, 'noaa': 2.17, 'sg': 8.9}}, {'airTemperature': {'dwd': 10.33, 'noaa': 7.8, 'sg': 10.33}, 'swellDirection': {'dwd': 321.19, 'icon': 312.19, 'meteo': 313.89, 'noaa': 324.71, 'sg': 313.89}, 'swellHeight': {'dwd': 5.68, 'icon': 5.73, 'meteo': 5.97, 'noaa': 5.04, 'sg': 5.97}, 'swellPeriod': {'dwd': 16.73, 'icon': 16.23, 'meteo': 12.96, 'noaa': 17.43, 'sg': 12.96}, 'time': '2022-02-25T02:00:00+00:00', 'waveDirection': {'icon': 312.69, 'meteo': 314.58, 'noaa': 324.49, 'sg': 314.58}, 'windSpeed': {'icon': 8.96, 'noaa': 2.18, 'sg': 8.96}}, {'airTemperature': {'dwd': 10.22, 'noaa': 7.66, 'sg': 10.22}, 'swellDirection': {'dwd': 321.23, 'icon': 312.42, 'meteo': 314.16, 'noaa': 324.87, 'sg': 314.16}, 'swellHeight': {'dwd': 5.66, 'icon': 5.77, 'meteo': 5.99, 'noaa': 5.1, 'sg': 5.99}, 'swellPeriod': {'dwd': 16.65, 'icon': 16.19, 'meteo': 12.93, 'noaa': 17.43, 'sg': 12.93}, 'time': '2022-02-25T03:00:00+00:00', 'waveDirection': {'icon': 312.96, 'meteo': 314.7, 'noaa': 324.93, 'sg': 314.7}, 'windSpeed': {'icon': 9.01, 'noaa': 2.2, 'sg': 9.01}}, {'airTemperature': {'dwd': 10.19, 'noaa': 7.38, 'sg': 10.19}, 'swellDirection': {'dwd': 321.23, 'icon': 312.57, 'meteo': 314.19, 'noaa': 324.96, 'sg': 314.19}, 'swellHeight': {'dwd': 5.62, 'icon': 5.75, 'meteo': 5.98, 'noaa': 5.08, 'sg': 5.98}, 'swellPeriod': {'dwd': 16.58, 'icon': 16.14, 'meteo': 12.95, 'noaa': 17.46, 'sg': 12.95}, 'time': '2022-02-25T04:00:00+00:00', 'waveDirection': {'icon': 313.16, 'meteo': 314.75, 'noaa': 324.88, 'sg': 314.75}, 'windSpeed': {'icon': 9.16, 'noaa': 2.04, 'sg': 9.16}}, {'airTemperature': {'dwd': 10.17, 'noaa': 7.1, 'sg': 10.17}, 'swellDirection': {'dwd': 321.23, 'icon': 312.73, 'meteo': 314.23, 'noaa': 325.05, 'sg': 314.23}, 'swellHeight': {'dwd': 5.56, 'icon': 5.72, 'meteo': 5.96, 'noaa': 5.05, 'sg': 5.96}, 'swellPeriod': {'dwd': 16.52, 'icon': 16.1, 'meteo': 12.97, 'noaa': 17.5, 'sg': 12.97}, 'time': '2022-02-25T05:00:00+00:00', 'waveDirection': {'icon': 313.37, 'meteo': 314.8, 'noaa': 324.83, 'sg': 314.8}, 'windSpeed': {'icon': 9.3, 'noaa': 
    1.87, 'sg': 9.3}}, {'airTemperature': {'dwd': 10.15, 'noaa': 6.83, 'sg': 10.15}, 'swellDirection': {'dwd': 321.27, 'icon': 312.88, 'meteo': 314.26, 'noaa': 325.14, 'sg': 314.26}, 'swellHeight': {'dwd': 5.5, 'icon': 5.7, 'meteo': 5.95, 'noaa': 5.03, 'sg': 5.95}, 'swellPeriod': {'dwd': 16.47, 'icon': 16.05, 'meteo': 12.99, 'noaa': 17.53, 'sg': 12.99}, 'time': '2022-02-25T06:00:00+00:00', 'waveDirection': {'icon': 313.57, 'meteo': 314.85, 'noaa': 324.78, 'sg': 314.85}, 'windSpeed': {'icon': 9.45, 'noaa': 1.71, 'sg': 9.45}}, {'airTemperature': {'dwd': 10.15, 'noaa': 7.18, 'sg': 10.15}, 'swellDirection': {'dwd': 321.29, 'icon': 313.0, 'meteo': 314.29, 'noaa': 325.31, 'sg': 314.29}, 'swellHeight': {'dwd': 5.44, 'icon': 5.64, 'meteo': 5.92, 'noaa': 4.97, 'sg': 5.92}, 'swellPeriod': {'dwd': 16.42, 'icon': 15.99, 'meteo': 13.02, 'noaa': 17.52, 'sg': 13.02}, 'time': '2022-02-25T07:00:00+00:00', 'waveDirection': {'icon': 313.96, 'meteo': 314.95, 'noaa': 324.79, 'sg': 314.95}, 'windSpeed': {'icon': 9.89, 'noaa': 2.1, 'sg': 9.89}}, {'airTemperature': {'dwd': 
    10.26, 'noaa': 7.53, 'sg': 10.26}, 'swellDirection': {'dwd': 321.27, 'icon': 313.12, 'meteo': 314.33, 'noaa': 325.48, 'sg': 314.33}, 'swellHeight': {'dwd': 5.37, 'icon': 5.57, 'meteo': 5.9, 'noaa': 4.9, 'sg': 5.9}, 'swellPeriod': {'dwd': 16.38, 'icon': 15.94, 'meteo': 13.04, 'noaa': 17.5, 'sg': 13.04}, 'time': '2022-02-25T08:00:00+00:00', 'waveDirection': {'icon': 314.36, 'meteo': 315.06, 'noaa': 324.79, 'sg': 315.06}, 'windSpeed': {'icon': 10.34, 'noaa': 2.48, 'sg': 10.34}}, {'airTemperature': {'dwd': 10.47, 'noaa': 7.88, 'sg': 10.47}, 'swellDirection': {'dwd': 321.31, 'icon': 313.24, 'meteo': 314.36, 'noaa': 325.65, 'sg': 314.36}, 'swellHeight': {'dwd': 5.3, 'icon': 5.51, 'meteo': 5.87, 'noaa': 4.84, 'sg': 5.87}, 'swellPeriod': {'dwd': 16.33, 'icon': 15.88, 'meteo': 13.07, 'noaa': 17.49, 'sg': 13.07}, 'time': '2022-02-25T09:00:00+00:00', 'waveDirection': {'icon': 314.75, 'meteo': 315.16, 'noaa': 324.8, 'sg': 315.16}, 'windSpeed': {'icon': 10.78, 'noaa': 2.87, 'sg': 10.78}}, {'airTemperature': {'dwd': 10.8, 'noaa': 8.98, 'sg': 10.8}, 'swellDirection': {'dwd': 321.29, 'icon': 313.36, 'meteo': 314.43, 'noaa': 325.77, 'sg': 314.43}, 'swellHeight': {'dwd': 5.22, 'icon': 5.44, 'meteo': 5.82, 'noaa': 4.76, 'sg': 5.82}, 'swellPeriod': {'dwd': 16.29, 'icon': 15.83, 'meteo': 13.1, 'noaa': 17.43, 'sg': 13.1}, 'time': '2022-02-25T10:00:00+00:00', 'waveDirection': {'icon': 315.35, 'meteo': 315.35, 'noaa': 324.76, 'sg': 315.35}, 'windSpeed': {'icon': 10.98, 'noaa': 3.22, 'sg': 10.98}}, {'airTemperature': {'dwd': 11.17, 'noaa': 10.08, 'sg': 11.17}, 'swellDirection': {'dwd': 321.3, 'icon': 313.48, 'meteo': 314.51, 'noaa': 325.89, 'sg': 314.51}, 'swellHeight': {'dwd': 5.14, 'icon': 5.36, 'meteo': 5.78, 'noaa': 4.68, 'sg': 5.78}, 'swellPeriod': {'dwd': 16.25, 'icon': 15.77, 'meteo': 13.14, 'noaa': 17.37, 'sg': 13.14}, 'time': '2022-02-25T11:00:00+00:00', 'waveDirection': {'icon': 315.95, 'meteo': 315.54, 'noaa': 324.72, 'sg': 315.54}, 'windSpeed': {'icon': 11.17, 'noaa': 3.56, 'sg': 11.17}}, {'airTemperature': {'dwd': 11.51, 'noaa': 11.18, 'sg': 11.51}, 'swellDirection': {'dwd': 321.29, 'icon': 313.6, 'meteo': 314.58, 'noaa': 326.01, 'sg': 314.58}, 'swellHeight': {'dwd': 5.06, 'icon': 5.29, 'meteo': 5.73, 'noaa': 4.6, 'sg': 5.73}, 'swellPeriod': {'dwd': 16.21, 'icon': 15.72, 'meteo': 13.17, 'noaa': 17.31, 'sg': 13.17}, 'time': '2022-02-25T12:00:00+00:00', 'waveDirection': {'icon': 316.55, 'meteo': 315.73, 'noaa': 324.68, 'sg': 315.73}, 'windSpeed': {'icon': 11.37, 'noaa': 3.91, 'sg': 11.37}}, {'airTemperature': {'dwd': 11.68, 'noaa': 11.19, 'sg': 11.68}, 'swellDirection': {'dwd': 321.31, 'icon': 313.67, 'meteo': 314.69, 'noaa': 325.84, 'sg': 314.69}, 'swellHeight': {'dwd': 4.98, 'icon': 5.21, 'meteo': 5.66, 'noaa': 4.51, 'sg': 5.66}, 'swellPeriod': {'dwd': 16.15, 'icon': 15.67, 'meteo': 13.17, 'noaa': 17.19, 'sg': 13.17}, 'time': '2022-02-25T13:00:00+00:00', 'waveDirection': {'icon': 317.62, 'meteo': 316.08, 'noaa': 324.33, 'sg': 316.08}, 'windSpeed': {'icon': 11.74, 'noaa': 4.07, 'sg': 11.74}}, {'airTemperature': {'dwd': 11.61, 'noaa': 11.2, 'sg': 11.61}, 'swellDirection': {'dwd': 321.3, 'icon': 313.73, 'meteo': 314.79, 'noaa': 325.67, 'sg': 314.79}, 'swellHeight': {'dwd': 4.9, 'icon': 5.14, 'meteo': 5.6, 'noaa': 4.41, 'sg': 5.6}, 'swellPeriod': {'dwd': 16.09, 'icon': 15.61, 'meteo': 13.17, 'noaa': 17.08, 'sg': 13.17}, 'time': '2022-02-25T14:00:00+00:00', 'waveDirection': {'icon': 318.7, 'meteo': 316.44, 'noaa': 323.97, 'sg': 316.44}, 'windSpeed': {'icon': 12.12, 'noaa': 4.23, 'sg': 12.12}}, {'airTemperature': {'dwd': 11.35, 'noaa': 11.21, 'sg': 11.35}, 'swellDirection': {'dwd': 321.27, 'icon': 313.8, 'meteo': 314.9, 'noaa': 325.5, 'sg': 314.9}, 'swellHeight': {'dwd': 4.81, 'icon': 5.06, 'meteo': 5.53, 'noaa': 4.32, 'sg': 5.53}, 'swellPeriod': {'dwd': 16.03, 'icon': 15.56, 'meteo': 13.17, 'noaa': 16.96, 'sg': 13.17}, 'time': '2022-02-25T15:00:00+00:00', 'waveDirection': {'icon': 319.77, 'meteo': 316.79, 'noaa': 323.62, 'sg': 316.79}, 'windSpeed': {'icon': 12.49, 'noaa': 4.39, 'sg': 12.49}}, {'airTemperature': {'dwd': 10.89, 'noaa': 10.02, 'sg': 10.89}, 'swellDirection': {'dwd': 321.37, 'icon': 313.9, 'meteo': 315.02, 'noaa': 325.11, 'sg': 315.02}, 'swellHeight': {'dwd': 4.72, 'icon': 
    4.97, 'meteo': 5.42, 'noaa': 4.21, 'sg': 5.42}, 'swellPeriod': {'dwd': 15.93, 'icon': 15.49, 'meteo': 13.12, 'noaa': 16.88, 'sg': 13.12}, 'time': '2022-02-25T16:00:00+00:00', 'waveDirection': {'icon': 321.9, 'meteo': 317.25, 'noaa': 323.78, 'sg': 317.25}, 'windSpeed': {'icon': 12.94, 'noaa': 4.13, 'sg': 12.94}}, {'airTemperature': {'dwd': 10.41, 'noaa': 8.83, 'sg': 10.41}, 'swellDirection': {'dwd': 321.66, 'icon': 313.99, 'meteo': 315.15, 'noaa': 324.73, 'sg': 315.15}, 'swellHeight': {'dwd': 4.63, 'icon': 4.88, 'meteo': 5.32, 'noaa': 4.11, 'sg': 5.32}, 'swellPeriod': {'dwd': 15.8, 'icon': 15.43, 'meteo': 13.06, 'noaa': 16.8, 'sg': 13.06}, 'time': '2022-02-25T17:00:00+00:00', 'waveDirection': {'icon': 324.04, 'meteo': 317.72, 'noaa': 323.95, 'sg': 317.72}, 'windSpeed': {'icon': 13.4, 'noaa': 3.88, 'sg': 13.4}}, {'airTemperature': {'dwd': 10.07, 'noaa': 7.64, 'sg': 10.07}, 'swellDirection': {'dwd': 322.27, 'icon': 314.09, 'meteo': 315.27, 'noaa': 324.34, 'sg': 315.27}, 'swellHeight': {'dwd': 4.55, 'icon': 4.79, 'meteo': 5.21, 'noaa': 4.0, 'sg': 5.21}, 'swellPeriod': {'dwd': 15.62, 'icon': 15.36, 'meteo': 13.01, 'noaa': 16.72, 'sg': 13.01}, 'time': '2022-02-25T18:00:00+00:00', 'waveDirection': {'icon': 326.17, 'meteo': 318.18, 'noaa': 324.11, 'sg': 318.18}, 'windSpeed': {'icon': 13.85, 'noaa': 3.62, 'sg': 13.85}}, {'airTemperature': {'dwd': 9.91, 'noaa': 6.77, 'sg': 9.91}, 'swellDirection': {'dwd': 323.15, 'icon': 314.23, 'meteo': 315.32, 'noaa': 324.34, 'sg': 315.32}, 'swellHeight': {'dwd': 4.48, 'icon': 4.69, 'meteo': 5.06, 'noaa': 3.89, 'sg': 5.06}, 'swellPeriod': {'dwd': 15.39, 'icon': 15.27, 'meteo': 12.93, 'noaa': 16.62, 'sg': 12.93}, 'time': '2022-02-25T19:00:00+00:00', 'waveDirection': {'icon': 328.99, 'meteo': 318.91, 'noaa': 324.29, 
    'sg': 318.91}, 'windSpeed': {'icon': 13.98, 'noaa': 3.17, 'sg': 13.98}}, {'airTemperature': {'dwd': 9.61, 'noaa': 5.91, 'sg': 9.61}, 'swellDirection': {'dwd': 324.13, 'icon': 314.38, 'meteo': 315.37, 'noaa': 324.34, 'sg': 315.37}, 'swellHeight': {'dwd': 4.4, 'icon': 4.59, 'meteo': 4.92, 'noaa': 3.79, 'sg': 4.92}, 'swellPeriod': {'dwd': 15.14, 'icon': 15.18, 'meteo': 12.84, 'noaa': 16.52, 'sg': 12.84}, 'time': '2022-02-25T20:00:00+00:00', 'waveDirection': {'icon': 331.82, 'meteo': 319.63, 'noaa': 324.48, 'sg': 319.63}, 'windSpeed': {'icon': 14.1, 'noaa': 2.73, 'sg': 14.1}}, {'airTemperature': {'dwd': 9.32, 'noaa': 5.04, 'sg': 9.32}, 'swellDirection': {'dwd': 324.49, 'icon': 314.52, 'meteo': 315.42, 'noaa': 324.34, 'sg': 315.42}, 'swellHeight': {'dwd': 4.3, 'icon': 4.49, 'meteo': 4.77, 'noaa': 3.68, 'sg': 4.77}, 'swellPeriod': {'dwd': 14.98, 'icon': 15.09, 'meteo': 12.76, 'noaa': 16.42, 'sg': 12.76}, 'time': '2022-02-25T21:00:00+00:00', 'waveDirection': {'icon': 334.64, 'meteo': 320.36, 'noaa': 324.66, 'sg': 320.36}, 'windSpeed': {'icon': 14.23, 'noaa': 2.28, 'sg': 14.23}}, {'airTemperature': {'dwd': 9.19, 'noaa': 4.31, 'sg': 9.19}, 'swellDirection': {'dwd': 324.57, 'icon': 314.77, 'meteo': 315.35, 'noaa': 324.3, 'sg': 315.35}, 'swellHeight': {'dwd': 4.19, 'icon': 4.38, 'meteo': 4.6, 'noaa': 3.56, 'sg': 4.6}, 'swellPeriod': {'dwd': 14.85, 'icon': 14.97, 'meteo': 12.66, 'noaa': 16.31, 'sg': 12.66}, 'time': '2022-02-25T22:00:00+00:00', 'waveDirection': {'icon': 336.69, 'meteo': 321.26, 'noaa': 324.51, 'sg': 321.26}, 'windSpeed': {'icon': 13.94, 'noaa': 2.12, 'sg': 13.94}}, {'airTemperature': {'dwd': 9.1, 'noaa': 3.57, 'sg': 9.1}, 'swellDirection': {'dwd': 324.7, 'icon': 315.02, 'meteo': 315.28, 'noaa': 324.26, 'sg': 315.28}, 'swellHeight': {'dwd': 4.07, 'icon': 4.27, 'meteo': 4.42, 'noaa': 3.43, 'sg': 4.42}, 'swellPeriod': {'dwd': 14.72, 'icon': 14.84, 'meteo': 12.55, 'noaa': 16.2, 'sg': 12.55}, 'time': '2022-02-25T23:00:00+00:00', 'waveDirection': {'icon': 338.73, 'meteo': 322.16, 'noaa': 324.35, 'sg': 322.16}, 'windSpeed': {'icon': 13.64, 'noaa': 1.96, 'sg': 13.64}}, {'airTemperature': {'dwd': 8.98, 'noaa': 2.84, 'sg': 8.98}, 'swellDirection': {'dwd': 325.03, 'icon': 315.27, 'meteo': 315.21, 'noaa': 324.22, 'sg': 315.21}, 'swellHeight': {'dwd': 3.96, 'icon': 4.16, 'meteo': 4.25, 'noaa': 3.31, 'sg': 4.25}, 'swellPeriod': {'dwd': 14.56, 'icon': 14.72, 'meteo': 12.45, 'noaa': 16.09, 'sg': 12.45}, 'time': '2022-02-26T00:00:00+00:00', 'waveDirection': {'icon': 340.78, 'meteo': 323.06, 'noaa': 324.2, 'sg': 323.06}, 'windSpeed': {'icon': 13.35, 'noaa': 1.8, 'sg': 13.35}}, {'airTemperature': {'dwd': 8.64, 'noaa': 2.54, 'sg': 8.64}, 'swellDirection': {'dwd': 325.18, 'icon': 315.71, 'meteo': 315.12, 'noaa': 324.06, 'sg': 315.12}, 'swellHeight': {'dwd': 3.85, 'icon': 4.05, 'meteo': 4.07, 'noaa': 3.17, 'sg': 4.07}, 'swellPeriod': {'dwd': 14.42, 'icon': 14.57, 'meteo': 12.34, 'noaa': 15.85, 'sg': 12.34}, 'time': '2022-02-26T01:00:00+00:00', 'waveDirection': {'icon': 342.99, 'meteo': 324.66, 'noaa': 323.98, 'sg': 324.66}, 'windSpeed': {'icon': 13.14, 'noaa': 1.76, 'sg': 13.14}}, {'airTemperature': {'dwd': 8.59, 'noaa': 2.25, 'sg': 8.59}, 'swellDirection': {'dwd': 325.31, 'icon': 316.14, 'meteo': 315.02, 'noaa': 323.91, 'sg': 315.02}, 'swellHeight': {'dwd': 3.74, 'icon': 3.94, 'meteo': 3.9, 'noaa': 3.03, 'sg': 3.9}, 'swellPeriod': {'dwd': 14.28, 'icon': 14.42, 'meteo': 12.22, 'noaa': 15.62, 'sg': 12.22}, 'time': '2022-02-26T02:00:00+00:00', 'waveDirection': {'icon': 345.21, 'meteo': 326.27, 'noaa': 323.75, 'sg': 326.27}, 'windSpeed': {'icon': 12.93, 'noaa': 1.71, 'sg': 12.93}}, {'airTemperature': {'dwd': 7.9, 'noaa': 1.95, 'sg': 7.9}, 'swellDirection': {'dwd': 325.58, 'icon': 316.58, 'meteo': 314.93, 'noaa': 323.75, 'sg': 314.93}, 'swellHeight': {'dwd': 3.63, 'icon': 3.83, 'meteo': 3.72, 'noaa': 2.89, 'sg': 3.72}, 'swellPeriod': {'dwd': 14.13, 'icon': 14.27, 'meteo': 12.11, 'noaa': 15.38, 'sg': 12.11}, 'time': '2022-02-26T03:00:00+00:00', 'waveDirection': {'icon': 347.42, 'meteo': 327.87, 'noaa': 323.53, 'sg': 327.87}, 'windSpeed': {'icon': 12.72, 'noaa': 1.67, 'sg': 12.72}}, {'airTemperature': {'dwd': 7.02, 'noaa': 1.92, 'sg': 7.02}, 'swellDirection': {'dwd': 326.04, 'icon': 321.57, 'meteo': 314.78, 'noaa': 323.47, 'sg': 314.78}, 'swellHeight': {'dwd': 3.53, 'icon': 3.85, 'meteo': 3.55, 'noaa': 2.76, 'sg': 3.55}, 'swellPeriod': {'dwd': 13.96, 'icon': 13.73, 'meteo': 12.0, 'noaa': 15.3, 'sg': 12.0}, 'time': '2022-02-26T04:00:00+00:00', 'waveDirection': {'icon': 348.88, 'meteo': 330.89, 'noaa': 323.27, 'sg': 330.89}, 'windSpeed': {'icon': 11.82, 'noaa': 1.64, 'sg': 11.82}}, {'airTemperature': {'dwd': 6.01, 'noaa': 1.89, 'sg': 6.01}, 'swellDirection': {'dwd': 326.66, 'icon': 326.56, 'meteo': 314.63, 'noaa': 323.18, 'sg': 314.63}, 'swellHeight': {'dwd': 3.42, 'icon': 3.86, 'meteo': 3.38, 'noaa': 2.62, 'sg': 3.38}, 'swellPeriod': {'dwd': 13.78, 'icon': 13.2, 'meteo': 11.89, 'noaa': 15.22, 'sg': 11.89}, 'time': '2022-02-26T05:00:00+00:00', 'waveDirection': {'icon': 350.35, 'meteo': 333.92, 'noaa': 323.01, 'sg': 333.92}, 'windSpeed': {'icon': 10.92, 'noaa': 1.62, 'sg': 10.92}}, {'airTemperature': {'dwd': 5.31, 'noaa': 1.87, 'sg': 5.31}, 'swellDirection': {'dwd': 327.12, 'icon': 331.55, 'meteo': 314.48, 'noaa': 322.9, 'sg': 314.48}, 'swellHeight': {'dwd': 3.32, 'icon': 3.88, 'meteo': 3.21, 'noaa': 2.49, 'sg': 3.21}, 'swellPeriod': {'dwd': 13.63, 'icon': 12.66, 'meteo': 11.78, 'noaa': 15.14, 'sg': 11.78}, 'time': '2022-02-26T06:00:00+00:00', 'waveDirection': {'icon': 351.81, 'meteo': 336.94, 'noaa': 322.75, 'sg': 336.94}, 'windSpeed': {'icon': 10.02, 'noaa': 1.59, 'sg': 10.02}}, {'airTemperature': {'dwd': 4.95, 'noaa': 3.3, 'sg': 4.95}, 'swellDirection': {'dwd': 327.2, 'icon': 336.05, 'meteo': 314.31, 'noaa': 322.58, 'sg': 314.31}, 'swellHeight': {'dwd': 3.2, 'icon': 3.83, 'meteo': 3.07, 'noaa': 2.38, 'sg': 3.07}, 'swellPeriod': {'dwd': 13.5, 'icon': 12.31, 'meteo': 11.67, 'noaa': 14.95, 'sg': 11.67}, 'time': '2022-02-26T07:00:00+00:00', 'waveDirection': {'icon': 351.49, 'meteo': 337.55, 'noaa': 322.39, 'sg': 337.55}, 'windSpeed': {'icon': 9.31, 'noaa': 1.41, 'sg': 9.31}}, {'airTemperature': {'dwd': 5.0, 'noaa': 4.74, 'sg': 5.0}, 'swellDirection': {'dwd': 327.02, 'icon': 340.55, 'meteo': 314.15, 'noaa': 322.26, 'sg': 314.15}, 'swellHeight': {'dwd': 3.08, 'icon': 3.79, 'meteo': 2.93, 'noaa': 2.26, 'sg': 2.93}, 'swellPeriod': {'dwd': 13.39, 'icon': 11.96, 'meteo': 11.57, 'noaa': 14.75, 'sg': 11.57}, 'time': '2022-02-26T08:00:00+00:00', 'waveDirection': {'icon': 351.16, 'meteo': 338.16, 'noaa': 322.03, 'sg': 338.16}, 'windSpeed': {'icon': 8.6, 'noaa': 1.23, 'sg': 8.6}}, {'airTemperature': {'dwd': 6.99, 'noaa': 6.18, 'sg': 6.99}, 'swellDirection': {'dwd': 326.73, 'icon': 345.05, 'meteo': 313.98, 'noaa': 321.94, 'sg': 313.98}, 'swellHeight': {'dwd': 2.96, 'icon': 3.74, 'meteo': 2.79, 'noaa': 2.15, 'sg': 2.79}, 'swellPeriod': {'dwd': 13.28, 'icon': 11.61, 'meteo': 11.46, 'noaa': 14.56, 'sg': 11.46}, 'time': '2022-02-26T09:00:00+00:00', 'waveDirection': {'icon': 350.84, 'meteo': 338.77, 'noaa': 321.67, 'sg': 338.77}, 'windSpeed': {'icon': 7.89, 'noaa': 1.05, 'sg': 7.89}}, {'airTemperature': {'dwd': 9.32, 'noaa': 8.62, 'sg': 9.32}, 'swellDirection': {'dwd': 326.45, 'icon': 345.52, 'meteo': 313.74, 'noaa': 321.73, 'sg': 313.74}, 'swellHeight': {'dwd': 2.88, 'icon': 3.61, 'meteo': 2.67, 'noaa': 2.06, 'sg': 2.67}, 'swellPeriod': {'dwd': 13.18, 'icon': 11.47, 'meteo': 11.36, 'noaa': 14.44, 'sg': 11.36}, 'time': '2022-02-26T10:00:00+00:00', 'waveDirection': {'icon': 349.39, 'meteo': 338.13, 'noaa': 321.58, 'sg': 338.13}, 'windSpeed': {'icon': 6.44, 'noaa': 1.02, 'sg': 6.44}}, {'airTemperature': {'dwd': 11.54, 'noaa': 11.06, 'sg': 11.54}, 'swellDirection': {'dwd': 326.65, 'icon': 346.0, 'meteo': 313.51, 'noaa': 321.52, 'sg': 313.51}, 'swellHeight': {'dwd': 2.76, 'icon': 3.48, 'meteo': 2.56, 'noaa': 1.97, 'sg': 2.56}, 'swellPeriod': {'dwd': 13.01, 'icon': 11.34, 'meteo': 11.25, 'noaa': 14.33, 'sg': 11.25}, 'time': '2022-02-26T11:00:00+00:00', 'waveDirection': {'icon': 347.94, 'meteo': 337.49, 'noaa': 321.5, 'sg': 337.49}, 'windSpeed': {'icon': 4.98, 'noaa': 0.99, 'sg': 4.98}}, {'airTemperature': {'dwd': 13.55, 'noaa': 13.51, 'sg': 13.55}, 'swellDirection': {'dwd': 327.0, 'icon': 346.47, 'meteo': 313.27, 'noaa': 321.31, 'sg': 313.27}, 'swellHeight': {'dwd': 2.64, 'icon': 3.35, 'meteo': 2.44, 'noaa': 1.88, 'sg': 2.44}, 'swellPeriod': {'dwd': 12.83, 'icon': 11.2, 'meteo': 11.15, 'noaa': 14.21, 'sg': 11.15}, 'time': '2022-02-26T12:00:00+00:00', 'waveDirection': {'icon': 346.49, 'meteo': 336.85, 'noaa': 321.41, 'sg': 336.85}, 'windSpeed': {'icon': 3.53, 'noaa': 0.96, 'sg': 3.53}}, {'airTemperature': {'dwd': 14.46, 'noaa': 13.95, 'sg': 14.46}, 'swellDirection': {'dwd': 327.32, 'icon': 345.69, 'meteo': 312.93, 'noaa': 321.17, 'sg': 312.93}, 'swellHeight': {'dwd': 2.54, 'icon': 3.23, 'meteo': 2.36, 'noaa': 1.81, 'sg': 2.36}, 'swellPeriod': {'dwd': 12.66, 'icon': 11.16, 'meteo': 11.07, 'noaa': 14.14, 'sg': 11.07}, 'time': '2022-02-26T13:00:00+00:00', 'waveDirection': {'icon': 345.71, 'meteo': 336.93, 'noaa': 321.35, 'sg': 336.93}, 'windSpeed': {'icon': 2.8, 'noaa': 1.3, 'sg': 
    2.8}}, {'airTemperature': {'dwd': 14.1, 'noaa': 14.39, 'sg': 14.1}, 'swellDirection': {'dwd': 327.6, 'icon': 344.92, 'meteo': 312.59, 'noaa': 321.02, 'sg': 312.59}, 'swellHeight': {'dwd': 2.45, 'icon': 3.1, 'meteo': 2.27, 'noaa': 1.75, 'sg': 2.27}, 'swellPeriod': {'dwd': 12.5, 'icon': 11.12, 'meteo': 10.99, 'noaa': 14.08, 'sg': 10.99}, 'time': '2022-02-26T14:00:00+00:00', 'waveDirection': {'icon': 344.92, 'meteo': 337.01, 'noaa': 321.29, 'sg': 337.01}, 'windSpeed': {'icon': 2.07, 'noaa': 1.64, 'sg': 2.07}}, {'airTemperature': {'dwd': 13.61, 'noaa': 14.83, 'sg': 13.61}, 'swellDirection': {'dwd': 327.64, 'icon': 344.14, 'meteo': 312.25, 'noaa': 320.88, 'sg': 312.25}, 'swellHeight': {'dwd': 2.35, 'icon': 2.98, 'meteo': 2.19, 'noaa': 1.68, 'sg': 2.19}, 'swellPeriod': {'dwd': 12.37, 'icon': 11.08, 'meteo': 10.91, 'noaa': 14.01, 'sg': 10.91}, 'time': '2022-02-26T15:00:00+00:00', 'waveDirection': {'icon': 344.14, 'meteo': 337.09, 'noaa': 321.23, 'sg': 337.09}, 'windSpeed': {'icon': 1.34, 'noaa': 1.98, 'sg': 1.34}}, {'airTemperature': {'dwd': 12.86, 'noaa': 12.82, 'sg': 12.86}, 'swellDirection': {'dwd': 327.35, 'icon': 342.48, 'meteo': 311.8, 'noaa': 320.09, 'sg': 311.8}, 'swellHeight': {'dwd': 2.27, 'icon': 2.89, 'meteo': 2.14, 'noaa': 1.24, 'sg': 2.14}, 'swellPeriod': {'dwd': 12.26, 'icon': 11.09, 'meteo': 10.88, 'noaa': 15.69, 'sg': 10.88}, 'time': '2022-02-26T16:00:00+00:00', 'waveDirection': {'icon': 342.48, 'meteo': 335.73, 'noaa': 321.03, 'sg': 335.73}, 'windSpeed': {'icon': 1.38, 'noaa': 1.41, 'sg': 1.38}}, {'airTemperature': {'dwd': 12.76, 'noaa': 10.8, 'sg': 12.76}, 'swellDirection': {'dwd': 326.83, 'icon': 340.83, 'meteo': 311.35, 'noaa': 319.31, 'sg': 311.35}, 'swellHeight': {'dwd': 2.2, 'icon': 2.81, 'meteo': 2.1, 'noaa': 0.79, 'sg': 2.1}, 'swellPeriod': {'dwd': 12.19, 'icon': 11.09, 'meteo': 10.85, 'noaa': 17.36, 'sg': 10.85}, 'time': '2022-02-26T17:00:00+00:00', 'waveDirection': {'icon': 340.83, 'meteo': 334.38, 'noaa': 320.84, 'sg': 334.38}, 'windSpeed': {'icon': 1.43, 'noaa': 0.85, 'sg': 1.43}}, {'airTemperature': {'dwd': 12.45, 'noaa': 8.78, 'sg': 12.45}, 'swellDirection': {'dwd': 326.21, 'icon': 339.17, 'meteo': 310.9, 'noaa': 318.52, 'sg': 310.9}, 'swellHeight': {'dwd': 2.13, 'icon': 2.72, 'meteo': 2.05, 'noaa': 0.35, 'sg': 2.05}, 'swellPeriod': {'dwd': 12.14, 'icon': 11.1, 'meteo': 10.82, 'noaa': 19.04, 'sg': 10.82}, 'time': '2022-02-26T18:00:00+00:00', 'waveDirection': {'icon': 339.17, 'meteo': 333.02, 'noaa': 320.64, 'sg': 333.02}, 'windSpeed': {'icon': 1.47, 'noaa': 0.28, 'sg': 1.47}}, {'airTemperature': {'dwd': 11.75, 'noaa': 8.09, 'sg': 11.75}, 'swellDirection': {'dwd': 325.1, 'icon': 335.52, 'meteo': 310.28, 'noaa': 318.46, 'sg': 310.28}, 'swellHeight': {'dwd': 2.07, 'icon': 2.67, 'meteo': 2.04, 'noaa': 0.47, 'sg': 2.04}, 'swellPeriod': {'dwd': 12.14, 'icon': 11.24, 'meteo': 10.85, 'noaa': 18.57, 'sg': 10.85}, 'time': '2022-02-26T19:00:00+00:00', 'waveDirection': {'icon': 335.52, 'meteo': 330.09, 'noaa': 320.28, 'sg': 330.09}, 'windSpeed': {'icon': 1.33, 'noaa': 0.75, 'sg': 1.33}}, {'airTemperature': {'dwd': 11.2, 'noaa': 7.41, 'sg': 11.2}, 'swellDirection': {'dwd': 323.81, 'icon': 331.88, 'meteo': 309.66, 'noaa': 318.39, 'sg': 309.66}, 'swellHeight': {'dwd': 2.02, 'icon': 2.63, 'meteo': 2.04, 'noaa': 0.59, 'sg': 2.04}, 'swellPeriod': {'dwd': 12.18, 'icon': 11.39, 'meteo': 10.88, 'noaa': 18.1, 'sg': 10.88}, 'time': '2022-02-26T20:00:00+00:00', 'waveDirection': {'icon': 331.88, 'meteo': 327.16, 'noaa': 319.92, 'sg': 327.16}, 'windSpeed': {'icon': 1.18, 'noaa': 1.22, 'sg': 1.18}}, {'airTemperature': {'dwd': 11.08, 'noaa': 6.73, 'sg': 11.08}, 'swellDirection': {'dwd': 322.37, 'icon': 328.23, 'meteo': 309.04, 'noaa': 318.33, 'sg': 309.04}, 'swellHeight': {'dwd': 1.99, 'icon': 2.58, 'meteo': 2.03, 'noaa': 0.71, 'sg': 2.03}, 'swellPeriod': {'dwd': 12.27, 'icon': 11.53, 'meteo': 10.91, 'noaa': 17.63, 'sg': 10.91}, 'time': '2022-02-26T21:00:00+00:00', 'waveDirection': {'icon': 328.23, 'meteo': 324.23, 'noaa': 319.56, 'sg': 324.23}, 'windSpeed': {'icon': 1.04, 'noaa': 1.69, 'sg': 1.04}}, {'airTemperature': {'dwd': 11.16, 'noaa': 6.86, 'sg': 11.16}, 'swellDirection': {'dwd': 320.77, 'icon': 324.3, 'meteo': 308.26, 'noaa': 352.48, 'sg': 308.26}, 'swellHeight': {'dwd': 1.98, 'icon': 2.58, 'meteo': 2.07, 'noaa': 0.7, 'sg': 2.07}, 'swellPeriod': {'dwd': 12.42, 'icon': 11.81, 'meteo': 11.03, 'noaa': 13.93, 'sg': 11.03}, 'time': '2022-02-26T22:00:00+00:00', 'waveDirection': {'icon': 324.3, 'meteo': 321.39, 'noaa': 317.68, 'sg': 321.39}, 'windSpeed': {'icon': 0.93, 'noaa': 1.54, 'sg': 0.93}}, {'airTemperature': {'dwd': 11.45, 'noaa': 7.0, 'sg': 11.45}, 'swellDirection': {'dwd': 319.08, 'icon': 320.38, 'meteo': 307.48, 'noaa': 26.64, 'sg': 307.48}, 'swellHeight': {'dwd': 1.99, 'icon': 2.59, 'meteo': 2.1, 'noaa': 0.7, 'sg': 2.1}, 'swellPeriod': {'dwd': 12.63, 'icon': 12.08, 'meteo': 11.14, 'noaa': 10.24, 'sg': 11.14}, 'time': '2022-02-26T23:00:00+00:00', 'waveDirection': {'icon': 320.38, 'meteo': 318.54, 'noaa': 315.8, 'sg': 318.54}, 'windSpeed': {'icon': 0.83, 'noaa': 1.4, 'sg': 0.83}}], 'meta': {'cost': 1, 'dailyQuota': 10, 'end': '2022-02-26 23:00', 'lat': 43.5777, 'lng': -5.9619, 'params': ['airTemperature', 'windSpeed', 'waveDirection', 'swellPeriod', 'swellHeight', 'swellDirection'], 'requestCount': 1, 'start': '2022-02-24 23:00'}}
    
     

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
    
    MSN=update.message.message_id
    print("----------")
    print(MSN)
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
                        [buttonI2 , buttonNUEVO ]
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

   





def cambioI(update):
    global MSN
    MSN1=MSN+1
    print("---")
    print(MSN1)
    bot=telegram.Bot(TOKEN)
    bot.editMessageText(text=TABLA1,
                                    reply_markup= InlineKeyboardMarkup([
                        [buttonI , buttonD ]
                    ]),
                    chat_id=CHAT,
                    message_id=MSN1
    )


def cambioD(update):
    global MSN
    MSN1=MSN+1
    print("---")
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
    global MSN
    print(MSN)
    MSN2=MSN+2
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
    global MSN
    print(MSN)
    MSN2=MSN+2
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
    global MSN
    print(MSN)
    MSN2=MSN+4
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
    global MSN
    print(MSN)
    MSN2=MSN+4
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
    global MSN
    print(MSN)
    MSN4=MSN+5
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
    global MSN
    print(MSN)
    MSN4=MSN+5
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


