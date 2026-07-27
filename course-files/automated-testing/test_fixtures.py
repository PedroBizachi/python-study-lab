# Section: Defining a Simple Fixture with @pytest.fixture

import tempfile
from pathlib import Path
from typing import Iterator

import pytest

from conftest import ManagedResource

ConfigDict = dict[str, str | int]


@pytest.fixture
def sample_config_dict() -> ConfigDict:
    return {
        "api_url": "https://test.api.example.com",
        "timeout": 30,
        "Retries": 3,
    }


def test_api_url_is_present(sample_config_dict: ConfigDict):
    print("  [TEST]: test_api_url_is_present running...")
    assert "api_url" in sample_config_dict
    assert sample_config_dict["api_url"] == "https://test.api.example.com"


@pytest.fixture
def temp_config_file() -> Iterator[Path]:
    temp_file = tempfile.NamedTemporaryFile(mode="w+t", suffix=".yaml", delete=False)
    temp_file_path = Path(temp_file.name)
    print(f"  [FIXTURE SETUP]: temp_config_file created at {temp_file_path}")
    temp_file.write("setting1: value1\nsetting2: value2\n")
    temp_file.close()
    yield temp_file_path
    print(f"  [FIXTURE TEARDOWN]: temp_config_file deleted at {temp_file_path}")
    if temp_file_path.exists():
        temp_file_path.unlink()


def test_read_from_temp_file(temp_config_file: Path):
    print("  [TEST]: test_read_from_temp_file running...")
    assert temp_config_file.exists()
    content = temp_config_file.read_text(encoding="utf-8")
    assert "setting1: value1" in content


# Section: Using Fixtures in Test Functions


@pytest.fixture(scope="session")
def expensive_resource() -> Iterator[ConfigDict]:
    print("\n  [SESSION FIXTURE]: expensive_resource - creating...")
    yield {"id": "session-resource", "value": 123}
    print("\n  [SESSION FIXTURE]: expensive_resource - deleting...")


def test_expensive_resource_id(expensive_resource: ConfigDict):
    print("\n  [TEST]: test_expensive_resource_id running...")
    assert expensive_resource["id"] == "session-resource"


def test_expensive_resource_value(expensive_resource: ConfigDict):
    print("\n  [TEST]: test_expensive_resource_value running...")
    assert expensive_resource["value"] == 123


# Section: Sharing Fixtures with conftest.py


def test_managed_resource_status(managed_resource: ManagedResource):
    assert managed_resource["status"] == "lock_acquired"
