# Section: Skipping Tests Unconditionally: @pytest.mark.skip

import time

import pytest

try:
    import some_optional_library  # pyright: ignore[reportMissingImports]
except ModuleNotFoundError:
    some_optional_library = None


@pytest.mark.skip(reason="Unconditional skip")
def test_new_experimental_feature() -> None:
    assert False


# Section: Skipping Tests Conditionally: @pytest.mark.skipif


@pytest.mark.skipif(
    some_optional_library is None,
    reason="Requires 'some_optional_library' to be installed",
)
def test_with_optional_dependency() -> None:
    print("Running tests that depends on an optional library")
    assert some_optional_library


# Section: Expected Failures: @pytest.mark.xfail


@pytest.mark.xfail(reason="Bug #123: Division by zero not handled properly")
def test_division_by_zero() -> None:
    _division = 1 / 0
    assert False


@pytest.mark.xfail  # Add strict=True to make XPASS lead to a failure
def test_expected_to_fail() -> None:
    assert True


# Section: Custom Markers and Registration


@pytest.mark.slow
def test_very_long_computations() -> None:
    time.sleep(5)
    assert True


@pytest.mark.api
@pytest.mark.smoke
def test_user_creation() -> None:
    assert True


# Section: Running Tests by Marker (m option)
