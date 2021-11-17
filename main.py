import time
import requests
import serial
import datetime as datetime

if __name__ == '__main__':
    arduino = serial.Serial('COM5', 9600, timeout=.1)
    while(True):
        key = "ba9dd55aba121f568d125875e463b15c"
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q=Budapest&appid={key}&units=metric")
        if response.status_code == 200:
            weather = (response.json()["weather"][0]['main'])
            temp = (response.json()["main"]['temp'])
            clouds = response.json()["clouds"]['all']
            weather_info = f"weather: {weather}, temperature: {temp}°C, cloudiness: {clouds}%"
            arduino.write("weather_info".encode())
        for i in range(100):
            line = arduino.readlines()
            if line == 'on' or line == 'off':
                data = open('times.txt', 'at')
                if line == 'on':
                    data.write(f'on {datetime.now().hour} {datetime.now().minute} {datetime.now().second}')
                else:
                    data.write(f'off {datetime.now().hour} {datetime.now().minute} {datetime.now().second}')
                data.close()
                time.sleep(0.1)
