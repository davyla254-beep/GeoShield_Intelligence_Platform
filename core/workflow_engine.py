from core.event_enrichment import EventEnrichmentEngine
from core.risk_engine import RiskEngine
from core.decision_engine import DecisionEngine


class WorkflowEngine:

    def __init__(self, data_manager):

        self.enrichment = EventEnrichmentEngine(data_manager)
        self.risk = RiskEngine()
        self.decision = DecisionEngine()

    def process(self, event):

        # STEP 1
        location = self.enrichment.enrich(
            event["longitude"],
            event["latitude"]
        )

        # STEP 2
        event.update(location)

        # STEP 3
        risk = self.risk.calculate_fire_risk(event)

        event.update(risk)

        # STEP 4
        decision = self.decision.recommend(event)

        event.update(decision)

        return event