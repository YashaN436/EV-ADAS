class ADASEngine:

    def check(self, data):

        speed = data["speed"]
        battery = data["battery"]
        temperature = data["temperature"]
        distance = data.get("distance", 100)

        warnings = []

        if speed > 70:
            warnings.append("HIGH SPEED")

        if battery < 20:
            warnings.append("LOW BATTERY")

        if temperature > 55:
            warnings.append("MOTOR OVERHEATING")

        if distance < 10:
            warnings.append("COLLISION WARNING")

        if temperature > 65 or distance < 5:
            risk = "CRITICAL"
        elif len(warnings) > 0:
            risk = "WARNING"
        else:
            risk = "SAFE"

        if len(warnings) == 0:
            status = "SYSTEM SAFE"
        else:
            status = " | ".join(warnings)

        return {
            "status": status,
            "warnings": warnings,
            "risk": risk
        }
