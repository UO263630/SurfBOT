"""
-Clase: Forecast.py
-Descripción:
"""
#Librerias para conectarse con Telegram
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto
import telegram

#Libreria para obtener fechas y horas y manipularlas
import arrow

#Libreraia para crear tablas de datos
from tabulate import tabulate

#lLibreria para hacer peticiones HTTP
import requests

#Conexión con la clase Graficas
import Graficas

#Libreria para la apertura de archivos
import os

#Librerai para tratar archivos json
import json
    
import bot
#Variables auxiliares globales
AP=0
AUX=0
DIC=[]
TOKEN=""



#Función que obtiene las predicciones meteorologicas para cada playa
#y las guarda en archivos json diferentes, si estos archivos ya existen
#se sobreescriben
def busqueda(x,y,aux):
        print()
        global AP,AUX
        s="JSON_"+str(x)+"_"+str(y)+"_"+".json"
        if(os.path.exists(s) == False):
            
            if(aux==0):
                AP=0
                AUX=0
            if(AP==10):
                AP=0
                AUX=AUX+1
            s="JSON_"+str(x)+"_"+str(y)+"_"+".json"
            s2="JSON_"+str(x)+"_"+str(y)+"_OLAS"+".json"
                
            print(s)
            file = open(s,"w")
            file2=open(s2,"w")
            # Get first hour of today
            start = arrow.now().floor('day')
            print(start)
            # Get last hour of today
            end = start.shift(days=+2)
            print(end)

            txt=""
            api =open("api.txt","r")
            n=api.readlines()
            response = requests.get(
            'https://api.stormglass.io/v2/weather/point',
            params={
                'lat': x,
                'lng': y,
                'params': ','.join(['airTemperature', 'windSpeed','waveHeight','waveDirection','swellPeriod','swellHeight','swellDirection','waterTemperature']),
                'start': start.to('UTC+2').timestamp(),  # Convert to UTC timestamp
                'end': end.to('UTC+2').timestamp()  # Convert to UTC timestamp
            },
            headers={
                'Authorization': n[AUX].rstrip()
            }
            )

            response2 = requests.get(
            'https://api.stormglass.io/v2/tide/extremes/point',
            params={
                'lat': x,
                'lng': y,
                
                'start': start.to('UTC+2').timestamp(),  # Convert to UTC timestamp
                'end': end.to('UTC+2').timestamp(),  # Convert to UTC timestam
            },
            headers={
                'Authorization': n[AUX].rstrip()
            }
            )

            AP=AP+1
            print(AP)
            api.close()

            # Do something with response data.
            json_data = response.json()
            json_data2= response2.json()
            print("JSON")
            print(json_data2)
            #print(json_data)

            """
            json_data = {'hours': [{'airTemperature': {'dwd': 12.56, 'noaa': 9.78, 'sg': 12.56}, 'swellDirection': {'dwd': 355.72, 'icon': 320.69, 'meteo': 315.38, 'noaa': 353.72, 'sg': 315.38}, 'swellHeight': {'dwd': 1.24, 'icon': 1.79, 'meteo': 1.29, 'noaa': 0.55, 'sg': 1.29}, 'swellPeriod': {'dwd': 10.91, 'icon': 11.77, 'meteo': 12.17, 'noaa': 11.58, 'sg': 12.17}, 'time': 
            '2022-03-19T23:00:00+00:00', 'waterTemperature': {'meto': 12.17, 'noaa': 8.44, 'sg': 12.17}, 'waveDirection': {'icon': 320.69, 'meteo': 313.12, 'noaa': 319.04, 'sg': 313.12}, 'windSpeed': {'icon': 1.41, 'noaa': 2.02, 'sg': 1.41}}, {'airTemperature': {'dwd': 12.27, 'noaa': 9.84, 'sg': 12.27}, 'swellDirection': {'dwd': 354.55, 'icon': 317.72, 'meteo': 319.31, 'noaa': 5.5, 'sg': 319.31}, 'swellHeight': {'dwd': 1.21, 'icon': 1.78, 'meteo': 1.14, 'noaa': 0.58, 'sg': 1.14}, 'swellPeriod': {'dwd': 11.1, 'icon': 12.02, 'meteo': 12.47, 'noaa': 9.91, 'sg': 12.47}, 'time': '2022-03-20T00:00:00+00:00', 'waterTemperature': {'meto': 13.16, 'noaa': 8.55, 'sg': 13.16}, 'waveDirection': {'icon': 317.72, 'meteo': 311.19, 'noaa': 319.15, 'sg': 311.19}, 'windSpeed': {'icon': 1.01, 'noaa': 2.2, 'sg': 1.01}}, {'airTemperature': {'dwd': 11.78, 'noaa': 9.77, 'sg': 11.78}, 'swellDirection': {'dwd': 353.55, 'icon': 314.08, 'meteo': 316.55, 'noaa': 353.66, 'sg': 316.55}, 'swellHeight': {'dwd': 1.19, 'icon': 1.81, 'meteo': 1.19, 'noaa': 0.55, 'sg': 1.19}, 'swellPeriod': {'dwd': 11.31, 'icon': 12.33, 'meteo': 12.1, 'noaa': 11.06, 'sg': 12.1}, 'time': '2022-03-20T01:00:00+00:00', 'waterTemperature': {'meto': 13.18, 'noaa': 8.45, 'sg': 13.18}, 'waveDirection': {'icon': 314.08, 'meteo': 308.33, 'noaa': 318.12, 'sg': 308.33}, 'windSpeed': {'icon': 0.87, 'noaa': 2.22, 'sg': 0.87}}, {'airTemperature': {'dwd': 11.27, 'noaa': 9.69, 'sg': 11.27}, 'swellDirection': {'dwd': 352.87, 'icon': 310.44, 'meteo': 313.8, 'noaa': 341.82, 'sg': 313.8}, 'swellHeight': {'dwd': 1.18, 'icon': 1.83, 'meteo': 1.25, 'noaa': 0.53, 'sg': 1.25}, 'swellPeriod': {'dwd': 11.5, 'icon': 12.65, 'meteo': 11.72, 'noaa': 12.22, 'sg': 11.72}, 'time': '2022-03-20T02:00:00+00:00', 'waterTemperature': {'meto': 13.2, 'noaa': 8.35, 'sg': 13.2}, 'waveDirection': {'icon': 310.44, 'meteo': 305.48, 'noaa': 317.08, 'sg': 305.48}, 'windSpeed': {'icon': 0.73, 'noaa': 2.23, 'sg': 0.73}}, {'airTemperature': {'dwd': 11.3, 'noaa': 9.61, 'sg': 11.3}, 'swellDirection': {'dwd': 352.61, 'icon': 306.8, 'meteo': 311.04, 'noaa': 329.98, 'sg': 311.04}, 'swellHeight': {'dwd': 1.18, 'icon': 1.86, 'meteo': 1.3, 'noaa': 0.5, 'sg': 1.3}, 'swellPeriod': {'dwd': 11.67, 'icon': 12.96, 'meteo': 11.35, 'noaa': 13.37, 'sg': 11.35}, 'time': '2022-03-20T03:00:00+00:00', 'waterTemperature': {'meto': 13.21, 'noaa': 8.25, 'sg': 13.21}, 'waveDirection': {'icon': 306.8, 'meteo': 302.62, 'noaa': 316.05, 'sg': 302.62}, 'windSpeed': {'icon': 0.59, 'noaa': 2.25, 'sg': 0.59}}, {'airTemperature': {'dwd': 11.26, 'noaa': 9.51, 'sg': 11.26}, 'swellDirection': {'dwd': 352.69, 'icon': 304.11, 'meteo': 299.42, 'noaa': 357.52, 'sg': 299.42}, 'swellHeight': {'dwd': 1.2, 'icon': 1.92, 'meteo': 1.4, 'noaa': 0.52, 'sg': 1.4}, 'swellPeriod': {'dwd': 11.81, 'icon': 13.19, 'meteo': 12.05, 'noaa': 10.64, 'sg': 12.05}, 'time': '2022-03-20T04:00:00+00:00', 'waterTemperature': {'meto': 13.23, 'noaa': 8.11, 'sg': 13.23}, 'waveDirection': {'icon': 304.11, 'meteo': 299.8, 'noaa': 313.18, 'sg': 299.8}, 'windSpeed': {'icon': 0.77, 'noaa': 2.4, 'sg': 0.77}}, {'airTemperature': {'dwd': 10.99, 'noaa': 9.4, 'sg': 10.99}, 'swellDirection': {'dwd': 352.81, 'icon': 301.41, 
            'meteo': 287.81, 'noaa': 25.05, 'sg': 287.81}, 'swellHeight': {'dwd': 1.22, 'icon': 1.98, 'meteo': 1.5, 'noaa': 0.55, 'sg': 1.5}, 'swellPeriod': {'dwd': 11.93, 'icon': 13.42, 'meteo': 12.76, 'noaa': 7.9, 'sg': 12.76}, 'time': '2022-03-20T05:00:00+00:00', 'waterTemperature': {'meto': 13.24, 'noaa': 7.97, 'sg': 13.24}, 'waveDirection': {'icon': 301.41, 'meteo': 296.98, 'noaa': 310.32, 'sg': 296.98}, 'windSpeed': {'icon': 0.95, 'noaa': 2.54, 'sg': 0.95}}, {'airTemperature': {'dwd': 10.92, 'noaa': 9.29, 'sg': 10.92}, 'swellDirection': {'dwd': 352.55, 'icon': 298.72, 'meteo': 276.19, 'noaa': 52.59, 'sg': 276.19}, 'swellHeight': {'dwd': 1.24, 'icon': 2.04, 'meteo': 1.6, 'noaa': 0.57, 'sg': 1.6}, 'swellPeriod': {'dwd': 12.06, 'icon': 13.65, 'meteo': 13.46, 'noaa': 5.17, 'sg': 13.46}, 'time': '2022-03-20T06:00:00+00:00', 'waterTemperature': {'meto': 13.26, 'noaa': 7.83, 'sg': 13.26}, 'waveDirection': {'icon': 298.72, 'meteo': 294.16, 'noaa': 307.45, 'sg': 294.16}, 'windSpeed': {'icon': 1.13, 'noaa': 2.69, 'sg': 1.13}}, {'airTemperature': {'dwd': 10.98, 'noaa': 11.15, 'sg': 10.98}, 'swellDirection': {'dwd': 351.65, 'icon': 297.25, 'meteo': 279.59, 'noaa': 55.89, 'sg': 279.59}, 'swellHeight': {'dwd': 1.26, 'icon': 2.09, 'meteo': 
            1.84, 'noaa': 0.55, 'sg': 1.84}, 'swellPeriod': {'dwd': 12.21, 'icon': 13.76, 'meteo': 13.18, 'noaa': 5.07, 'sg': 13.18}, 'time': '2022-03-20T07:00:00+00:00', 'waterTemperature': {'meto': 13.27, 'noaa': 10.41, 'sg': 13.27}, 'waveDirection': {'icon': 297.25, 'meteo': 292.26, 'noaa': 307.31, 'sg': 292.26}, 'windSpeed': {'icon': 0.93, 'noaa': 2.52, 'sg': 
            0.93}}, {'airTemperature': {'dwd': 11.19, 'noaa': 13.01, 'sg': 11.19}, 'swellDirection': {'dwd': 350.12, 'icon': 295.77, 'meteo': 282.98, 'noaa': 59.18, 'sg': 282.98}, 'swellHeight': {'dwd': 1.27, 'icon': 2.14, 'meteo': 2.09, 'noaa': 0.53, 'sg': 2.09}, 'swellPeriod': {'dwd': 12.38, 'icon': 13.87, 'meteo': 12.9, 'noaa': 4.97, 'sg': 12.9}, 'time': '2022-03-20T08:00:00+00:00', 'waterTemperature': {'meto': 13.28, 'noaa': 12.99, 'sg': 13.28}, 'waveDirection': {'icon': 295.77, 'meteo': 290.35, 'noaa': 307.18, 'sg': 290.35}, 'windSpeed': {'icon': 0.74, 'noaa': 2.36, 'sg': 0.74}}, {'airTemperature': {'dwd': 12.03, 'noaa': 14.87, 'sg': 12.03}, 'swellDirection': {'dwd': 348.15, 'icon': 294.3, 'meteo': 286.38, 'noaa': 62.48, 'sg': 286.38}, 'swellHeight': {'dwd': 1.28, 'icon': 2.19, 'meteo': 2.33, 'noaa': 0.51, 'sg': 2.33}, 'swellPeriod': {'dwd': 12.56, 'icon': 13.98, 'meteo': 12.62, 
            'noaa': 4.87, 'sg': 12.62}, 'time': '2022-03-20T09:00:00+00:00', 'waterTemperature': {'meto': 13.29, 'noaa': 15.57, 'sg': 13.29}, 'waveDirection': {'icon': 294.3, 'meteo': 288.45, 'noaa': 307.04, 'sg': 288.45}, 'windSpeed': {'icon': 0.54, 'noaa': 2.19, 'sg': 0.54}}, {'airTemperature': {'dwd': 12.4, 'noaa': 15.99, 'sg': 12.4}, 'swellDirection': {'dwd': 
            345.99, 'icon': 293.66, 'meteo': 285.86, 'noaa': 24.74, 'sg': 285.86}, 'swellHeight': {'dwd': 1.28, 'icon': 2.21, 'meteo': 2.38, 'noaa': 0.76, 'sg': 2.38}, 'swellPeriod': {'dwd': 12.74, 'icon': 13.99, 'meteo': 12.54, 'noaa': 8.37, 'sg': 12.54}, 'time': '2022-03-20T10:00:00+00:00', 'waterTemperature': {'meto': 13.3, 'noaa': 17.62, 'sg': 13.3}, 'waveDirection': {'icon': 293.66, 'meteo': 287.67, 'noaa': 307.06, 'sg': 287.67}, 'windSpeed': {'icon': 0.82, 'noaa': 1.98, 'sg': 0.82}}, {'airTemperature': {'dwd': 12.03, 'noaa': 17.11, 'sg': 12.03}, 'swellDirection': {'dwd': 343.88, 'icon': 293.01, 'meteo': 285.34, 'noaa': 346.99, 'sg': 285.34}, 'swellHeight': {'dwd': 1.29, 'icon': 2.24, 'meteo': 2.43, 'noaa': 1.0, 'sg': 2.43}, 'swellPeriod': {'dwd': 12.89, 'icon': 14.01, 'meteo': 12.45, 'noaa': 11.87, 'sg': 12.45}, 'time': '2022-03-20T11:00:00+00:00', 'waterTemperature': {'meto': 13.31, 'noaa': 19.67, 'sg': 13.31}, 'waveDirection': {'icon': 293.01, 'meteo': 286.88, 'noaa': 307.09, 'sg': 286.88}, 'windSpeed': {'icon': 1.1, 'noaa': 1.76, 'sg': 1.1}}, {'airTemperature': {'dwd': 12.06, 'noaa': 18.23, 'sg': 12.06}, 'swellDirection': {'dwd': 341.91, 'icon': 292.37, 'meteo': 284.82, 'noaa': 309.25, 'sg': 284.82}, 'swellHeight': {'dwd': 1.28, 'icon': 2.26, 'meteo': 2.48, 'noaa': 1.25, 'sg': 2.48}, 'swellPeriod': {'dwd': 13.01, 'icon': 14.02, 'meteo': 12.37, 'noaa': 15.37, 'sg': 12.37}, 'time': '2022-03-20T12:00:00+00:00', 'waterTemperature': {'meto': 13.33, 'noaa': 21.72, 'sg': 13.33}, 'waveDirection': {'icon': 292.37, 'meteo': 286.1, 'noaa': 307.11, 'sg': 286.1}, 'windSpeed': {'icon': 1.38, 'noaa': 1.55, 'sg': 1.38}}, {'airTemperature': {'dwd': 12.33, 'noaa': 17.53, 'sg': 12.33}, 'swellDirection': {'dwd': 340.14, 'icon': 292.22, 'meteo': 284.88, 'noaa': 309.02, 'sg': 284.88}, 'swellHeight': {'dwd': 1.28, 'icon': 2.26, 'meteo': 2.48, 'noaa': 1.25, 'sg': 2.48}, 'swellPeriod': {'dwd': 13.1, 'icon': 13.97, 'meteo': 12.26, 'noaa': 15.12, 'sg': 12.26}, 'time': '2022-03-20T13:00:00+00:00', 'waterTemperature': {'meto': 13.34, 'noaa': 20.16, 'sg': 13.34}, 'waveDirection': {'icon': 292.22, 'meteo': 286.05, 'noaa': 307.14, 'sg': 286.05}, 'windSpeed': {'icon': 1.68, 'noaa': 1.65, 'sg': 1.68}}, {'airTemperature': {'dwd': 12.39, 'noaa': 16.83, 'sg': 12.39}, 'swellDirection': {'dwd': 338.56, 'icon': 292.06, 'meteo': 284.94, 'noaa': 308.78, 'sg': 284.94}, 'swellHeight': {'dwd': 1.27, 'icon': 2.25, 'meteo': 2.48, 'noaa': 1.24, 'sg': 2.48}, 'swellPeriod': {'dwd': 13.16, 'icon': 13.91, 'meteo': 12.15, 'noaa': 14.86, 'sg': 12.15}, 'time': '2022-03-20T14:00:00+00:00', 'waterTemperature': {'meto': 13.35, 'noaa': 18.61, 'sg': 13.35}, 'waveDirection': {'icon': 292.06, 'meteo': 285.99, 'noaa': 307.17, 'sg': 285.99}, 'windSpeed': {'icon': 1.97, 'noaa': 1.74, 'sg': 1.97}}, {'airTemperature': {'dwd': 12.72, 'noaa': 16.12, 'sg': 12.72}, 'swellDirection': {'dwd': 337.17, 'icon': 291.91, 'meteo': 285.0, 'noaa': 308.55, 'sg': 285.0}, 'swellHeight': {'dwd': 1.26, 'icon': 2.25, 'meteo': 2.48, 'noaa': 1.24, 'sg': 2.48}, 'swellPeriod': {'dwd': 13.18, 'icon': 13.86, 'meteo': 12.04, 'noaa': 14.61, 'sg': 12.04}, 'time': '2022-03-20T15:00:00+00:00', 'waterTemperature': {'meto': 13.36, 'noaa': 17.05, 'sg': 13.36}, 'waveDirection': {'icon': 291.91, 'meteo': 285.94, 'noaa': 307.2, 'sg': 285.94}, 'windSpeed': {'icon': 2.27, 'noaa': 1.84, 'sg': 2.27}}, {'airTemperature': {'dwd': 12.96, 'noaa': 15.42, 'sg': 12.96}, 'swellDirection': {'dwd': 335.99, 'icon': 292.05, 'meteo': 285.35, 'noaa': 308.61, 'sg': 285.35}, 'swellHeight': {'dwd': 1.26, 'icon': 2.23, 'meteo': 2.45, 'noaa': 1.23, 'sg': 2.45}, 'swellPeriod': {'dwd': 13.15, 'icon': 13.76, 'meteo': 11.92, 'noaa': 14.39, 'sg': 11.92}, 'time': '2022-03-20T16:00:00+00:00', 'waterTemperature': {'meto': 13.37, 'noaa': 15.84, 'sg': 13.37}, 'waveDirection': {'icon': 292.05, 'meteo': 286.3, 'noaa': 307.52, 'sg': 286.3}, 'windSpeed': {'icon': 
            2.33, 'noaa': 1.78, 'sg': 2.33}}, {'airTemperature': {'dwd': 13.07, 'noaa': 14.72, 'sg': 13.07}, 'swellDirection': {'dwd': 334.96, 'icon': 292.18, 'meteo': 285.69, 'noaa': 308.68, 'sg': 285.69}, 'swellHeight': {'dwd': 1.24, 'icon': 2.21, 'meteo': 2.41, 'noaa': 1.21, 'sg': 2.41}, 'swellPeriod': {'dwd': 13.12, 'icon': 13.66, 'meteo': 11.79, 'noaa': 14.18, 'sg': 11.79}, 'time': '2022-03-20T17:00:00+00:00', 'waterTemperature': {'meto': 13.38, 'noaa': 14.63, 'sg': 13.38}, 'waveDirection': {'icon': 292.18, 'meteo': 286.65, 'noaa': 
            307.85, 'sg': 286.65}, 'windSpeed': {'icon': 2.38, 'noaa': 1.71, 'sg': 2.38}}, {'airTemperature': {'dwd': 13.16, 'noaa': 14.01, 'sg': 13.16}, 'swellDirection': {'dwd': 333.98, 'icon': 292.32, 'meteo': 286.04, 'noaa': 308.74, 'sg': 286.04}, 'swellHeight': {'dwd': 1.23, 'icon': 2.19, 'meteo': 2.38, 'noaa': 1.2, 'sg': 2.38}, 'swellPeriod': {'dwd': 13.08, 
            'icon': 13.56, 'meteo': 11.67, 'noaa': 13.96, 'sg': 11.67}, 'time': '2022-03-20T18:00:00+00:00', 'waterTemperature': {'meto': 13.39, 'noaa': 13.42, 'sg': 13.39}, 'waveDirection': {'icon': 292.32, 'meteo': 287.01, 'noaa': 308.17, 'sg': 287.01}, 'windSpeed': {'icon': 2.44, 'noaa': 1.65, 'sg': 2.44}}, {'airTemperature': {'dwd': 13.27, 'noaa': 13.08, 'sg': 13.27}, 'swellDirection': {'dwd': 333.1, 'icon': 292.64, 'meteo': 286.49, 'noaa': 308.86, 'sg': 286.49}, 'swellHeight': {'dwd': 1.22, 'icon': 2.16, 'meteo': 2.34, 'noaa': 1.19, 'sg': 2.34}, 'swellPeriod': {'dwd': 13.02, 'icon': 13.43, 'meteo': 11.54, 'noaa': 13.82, 'sg': 11.54}, 'time': '2022-03-20T19:00:00+00:00', 'waterTemperature': {'meto': 13.4, 'noaa': 12.3, 'sg': 13.4}, 'waveDirection': {'icon': 292.64, 'meteo': 287.53, 'noaa': 308.63, 'sg': 287.53}, 'windSpeed': {'icon': 2.48, 'noaa': 1.86, 'sg': 2.48}}, {'airTemperature': {'dwd': 13.29, 'noaa': 12.14, 'sg': 13.29}, 'swellDirection': {'dwd': 332.41, 'icon': 292.95, 'meteo': 286.94, 'noaa': 308.98, 'sg': 286.94}, 'swellHeight': {'dwd': 1.21, 
            'icon': 2.13, 'meteo': 2.29, 'noaa': 1.17, 'sg': 2.29}, 'swellPeriod': {'dwd': 12.94, 'icon': 13.29, 'meteo': 11.42, 'noaa': 13.67, 'sg': 11.42}, 'time': '2022-03-20T20:00:00+00:00', 'waterTemperature': {'meto': 13.41, 'noaa': 11.18, 'sg': 13.41}, 'waveDirection': {'icon': 292.95, 'meteo': 288.05, 'noaa': 309.08, 'sg': 288.05}, 'windSpeed': {'icon': 2.52, 'noaa': 2.08, 'sg': 2.52}}, {'airTemperature': {'dwd': 13.31, 'noaa': 11.21, 'sg': 13.31}, 'swellDirection': {'dwd': 331.9, 'icon': 293.27, 'meteo': 287.39, 'noaa': 309.1, 'sg': 287.39}, 'swellHeight': {'dwd': 1.2, 'icon': 2.1, 'meteo': 2.25, 'noaa': 1.16, 'sg': 2.25}, 'swellPeriod': {'dwd': 12.83, 'icon': 13.16, 'meteo': 11.29, 'noaa': 13.53, 'sg': 11.29}, 'time': '2022-03-20T21:00:00+00:00', 'waterTemperature': {'meto': 13.41, 'noaa': 10.06, 'sg': 13.41}, 'waveDirection': {'icon': 293.27, 'meteo': 288.57, 'noaa': 309.54, 'sg': 288.57}, 'windSpeed': {'icon': 2.56, 'noaa': 2.29, 'sg': 2.56}}, {'airTemperature': {'dwd': 13.23, 'noaa': 11.11, 'sg': 13.23}, 'swellDirection': {'dwd': 331.5, 'icon': 
            293.67, 'meteo': 287.84, 'noaa': 309.19, 'sg': 287.84}, 'swellHeight': {'dwd': 1.19, 'icon': 2.07, 'meteo': 2.21, 'noaa': 1.15, 'sg': 2.21}, 'swellPeriod': {'dwd': 12.72, 'icon': 13.02, 'meteo': 11.17, 'noaa': 13.37, 'sg': 11.17}, 'time': '2022-03-20T22:00:00+00:00', 'waterTemperature': {'meto': 13.42, 'noaa': 9.97, 'sg': 13.42}, 'waveDirection': {'icon': 293.67, 'meteo': 289.06, 'noaa': 309.53, 'sg': 289.06}, 'windSpeed': {'icon': 2.14, 'noaa': 2.36, 'sg': 2.14}}, {'airTemperature': {'dwd': 13.04, 'noaa': 11.01, 'sg': 13.04}, 'swellDirection': {'dwd': 331.2, 'icon': 294.07, 'meteo': 288.28, 'noaa': 309.29, 'sg': 288.28}, 'swellHeight': {'dwd': 1.17, 'icon': 2.04, 'meteo': 2.17, 'noaa': 1.14, 'sg': 
            2.17}, 'swellPeriod': {'dwd': 12.6, 'icon': 12.87, 'meteo': 11.04, 'noaa': 13.22, 'sg': 11.04}, 'time': '2022-03-20T23:00:00+00:00', 'waterTemperature': {'meto': 13.43, 'noaa': 
            9.89, 'sg': 13.43}, 'waveDirection': {'icon': 294.07, 'meteo': 289.54, 'noaa': 309.52, 'sg': 289.54}, 'windSpeed': {'icon': 1.73, 'noaa': 2.43, 'sg': 1.73}}, {'airTemperature': 
            {'dwd': 12.86, 'noaa': 10.92, 'sg': 12.86}, 'swellDirection': {'dwd': 331.0, 'icon': 294.47, 'meteo': 288.73, 'noaa': 309.38, 'sg': 288.73}, 'swellHeight': {'dwd': 1.16, 'icon': 2.01, 'meteo': 2.13, 'noaa': 1.13, 'sg': 2.13}, 'swellPeriod': {'dwd': 12.47, 'icon': 12.73, 'meteo': 10.92, 'noaa': 13.06, 'sg': 10.92}, 'time': '2022-03-21T00:00:00+00:00', 'waterTemperature': {'meto': 12.36, 'noaa': 9.8, 'sg': 12.36}, 'waveDirection': {'icon': 294.47, 'meteo': 290.03, 'noaa': 309.51, 'sg': 290.03}, 'windSpeed': {'icon': 1.31, 'noaa': 2.5, 'sg': 1.31}}, {'airTemperature': {'dwd': 12.88, 'noaa': 10.72, 'sg': 12.88}, 'swellDirection': {'dwd': 330.89, 'icon': 294.92, 'meteo': 289.17, 'noaa': 309.63, 'sg': 289.17}, 'swellHeight': {'dwd': 1.15, 'icon': 1.98, 'meteo': 2.09, 'noaa': 1.13, 'sg': 2.09}, 'swellPeriod': {'dwd': 12.33, 'icon': 12.57, 'meteo': 10.8, 'noaa': 12.95, 'sg': 10.8}, 'time': '2022-03-21T01:00:00+00:00', 'waterTemperature': {'meto': 12.34, 'noaa': 9.57, 'sg': 12.34}, 'waveDirection': {'icon': 294.92, 'meteo': 290.85, 'noaa': 309.76, 'sg': 290.85}, 'windSpeed': {'icon': 1.3, 'noaa': 2.48, 'sg': 1.3}}, {'airTemperature': {'dwd': 12.85, 'noaa': 10.53, 'sg': 12.85}, 'swellDirection': {'dwd': 331.03, 'icon': 295.38, 'meteo': 289.61, 'noaa': 309.89, 'sg': 289.61}, 'swellHeight': {'dwd': 1.15, 'icon': 1.95, 'meteo': 2.06, 'noaa': 1.12, 'sg': 2.06}, 'swellPeriod': {'dwd': 12.16, 'icon': 12.42, 'meteo': 10.68, 'noaa': 12.84, 'sg': 10.68}, 'time': '2022-03-21T02:00:00+00:00', 'waterTemperature': {'meto': 12.33, 'noaa': 9.33, 'sg': 12.33}, 'waveDirection': {'icon': 295.38, 'meteo': 291.66, 'noaa': 310.0, 'sg': 291.66}, 'windSpeed': {'icon': 1.28, 'noaa': 2.46, 'sg': 1.28}}, {'airTemperature': {'dwd': 12.81, 'noaa': 10.34, 'sg': 12.81}, 'swellDirection': {'dwd': 331.88, 'icon': 295.83, 'meteo': 290.05, 'noaa': 310.14, 'sg': 290.05}, 'swellHeight': {'dwd': 1.14, 'icon': 1.92, 'meteo': 2.02, 'noaa': 1.12, 'sg': 2.02}, 'swellPeriod': {'dwd': 11.93, 'icon': 12.26, 'meteo': 10.56, 'noaa': 12.73, 'sg': 10.56}, 'time': '2022-03-21T03:00:00+00:00', 'waterTemperature': {'meto': 12.31, 'noaa': 9.09, 'sg': 12.31}, 'waveDirection': {'icon': 295.83, 'meteo': 292.48, 'noaa': 310.25, 'sg': 292.48}, 'windSpeed': {'icon': 1.27, 'noaa': 2.44, 'sg': 1.27}}, {'airTemperature': {'dwd': 12.9, 'noaa': 10.32, 'sg': 12.9}, 'swellDirection': {'dwd': 334.04, 'icon': 296.54, 'meteo': 290.46, 'noaa': 310.04, 'sg': 290.46}, 'swellHeight': {'dwd': 1.15, 'icon': 1.9, 'meteo': 1.98, 'noaa': 1.11, 'sg': 1.98}, 'swellPeriod': {'dwd': 11.6, 'icon': 12.07, 'meteo': 10.45, 'noaa': 12.62, 'sg': 10.45}, 'time': '2022-03-21T04:00:00+00:00', 'waterTemperature': {'meto': 12.3, 'noaa': 9.09, 'sg': 12.3}, 'waveDirection': {'icon': 296.54, 'meteo': 293.22, 'noaa': 310.71, 'sg': 293.22}, 'windSpeed': {'icon': 1.47, 'noaa': 2.55, 'sg': 1.47}}, {'airTemperature': {'dwd': 12.94, 'noaa': 10.3, 'sg': 12.94}, 'swellDirection': {'dwd': 337.69, 'icon': 297.25, 'meteo': 290.86, 'noaa': 309.95, 'sg': 290.86}, 'swellHeight': {'dwd': 1.16, 'icon': 1.88, 'meteo': 1.94, 'noaa': 1.09, 'sg': 1.94}, 'swellPeriod': {'dwd': 11.2, 'icon': 11.88, 'meteo': 10.35, 'noaa': 12.5, 'sg': 10.35}, 'time': '2022-03-21T05:00:00+00:00', 'waterTemperature': {'meto': 12.28, 'noaa': 9.09, 'sg': 12.28}, 'waveDirection': {'icon': 297.25, 'meteo': 293.97, 'noaa': 311.18, 'sg': 293.97}, 'windSpeed': {'icon': 1.67, 'noaa': 2.65, 'sg': 1.67}}, {'airTemperature': {'dwd': 12.93, 'noaa': 10.28, 'sg': 12.93}, 'swellDirection': {'dwd': 342.36, 'icon': 297.96, 'meteo': 291.27, 'noaa': 309.85, 'sg': 291.27}, 'swellHeight': {'dwd': 1.18, 'icon': 1.86, 'meteo': 1.9, 'noaa': 1.08, 'sg': 1.9}, 'swellPeriod': {'dwd': 10.78, 'icon': 11.69, 'meteo': 10.24, 'noaa': 12.39, 'sg': 10.24}, 'time': '2022-03-21T06:00:00+00:00', 'waterTemperature': {'meto': 12.27, 'noaa': 9.08, 'sg': 12.27}, 'waveDirection': {'icon': 297.96, 'meteo': 294.71, 'noaa': 311.64, 'sg': 294.71}, 'windSpeed': {'icon': 1.87, 'noaa': 2.76, 'sg': 1.87}}, {'airTemperature': {'dwd': 12.86, 'noaa': 11.82, 'sg': 12.86}, 'swellDirection': {'dwd': 347.19, 'icon': 298.92, 'meteo': 291.61, 'noaa': 309.97, 'sg': 291.61}, 'swellHeight': {'dwd': 1.2, 'icon': 1.85, 'meteo': 1.86, 'noaa': 1.06, 'sg': 1.86}, 'swellPeriod': {'dwd': 10.42, 'icon': 11.49, 'meteo': 10.14, 'noaa': 12.24, 'sg': 10.14}, 'time': '2022-03-21T07:00:00+00:00', 'waterTemperature': {'meto': 12.26, 'noaa': 11.2, 'sg': 12.26}, 'waveDirection': {'icon': 298.92, 'meteo': 295.3, 'noaa': 311.35, 'sg': 295.3}, 'windSpeed': {'icon': 1.98, 'noaa': 2.64, 'sg': 1.98}}, {'airTemperature': {'dwd': 13.09, 'noaa': 13.35, 'sg': 13.09}, 'swellDirection': {'dwd': 351.53, 'icon': 299.89, 'meteo': 291.94, 'noaa': 310.09, 'sg': 291.94}, 'swellHeight': {'dwd': 1.21, 'icon': 1.83, 'meteo': 1.82, 'noaa': 1.05, 'sg': 1.82}, 'swellPeriod': {'dwd': 10.12, 'icon': 11.29, 'meteo': 10.04, 'noaa': 12.08, 'sg': 10.04}, 'time': '2022-03-21T08:00:00+00:00', 'waterTemperature': {'meto': 12.25, 'noaa': 13.32, 'sg': 12.25}, 'waveDirection': {'icon': 299.89, 'meteo': 295.9, 'noaa': 311.07, 'sg': 295.9}, 'windSpeed': {'icon': 2.08, 'noaa': 2.53, 'sg': 2.08}}, 
            {'airTemperature': {'dwd': 13.61, 'noaa': 14.89, 'sg': 13.61}, 'swellDirection': {'dwd': 355.13, 'icon': 300.85, 'meteo': 292.28, 'noaa': 310.21, 'sg': 292.28}, 'swellHeight': {'dwd': 1.22, 'icon': 1.82, 'meteo': 1.78, 'noaa': 1.03, 'sg': 1.78}, 'swellPeriod': {'dwd': 9.87, 'icon': 11.09, 'meteo': 9.94, 'noaa': 11.93, 'sg': 9.94}, 'time': '2022-03-21T09:00:00+00:00', 'waterTemperature': {'meto': 12.25, 'noaa': 15.44, 'sg': 12.25}, 'waveDirection': {'icon': 300.85, 'meteo': 296.49, 'noaa': 310.78, 'sg': 296.49}, 'windSpeed': {'icon': 2.19, 'noaa': 2.41, 'sg': 2.19}}, {'airTemperature': {'dwd': 14.21, 'noaa': 16.03, 'sg': 14.21}, 'swellDirection': {'dwd': 357.85, 'icon': 301.75, 'meteo': 292.54, 'noaa': 310.36, 'sg': 292.54}, 'swellHeight': {'dwd': 1.22, 'icon': 1.8, 'meteo': 1.74, 'noaa': 1.02, 'sg': 1.74}, 'swellPeriod': {'dwd': 9.68, 'icon': 10.93, 'meteo': 9.84, 'noaa': 
            11.84, 'sg': 9.84}, 'time': '2022-03-21T10:00:00+00:00', 'waterTemperature': {'meto': 12.25, 'noaa': 17.21, 'sg': 12.25}, 'waveDirection': {'icon': 301.75, 'meteo': 297.72, 'noaa': 311.29, 'sg': 297.72}, 'windSpeed': {'icon': 2.15, 'noaa': 2.05, 'sg': 2.15}}, {'airTemperature': {'dwd': 14.37, 'noaa': 17.17, 'sg': 14.37}, 'swellDirection': {'dwd': 359.68, 'icon': 302.64, 'meteo': 292.79, 'noaa': 310.51, 'sg': 292.79}, 'swellHeight': {'dwd': 1.21, 'icon': 1.78, 'meteo': 1.71, 'noaa': 1.01, 'sg': 1.71}, 'swellPeriod': {'dwd': 9.53, 'icon': 10.76, 'meteo': 9.75, 'noaa': 11.74, 'sg': 9.75}, 'time': '2022-03-21T11:00:00+00:00', 'waterTemperature': {'meto': 12.24, 'noaa': 18.98, 'sg': 12.24}, 'waveDirection': {'icon': 302.64, 'meteo': 298.94, 'noaa': 311.8, 'sg': 298.94}, 'windSpeed': {'icon': 2.12, 'noaa': 1.7, 'sg': 2.12}}, {'airTemperature': {'dwd': 14.25, 'noaa': 18.3, 'sg': 
            14.25}, 'swellDirection': {'dwd': 0.75, 'icon': 303.54, 'meteo': 293.05, 'noaa': 310.66, 'sg': 293.05}, 'swellHeight': {'dwd': 1.2, 'icon': 1.76, 'meteo': 1.67, 'noaa': 1.0, 'sg': 1.67}, 'swellPeriod': {'dwd': 9.41, 'icon': 10.6, 'meteo': 9.65, 'noaa': 11.65, 'sg': 9.65}, 'time': '2022-03-21T12:00:00+00:00', 'waterTemperature': {'meto': 12.24, 'noaa': 
            20.75, 'sg': 12.24}, 'waveDirection': {'icon': 303.54, 'meteo': 300.17, 'noaa': 312.31, 'sg': 300.17}, 'windSpeed': {'icon': 2.08, 'noaa': 1.34, 'sg': 2.08}}, {'airTemperature': {'dwd': 13.01, 'noaa': 17.77, 'sg': 13.01}, 'swellDirection': {'dwd': 1.4, 'icon': 304.29, 'meteo': 293.26, 'noaa': 310.87, 'sg': 293.26}, 'swellHeight': {'dwd': 1.18, 'icon': 
            1.74, 'meteo': 1.63, 'noaa': 0.99, 'sg': 1.63}, 'swellPeriod': {'dwd': 9.31, 'icon': 10.47, 'meteo': 9.56, 'noaa': 11.52, 'sg': 9.56}, 'time': '2022-03-21T13:00:00+00:00', 'waterTemperature': {'meto': 12.24, 'noaa': 19.79, 'sg': 12.24}, 'waveDirection': {'icon': 304.3, 'meteo': 302.45, 'noaa': 311.97, 'sg': 302.45}, 'windSpeed': {'icon': 2.58, 'noaa': 
            2.01, 'sg': 2.58}}, {'airTemperature': {'dwd': 12.49, 'noaa': 17.24, 'sg': 12.49}, 'swellDirection': {'dwd': 1.97, 'icon': 305.03, 'meteo': 293.48, 'noaa': 311.07, 'sg': 293.48}, 'swellHeight': {'dwd': 1.17, 'icon': 1.73, 'meteo': 1.6, 'noaa': 0.97, 'sg': 1.6}, 'swellPeriod': {'dwd': 9.22, 'icon': 10.33, 'meteo': 9.47, 'noaa': 11.39, 'sg': 9.47}, 'time': '2022-03-21T14:00:00+00:00', 'waterTemperature': {'meto': 12.24, 'noaa': 18.83, 'sg': 12.24}, 'waveDirection': {'icon': 305.05, 'meteo': 304.73, 'noaa': 311.62, 'sg': 304.73}, 'windSpeed': {'icon': 3.08, 'noaa': 2.68, 'sg': 3.08}}, {'airTemperature': {'dwd': 13.1, 'noaa': 16.71, 'sg': 13.1}, 'swellDirection': {'dwd': 3.39, 'icon': 305.78, 'meteo': 293.69, 'noaa': 311.28, 'sg': 293.69}, 'swellHeight': {'dwd': 1.16, 'icon': 1.71, 'meteo': 1.56, 'noaa': 0.96, 'sg': 1.56}, 'swellPeriod': {'dwd': 9.09, 'icon': 10.2, 'meteo': 9.38, 'noaa': 11.26, 'sg': 9.38}, 'time': '2022-03-21T15:00:00+00:00', 'waterTemperature': {'meto': 12.24, 'noaa': 17.87, 'sg': 12.24}, 'waveDirection': {'icon': 305.81, 'meteo': 
            307.01, 'noaa': 311.28, 'sg': 307.01}, 'windSpeed': {'icon': 3.58, 'noaa': 3.35, 'sg': 3.58}}, {'airTemperature': {'dwd': 13.27, 'noaa': 15.64, 'sg': 13.27}, 'swellDirection': {'dwd': 5.56, 'icon': 306.57, 'meteo': 293.88, 'noaa': 350.05, 'sg': 293.88}, 'swellHeight': {'dwd': 1.15, 'icon': 1.69, 'meteo': 1.53, 'noaa': 0.71, 'sg': 1.53}, 'swellPeriod': 
            {'dwd': 8.96, 'icon': 10.09, 'meteo': 9.3, 'noaa': 9.64, 'sg': 9.3}, 'time': '2022-03-21T16:00:00+00:00', 'waterTemperature': {'meto': 12.24, 'noaa': 16.14, 'sg': 12.24}, 'waveDirection': {'icon': 306.62, 'meteo': 309.56, 'noaa': 311.86, 'sg': 309.56}, 'windSpeed': {'icon': 3.58, 'noaa': 2.81, 'sg': 3.58}}, {'airTemperature': {'dwd': 13.57, 'noaa': 14.57, 'sg': 13.57}, 'swellDirection': {'dwd': 8.34, 'icon': 307.36, 'meteo': 294.08, 'noaa': 28.81, 'sg': 294.08}, 'swellHeight': {'dwd': 1.15, 'icon': 1.68, 'meteo': 1.49, 'noaa': 0.47, 'sg': 1.49}, 'swellPeriod': {'dwd': 8.83, 'icon': 9.99, 'meteo': 9.22, 'noaa': 8.03, 'sg': 9.22}, 'time': '2022-03-21T17:00:00+00:00', 'waterTemperature': {'meto': 12.24, 'noaa': 14.4, 'sg': 12.24}, 'waveDirection': {'icon': 307.42, 'meteo': 312.12, 'noaa': 312.43, 'sg': 312.12}, 'windSpeed': {'icon': 3.57, 'noaa': 2.28, 'sg': 3.57}}, {'airTemperature': {'dwd': 13.96, 'noaa': 13.49, 'sg': 13.96}, 'swellDirection': {'dwd': 11.02, 'icon': 308.15, 'meteo': 294.27, 'noaa': 67.58, 'sg': 294.27}, 'swellHeight': {'dwd': 1.15, 'icon': 1.66, 'meteo': 1.46, 'noaa': 0.22, 'sg': 1.46}, 'swellPeriod': {'dwd': 8.7, 'icon': 9.88, 'meteo': 9.14, 'noaa': 6.41, 'sg': 9.14}, 'time': '2022-03-21T18:00:00+00:00', 'waterTemperature': {'meto': 12.23, 'noaa': 12.67, 'sg': 12.23}, 'waveDirection': {'icon': 308.23, 'meteo': 314.67, 'noaa': 313.01, 'sg': 314.67}, 'windSpeed': {'icon': 3.57, 
            'noaa': 1.74, 'sg': 3.57}}, {'airTemperature': {'dwd': 14.57, 'noaa': 12.55, 'sg': 14.57}, 'swellDirection': {'dwd': 13.06, 'icon': 308.85, 'meteo': 294.4, 'noaa': 42.0, 'sg': 294.4}, 'swellHeight': {'dwd': 1.15, 'icon': 1.65, 'meteo': 1.43, 'noaa': 0.21, 'sg': 1.43}, 'swellPeriod': {'dwd': 8.61, 'icon': 9.82, 'meteo': 9.06, 'noaa': 8.0, 'sg': 9.06}, 'time': '2022-03-21T19:00:00+00:00', 'waterTemperature': {'meto': 12.23, 'noaa': 11.57, 'sg': 12.23}, 'waveDirection': {'icon': 308.9, 'meteo': 317.41, 'noaa': 313.67, 'sg': 317.41}, 'windSpeed': {'icon': 3.27, 'noaa': 2.07, 'sg': 3.27}}, {'airTemperature': {'dwd': 14.69, 'noaa': 11.62, 'sg': 14.69}, 'swellDirection': {'dwd': 14.67, 'icon': 309.54, 'meteo': 294.54, 'noaa': 16.42, 'sg': 294.54}, 'swellHeight': {'dwd': 1.15, 'icon': 1.64, 'meteo': 1.39, 'noaa': 0.19, 'sg': 1.39}, 'swellPeriod': {'dwd': 8.56, 'icon': 9.77, 'meteo': 8.98, 'noaa': 9.6, 'sg': 8.98}, 'time': '2022-03-21T20:00:00+00:00', 'waterTemperature': {'meto': 12.22, 'noaa': 10.48, 'sg': 12.22}, 'waveDirection': {'icon': 309.58, 'meteo': 320.14, 'noaa': 314.34, 'sg': 320.14}, 'windSpeed': {'icon': 2.96, 'noaa': 2.39, 'sg': 2.96}}, {'airTemperature': {'dwd': 14.6, 'noaa': 10.68, 'sg': 14.6}, 'swellDirection': 
            {'dwd': 16.24, 'icon': 310.24, 'meteo': 294.67, 'noaa': 350.84, 'sg': 294.67}, 'swellHeight': {'dwd': 1.15, 'icon': 1.63, 'meteo': 1.36, 'noaa': 0.18, 'sg': 1.36}, 'swellPeriod': {'dwd': 8.52, 'icon': 9.71, 'meteo': 8.9, 'noaa': 11.19, 'sg': 8.9}, 'time': '2022-03-21T21:00:00+00:00', 'waterTemperature': {'meto': 12.21, 'noaa': 9.39, 'sg': 12.21}, 'waveDirection': {'icon': 310.25, 'meteo': 322.88, 'noaa': 315.0, 'sg': 322.88}, 'windSpeed': {'icon': 2.66, 'noaa': 2.72, 'sg': 2.66}}, {'airTemperature': {'dwd': 14.72, 'noaa': 10.37, 'sg': 14.72}, 'swellDirection': {'dwd': 17.85, 'icon': 310.61, 'meteo': 298.61, 'noaa': 337.27, 'sg': 298.61}, 'swellHeight': {'dwd': 1.15, 'icon': 1.64, 'meteo': 1.25, 'noaa': 0.16, 'sg': 1.25}, 'swellPeriod': {'dwd': 8.5, 'icon': 9.77, 'meteo': 8.85, 'noaa': 14.11, 'sg': 8.85}, 'time': '2022-03-21T22:00:00+00:00', 'waterTemperature': {'meto': 12.2, 'noaa': 9.07, 'sg': 12.2}, 'waveDirection': {'icon': 310.61, 'meteo': 336.57, 'noaa': 314.1, 'sg': 336.57}, 'windSpeed': {'icon': 2.83, 'noaa': 2.6, 'sg': 2.83}}, {'airTemperature': {'dwd': 14.78, 'noaa': 10.05, 'sg': 14.78}, 'swellDirection': {'dwd': 19.52, 'icon': 310.97, 'meteo': 302.56, 'noaa': 323.71, 'sg': 302.56}, 'swellHeight': {'dwd': 1.17, 'icon': 1.66, 'meteo': 1.13, 'noaa': 0.13, 'sg': 1.13}, 'swellPeriod': {'dwd': 8.51, 'icon': 9.82, 'meteo': 8.81, 'noaa': 17.03, 'sg': 8.81}, 'time': '2022-03-21T23:00:00+00:00', 'waterTemperature': {'meto': 12.2, 'noaa': 8.74, 'sg': 12.2}, 'waveDirection': {'icon': 310.98, 'meteo': 350.27, 'noaa': 313.21, 'sg': 350.27}, 'windSpeed': {'icon': 2.99, 'noaa': 2.47, 'sg': 2.99}}], 'meta': {'cost': 1, 'dailyQuota': 10, 'end': '2022-03-21 23:00', 'lat': 43.5423, 'lng': -5.6592, 'params': ['airTemperature', 'windSpeed', 'waveDirection', 'swellPeriod', 'swellHeight', 'swellDirection', 'waterTemperature'], 'requestCount': 2, 'start': '2022-03-19 23:00'}}
            """

            #json.dump(json.loads(json_data) , file)
            json.dump(json_data , file)
            json.dump(json_data2,file2)
            #file.write(json_data)
            file.close()
            file2.close()
            print("------------------------forecast---------------------")


