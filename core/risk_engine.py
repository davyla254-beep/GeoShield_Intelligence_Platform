class RiskEngine:

    def calculate_fire_risk(self, fire):

        score = 0

        # Brightness
        if fire["brightness"] >= 360:
            score += 40
        elif fire["brightness"] >= 340:
            score += 30
        else:
            score += 20

        # Fire Radiative Power
        if fire["frp"] >= 10:
            score += 30
        elif fire["frp"] >= 5:
            score += 20
        else:
            score += 10

        # Confidence
        confidence = fire["confidence"].lower()

        if confidence == "h":
            score += 30
        elif confidence == "n":
            score += 20
        else:
            score += 10

        # Severity Classification
        if score >= 90:
            severity = "Extreme"

        elif score >= 70:
            severity = "High"

        elif score >= 50:
            severity = "Moderate"

        else:
            severity = "Low"

        return {

            "risk_score": score,

            "severity": severity

        }