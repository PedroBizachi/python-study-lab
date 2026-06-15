import json
from pathlib import Path


def update_image_tag(config_path: str | Path, service_name: str, new_tag: str) -> None:
    """
    Reads a JSON config file, updates a service's image tag, and writes it back.
    """
    # TODO: Implement input validation.

    if not isinstance(config_path, (str, Path)):
        raise TypeError("Must provide a properly file path.")

    config_path = Path(config_path)

    if not config_path.is_file():
        raise FileNotFoundError("Can't find the provided file.")

    for val in [service_name, new_tag]:
        if not isinstance(val, str):
            raise TypeError(f"'{val}' must be of type String")
        elif not val:
            raise ValueError(f"'{val}' must have a valid value")

    # TODO: Read, update, and save updated JSON object.
    # Remember to use an indent of 4 for human-readable output.

    with config_path.open(mode="r", encoding="utf-8") as file:
        config_data = json.load(file)

    if not config_data["services"][service_name]:
        raise KeyError("'service_name' not found")

    config_data["services"][service_name]["image_tag"] = new_tag

    with config_path.open(mode="w", encoding="utf-8") as file:
        json.dump(config_data, file, indent=4)