#Función que se llama cada vez que se pulsa un boton. Su funcionamiento
#es el de cambiar los datos que se van a mostrar en función del boton
#que se ha pulsado y cambiar el boton que se tiene que mostrar. Esta
#función retorna el resultado de llamar a la función tablas
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
            print(x[3])
            if(str(x[3]) == str(chat)):
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


#Función que obtiene los datos del json los ordena y devuelve la tabla
#o imagen necesaria en función del valor del parametro que se pasa como
#primer argumento
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
    tem3=[]
    tem4=[]
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
                time = fecha[0].split(":")
                time=time[0]+":"+time[1]

                aT = str(row['airTemperature']['noaa'])
            
                n=aT.split(".")
                if(len(n[1]) ==1):
                    aT=n[0]+"."+n[1]+"0"
                if(len(n[0]) ==1):
                    aT=" "+n[0]+"."+n[1]
                if(len(n[0]) ==1 and len(n[1]) ==1):
                    aT="0"+n[0]+"."+n[1]+"0"

                aT=aT + " ºC"


                wS=str(row['windSpeed']['noaa'])

                w=wS.split(".")
                if(len(w[1])==1):
                    wS=w[0]+"."+w[1]+"0"
                wS=wS+ " m/s"

                wD=row['waveDirection']['noaa']

                sP=str(row['swellPeriod']['noaa'])

                n=sP.split(".")
                if(len(n[1]) ==1):
                    sP=n[0]+"."+n[1]+"0"
                if(len(n[0]) ==1):
                    sP="0"+n[0]+"."+n[1]
                if(len(n[0]) ==1 and len(n[1]) ==1):
                    sP="0"+n[0]+"."+n[1]+"0"

                sP=sP + " s"
    
                sH=str(row['waveHeight']['noaa'])

                w=sH.split(".")
                if(len(w[1])==1):
                    sH=w[0]+"."+w[1]+"0"
                sH=sH + " m"

                sD=row['swellDirection']['noaa'] 
                
                wT=str(row['waterTemperature']['noaa'])+" ºC"

                #d= [ time , aT ,  wS, wD ,sP , sH , sD ]
                d= [ time , aT ,  wS ]
                d2= [time, sP,sH, wT]
                data.append(d[:])
                data2.append(d2[:])
                dirv.append(wD)
                dirs.append(sD)
                tem1.append(aT)
                tem3.append(wT)
            if(int(di[2]) > int(dia[2]) or int(di[1]) > int(dia[1]) ):
                
                fecha=dyh.split("T")
                fecha=fecha[1].split("+")
                time = fecha[0].split(":")
                time=time[0]+":"+time[1]

                aT = str(row['airTemperature']['noaa'])
                
                n=aT.split(".")
                if(len(n[1]) ==1):
                    aT=n[0]+"."+n[1]+"0"
                if(len(n[0]) ==1):
                    aT=" "+n[0]+"."+n[1]
                if(len(n[0]) ==1 and len(n[1]) ==1):
                    aT="0"+n[0]+"."+n[1]+"0"

                aT=aT + " ºC"


                wS=str(row['windSpeed']['noaa'])

                w=wS.split(".")
                if(len(w[1])==1):
                    wS=w[0]+"."+w[1]+"0"
                wS=wS+ " m/s"

                wD=row['waveDirection']['noaa']

                sP=str(row['swellPeriod']['noaa'])

                n=sP.split(".")
                if(len(n[1]) ==1):
                    sP=n[0]+"."+n[1]+"0"
                if(len(n[0]) ==1):
                    sP="0"+n[0]+"."+n[1]
                if(len(n[0]) ==1 and len(n[1]) ==1):
                    sP="0"+n[0]+"."+n[1]+"0"

                sP=sP + " s"

                sH=str(row['waveHeight']['noaa']) 

                w=sH.split(".")
                if(len(w[1])==1):
                    sH=w[0]+"."+w[1]+"0"
                sH=sH + " m"

                sD=row['swellDirection']['noaa'] 

                wT=str(row['waterTemperature']['noaa'])+" ºC"

                #d= [ time , aT ,  wS, wD ,sP , sH , sD ]
                d= [time, aT, wS]
                d2= [time, sP, sH, wT]
                data3.append(d[:])
                data4.append(d2[:])
                dirs2.append(sD)
                dirv2.append(wD)
                tem2.append(aT)
                tem4.append(wT)
        x=x+1


    if(id==0):
        tabla1=tabulate( data , headers=["hora","Temperatura" , "Velocidad viento"]  )
        return tabla1
    if(id==1):
        Graficas.grafica1(dirs,0,tem1,data)
        #dirs=[]
        g="WindDirection.png"
        return g
    if(id==2):
        tabla3=tabulate( data3 , headers=["hora","Temperatura" , "Velocidad viento"]  )
        return tabla3
    if(id==3):
        Graficas.grafica1(dirs2,1,tem2,data3)
        #dirs2=[]
        g="WindDirection2.png"
        return g
    if(id==4):
        tabla2= tabulate( data2 , headers=["hora","Periodo oleaje" , "Altura de ola", "Tem. del agua"]  ) 
        return tabla2
    if(id==5):
        Graficas.grafica2(dirv,0,tem3,data2)
        #dirv=[]
        g="SwellDirection.png"
        return g
    if(id==6):
        tabla4=tabulate( data4 , headers=["hora","Periodo oleaje" , "Altura de ola", "Tem. del agua"]  )
        return tabla4
    if(id==7):
        Graficas.grafica2(dirv2,1,tem4,data4)
        #dirv2=[]
        g="SwellDirection2.png"
        return g
        
    print()


