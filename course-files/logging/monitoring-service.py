import logging
import logging.handlers


def configure_rotating_logger(
    logger_name: str, log_filepath: str, max_size_bytes: int, backup_count: int
) -> logging.Logger:
    """Sets up a logger that writes to a file and automatically rotates when it reaches a certain size.

    Args:
        logger_name (str): The name for the logger.
        log_filepath (str): The path to the log file.
        max_size_bytes (int): The maximum size of the log file in bytes before it rotates.
        backup_count (int): The number of old log files to keep.

    Returns:
        Logger (obj): Fully configured logger object.
    """

    for val in [logger_name, log_filepath]:
        if not isinstance(val, str):
            raise TypeError("'logger_name' or 'log_filepath' must be a String type")
        elif not val:
            raise ValueError("'logger_name' or 'log_filepath' must have a value")

    for val in [max_size_bytes, backup_count]:
        if not isinstance(val, int):
            raise TypeError("'max_size_bytes' or 'backup_count' must be a Integer type")

    if not max_size_bytes > 0:
        raise ValueError("'max_size_bytes' must be greater than zero")
    elif not backup_count >= 0:
        raise ValueError("'backup_count' must be a non-negative integer")

    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)

    logger_rfh = logging.handlers.RotatingFileHandler(
        log_filepath, maxBytes=max_size_bytes, backupCount=backup_count
    )
    logger.addHandler(logger_rfh)

    return logger
