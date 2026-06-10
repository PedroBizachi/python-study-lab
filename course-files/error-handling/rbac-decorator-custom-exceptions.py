import functools

# TODO: Define the AuthorizationError custom exception.
# It should inherit from Exception.
# Its __init__ method should accept `user_name` and `required_role`.
# It should store these as attributes and create a descriptive error message to pass to the parent class's __init__.


class AuthorizationError(Exception):
    def __init__(self, user_name, required_role) -> None:
        self.user_name = user_name
        self.required_role = required_role
        error_message = f"User '{user_name}' lacks the required role: '{required_role}'"
        super().__init__(error_message)


def require_role(required_role):
    """
    A decorator factory that creates a decorator to check for a specific user role, with robust validation and custom exceptions.
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # This is the solution from our previous exercise.
            # You will modify it.
            # Start with this known-good implementation.

            if not kwargs.get("user"):
                raise ValueError("A 'user' keyword argument is required")

            user = kwargs.get("user")

            if (
                not isinstance(user, dict)
                or "roles" not in user
                or not isinstance(user["roles"], list)
            ):
                raise ValueError("Wrong value for 'user'")

            user_roles = user.get("roles", [])

            if required_role not in user_roles:
                raise AuthorizationError(user["name"], required_role)
            return func(*args, **kwargs)

            # TODO: Check if the 'user' keyword argument exists in kwargs and raise a ValueError if not.
            # TODO: Raise a ValueError if the user keyword argument is not a dict, is missing a 'roles' key, or if 'roles' is not a list.
            # TODO: Modify the permission check to raise an AuthorizationError instead of PermissionError.

        return wrapper

    return decorator
