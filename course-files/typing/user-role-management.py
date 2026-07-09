from typing import Optional, Any

# TODO: Add the correct type hints to this function signature.
# Use modern, built-in generic types (`list`, `dict`, etc.).
# - `users` is a list of dictionaries. Each dictionary has string keys and
#   values of any type.
# - `default_role` is an optional string.
# - The function returns a dictionary where keys are strings and values are
#   lists of strings.
def assign_default_role(users, default_role = None):
    """
    Assigns a default role to users who have none and returns a role map.
    """
    user_roles: dict[str, list[str]] = {}
    for user in users:
        user_id = user.get("id")
        roles = user.get("roles", [])

        if not roles and default_role:
            roles.append(default_role)
        
        if user_id:
            user_roles[user_id] = roles
            
    return user_roles
