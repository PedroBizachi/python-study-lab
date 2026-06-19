import subprocess


def check_host_status(hostname: str) -> str:
    """
    Checks if a host is online by pinging it a limited number of times.

    Args:
        hostname (str): The hostname or IP address to ping.

    Returns:
        'online' if the host is reachable (ping exit code 0), 'offline' otherwise.

    Raises:
        TypeError: If hostname is not a string.
        ValueError: If hostname is not a non-empty string.
    """
    # TODO: Input validation
    # TODO: Construct and run the ping command. Make sure that subprocess does not raise an exception on non-zero exit codes.
    # TODO: Handle relevant exceptions.
    # TODO: Return "online" or "offline" according to the exercise description.

    if not isinstance(hostname, str):
        raise TypeError("'hostname' must be of type String")
    elif not hostname:
        raise ValueError("Must provide a valid value for 'hostname")

    cmd = ['ping', hostname, '-c', 3]

    try:
        result = subprocess.run(cmd, timeout=5, capture_output=True, check=True, text=True)
        return 'online' if result.returncode == 0 else 'offline'
    except subprocess.TimeoutExpired:
        return 'offline'
