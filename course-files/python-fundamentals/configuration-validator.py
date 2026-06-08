def validate_config(config: dict) -> bool:
    """
    Validates a configuration dictionary against a set of rules.

    A valid configuration must have:
    - Required keys: 'service_name', 'env', 'port'.
    - 'env' must be one of 'dev', 'staging', 'prod'.
    - 'service_name' must be a non-empty string.
    - 'port' must be an integer between 1 and 65535.

    Args:
        config: A dictionary containing configuration parameters.

    Returns:
        True if the configuration is valid, False otherwise.
    """
    # TODO: Implement the validation logic here.
    # 1. Check if all required keys exist.
    # 2. Check if the 'env' value is one of the allowed environments.
    # 3. Check if 'service_name' is a non-empty string.
    # 4. Check if 'port' is an integer and within the valid range.
    # Remember to return False as soon as a check fails.
    # If all checks pass, return True at the end.

    required_keys = ["service_name", "env", "port"]
    envs = ["dev", "staging", "prod"]

    if not set(required_keys).issubset(config):
        print("False")
        return False

    if config["env"] not in envs:
        print("False")
        return False

    if not isinstance(config["service_name"], str) or not config["service_name"]:
        print("False")
        return False

    if not isinstance(config["port"], int) or not 1 <= config["port"] <= 65535:
        print("False")
        return False

    print("True")
    return True


validate_config({"service_name": "auth-service", "env": "prod", "port": 8080})
validate_config({"service_name": "auth-service", "env": "production", "port": 8080})
