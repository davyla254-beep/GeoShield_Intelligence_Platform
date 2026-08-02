class DecisionEngine:

    def __init__(self):
        pass

    def recommend(self, event):

        severity = event["severity"]

        actions = []

        if severity == "Low":

            actions = [

                "Monitor situation",

                "Log event"

            ]

        elif severity == "Moderate":

            actions = [

                "Notify County Disaster Office",

                "Notify Fire Department",

                "Increase Monitoring"

            ]

        elif severity == "High":

            actions = [

                "Dispatch Fire Brigade",

                "Notify NDMA",

                "Notify Police",

                "Prepare Evacuation Teams"

            ]

        elif severity == "Extreme":

            actions = [

                "Dispatch Fire Brigade Immediately",

                "Notify National Disaster Operations Centre",

                "Deploy Aerial Surveillance",

                "Issue Public Warning",

                "Prepare Medical Response",

                "Prepare Evacuation"

            ]

        return {

            "recommended_actions": actions

        }