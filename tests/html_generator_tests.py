import pytest

from src.html_generator import generate_html


@pytest.fixture()
def items():
    return [
        "Citizen Kane",
        "The Godfather",
        "Casablanca",
        "Raging Bull",
        "Singin' in the Rain",
        "Gone with the Wind",
        "Lawrence of Arabia",
        "Schindler's List",
        "Vertigo",
        "The Wizard of Oz",
        "City Lights",
        "The Searchers",
        "Star Wars",
        "Psycho",
        "2001: A Space Odyssey",
    ]


@pytest.fixture()
def expected_html():
    with open("./tests/expected_output.html", "r") as fs:
        result = fs.read()

    return result


def test_generate_html(items, expected_html):
    results = generate_html(items)
    assert results == expected_html
