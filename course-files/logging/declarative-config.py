import logging
import logging.config
import json

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

"""
# Uncomment to test Dictionary configuration

# Declarative logging configuration - Dictionary config

print("\nDeclarative configuration using dictionary config")
print("-----------------------\n")

dict_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {"simple": {"format": "%(levelname)-8s - %(message)s"}},
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "simple",
            "stream": "ext://sys.stdout",
        }
    },
    "loggers": {
        "config.dict": {
            "level": "DEBUG",
            "handlers": ["console"],
        }
    },
}

logging.config.dictConfig(dict_config)
config_logger = logging.getLogger("config.dict")
config_logger.debug("dictConfig setup successfully")
config_logger.info("Info goes to console")
"""
# Declarative logging configuration - JSON config

print("\nDeclarative logging configuration - JSON config")
print("-----------------------\n")

config_path = "declarative-config.json"

with open(config_path, "r") as config_file:
    json_config = json.load(config_file)

logging.config.dictConfig(json_config)
config_logger = logging.getLogger("config.json")
config_logger.debug("JSON config setup successfully")
config_logger.info("Info goes to console")

# Dynamically building config
