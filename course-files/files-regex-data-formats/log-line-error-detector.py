import re


def has_critical_error(log_line: str) -> bool:
    """
    Checks if a log line contains a critical error indicator ('ERROR:' or 'FAIL:').
    The check is case-insensitive.

    Args:
        log_line (str): The log line to check.

    Returns:
        bool: True if a critical error indicator is found, False otherwise.
    """
    # TODO: Define a regular expression pattern that matches either the literal string "ERROR:" or "FAIL:".

    # TODO: Look for the pattern in the `log_line` and return a boolean indicating whether it was found.

    pattern = re.compile(r"(ERROR|FAIL):", re.IGNORECASE)

    return bool(re.search(pattern, log_line))
