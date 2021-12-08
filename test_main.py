from unittest import TestCase

from main import MainLoop


class TestMainLoop(TestCase):
    def setUp(self):
        self.mainLoop = MainLoop()

#class TestInit(TestMainLoop):


class TestWriteLog(TestMainLoop):
    def test_write_log_invalid(self):
        self.mainLoop.writeLog("alma")
        file = open('times.txt', 'r+')
        self.assertEqual(sum(1 for line in file), 0)
        file.close()

    def test_write_log_off(self):
        self.mainLoop.writeLog(b"OFF\n")
        file = open('times.txt', 'r')
        self.assertEqual(sum(1 for line in file), 1)
        file.close()


    def test_write_log_on(self):
        self.mainLoop.writeLog(b"ON\n")
        file = open('times.txt', 'r')
        self.assertEqual(sum(1 for line in file), 2)
        file.close()

class TestFetchWeatherData(TestMainLoop):
    def test_weather_budapest(self):
        self.mainLoop.fetchWeatherData("error")
        self.assertEqual(self.mainLoop.weatherSent, False)

    def test_weather_error(self):
        self.mainLoop.fetchWeatherData("Budapest")
        self.assertEqual(self.mainLoop.weatherSent, True)
        