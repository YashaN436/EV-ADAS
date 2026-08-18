class ADASEngine:

    def check(self, data):

        speed = data["speed"]
        battery = data["battery"]
        temperature = data["temperature"]

        # Distance to vehicle in front
        obstacle_distance = data.get("obstacle_distance", 100)

        warnings = []

        # High speed warning
        if speed > 70:
            warnings.append("HIGH SPEED")

        # Low battery warning
        if battery < 20:
            warnings.append("LOW BATTERY")

        # Motor overheating warning
        if temperature > 55:
            warnings.append("MOTOR OVERHEATING")

        # Front collision warning
        if obstacle_distance < 10:
            warnings.append("COLLISION WARNING")

        # Risk calculation
        if temperature > 65 or obstacle_distance <= 5:
            risk = "CRITICAL"

        elif len(warnings) > 0:
            risk = "WARNING"

        else:
            risk = "SAFE"

        # Overall status
        if len(warnings) == 0:
            status = "SYSTEM SAFE"
        else:
            status = " | ".join(warnings)

        return {
            "status": status,
            "warnings": warnings,
            "risk": risk
        }
