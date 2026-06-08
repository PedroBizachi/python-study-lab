def manage_tags(existing_tags: dict, *simple_tags, **key_value_tags) -> dict:
    """
    Applies simple and key-value tags to an existing dictionary of tags.

    Args:
        existing_tags: The initial dictionary of tags.
        *simple_tags: Positional string arguments to be added as tags with a
                      value of 'true'. Duplicates should be ignored.
        **key_value_tags: Keyword arguments to be added or used to overwrite
                          existing tags.

    Returns:
        A new dictionary with all tags merged.
    """
    # TODO: Implement the tagging logic.
    # 1. Do not modify the original dictionary
    # 2. Process the 'simple_tags' (*args).
    # 3. Process the 'key_value_tags' (**kwargs).
    # 4. Return the new, merged dictionary.

    new_dict = existing_tags.copy()

    for tag in simple_tags:
        new_dict[tag] = "true"

    for k, v in key_value_tags.items():
        new_dict[k] = v

    return new_dict
