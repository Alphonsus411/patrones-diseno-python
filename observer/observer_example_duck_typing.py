

class TV:
    def __init__(self):
        self._temperature = None
        self._humidity = None
        self._pressure = None

    def update(self, temperature, humidity, pressure):
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure
        self.display()

    def display(self):
        print(
            f"Current conditions: "
            f"{self._temperature}F degrees, "
            f"humidity: {self._humidity}%, "
            f"pressure: {self._pressure}"
        )


class WeatherStation:
    def __init__(self):
        self._temperature = None
        self._humidity = None
        self._pressure = None
        self._observers = []

    def register_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(
                self._temperature,
                self._humidity,
                self._pressure
            )

    def set_measurements(self, temperature, humidity, pressure):
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure
        self.measurements_changed()

    def measurements_changed(self):
        self.notify_observers()


weather_station = WeatherStation()
current_display = TV()

weather_station.register_observer(current_display)

weather_station.set_measurements(80, 65, 30.4)
weather_station.set_measurements(82, 70, 29.2)
weather_station.set_measurements(78, 90, 29.2)