import datetime

import requests  # pyright: ignore[reportMissingModuleSource]


def is_today_a_public_holiday(country_code: str) -> bool:
    """
    Checks if today is a public holiday for a given country by querying an API.

    Args:
        country_code (str): The two-letter country code (e.g., "US").

    Returns:
        bool: True if today is a public holiday, False otherwise.

    Raises:
        TypeError: If country_code is not a string.
    """
    # TODO: Add a guard clause to validate that `country_code` is a string with two characters.

    if not isinstance(country_code, str):
        raise TypeError("Argument must be of Type 'String'")
    if not len(country_code) == 2:
        raise ValueError("Argument must have at least 2 characters")

    # TODO: Get today's date using the `datetime` module.

    today = datetime.date.today()

    # TODO: Make a GET request using `requests.get()`, passing the URL and params.

    api_endpoint = "https://api.example.com/v1/holidays"
    params = {
        "country": country_code,
        "year": today.year,
    }
    response = requests.get(api_endpoint, params=params)
    response.raise_for_status()

    results = response.json()

    # TODO: Return whether today is a holiday based on the results of the API.

    return any(holiday["date"] == today.isoformat() for holiday in results)
