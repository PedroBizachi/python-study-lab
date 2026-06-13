from pathlib import Path
from typing import Union
from datetime import datetime


def archive_log_files(log_directory: Union[str, Path], archive_date: str) -> list[Path]:
    """
    Finds and renames all .log files in a directory with a date stamp.

    Args:
        log_directory (Union[str, Path]): The directory to scan.
        archive_date (str): The date stamp to use for renaming (YYYY-MM-DD).

    Returns:
        list[Path]: A list of the new Path objects for the renamed files.

    Raises:
        TypeError: If an argument has an invalid type.
        ValueError: If an argument has an invalid value or format.
    """
    # TODO: Implement input validation first.
    # TODO: Rename .log files following instructions.
    # TODO: Return a list of renamed files.

    result = []

    if not isinstance(log_directory, (str, Path)):
        raise TypeError(
            "'log_directory' must be of type 'String' or a pathlib.Path object"
        )
    elif not isinstance(archive_date, str):
        raise TypeError("'archive_date' must be of type 'String'")

    log_directory = Path(log_directory)

    if not log_directory.is_dir():
        raise ValueError("'log_directory' must be a directory")

    if not log_directory.exists():
        raise ValueError("'log_directory' does not exist")

    try:
        datetime.strptime(archive_date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("'archive_date' must be in YYYY-MM-DD format")

    for log in log_directory.glob("*.log"):
        new_name = log.with_name(f"{log.stem}-{archive_date}{log.suffix}")
        result.append(log.rename(new_name))

    return result
