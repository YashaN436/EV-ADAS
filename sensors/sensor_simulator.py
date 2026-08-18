import random
import time


class EVSensorSimulator:

    def __init__(self):
        self.battery = 100.0
        self.distance = 0.0

    def update(self):

        speed = random.uniform(20, 80)
        voltage = random.uniform(360, 420)
        motor_temperature = random.uniform(35, 60)

        self.battery -= random.uniform(0.01, 0.05)
        self.distance += speed / 3600

        return {
            "battery": round(self.battery, 2),
            "speed": round(speed, 2),
            "voltage": round(voltage, 2),
            "temperature": round(motor_temperature, 2),
            "distance": round(self.distance, 2)
        }


if __name__ == "__main__":

    sensor = EVSensorSimulator()

    while True:

        data = sensor.update()

        print("--------------------------------")
        print("      ELECTRIC VEHICLE DATA")
        print("--------------------------------")
        print(f"🔋 Battery      : {data['battery']} %")
        print(f"🚗 Speed        : {data['speed']} km/h")
        print(f"⚡ Voltage      : {data['voltage']} V")
        print(f"🌡️ Temperature  : {data['temperature']} °C")
        print(f"📍 Distance     : {data['distance']} km")
        print("--------------------------------")

        time.sleep(1)
