class ADASEngine:

    def check(self, data):

        speed = data["speed"]
        battery = data["battery"]
        temperature = data["temperature"]
        distance = data.get("distance", 100)
        warnings = []

        # -----------------------------
        # HIGH SPEED
        # -----------------------------
        if speed > 70:
            warnings.append("HIGH SPEED")

        # -----------------------------
        # LOW BATTERY
        # -----------------------------
        if battery < 20:
            warnings.append("LOW BATTERY")

        # -----------------------------
        # MOTOR OVERHEATING
        # -----------------------------
        if temperature > 55:
            warnings.append("MOTOR OVERHEATING")

        # -----------------------------
        # COLLISION WARNING
        # -----------------------------
        if distance < 10:
            warnings.append("COLLISION WARNING")

        # -----------------------------
        # DETERMINE RISK LEVEL
        # -----------------------------
        if distance < 5 or temperature > 65:
            risk = "CRITICAL"

        elif len(warnings) >= 2:
            risk = "DANGER"

        elif len(warnings) == 1:
            risk = "WARNING"

        else:
            risk = "SAFE"

        # -----------------------------
        # OVERALL STATUS
        # -----------------------------
        if len(warnings) == 0:

            status = "SYSTEM SAFE"

        else:

            status = " | ".join(warnings)

        # -----------------------------
        # RETURN ADAS RESULT
        # -----------------------------
        return {
            "status": status,
            "warnings": warnings,
            "risk": risk
        }
