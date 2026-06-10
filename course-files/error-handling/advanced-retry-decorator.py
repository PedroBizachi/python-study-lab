# TODO: Define the MaxRetriesExceededError custom exception, accepting `attempts` and `last_exception` as arguments. It should also create a helpful error message to pass to the parent class.

from functools import wraps
import random
import time


class MaxRetriesExceededError(Exception):
    def __init__(self, attempts, last_exception):
        self.attempts = attempts
        self.last_exception = last_exception
        err_message = (
            f"Failed after {attempts} attempts. ",
            f"Last exception: {last_exception}",
        )
        super().__init__(err_message)


def retry_with_backoff(max_attempts, base_delay=1.0, jitter=0.1):
    """
    A decorator factory for retrying a function with validation, exponential
    backoff, jitter, and custom exceptions.
    """
    # TODO: Add validation for the factory's arguments.
    # TODO: Implement the retry logic, storing any exceptions from the decorated function for later use.
    # TODO: On success, return the result immediately.
    # TODO: On failure, store the exception in a suitable variable.
    # TODO: If the maximum attempts are exceeded, raise the appropriate exception, chaining it from the last raised exception.

    if not isinstance(max_attempts, int) or max_attempts <= 0:
        raise ValueError("max_attempts must be a positive integer")

    if not isinstance(base_delay, (int, float)) or base_delay < 0:
        raise ValueError("base_delay must be a non-negative number")

    if not isinstance(jitter, (int, float)) or jitter < 0:
        raise ValueError("jitter must be a non-negative number")

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None

            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as err:
                    last_exception = err

                    if attempt == max_attempts:
                        raise MaxRetriesExceededError(
                            max_attempts, last_exception
                        ) from last_exception

                    delay = base_delay * (2 ** (attempt - 1))
                    delay += random.uniform(0, jitter)
                    time.sleep(delay)

        return wrapper

    return decorator
