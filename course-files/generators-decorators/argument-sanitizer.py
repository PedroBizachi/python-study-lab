from functools import wraps


def sanitize_hostname(func):
    """
    A decorator that finds a 'hostname' keyword argument, sanitizes it
    (lowercase, stripped whitespace), and passes it to the wrapped function.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        hostname = kwargs.get("hostname")

        if hostname is not None:
            kwargs["hostname"] = hostname.lower().strip()

        return func(*args, **kwargs)

    return wrapper
