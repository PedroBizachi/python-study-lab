import logging
import logging.config
"""
# Uncomment to test INI configuration

# Declarative logging configuration - INI-file

print("\nDeclarative logging configuration - INI-file")
print("-----------------------\n")

config_path = "declarative-config.ini"

logging.config.fileConfig(
    fname=config_path,
)

app_logger = logging.getLogger("app")

app_logger.debug("INI-style fileConfig is working!")
"""

# Declarative logging configuration - Dictionary config

# Declarative logging configuration - JSON config

# Dynamically building config
