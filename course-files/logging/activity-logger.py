import logging
import sys


def setup_script_logger(logger_name: str):
    """
    Configures and returns a logger for script activity monitoring.

    Args:
        logger_name (str): The name for the logger.

    Returns:
        logging.Logger: A configured logger instance.
    """

    if not isinstance(logger_name, str):
        raise TypeError("Name must be of type 'String'")

    if not logger_name:
        raise ValueError("Name must have a value")

    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)

    logger_sh = logging.StreamHandler(sys.stdout)
    logger_formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
    )
    logger_sh.setFormatter(logger_formatter)

    logger.addHandler(logger_sh)

    return logger