#Función que obtiene los datos del json y los ordena y devuelve las tablas
#e imagenes necesarias para que el bot muestre al usuario. A diferencia de
#la clase anterior esta solo se llama la primera vez que se muestran la
#información de cada playa
def Forecast1(BOT_TOKEN,chat_id,json_data,json_data2):
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
    tem3=[]
    tem4=[]
    f=str(start).split("T")
    dia=f[0].split("-")
    #print(int(dia[2]))
    
    wd = []
    print(json_data)
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
                time = fecha[0].split(":")
                time=time[0]+":"+time[1]

                aT = str(row['airTemperature']['noaa'])
                
                n=aT.split(".")
                if(len(n[1]) ==1):
                    aT=n[0]+"."+n[1]+"0"
                if(len(n[0]) ==1):
                    aT="0"+n[0]+"."+n[1]
                if(len(n[0]) ==1 and len(n[1]) ==1):
                    aT="0"+n[0]+"."+n[1]+"0"

                aT=aT + " ºC"
                

                wS=str(row['windSpeed']['noaa'])

                w=wS.split(".")
                if(len(w[1])==1):
                    wS=w[0]+"."+w[1]+"0"
                wS=wS+ " m/s"

                wD=row['waveDirection']['noaa']

                sP=str(row['swellPeriod']['noaa'])

                n=sP.split(".")
                if(len(n[1]) ==1):
                    sP=n[0]+"."+n[1]+"0"
                if(len(n[0]) ==1):
                    sP="0"+n[0]+"."+n[1]
                if(len(n[0]) ==1 and len(n[1]) ==1):
                    sP="0"+n[0]+"."+n[1]+"0"

                sP=sP + " s"

                sH=str(row['waveHeight']['noaa'])

                w=sH.split(".")
                if(len(w[1])==1):
                    sH=w[0]+"."+w[1]+"0"
                sH=sH + " m"

                sD=row['swellDirection']['noaa'] 
                
                wT=str(row['waterTemperature']['noaa'])+" ºC"

                #d= [ time , aT ,  wS, wD ,sP , sH , sD ]
                d= [time ,aT ,wS ]
                d2= [time, sP ,sH, wT]
                data.append(d[:])
                data2.append(d2[:])
                dirv.append(wD)
                dirs.append(sD)
                tem1.append(aT)
                tem3.append(wT)
            if(int(di[2]) > int(dia[2]) or int(di[1]) > int(dia[1]) ):
                
                fecha=dyh.split("T")
                fecha=fecha[1].split("+")
                time = fecha[0].split(":")
                time=time[0]+":"+time[1]

                aT = str(row['airTemperature']['noaa'])

                n=aT.split(".")
                if(len(n[1]) ==1):
                    aT=n[0]+"."+n[1]+"0"
                if(len(n[0]) ==1):
                    aT="0"+n[0]+"."+n[1]
                if(len(n[0]) ==1 and len(n[1]) ==1):
                    aT="0"+n[0]+"."+n[1]+"0"

                aT=aT + " ºC"
                

                wS=str(row['windSpeed']['noaa'])

                w=wS.split(".")
                if(len(w[1])==1):
                    wS=w[0]+"."+w[1]+"0"
                wS=wS+ " m/s"

                wD=row['waveDirection']['noaa']

                sP=str(row['swellPeriod']['noaa'])

                n=sP.split(".")
                if(len(n[1]) ==1):
                    sP=n[0]+"."+n[1]+"0"
                if(len(n[0]) ==1):
                    sP="0"+n[0]+"."+n[1]
                if(len(n[0]) ==1 and len(n[1]) ==1):
                    sP="0"+n[0]+"."+n[1]+"0"

                sP=sP + " s"

                sH=str(row['waveHeight']['noaa'])

                w=sH.split(".")
                if(len(w[1])==1):
                    sH=w[0]+"."+w[1]+"0"
                sH=sH + " m"

                sD=row['swellDirection']['noaa'] 

                wT=str(row['waterTemperature']['noaa'])+" ºC"

                #d= [ time , aT ,  wS, wD ,sP , sH , sD ]
                d= [ time , aT ,  wS ]
                d2= [time, sP,sH, wT]
                data3.append(d[:])
                data4.append(d2[:])
                dirs2.append(sD)
                dirv2.append(wD)
                tem2.append(aT)
                tem4.append(wT)

        x=x+1
        
    pl=[]
    bj=[]
    pl2=[]
    bj2=[]
    for row in json_data2['data']:
        if(row['type']=='high'):
            p=row['time'].split("T")
            if(p[0]==start):
                p=p[1].split("+")
                p=p[0].split(":")
                n=p[0]+":"+p[1]
                pl.append(n)
            else:
                p=p[1].split("+")
                p=p[0].split(":")
                n=p[0]+":"+p[1]
                pl2.append(n)
        else:
            p=row['time'].split("T")
            if(p[0]==start):
                p=p[1].split("+")
                p=p[0].split(":")
                n=p[0]+":"+p[1]
                bj.append(n)
            else:
                p=row['time'].split("T")
                p=p[1].split("+")
                p=p[0].split(":")
                n=p[0]+":"+p[1]
                bj2.append(n)

    bot= telegram.Bot(BOT_TOKEN)
    



    tabla1=tabulate( data , headers=["hora","Temperatura" , "Velocidad viento"]  ) 
    
    
    tabla2= tabulate( data2 , headers=["hora","Periodo oleaje" , "Altura de ola", "Tem. del agua"]  ) 
    
    
    partes = str(start).split("T")[0].split("-")
    #print(partes)

    convertida = "/".join(reversed(partes))
    fe="Fecha:"+ convertida

    bot.sendMessage(chat,text=fe+"\n"+"Pleamar: "+str(pl)+"\n"+"Bajamar: "+str(bj))
    f=bot.sendMessage( chat, tabla1,           
                    reply_markup=InlineKeyboardMarkup([
                        [buttonI]])
                    )
    #print(f)
    msn=f['message_id']
    d=[msn,json_data,0,chat_id]
    DIC.append(d)
    print("-----MSN-----")
    print(msn)
    
    print(data)
    Graficas.grafica1(dirs,0,tem1,data)
    #dirs=[]
    Graficas.grafica2(dirv,0,tem3,data2)
    #dirv=[]

    n=bot.sendPhoto(chat_id=chat,
        photo=open('WindDirection.png','rb') ,
        reply_markup=InlineKeyboardMarkup([
                        [buttonGV]])
                    
    )
    print("----message_id------")
    print(n['message_id'])
    
    
    d=[n['message_id'],json_data,1,chat_id]

    DIC.append(d)

    f=start.shift(days=+1)
    partes = str(f).split("T")[0].split("-")
    #print(partes)

    convertida = "/".join(reversed(partes))

    bot.sendMessage(chat,text="Dia siguiente:"+ convertida+"\n"+"Pleamar: "+str(pl2)+"\n"+"Bajamar: "+str(bj2))


    tabla3=tabulate( data3 , headers=["hora","Temperatura" , "Velocidad viento"]  ) 

    tabla4=tabulate( data4 , headers=["hora","Periodo oleaje" , "Altura de ola", "Tem. del agua"]  )

    
    n=bot.sendMessage( chat, tabla3 ,           
                    reply_markup=InlineKeyboardMarkup([
                        [buttonI]])
                    )
    d=[n['message_id'],json_data,2,chat_id]

    DIC.append(d)
    

    Graficas.grafica1(dirs2,1,tem2,data3)
    #dirs2=[]
    Graficas.grafica2(dirv2,1,tem4,data4)
    #dirv2=[]

 
    n=bot.sendPhoto(chat_id=chat,
        photo=open('WindDirection2.png','rb'),
        reply_markup=InlineKeyboardMarkup([
                        [buttonGV]])
    )
    
    d=[n['message_id'],json_data,3,chat_id]

    DIC.append(d)
    

