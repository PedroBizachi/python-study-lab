import re


def redact_sensitive_data(content: str) -> str:
    """
    Finds and redacts sensitive values (api_key, password, secret) in a string.

    Args:
        content (str): The string content to be sanitized.

    Returns:
        str: The content with sensitive values replaced by '[REDACTED]'.

    Raises:
        TypeError: If content is not a string.
    """
    # TODO: Input validation.

    if not isinstance(content, str):
        raise TypeError("Argument must be of type String")

    # TODO: Define a regex that matches the sensitive key-value pairs, as specified in the exercise description.

    pattern = re.compile(
        r"(api_key|password|secret)(\s*[=:]\s*)(.*)", re.MULTILINE | re.IGNORECASE
    )

    # TODO: Define an apply a replacement string.

    redacted = r"\1\2[REDACTED]"

    # TODO: Return the redacted content.

    return pattern.sub(redacted, content)
