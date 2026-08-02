"""
GeoShield Intelligence Platform
Enterprise Application Factory

Author:
David Omondi Ouma
Founder & Chief Executive Officer (CEO)
"""

from core.logger import logger
from core.metadata import PROJECT_NAME
from core.version import __version__
from core.service_registry import ServiceRegistry
from core.engine_registry import EngineRegistry


class GeoShieldApplication:

    def __init__(self):

        self.project_name = PROJECT_NAME
        self.version = __version__

        self.initialized = False

        self.services = ServiceRegistry()
        self.engines = EngineRegistry()

    def initialize(self):

        logger.info("Initializing GeoShield Platform...")

        self.services.register("logger", logger)

        self.services.register(
            "configuration",
            {
                "project": self.project_name,
                "version": self.version,
            },
        )

        logger.info("Loading Engine Registry...")

        self.initialized = True

        logger.info("Platform initialization completed.")

    def status(self):

        return {
            "project": self.project_name,
            "version": self.version,
            "initialized": self.initialized,
            "registered_services": self.services.list_services(),
            "registered_engines": self.engines.list_engines(),
        }