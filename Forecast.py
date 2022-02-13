
def Forecast(update,lat,lon):

    la = lat
    lo = lon
    tz='UTC+1'

    import arrow
    import requests

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
    json_data = {'hours': [{'airTemperature': {'dwd': 9.54, 'noaa': 6.88, 'sg': 9.54}, 'swellDirection': {'dwd': 314.14, 'icon': 310.6, 'meteo': 306.47, 'noaa': 314.3, 'sg': 306.47}, 'swellHeight': {'dwd': 1.13, 'icon': 1.47, 'meteo': 1.43, 'noaa': 1.03, 'sg': 1.43}, 'swellPeriod': {'dwd': 10.1, 'icon': 10.45, 'meteo': 9.48, 'noaa': 11.87, 'sg': 9.48}, 'time': '2022-02-12T23:00:00+00:00', 'waveDirection': {'icon': 310.6, 'meteo': 308.33, 'noaa': 308.99, 'sg': 308.33}, 'windSpeed': {'icon': 2.21, 'noaa': 1.44, 'sg': 2.21}}, {'airTemperature': {'dwd': 8.83, 'noaa': 6.58, 'sg': 8.83}, 'swellDirection': {'dwd': 312.48, 'icon': 308.42, 'meteo': 305.37, 'noaa': 312.9, 'sg': 305.37}, 'swellHeight': {'dwd': 1.16, 'icon': 1.48, 'meteo': 1.43, 'noaa': 1.03, 'sg': 1.43}, 'swellPeriod': {'dwd': 10.45, 'icon': 10.65, 'meteo': 9.53, 'noaa': 11.64, 'sg': 9.53}, 'time': '2022-02-13T00:00:00+00:00', 'waveDirection': {'icon': 308.42, 'meteo': 306.94, 'noaa': 308.53, 'sg': 306.94}, 'windSpeed': {'icon': 2.78, 'noaa': 1.6, 'sg': 2.78}}, {'airTemperature': {'dwd': 8.26, 'noaa': 6.43, 'sg': 8.26}, 'swellDirection': {'dwd': 311.02, 'icon': 306.78, 'meteo': 304.34, 'noaa': 348.39, 'sg': 304.34}, 'swellHeight': {'dwd': 1.2, 'icon': 1.51, 'meteo': 1.45, 'noaa': 0.78, 'sg': 1.45}, 'swellPeriod': {'dwd': 10.77, 'icon': 10.85, 'meteo': 9.61, 'noaa': 9.23, 'sg': 9.61}, 'time': '2022-02-13T01:00:00+00:00', 'waveDirection': {'icon': 306.78, 'meteo': 305.69, 'noaa': 307.83, 'sg': 305.69}, 'windSpeed': {'icon': 2.31, 'noaa': 1.65, 'sg': 2.31}}, {'airTemperature': {'dwd': 7.65, 'noaa': 6.28, 'sg': 7.65}, 'swellDirection': {'dwd': 309.74, 'icon': 305.14, 'meteo': 303.31, 'noaa': 23.87, 'sg': 303.31}, 'swellHeight': {'dwd': 1.25, 'icon': 1.54, 'meteo': 1.48, 'noaa': 0.53, 'sg': 1.48}, 'swellPeriod': {'dwd': 11.06, 'icon': 11.06, 'meteo': 9.69, 'noaa': 6.81, 'sg': 9.69}, 'time': '2022-02-13T02:00:00+00:00', 'waveDirection': {'icon': 305.14, 'meteo': 304.44, 'noaa': 307.13, 'sg': 304.44}, 'windSpeed': {'icon': 1.84, 'noaa': 1.71, 'sg': 1.84}}, {'airTemperature': {'dwd': 7.15, 'noaa': 6.14, 'sg': 7.15}, 'swellDirection': {'dwd': 308.63, 'icon': 303.5, 'meteo': 302.28, 'noaa': 59.36, 'sg': 302.28}, 'swellHeight': {'dwd': 1.29, 'icon': 1.57, 'meteo': 1.5, 'noaa': 0.28, 'sg': 1.5}, 'swellPeriod': {'dwd': 11.31, 'icon': 11.26, 'meteo': 9.77, 'noaa': 4.4, 'sg': 9.77}, 'time': '2022-02-13T03:00:00+00:00', 'waveDirection': {'icon': 303.5, 'meteo': 303.19, 'noaa': 306.43, 'sg': 303.19}, 'windSpeed': {'icon': 1.37, 'noaa': 1.76, 'sg': 1.37}}, {'airTemperature': {'dwd': 6.97, 'noaa': 6.18, 'sg': 6.97}, 'swellDirection': {'dwd': 307.71, 'icon': 302.44, 'meteo': 301.58, 'noaa': 65.57, 'sg': 301.58}, 'swellHeight': {'dwd': 1.33, 'icon': 1.6, 'meteo': 1.54, 'noaa': 0.28, 'sg': 1.54}, 'swellPeriod': {'dwd': 11.51, 'icon': 11.38, 'meteo': 9.86, 'noaa': 4.36, 'sg': 9.86}, 'time': '2022-02-13T04:00:00+00:00', 'waveDirection': {'icon': 302.43, 'meteo': 302.3, 'noaa': 305.62, 'sg': 302.3}, 'windSpeed': {'icon': 1.94, 'noaa': 1.92, 'sg': 1.94}}, {'airTemperature': {'dwd': 7.1, 'noaa': 6.23, 'sg': 7.1}, 'swellDirection': {'dwd': 306.94, 'icon': 301.37, 'meteo': 300.89, 'noaa': 71.77, 'sg': 300.89}, 'swellHeight': {'dwd': 1.37, 'icon': 1.64, 'meteo': 1.59, 'noaa': 0.27, 'sg': 1.59}, 'swellPeriod': {'dwd': 11.67, 'icon': 11.49, 'meteo': 9.96, 'noaa': 4.32, 'sg': 9.96}, 'time': '2022-02-13T05:00:00+00:00', 'waveDirection': {'icon': 301.37, 'meteo': 301.41, 'noaa': 304.82, 'sg': 301.41}, 'windSpeed': {'icon': 2.5, 'noaa': 2.08, 'sg': 2.5}}, {'airTemperature': {'dwd': 7.42, 'noaa': 6.27, 'sg': 7.42}, 'swellDirection': {'dwd': 306.32, 'icon': 300.31, 'meteo': 300.19, 'noaa': 77.98, 'sg': 300.19}, 'swellHeight': {'dwd': 1.4, 'icon': 1.67, 'meteo': 1.63, 'noaa': 0.27, 'sg': 1.63}, 'swellPeriod': {'dwd': 11.79, 'icon': 11.61, 'meteo': 10.05, 'noaa': 4.28, 'sg': 10.05}, 'time': '2022-02-13T06:00:00+00:00', 'waveDirection': {'icon': 300.3, 'meteo': 300.52, 'noaa': 304.01, 'sg': 300.52}, 'windSpeed': {'icon': 3.07, 'noaa': 2.24, 'sg': 3.07}}, {'airTemperature': {'dwd': 7.65, 'noaa': 7.18, 'sg': 7.65}, 'swellDirection': {'dwd': 305.82, 'icon': 299.34, 'meteo': 299.66, 'noaa': 32.9, 'sg': 299.66}, 'swellHeight': {'dwd': 1.42, 'icon': 1.7, 'meteo': 1.68, 'noaa': 0.47, 'sg': 1.68}, 'swellPeriod': {'dwd': 11.87, 'icon': 11.58, 'meteo': 10.04, 'noaa': 6.8, 'sg': 10.04}, 'time': '2022-02-13T07:00:00+00:00', 'waveDirection': {'icon': 299.33, 'meteo': 299.97, 'noaa': 305.46, 'sg': 299.97}, 'windSpeed': {'icon': 2.92, 'noaa': 2.27, 'sg': 2.92}}, {'airTemperature': {'dwd': 7.67, 'noaa': 8.1, 'sg': 7.67}, 'swellDirection': {'dwd': 305.39, 'icon': 298.37, 'meteo': 299.13, 'noaa': 347.81, 'sg': 299.13}, 'swellHeight': {'dwd': 1.43, 'icon': 1.74, 'meteo': 1.73, 'noaa': 0.66, 'sg': 1.73}, 'swellPeriod': {'dwd': 11.88, 'icon': 11.56, 'meteo': 10.03, 'noaa': 9.31, 'sg': 10.03}, 'time': '2022-02-13T08:00:00+00:00', 'waveDirection': {'icon': 298.37, 'meteo': 299.41, 'noaa': 306.92, 'sg': 299.41}, 'windSpeed': {'icon': 2.77, 'noaa': 2.31, 'sg': 2.77}}, {'airTemperature': {'dwd': 9.03, 'noaa': 9.01, 'sg': 9.03}, 'swellDirection': {'dwd': 304.97, 'icon': 297.4, 'meteo': 298.6, 'noaa': 302.73, 'sg': 298.6}, 'swellHeight': {'dwd': 1.45, 'icon': 1.77, 'meteo': 1.78, 'noaa': 0.86, 'sg': 1.78}, 'swellPeriod': {'dwd': 11.77, 'icon': 11.53, 'meteo': 10.02, 'noaa': 11.83, 'sg': 10.02}, 'time': '2022-02-13T09:00:00+00:00', 'waveDirection': {'icon': 297.4, 'meteo': 298.86, 'noaa': 308.37, 'sg': 298.86}, 'windSpeed': {'icon': 2.62, 'noaa': 2.34, 'sg': 2.62}}, {'airTemperature': {'dwd': 10.88, 'noaa': 11.32, 'sg': 10.88}, 'swellDirection': {'dwd': 304.41, 'icon': 296.13, 'meteo': 
    298.01, 'noaa': 301.77, 'sg': 298.01}, 'swellHeight': {'dwd': 1.49, 'icon': 1.81, 'meteo': 1.84, 'noaa': 1.03, 'sg': 1.84}, 'swellPeriod': {'dwd': 11.56, 'icon': 11.41, 'meteo': 9.9, 'noaa': 12.13, 'sg': 9.9}, 'time': '2022-02-13T10:00:00+00:00', 'waveDirection': {'icon': 296.13, 'meteo': 298.22, 'noaa': 307.94, 'sg': 298.22}, 'windSpeed': {'icon': 2.32, 'noaa': 2.01, 'sg': 2.32}}, {'airTemperature': {'dwd': 12.55, 'noaa': 13.63, 'sg': 12.55}, 'swellDirection': {'dwd': 303.61, 'icon': 294.85, 'meteo': 297.43, 'noaa': 300.82, 
    'sg': 297.43}, 'swellHeight': {'dwd': 1.53, 'icon': 1.86, 'meteo': 1.89, 'noaa': 1.2, 'sg': 1.89}, 'swellPeriod': {'dwd': 11.35, 'icon': 11.28, 'meteo': 9.79, 'noaa': 12.44, 'sg': 9.79}, 'time': '2022-02-13T11:00:00+00:00', 'waveDirection': {'icon': 294.85, 'meteo': 297.59, 'noaa': 307.52, 'sg': 297.59}, 'windSpeed': {'icon': 2.03, 'noaa': 1.69, 'sg': 
    2.03}}, {'airTemperature': {'dwd': 13.53, 'noaa': 15.93, 'sg': 13.53}, 'swellDirection': {'dwd': 302.62, 'icon': 293.58, 'meteo': 296.84, 'noaa': 299.86, 'sg': 296.84}, 'swellHeight': {'dwd': 1.58, 'icon': 1.9, 'meteo': 1.95, 'noaa': 1.37, 'sg': 1.95}, 'swellPeriod': {'dwd': 11.21, 'icon': 11.16, 'meteo': 9.67, 'noaa': 12.74, 'sg': 9.67}, 'time': '2022-02-13T12:00:00+00:00', 'waveDirection': {'icon': 293.58, 'meteo': 296.95, 'noaa': 307.09, 'sg': 296.95}, 'windSpeed': {'icon': 1.73, 'noaa': 1.36, 'sg': 1.73}}, {'airTemperature': {'dwd': 13.71, 'noaa': 15.12, 'sg': 13.71}, 'swellDirection': {'dwd': 301.63, 'icon': 292.03, 'meteo': 296.43, 'noaa': 297.73, 'sg': 296.43}, 'swellHeight': {'dwd': 1.62, 'icon': 1.94, 'meteo': 2.0, 'noaa': 1.46, 'sg': 2.0}, 'swellPeriod': {'dwd': 11.15, 'icon': 11.02, 'meteo': 9.54, 'noaa': 12.48, 'sg': 9.54}, 'time': '2022-02-13T13:00:00+00:00', 
    'waveDirection': {'icon': 292.03, 'meteo': 292.31, 'noaa': 306.64, 'sg': 292.31}, 'windSpeed': {'icon': 1.64, 'noaa': 2.09, 'sg': 1.64}}, {'airTemperature': {'dwd': 12.81, 'noaa': 14.31, 'sg': 12.81}, 'swellDirection': {'dwd': 300.8, 'icon': 290.47, 'meteo': 296.03, 'noaa': 295.6, 'sg': 296.03}, 'swellHeight': {'dwd': 1.65, 'icon': 1.99, 'meteo': 2.05, 'noaa': 1.56, 'sg': 2.05}, 'swellPeriod': {'dwd': 11.16, 'icon': 10.88, 'meteo': 9.42, 'noaa': 12.23, 'sg': 9.42}, 'time': '2022-02-13T14:00:00+00:00', 'waveDirection': {'icon': 290.47, 'meteo': 287.66, 'noaa': 306.18, 'sg': 287.66}, 'windSpeed': {'icon': 1.55, 'noaa': 2.81, 'sg': 1.55}}, {'airTemperature': {'dwd': 11.78, 'noaa': 13.49, 'sg': 11.78}, 
    'swellDirection': {'dwd': 300.17, 'icon': 288.92, 'meteo': 295.62, 'noaa': 293.47, 'sg': 295.62}, 'swellHeight': {'dwd': 1.66, 'icon': 2.03, 'meteo': 2.1, 'noaa': 1.65, 'sg': 2.1}, 'swellPeriod': {'dwd': 11.19, 'icon': 10.74, 'meteo': 9.29, 'noaa': 11.97, 'sg': 9.29}, 'time': '2022-02-13T15:00:00+00:00', 'waveDirection': {'icon': 288.92, 'meteo': 283.02, 'noaa': 305.73, 'sg': 283.02}, 'windSpeed': {'icon': 1.46, 'noaa': 3.54, 'sg': 1.46}}, {'airTemperature': {'dwd': 11.4, 'noaa': 12.14, 'sg': 11.4}, 'swellDirection': {'dwd': 
    299.57, 'icon': 287.85, 'meteo': 299.44, 'noaa': 296.55, 'sg': 299.44}, 'swellHeight': {'dwd': 1.66, 'icon': 2.06, 'meteo': 1.95, 'noaa': 1.56, 'sg': 1.95}, 'swellPeriod': {'dwd': 11.15, 'icon': 10.77, 'meteo': 9.73, 'noaa': 11.84, 'sg': 9.73}, 'time': '2022-02-13T16:00:00+00:00', 'waveDirection': {'icon': 286.04, 'meteo': 280.21, 'noaa': 303.5, 'sg': 
    280.21}, 'windSpeed': {'icon': 3.96, 'noaa': 3.36, 'sg': 3.96}}, {'airTemperature': {'dwd': 11.68, 'noaa': 10.78, 'sg': 11.68}, 'swellDirection': {'dwd': 298.61, 'icon': 286.78, 'meteo': 303.26, 'noaa': 299.64, 'sg': 303.26}, 'swellHeight': {'dwd': 1.65, 'icon': 2.08, 'meteo': 1.81, 'noaa': 1.48, 'sg': 1.81}, 'swellPeriod': {'dwd': 10.9, 'icon': 10.8, 
    'meteo': 10.18, 'noaa': 11.72, 'sg': 10.18}, 'time': '2022-02-13T17:00:00+00:00', 'waveDirection': {'icon': 283.17, 'meteo': 277.4, 'noaa': 301.27, 'sg': 277.4}, 'windSpeed': {'icon': 6.47, 'noaa': 3.19, 'sg': 6.47}}, {'airTemperature': {'dwd': 12.32, 'noaa': 9.43, 'sg': 12.32}, 'swellDirection': {'dwd': 297.32, 'icon': 285.71, 'meteo': 307.08, 'noaa': 302.72, 'sg': 307.08}, 'swellHeight': {'dwd': 1.69, 'icon': 2.11, 'meteo': 1.66, 'noaa': 1.39, 'sg': 1.66}, 'swellPeriod': {'dwd': 10.47, 'icon': 10.83, 'meteo': 10.62, 'noaa': 11.59, 'sg': 10.62}, 'time': '2022-02-13T18:00:00+00:00', 'waveDirection': {'icon': 280.29, 'meteo': 274.59, 'noaa': 299.04, 'sg': 274.59}, 'windSpeed': {'icon': 8.97, 'noaa': 
    3.01, 'sg': 8.97}}, {'airTemperature': {'dwd': 13.32, 'noaa': 9.06, 'sg': 13.32}, 'swellDirection': {'dwd': 304.3, 'icon': 291.64, 'meteo': 305.73, 'noaa': 305.15, 'sg': 305.73}, 'swellHeight': {'dwd': 1.37, 'icon': 1.85, 'meteo': 1.93, 'noaa': 1.04, 'sg': 1.93}, 'swellPeriod': {'dwd': 12.48, 'icon': 11.56, 'meteo': 10.46, 'noaa': 12.03, 'sg': 10.46}, 
    'time': '2022-02-13T19:00:00+00:00', 'waveDirection': {'icon': 279.63, 'meteo': 277.81, 'noaa': 299.93, 'sg': 277.81}, 'windSpeed': {'icon': 10.9, 'noaa': 3.41, 'sg': 10.9}}, {'airTemperature': {'dwd': 11.0, 'noaa': 8.69, 'sg': 11.0}, 'swellDirection': {'dwd': 303.85, 'icon': 297.58, 'meteo': 304.39, 'noaa': 307.58, 'sg': 304.39}, 'swellHeight': {'dwd': 1.5, 'icon': 1.58, 'meteo': 2.21, 'noaa': 0.69, 'sg': 2.21}, 'swellPeriod': {'dwd': 12.29, 'icon': 12.29, 'meteo': 10.31, 'noaa': 12.48, 'sg': 10.31}, 'time': '2022-02-13T20:00:00+00:00', 'waveDirection': {'icon': 278.98, 'meteo': 281.02, 'noaa': 300.83, 'sg': 281.02}, 'windSpeed': {'icon': 12.83, 'noaa': 3.8, 'sg': 12.83}}, {'airTemperature': {'dwd': 10.84, 'noaa': 8.33, 'sg': 10.84}, 'swellDirection': {'dwd': 302.52, 'icon': 303.51, 'meteo': 303.04, 'noaa': 310.01, 'sg': 303.04}, 'swellHeight': {'dwd': 1.94, 'icon': 1.32, 'meteo': 2.48, 'noaa': 0.34, 'sg': 2.48}, 'swellPeriod': {'dwd': 11.02, 'icon': 13.02, 'meteo': 10.15, 'noaa': 12.92, 'sg': 10.15}, 'time': '2022-02-13T21:00:00+00:00', 'waveDirection': {'icon': 278.32, 'meteo': 284.24, 'noaa': 301.72, 'sg': 284.24}, 'windSpeed': {'icon': 14.76, 'noaa': 4.2, 'sg': 14.76}}, {'airTemperature': {'dwd': 10.6, 'noaa': 7.81, 'sg': 10.6}, 'swellDirection': {'dwd': 301.6, 'icon': 305.11, 'meteo': 305.63, 'noaa': 307.4, 'sg': 305.63}, 'swellHeight': {'dwd': 2.17, 'icon': 1.28, 'meteo': 2.37, 'noaa': 
    0.35, 'sg': 2.37}, 'swellPeriod': {'dwd': 10.33, 'icon': 12.89, 'meteo': 10.02, 'noaa': 11.92, 'sg': 10.02}, 'time': '2022-02-13T22:00:00+00:00', 'waveDirection': {'icon': 279.48, 'meteo': 283.97, 'noaa': 302.28, 'sg': 283.97}, 'windSpeed': {'icon': 14.84, 'noaa': 4.27, 'sg': 14.84}}, {'airTemperature': {'dwd': 10.48, 'noaa': 7.29, 'sg': 10.48}, 'swellDirection': {'dwd': 303.51, 'icon': 306.71, 'meteo': 308.22, 'noaa': 304.78, 'sg': 308.22}, 'swellHeight': {'dwd': 1.96, 'icon': 1.23, 'meteo': 2.26, 'noaa': 0.35, 'sg': 2.26}, 
    'swellPeriod': {'dwd': 10.81, 'icon': 12.75, 'meteo': 9.89, 'noaa': 10.92, 'sg': 9.89}, 'time': '2022-02-13T23:00:00+00:00', 'waveDirection': {'icon': 280.65, 'meteo': 283.71, 'noaa': 302.84, 'sg': 283.71}, 'windSpeed': {'icon': 14.91, 'noaa': 4.34, 'sg': 14.91}}, {'airTemperature': {'dwd': 9.89, 'noaa': 6.77, 'sg': 9.89}, 'swellDirection': {'dwd': 302.44, 'icon': 308.31, 'meteo': 310.81, 'noaa': 302.17, 'sg': 310.81}, 'swellHeight': {'dwd': 2.12, 'icon': 1.19, 'meteo': 2.15, 'noaa': 0.36, 'sg': 2.15}, 'swellPeriod': {'dwd': 
    10.15, 'icon': 12.62, 'meteo': 9.76, 'noaa': 9.92, 'sg': 9.76}, 'time': '2022-02-14T00:00:00+00:00', 'waveDirection': {'icon': 281.81, 'meteo': 283.44, 'noaa': 303.4, 'sg': 283.44}, 'windSpeed': {'icon': 14.99, 'noaa': 4.41, 'sg': 14.99}}, {'airTemperature': {'dwd': 9.67, 'noaa': 6.91, 'sg': 9.67}, 'swellDirection': {'dwd': 299.75, 'icon': 306.61, 'meteo': 311.93, 'noaa': 309.99, 'sg': 311.93}, 'swellHeight': {'dwd': 2.45, 'icon': 1.53, 'meteo': 2.16, 'noaa': 0.48, 'sg': 2.16}, 'swellPeriod': {'dwd': 8.94, 'icon': 11.92, 'meteo': 9.68, 'noaa': 11.34, 'sg': 9.68}, 'time': '2022-02-14T01:00:00+00:00', 'waveDirection': {'icon': 282.66, 'meteo': 283.73, 'noaa': 303.85, 'sg': 283.73}, 'windSpeed': {'icon': 14.38, 'noaa': 4.54, 'sg': 14.38}}, {'airTemperature': {'dwd': 9.61, 'noaa': 7.05, 'sg': 9.61}, 'swellDirection': {'dwd': 300.38, 'icon': 304.92, 'meteo': 313.05, 'noaa': 317.81, 'sg': 313.05}, 'swellHeight': {'dwd': 2.39, 'icon': 1.87, 'meteo': 2.16, 'noaa': 0.6, 'sg': 2.16}, 'swellPeriod': {'dwd': 8.96, 'icon': 11.23, 'meteo': 9.6, 'noaa': 12.77, 
    'sg': 9.6}, 'time': '2022-02-14T02:00:00+00:00', 'waveDirection': {'icon': 283.51, 'meteo': 284.02, 'noaa': 304.29, 'sg': 284.02}, 'windSpeed': {'icon': 13.77, 'noaa': 4.66, 'sg': 13.77}}, {'airTemperature': {'dwd': 9.53, 'noaa': 7.19, 'sg': 9.53}, 'swellDirection': {'dwd': 301.03, 'icon': 303.22, 'meteo': 314.17, 'noaa': 325.63, 'sg': 314.17}, 'swellHeight': {'dwd': 2.33, 'icon': 2.21, 'meteo': 2.17, 'noaa': 0.72, 'sg': 2.17}, 'swellPeriod': {'dwd': 9.02, 'icon': 10.53, 'meteo': 9.52, 'noaa': 14.19, 'sg': 9.52}, 'time': '2022-02-14T03:00:00+00:00', 'waveDirection': {'icon': 284.36, 'meteo': 284.31, 'noaa': 304.74, 'sg': 284.31}, 'windSpeed': {'icon': 13.16, 'noaa': 4.79, 'sg': 13.16}}, {'airTemperature': {'dwd': 9.28, 'noaa': 7.46, 'sg': 9.28}, 'swellDirection': {'dwd': 301.5, 'icon': 305.84, 'meteo': 314.76, 'noaa': 325.47, 'sg': 314.76}, 'swellHeight': {'dwd': 2.3, 'icon': 2.1, 'meteo': 2.25, 'noaa': 0.81, 'sg': 2.25}, 'swellPeriod': {'dwd': 9.04, 'icon': 10.69, 'meteo': 9.54, 'noaa': 14.09, 'sg': 9.54}, 'time': '2022-02-14T04:00:00+00:00', 'waveDirection': {'icon': 284.8, 'meteo': 285.43, 'noaa': 305.54, 'sg': 285.43}, 'windSpeed': {'icon': 13.78, 'noaa': 4.98, 'sg': 13.78}}, {'airTemperature': {'dwd': 9.25, 'noaa': 7.74, 'sg': 9.25}, 'swellDirection': {'dwd': 301.81, 'icon': 308.46, 'meteo': 315.35, 'noaa': 325.32, 'sg': 315.35}, 'swellHeight': {'dwd': 2.29, 'icon': 1.98, 'meteo': 2.33, 'noaa': 0.89, 'sg': 2.33}, 'swellPeriod': {'dwd': 9.04, 'icon': 10.85, 'meteo': 9.55, 'noaa': 13.99, 'sg': 9.55}, 'time': '2022-02-14T05:00:00+00:00', 'waveDirection': {'icon': 285.23, 'meteo': 286.54, 'noaa': 306.33, 'sg': 286.54}, 'windSpeed': {'icon': 14.41, 'noaa': 5.16, 'sg': 14.41}}, {'airTemperature': {'dwd': 9.59, 'noaa': 8.01, 'sg': 9.59}, 'swellDirection': {'dwd': 303.16, 'icon': 311.08, 'meteo': 315.94, 'noaa': 325.16, 'sg': 315.94}, 'swellHeight': {'dwd': 2.3, 'icon': 1.87, 'meteo': 2.41, 'noaa': 0.98, 'sg': 2.41}, 'swellPeriod': {'dwd': 9.17, 'icon': 11.01, 'meteo': 9.57, 'noaa': 13.89, 'sg': 9.57}, 'time': '2022-02-14T06:00:00+00:00', 'waveDirection': {'icon': 285.67, 'meteo': 287.66, 'noaa': 307.13, 'sg': 287.66}, 'windSpeed': {'icon': 15.03, 'noaa': 5.35, 'sg': 15.03}}, {'airTemperature': {'dwd': 10.23, 'noaa': 8.23, 'sg': 10.23}, 'swellDirection': {'dwd': 305.76, 'icon': 313.55, 'meteo': 313.43, 'noaa': 356.63, 'sg': 313.43}, 'swellHeight': {'dwd': 2.27, 'icon': 1.82, 'meteo': 2.7, 'noaa': 0.71, 'sg': 2.7}, 'swellPeriod': {'dwd': 
    9.61, 'icon': 11.14, 'meteo': 9.49, 'noaa': 10.67, 'sg': 9.49}, 'time': '2022-02-14T07:00:00+00:00', 'waveDirection': {'icon': 286.62, 'meteo': 288.6, 'noaa': 307.68, 'sg': 288.6}, 'windSpeed': {'icon': 15.28, 'noaa': 5.33, 'sg': 15.28}}, {'airTemperature': {'dwd': 10.34, 'noaa': 8.45, 'sg': 10.34}, 'swellDirection': {'dwd': 306.2, 'icon': 316.03, 'meteo': 310.92, 'noaa': 28.09, 'sg': 310.92}, 'swellHeight': {'dwd': 2.41, 'icon': 1.78, 'meteo': 2.98, 'noaa': 0.45, 'sg': 2.98}, 'swellPeriod': {'dwd': 9.62, 'icon': 11.27, 'meteo': 9.4, 'noaa': 7.44, 'sg': 9.4}, 'time': '2022-02-14T08:00:00+00:00', 'waveDirection': {'icon': 287.58, 'meteo': 289.55, 'noaa': 308.22, 'sg': 289.55}, 'windSpeed': {'icon': 15.53, 'noaa': 5.31, 'sg': 15.53}}, {'airTemperature': {'dwd': 10.3, 'noaa': 8.67, 'sg': 10.3}, 'swellDirection': {'dwd': 307.77, 'icon': 318.5, 'meteo': 308.41, 'noaa': 59.56, 'sg': 308.41}, 'swellHeight': {'dwd': 2.37, 'icon': 1.73, 'meteo': 3.27, 'noaa': 0.18, 'sg': 3.27}, 'swellPeriod': {'dwd': 10.12, 'icon': 11.4, 'meteo': 9.32, 'noaa': 4.22, 'sg': 9.32}, 'time': '2022-02-14T09:00:00+00:00', 'waveDirection': {'icon': 288.53, 'meteo': 290.49, 'noaa': 308.77, 'sg': 290.49}, 'windSpeed': {'icon': 15.78, 'noaa': 5.29, 'sg': 15.78}}, {'airTemperature': {'dwd': 10.03, 'noaa': 8.96, 'sg': 10.03}, 'swellDirection': {'dwd': 309.76, 'icon': 317.98, 'meteo': 308.77, 'noaa': 21.7, 'sg': 308.77}, 'swellHeight': {'dwd': 2.23, 'icon': 1.86, 'meteo': 3.3, 'noaa': 0.59, 'sg': 3.3}, 'swellPeriod': {'dwd': 10.69, 'icon': 11.5, 'meteo': 9.32, 'noaa': 6.69, 'sg': 9.32}, 'time': '2022-02-14T10:00:00+00:00', 'waveDirection': {'icon': 289.84, 'meteo': 291.75, 'noaa': 308.68, 'sg': 291.75}, 'windSpeed': {'icon': 15.42, 'noaa': 5.31, 'sg': 15.42}}, {'airTemperature': 
    {'dwd': 10.01, 'noaa': 9.24, 'sg': 10.01}, 'swellDirection': {'dwd': 309.37, 'icon': 317.46, 'meteo': 309.12, 'noaa': 343.83, 'sg': 309.12}, 'swellHeight': {'dwd': 2.47, 'icon': 1.99, 'meteo': 3.34, 'noaa': 1.0, 'sg': 3.34}, 'swellPeriod': {'dwd': 10.5, 'icon': 11.6, 'meteo': 9.32, 'noaa': 9.17, 'sg': 9.32}, 'time': '2022-02-14T11:00:00+00:00', 'waveDirection': {'icon': 291.14, 'meteo': 293.01, 'noaa': 308.58, 'sg': 293.01}, 'windSpeed': {'icon': 15.07, 'noaa': 5.34, 'sg': 15.07}}, {'airTemperature': {'dwd': 9.92, 'noaa': 9.53, 'sg': 9.92}, 'swellDirection': {'dwd': 308.51, 'icon': 316.94, 'meteo': 309.48, 'noaa': 305.97, 'sg': 309.48}, 'swellHeight': {'dwd': 2.69, 'icon': 2.12, 'meteo': 3.37, 'noaa': 1.41, 'sg': 3.37}, 'swellPeriod': {'dwd': 10.36, 'icon': 11.7, 'meteo': 9.32, 'noaa': 11.64, 'sg': 9.32}, 'time': '2022-02-14T12:00:00+00:00', 'waveDirection': {'icon': 292.45, 'meteo': 294.27, 'noaa': 308.49, 'sg': 294.27}, 'windSpeed': {'icon': 14.71, 'noaa': 5.36, 'sg': 14.71}}, {'airTemperature': {'dwd': 9.97, 'noaa': 9.36, 'sg': 9.97}, 'swellDirection': {'dwd': 308.8, 'icon': 313.17, 'meteo': 308.17, 'noaa': 310.73, 'sg': 308.17}, 'swellHeight': {'dwd': 2.78, 'icon': 2.52, 'meteo': 3.46, 'noaa': 2.13, 'sg': 3.46}, 'swellPeriod': {'dwd': 10.44, 'icon': 11.53, 'meteo': 9.37, 'noaa': 11.73, 'sg': 9.37}, 'time': '2022-02-14T13:00:00+00:00', 'waveDirection': {'icon': 294.36, 'meteo': 295.88, 'noaa': 308.57, 'sg': 295.88}, 'windSpeed': {'icon': 13.73, 'noaa': 5.29, 'sg': 13.73}}, {'airTemperature': {'dwd': 9.91, 'noaa': 9.19, 'sg': 9.91}, 'swellDirection': {'dwd': 309.09, 'icon': 309.4, 'meteo': 306.85, 'noaa': 315.5, 'sg': 306.85}, 'swellHeight': {'dwd': 2.95, 'icon': 2.92, 'meteo': 3.54, 'noaa': 2.86, 'sg': 3.54}, 'swellPeriod': {'dwd': 10.35, 'icon': 11.35, 'meteo': 9.43, 'noaa': 11.81, 'sg': 9.43}, 'time': '2022-02-14T14:00:00+00:00', 'waveDirection': {'icon': 296.27, 'meteo': 297.5, 'noaa': 308.64, 'sg': 297.5}, 
    'windSpeed': {'icon': 12.76, 'noaa': 5.22, 'sg': 12.76}}, {'airTemperature': {'dwd': 10.01, 'noaa': 9.02, 'sg': 10.01}, 'swellDirection': {'dwd': 309.99, 'icon': 305.63, 'meteo': 305.54, 'noaa': 320.26, 'sg': 305.54}, 'swellHeight': {'dwd': 3.06, 'icon': 3.32, 'meteo': 3.63, 'noaa': 3.58, 'sg': 3.63}, 'swellPeriod': {'dwd': 10.34, 'icon': 11.18, 'meteo': 9.48, 'noaa': 11.9, 'sg': 9.48}, 'time': '2022-02-14T15:00:00+00:00', 'waveDirection': {'icon': 298.18, 'meteo': 299.11, 'noaa': 308.72, 'sg': 299.11}, 'windSpeed': {'icon': 
    11.78, 'noaa': 5.15, 'sg': 11.78}}, {'airTemperature': {'dwd': 9.93, 'noaa': 8.48, 'sg': 9.93}, 'swellDirection': {'dwd': 310.6, 'icon': 306.33, 'meteo': 306.1, 'noaa': 320.82, 
    'sg': 306.1}, 'swellHeight': {'dwd': 3.15, 'icon': 3.32, 'meteo': 3.68, 'noaa': 3.51, 'sg': 3.68}, 'swellPeriod': {'dwd': 10.32, 'icon': 11.18, 'meteo': 9.51, 'noaa': 11.86, 'sg': 9.51}, 'time': '2022-02-14T16:00:00+00:00', 'waveDirection': {'icon': 299.55, 'meteo': 300.86, 'noaa': 309.2, 'sg': 300.86}, 'windSpeed': {'icon': 11.68, 'noaa': 4.81, 'sg': 
    11.68}}, {'airTemperature': {'dwd': 9.85, 'noaa': 7.95, 'sg': 9.85}, 'swellDirection': {'dwd': 311.01, 'icon': 307.03, 'meteo': 306.67, 'noaa': 321.38, 'sg': 306.67}, 'swellHeight': {'dwd': 3.22, 'icon': 3.33, 'meteo': 3.73, 'noaa': 3.45, 'sg': 3.73}, 'swellPeriod': {'dwd': 10.27, 'icon': 11.19, 'meteo': 9.55, 'noaa': 11.83, 'sg': 9.55}, 'time': '2022-02-14T17:00:00+00:00', 'waveDirection': {'icon': 300.93, 'meteo': 302.61, 'noaa': 309.68, 'sg': 302.61}, 'windSpeed': {'icon': 11.57, 'noaa': 4.47, 'sg': 11.57}}, {'airTemperature': {'dwd': 9.78, 'noaa': 7.42, 'sg': 9.78}, 'swellDirection': {'dwd': 311.88, 'icon': 307.73, 'meteo': 307.23, 'noaa': 321.94, 'sg': 307.23}, 'swellHeight': {'dwd': 3.23, 'icon': 3.33, 'meteo': 3.78, 'noaa': 3.38, 'sg': 3.78}, 'swellPeriod': {'dwd': 10.31, 'icon': 11.19, 'meteo': 9.58, 'noaa': 11.79, 'sg': 9.58}, 'time': '2022-02-14T18:00:00+00:00', 
    'waveDirection': {'icon': 302.3, 'meteo': 304.36, 'noaa': 310.16, 'sg': 304.36}, 'windSpeed': {'icon': 11.47, 'noaa': 4.13, 'sg': 11.47}}, {'airTemperature': {'dwd': 9.79, 'noaa': 6.92, 'sg': 9.79}, 'swellDirection': {'dwd': 312.5, 'icon': 308.39, 'meteo': 308.18, 'noaa': 320.16, 'sg': 308.18}, 'swellHeight': {'dwd': 3.23, 'icon': 3.35, 'meteo': 3.84, 
    'noaa': 3.34, 'sg': 3.84}, 'swellPeriod': {'dwd': 10.33, 'icon': 11.09, 'meteo': 9.49, 'noaa': 11.82, 'sg': 9.49}, 'time': '2022-02-14T19:00:00+00:00', 'waveDirection': {'icon': 303.08, 'meteo': 305.44, 'noaa': 310.83, 'sg': 305.44}, 'windSpeed': {'icon': 11.23, 'noaa': 3.47, 'sg': 11.23}}, {'airTemperature': {'dwd': 9.72, 'noaa': 6.43, 'sg': 9.72}, 'swellDirection': {'dwd': 312.95, 'icon': 309.05, 'meteo': 309.12, 'noaa': 318.38, 'sg': 309.12}, 'swellHeight': {'dwd': 3.22, 'icon': 3.37, 'meteo': 3.9, 'noaa': 3.3, 'sg': 3.9}, 'swellPeriod': {'dwd': 10.3, 'icon': 10.99, 'meteo': 9.41, 'noaa': 11.86, 'sg': 9.41}, 'time': '2022-02-14T20:00:00+00:00', 'waveDirection': {'icon': 303.86, 'meteo': 306.51, 'noaa': 311.51, 'sg': 306.51}, 'windSpeed': {'icon': 10.98, 'noaa': 2.8, 'sg': 10.98}}, {'airTemperature': {'dwd': 9.78, 'noaa': 5.94, 'sg': 9.78}, 'swellDirection': {'dwd': 313.37, 'icon': 309.71, 'meteo': 310.07, 'noaa': 316.6, 'sg': 310.07}, 'swellHeight': {'dwd': 3.17, 'icon': 3.39, 'meteo': 3.96, 'noaa': 3.26, 'sg': 3.96}, 'swellPeriod': {'dwd': 10.32, 'icon': 10.89, 'meteo': 9.32, 'noaa': 11.89, 'sg': 9.32}, 'time': '2022-02-14T21:00:00+00:00', 'waveDirection': {'icon': 304.64, 'meteo': 307.59, 'noaa': 312.18, 'sg': 307.59}, 'windSpeed': {'icon': 10.74, 'noaa': 2.14, 'sg': 10.74}}, {'airTemperature': {'dwd': 10.03, 'noaa': 5.46, 'sg': 10.03}, 'swellDirection': {'dwd': 313.63, 'icon': 309.91, 'meteo': 310.21, 'noaa': 317.61, 'sg': 310.21}, 'swellHeight': {'dwd': 3.13, 'icon': 3.37, 'meteo': 3.95, 'noaa': 3.19, 'sg': 3.95}, 'swellPeriod': {'dwd': 10.27, 'icon': 10.79, 'meteo': 9.22, 'noaa': 11.84, 'sg': 9.22}, 'time': '2022-02-14T22:00:00+00:00', 'waveDirection': {'icon': 305.22, 'meteo': 308.15, 'noaa': 312.72, 'sg': 308.15}, 'windSpeed': {'icon': 10.35, 'noaa': 2.09, 'sg': 10.35}}, {'airTemperature': {'dwd': 9.68, 'noaa': 4.97, 'sg': 9.68}, 'swellDirection': {'dwd': 314.15, 'icon': 310.11, 'meteo': 310.35, 'noaa': 
    318.63, 'sg': 310.35}, 'swellHeight': {'dwd': 3.06, 'icon': 3.36, 'meteo': 3.93, 'noaa': 3.13, 'sg': 3.93}, 'swellPeriod': {'dwd': 10.32, 'icon': 10.69, 'meteo': 9.11, 'noaa': 11.79, 'sg': 9.11}, 'time': '2022-02-14T23:00:00+00:00', 'waveDirection': {'icon': 305.79, 'meteo': 308.72, 'noaa': 313.27, 'sg': 308.72}, 'windSpeed': {'icon': 9.96, 'noaa': 2.04, 'sg': 9.96}}], 'meta': {'cost': 1, 'dailyQuota': 10, 'end': '2022-02-14 23:00', 'lat': 43.588, 'lng': -5.9391, 'params': ['airTemperature', 'windSpeed', 'waveDirection', 'swellPeriod', 'swellHeight', 'swellDirection'], 'requestCount': 1, 'start': '2022-02-12 23:00'}}
        
   

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
        
    from tabulate import tabulate
    #print(data)
    #print(tabulate( data , headers=["hora","airTemperature" , "windSpeed","waveDirection","swellPeriod","swellHeight","swellDirection"]  ))
    update.message.reply_text( tabulate( data , headers=["hora","Temperatura" , "Velocidad viento"]  )  )
    update.message.reply_text( tabulate( data2 , headers=["hora","Periodo oleaje" , "Altura de ola"]  )  )
    print("Al dia siguiente")
    update.message.reply_text("Al dia siguiente")
    #print(tabulate( data3 , headers=["hora","airTemperature" , "windSpeed","waveDirection","swellPeriod","swellHeight","swellDirection"]  ))
    update.message.reply_text(tabulate( data3 , headers=["hora","Temperatura" , "Velocidad viento"]  )  )
    update.message.reply_text(tabulate( data4 , headers=["hora","Periodo oleaje" , "Altura de ola"]  ) )


    

    