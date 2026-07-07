import requests as req


def get_incident_summary(
    api_url: str, api_key: str, service_id: str
) -> list[str] | None:
    """
    Fetches open incidents for a specific service and formats them into a list
    of summary strings.

    Args:
        api_url (str): The base URL of the API.
        api_key (str): The API key for authentication.
        service_id (str): The ID of the service to query.

    Returns:
        A list of formatted incident summary strings on success, or None on an HTTP error.

    Raises:
        ValueError: If any argument is an empty or invalid string.
    """
    # TODO: Add validation to ensure all arguments are non-empty strings.

    if not all(
        isinstance(arg, str) for arg in [api_url, api_key, service_id]
    ) or not all([api_url, api_key, service_id]):
        raise ValueError("Arguments must be a valid non-empty string.")

    # TODO: Prepare the request components (URL, headers, params).

    url = f"{api_url}/incidents"
    headers = {"Authentication": f"Bearer {api_key}"}
    query_params = {"service_ids": service_id, "statuses": ["triggered"]}

    # TODO: Make the GET request using the requests library, and build the list of parsed incidents.

    try:
        res = req.get(url, params=query_params, headers=headers)
        res.raise_for_status()

        data = res.json().get("incidents", [])  # pyright: ignore[reportAny]

        result = [
            f"[{i.get('urgency', 'N/A').upper()}] {i.get('id', 'N/A')}: {i.get('title', 'No Title')}"
            for i in data
        ]

        # TODO: Return the new list of summary strings.

        return result

    # TODO: Inside the `except` block, return `None`.

    except req.exceptions.HTTPError:
        return None
