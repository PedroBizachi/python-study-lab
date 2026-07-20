# Section: The `assert` Statement

# Uncomment to play along with Python Asserting
# assert (
#   x == 10
# ), "x should be 10, but it's not!" # Raise an AssertionError

# Section: Pytest and `assert`


import pytest

from text_analysis import calculate_text_attributes


def test_string_equality() -> None:
    exepected_status = "SUCCESS"
    actual_status = "success".upper()

    assert actual_status == exepected_status


def test_word_count() -> None:
    text = "Deploying microservice to Kubernetes cluster."
    text_empty = ""

    assert (calculate_text_attributes(text)["word_count"]) == 5
    assert (calculate_text_attributes(text_empty)["word_count"]) == 0


def test_unique_words() -> None:
    text = "Deploying microservice to Kubernetes cluster."
    text_with_duplicates = "Deploying deploying."
    text_empty = ""

    text_results = calculate_text_attributes(text)
    text_with_duplicates_results = calculate_text_attributes(text_with_duplicates)
    text_empty_result = calculate_text_attributes(text_empty)

    assert (len(text_results["unique_words"])) == 5
    assert (len(text_with_duplicates_results["unique_words"])) == 1
    assert (len(text_empty_result["unique_words"])) == 0


def test_average_word_length() -> None:
    text = "Deploying microservice to Kubernetes cluster."  # 40 / 5 = 8
    text_with_duplicates = "Deploying deploying."  # 18 / 2 = 9
    text_empty = ""  # 0

    text_result = calculate_text_attributes(text)
    text_with_duplicates_result = calculate_text_attributes(text_with_duplicates)
    text_empty_result = calculate_text_attributes(text_empty)

    assert (text_result["average_word_length"]) == 8.0
    assert (text_with_duplicates_result["average_word_length"]) == 9.0
    assert (text_empty_result["average_word_length"]) == 0.0


def test_longest_word() -> None:
    text = "Deploying microservice to Kubernetes cluster."  # microservice
    text_with_duplicates = "Deploying deploying."  # Deploying
    text_empty = ""

    text_result = calculate_text_attributes(text)
    text_with_duplicates_result = calculate_text_attributes(text_with_duplicates)
    text_empty_result = calculate_text_attributes(text_empty)

    assert (text_result["longest_word"]) == "microservice"
    assert (text_with_duplicates_result["longest_word"]) == "Deploying"
    assert (text_empty_result["longest_word"]) == ""


# Section: Pytest’s Rich Failure Output


@pytest.mark.skip(reason="Intentional mismatch example")
def test_string_mismatch() -> None:
    expected = "HEllo WOrlD"
    actual = "Hello World"

    assert expected == actual


# Section: Asserting Floating-Point Numbers (`pytest.approx`)


def test_float_with_approx() -> None:
    calculated_val = 0.1 + 0.2
    expected_val = 0.3

    assert calculated_val == pytest.approx(expected_val)  # type: ignore


# Section: Asserting Exceptions (`pytest.raises`)


def test_raises_exeception() -> None:
    with pytest.raises(ZeroDivisionError):
        _division = 1 / 0
