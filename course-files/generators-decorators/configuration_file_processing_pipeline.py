def read_config_file(filepath):
    """
    Validates the filepath and yields each line from the file.

    Args:
        filepath (str): The path to the configuration file.

    Yields:
        str: A single line from the file.
    """
    with open(filepath) as file:
        for line in file:
            yield line


def filter_config_lines(lines):
    """
    Filters an iterable of lines, yielding stripped, non-empty, non-comment lines.

    Args:
        lines (iterable): An iterable producing string lines.

    Yields:
        str: A line that is not a comment or empty.
    """
    for line in lines:
        line = line.strip()
        if line and not line.startswith("#"):
            yield line


def parse_config_lines(lines):
    """
    Parses an iterable of clean config lines into (section, key, value) tuples.

    Args:
        lines (iterable): An iterable producing clean config lines.

    Yields:
        tuple: A tuple in the format (section, key, value).
    """
    curr_section = None
    for line in lines:
        if line.startswith("[") and line.endswith("]"):
            curr_section = line[1:-1].strip()
        else:
            key, value = line.split("=", 1)
            yield (curr_section, key.strip(), value.strip())
