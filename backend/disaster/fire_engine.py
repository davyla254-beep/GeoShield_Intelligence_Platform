from backend.connectors.firms_connector import FIRMSConnector
from backend.spatial.data_manager import GeoDataManager

from core.event_enrichment import EventEnrichmentEngine
from core.risk_engine import RiskEngine
from core.decision_engine import DecisionEngine


class FireIntelligenceEngine:

    def __init__(self):

        self.connector = FIRMSConnector()

        self.data_manager = GeoDataManager()

        self.data_manager.load_layer(
            "counties",
            "data/boundaries/Kenya_county.shp"
        )

        self.data_manager.load_layer(
            "roads",
            "data/roads/ken_roads.shp"
        )

        self.enrichment = EventEnrichmentEngine(
            self.data_manager
        )

        self.risk = RiskEngine()

        self.decision = DecisionEngine()

    def analyse(self, filepath):

        self.connector.load_csv(filepath)

        enriched = []

        for fire in self.connector.get_disasters():

            location = self.enrichment.enrich(
                fire["longitude"],
                fire["latitude"]
            )

            risk = self.risk.calculate_fire_risk(fire)

            decision = self.decision.recommend(risk)

            enriched.append({

                **fire,

                **location,

                **risk,

                **decision

            })

        return enriched