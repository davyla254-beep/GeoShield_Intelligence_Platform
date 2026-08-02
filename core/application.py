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


class GeoShieldApplication:
    """
    Main application bootstrapper.

    Responsible for initializing the entire GeoShield platform,
    loading core services, and preparing the system for operation.
    """

    def __init__(self):
        self.project_name = PROJECT_NAME
        self.version = __version__

        self.initialized = False

        # Central service registry
        self.services = ServiceRegistry()

    def initialize(self):
        """
        Initialize the GeoShield Platform.
        """

        logger.info("Initializing GeoShield Platform...")

        # Register core services
        self.services.register("logger", logger)

        self.services.register(
            "configuration",
            {
                "project": self.project_name,
                "version": self.version,
            },
        )

        self.initialized = True

        logger.info("Platform initialization completed.")

    def status(self):
        """
        Return the current platform status.
        """

        return {
            "project": self.project_name,
            "version": self.version,
            "initialized": self.initialized,
            "registered_services": self.services.list_services(),
        }