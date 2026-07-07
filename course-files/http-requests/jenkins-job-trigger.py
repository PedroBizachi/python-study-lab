import requests as req


def trigger_jenkins_job(jenkins_url: str, job_name: str, auth_token: str) -> bool:
    """
    Triggers a Jenkins job by making an authenticated POST request.

    Args:
        jenkins_url (str): The base URL of the Jenkins server.
        job_name (str): The name of the job to trigger.
        auth_token (str): The authentication token.

    Returns:
        bool: True if the job was triggered successfully (status 201), False otherwise.

    Raises:
        ValueError: If any argument is an empty or invalid string.
    """
    # TODO: Add validation to ensure all arguments are non-empty strings. Raise a ValueError if any argument is invalid.

    for arg in [jenkins_url, job_name, auth_token]:
        if not isinstance(arg, str) or not arg:  # pyright: ignore[reportUnnecessaryIsInstance]
            raise ValueError(f"Argument {arg} must have a valid type or value")

    # TODO: Send a post request using the requests library to the URL provided in the description. Make sure to include the necessary headers.

    headers = {"Authorization": f"Bearer {auth_token}"}

    try:
        res = req.post(f"{jenkins_url}/job/{job_name}/build", headers=headers)
        res.raise_for_status()

    # TODO: If a network error occurs, return False.

    except req.exceptions.RequestException:
        return False

    # TODO: Return True for a 201 response code, otherwise False.

    return True if res.status_code == 201 else False
