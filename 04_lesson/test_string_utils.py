import pytest

from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("skypro", "Skypro"),
        ("hello world", "Hello world"),
        ("python", "Python"),
    ],
)
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("123abc", "123abc"),
        ("", ""),
        ("   ", "   "),
    ],
)
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
def test_capitalize_none_negative():
    with pytest.raises(AttributeError):
        string_utils.capitalize(None)


@pytest.mark.positive
@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("   skypro", "skypro"),
        ("skypro", "skypro"),
        ("  04 апреля 2023", "04 апреля 2023"),
    ],
)
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("", ""),
        (" ", ""),
        ("     ", ""),
    ],
)
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
def test_trim_none_negative():
    with pytest.raises(AttributeError):
        string_utils.trim(None)


@pytest.mark.positive
@pytest.mark.parametrize(
    "input_str, symbol, expected",
    [
        ("SkyPro", "S", True),
        ("SkyPro", "Pro", True),
        ("04 апреля 2023", "апреля", True),
        ("123", "2", True),
    ],
)
def test_contains_positive(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize(
    "input_str, symbol, expected",
    [
        ("SkyPro", "U", False),
        ("SkyPro", "s", False),
        ("", "S", False),
        (" ", "S", False),
    ],
)
def test_contains_negative(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


@pytest.mark.negative
def test_contains_none_string_negative():
    with pytest.raises(AttributeError):
        string_utils.contains(None, "S")


@pytest.mark.negative
def test_contains_none_symbol_negative():
    with pytest.raises(TypeError):
        string_utils.contains("SkyPro", None)


@pytest.mark.positive
@pytest.mark.parametrize(
    "input_str, symbol, expected",
    [
        ("SkyPro", "k", "SyPro"),
        ("SkyPro", "Pro", "Sky"),
        ("123", "2", "13"),
        ("04 апреля 2023", " ", "04апреля2023"),
    ],
)
def test_delete_symbol_positive(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize(
    "input_str, symbol, expected",
    [
        ("SkyPro", "U", "SkyPro"),
        ("SkyPro", "s", "SkyPro"),
        ("", "S", ""),
        ("     ", " ", ""),
    ],
)
def test_delete_symbol_negative(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected


@pytest.mark.negative
def test_delete_symbol_none_string_negative():
    with pytest.raises(AttributeError):
        string_utils.delete_symbol(None, "S")


@pytest.mark.negative
def test_delete_symbol_none_symbol_negative():
    with pytest.raises(TypeError):
        string_utils.delete_symbol("SkyPro", None)
