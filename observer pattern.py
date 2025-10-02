# Observer Pattern demo: Weather Station
class Observer:
    def update(self, temp):
        pass

class PhoneDisplay(Observer):
    def update(self, temp):
        print(f"[Phone] Weather updated: {temp}°C")

class WeatherStation:
    def __init__(self):
        self._observers = []
        self._temp = 0

    def register(self, obs: Observer):
        self._observers.append(obs)

    def set_temp(self, temp):
        self._temp = temp
        for o in self._observers:
            o.update(temp)

if __name__ == "__main__":
    station = WeatherStation()
    station.register(PhoneDisplay())
    station.set_temp(30)
