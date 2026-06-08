def parse_log_line(log_line: str) -> dict | None:
    """
    Parses a single log line into a structured dictionary.

    The expected log format is: "TIMESTAMP [LOG_LEVEL] MESSAGE"
    Example: "2024-05-20T13:45:10Z [INFO] User 'alice' logged in successfully."

    Args:
        log_line: A string representing a single line from a log file.

    Returns:
        A dictionary containing the 'timestamp', 'log_level', and 'message'
        if the log line is valid, otherwise None.
    """
    # TODO: Implement the parsing logic here.
    # 1. Check if the log_line is valid. If not, return None.
    # 2. Split the line into its constituent parts: timestamp, log_level, and message.
    #    Remember that the message itself can contain spaces.
    # 3. Clean up the log_level to remove the square brackets.
    # 4. Create and return a dictionary with the extracted parts.

    if (
        not isinstance(log_line, str)
        or not log_line
    ):
        return None

    parsed_logline = log_line.split(" ", 2)

    if (
        len(parsed_logline) < 3
        or not parsed_logline[1].startswith("[")
        and not parsed_logline[1].endswith("]")
    ):
        return None

    return {
        "timestamp": f"{parsed_logline[0]}",
        "log_level": f"{parsed_logline[1].strip('[]').upper()}",
        "message": f"{parsed_logline[2]}",
    }
