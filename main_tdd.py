import time
import requests
import serial
from datetime import datetime


class MainLoop:
    def __init__(self):
        self.data = 'times.txt'
        self.key = "ba9dd55aba121f568d125875e463b15c"
        self.weatherSent = False
        #self.arduino = serial.Serial('COM5', 9600, timeout=.1)
        self.arduino = None

    def fetchWeatherData(self, city):
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.key}&units=metric")
        if response.status_code == 200:
            weather = (response.json()["weather"][0]['main'])
            temp = (response.json()["main"]['temp'])
            clouds = response.json()["clouds"]['all']
            weather_info = f"weather: {weather}, temperature: {temp}°C, cloudiness: {clouds}%"
            self.weatherSent = True
            return weather_info
        else:
            self.weatherSent = False

    def recieveData(self):
        line = self.arduino.readline()
        self.writeLog(line)

    def writeLog(self, state):
        if state == b'ON\n' or state == b'OFF\n':
            file = open('times.txt', 'a+')

            if state == b'ON\n':
                file.write(f'on {datetime.now().hour} {datetime.now().minute} {datetime.now().second}\n')
            else:
                file.write(f'off {datetime.now().hour} {datetime.now().minute} {datetime.now().second}\n')
            file.close()

    def start(self):
        while(True):
            weather_data = self.fetchWeatherData("Budapest")
            if weather_data != None:
                self.arduino.write(weather_data.encode())
            for i in range(100):
                self.recieveData()


if __name__ == '__main__':
    main = MainLoop()
    main.start()
