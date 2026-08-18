import random
import time


class EVSensorSimulator:

    def __init__(self):
        self.battery = 100.0
        self.distance = 0.0
        self.scenario = 0
        self.scenario_count = 0

    def update(self):

        # Change scenario every 10 readings
        if self.scenario_count >= 10:
            self.scenario_count = 0
            self.scenario = (self.scenario + 1) % 6

        self.scenario_count += 1

        # Default normal values
        speed = random.uniform(30, 55)
        voltage = random.uniform(380, 420)
        motor_temperature = random.uniform(35, 48)
        obstacle_distance = random.uniform(40, 100)

        # --------------------------------
        # ADAS DEMONSTRATION SCENARIOS
        # --------------------------------

        if self.scenario == 0:
            # NORMAL
            speed = random.uniform(30, 55)
            motor_temperature = random.uniform(35, 48)
            obstacle_distance = random.uniform(40, 100)

        elif self.scenario == 1:
            # HIGH SPEED
            speed = random.uniform(75, 90)
            motor_temperature = random.uniform(35, 48)
            obstacle_distance = random.uniform(40, 100)

        elif self.scenario == 2:
            # LOW BATTERY
            speed = random.uniform(30, 55)
            motor_temperature = random.uniform(35, 48)
            obstacle_distance = random.uniform(40, 100)

            self.battery = 15.0

        elif self.scenario == 3:
            # MOTOR OVERHEATING
            speed = random.uniform(30, 55)
            motor_temperature = random.uniform(56, 65)
            obstacle_distance = random.uniform(40, 100)

        elif self.scenario == 4:
            # COLLISION WARNING
            speed = random.uniform(30, 55)
            motor_temperature = random.uniform(35, 48)
            obstacle_distance = random.uniform(6, 9)

        elif self.scenario == 5:
            # CRITICAL COLLISION
            speed = random.uniform(30, 55)
            motor_temperature = random.uniform(35, 48)
            obstacle_distance = random.uniform(2, 4)

        # Battery decreases slowly during normal operation
        if self.scenario != 2:
            self.battery = max(
                0,
                self.battery - random.uniform(0.01, 0.05)
            )

        # Reset battery after completing demonstration cycle
        if self.scenario == 0 and self.scenario_count == 1:
            if self.battery < 50:
                self.battery = 100.0

        # Vehicle travel distance
        self.distance += speed / 3600

        return {
            "battery": round(self.battery, 2),
            "speed": round(speed, 2),
            "voltage": round(voltage, 2),
            "temperature": round(motor_temperature, 2),
            "distance": round(self.distance, 2),
            "obstacle_distance": round(obstacle_distance, 2)
        }


if __name__ == "__main__":

    sensor = EVSensorSimulator()

    while True:

        data = sensor.update()

        print("--------------------------------")
        print("      ELECTRIC VEHICLE DATA")
        print("--------------------------------")
        print(f"🔋 Battery          : {data['battery']} %")
        print(f"🚗 Speed            : {data['speed']} km/h")
        print(f"⚡ Voltage          : {data['voltage']} V")
        print(f"🌡️ Temperature      : {data['temperature']} °C")
        print(f"📍 Travel Distance  : {data['distance']} km")
        print(f"🚨 Obstacle Distance: {data['obstacle_distance']} m")
        print("--------------------------------")

        time.sleep(1)
