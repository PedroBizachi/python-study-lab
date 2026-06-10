from functools import wraps


def require_role(required_role):
    """
    A decorator factory that creates a decorator to check for a specific user role.

    Args:
        required_role (str): The role string that the user must have.

    Returns:
        A decorator function.
    """

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            user = kwargs.get("user")

            if user is None:
                raise PermissionError("User is required")

            roles = user.get("roles", [])

            if required_role not in roles:
                raise PermissionError("User does not have required role")

            return func(*args, **kwargs)

        return wrapper

    return decorator
