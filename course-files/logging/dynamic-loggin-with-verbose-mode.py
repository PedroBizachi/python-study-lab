import logging.config


def configure_logging(verbose: bool):
    """
    Configures logging dynamically based on a verbose flag.

    Args:
        verbose (bool): If True, sets the root logger level to DEBUG.
                        Otherwise, the level remains INFO.

    Returns:
        logging.Logger: The configured root logger instance.

    Raises:
        TypeError: If verbose is not a boolean.
    """
    # TODO: Implement input validation.
    # TODO: Implement base logging config dictionary.
    # TODO: Modify the config dictionary based on the verbose parameter value.
    # TODO: Apply the configuration to the logging library.
    # TODO: Return the configured root logger instance.

    if not isinstance(verbose, bool):
        raise TypeError("Argument must be of type 'Boolean'")

    base_config = {
        "version": 1,
        "disable_existing_loggers": True,
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "simple",
                "stream": "ext://sys.stdout",
            }
        },
        "formatters": {"simple": {"format": "%(levelname)s: %(message)s"}},
        "root": {"level": "INFO", "handlers": ["console"]},
    }

    if verbose:
        base_config["root"]["level"] = "DEBUG"

    logging.config.dictConfig(base_config)
    return logging.getLogger()
