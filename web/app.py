from flask import Flask, render_template, jsonify

from sensors.sensor_simulator import EVSensorSimulator
from adas.adas_engine import ADASEngine


app = Flask(__name__)

# Create sensor simulator
sensor = EVSensorSimulator()

# Create ADAS engine
adas = ADASEngine()


@app.route("/")
def dashboard():

    return render_template("index.html")


@app.route("/sensor-data")
def sensor_data():

    # Get live EV sensor data
    data = sensor.update()

    # Run ADAS analysis
    adas_result = adas.check(data)

    # Add ADAS result to sensor data
    data["adas_status"] = adas_result["status"]
    data["warnings"] = adas_result["warnings"]
    data["risk"] = adas_result["risk"]
    return jsonify(data)


if __name__ == "__main__":

    app.run(debug=True)