#Botones utilizados en los diferentes mensajes
buttonI = InlineKeyboardButton(
        text= "Mas Datos",
        callback_data='BD'
)
buttonD = InlineKeyboardButton(
        text= "Volver",
        callback_data='BI'
)
buttonGV = InlineKeyboardButton(
        text= "Mas Graficas",
        callback_data='BGV'
)
buttonGS = InlineKeyboardButton(
        text= "Grafica anterior",
        callback_data='BGI'
)


#Funciones realizan el cambio de información que se muestra en el mensaje
#en el que se pulsa el boton. La información que se muestra varia dependiendo
#del boton pulsado y del chat en el que esté.
def cambioI(id,chat):
    tabla=datos(id,chat)
    #print(chat)
    print("<<<<<<<<<<<<CAMBIOI<<<<<<<<<<<")
    bot2=telegram.Bot(TOKEN)
    bot2.editMessageText(text=tabla,
                    chat_id=chat,
                    message_id=id,
                    reply_markup=InlineKeyboardMarkup([
                    [buttonI]]
                    
                )
    )

def cambioD(id,chat):
    tabla=datos(id,chat)
    #print(chat)
    print("<<<<<<<<<<CAMBIOD<<<<<<<<<<<<<")
    bot2=telegram.Bot(TOKEN)
    bot2.editMessageText(text=tabla,
                    chat_id=chat,
                    message_id=id,
                    reply_markup=InlineKeyboardMarkup([
                    [buttonD]]
                    
                )
    )

def cambioGI(id,chat):
    tabla=datos(id,chat)
    #print(chat)
    print("<<<<<<<<<CAMBIOGI<<<<<<<<<<<<<<")
    bot2=telegram.Bot(TOKEN)
    bot2.editMessageMedia(
                            media=InputMediaPhoto(media = open(tabla,'rb')),
                            reply_markup= InlineKeyboardMarkup([
                            [buttonGV]
                            ]),
                            chat_id=chat,
                            message_id=id
        )

def cambioGV(id,chat):
    tabla=datos(id,chat)
    #print(chat)
    print("<<<<<<<<<<CAMBIOGV<<<<<<<<<<<<<")
    bot2=telegram.Bot(TOKEN)
    bot2.editMessageMedia(
                            media=InputMediaPhoto(media = open(tabla,'rb')),
                            reply_markup= InlineKeyboardMarkup([
                            [buttonGS]
                            ]),
                            chat_id=chat,
                            message_id=id
        )

def cambioGG(id,chat,token):
    #tabla=datos(id,chat)
    #print(chat)
    print("<<<<<<<<<<CAMBIOGG<<<<<<<<<<<<<")
    bot2=telegram.Bot(token)
    Graficas.guia(1)
    bot2.editMessageMedia(
                            media=InputMediaPhoto(media = open("guia2.png",'rb')),
                            reply_markup= InlineKeyboardMarkup([
                            [bot.buttonG2]
                            ]),
                            chat_id=chat,
                            message_id=id
        )

def cambioGG2(id,chat,token):
    #tabla=datos(id,chat)
    #print(chat)
    print("<<<<<<<<<<CAMBIOGG2<<<<<<<<<<<<<")
    bot2=telegram.Bot(token)
    Graficas.guia(0)
    bot2.editMessageMedia(
                            media=InputMediaPhoto(media = open("guia.png",'rb')),
                            reply_markup= InlineKeyboardMarkup([
                            [bot.buttonG]
                            ]),
                            chat_id=chat,
                            message_id=id
        )