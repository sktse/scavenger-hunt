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
    result = """<html><table>
  <tr>
    <td>Citizen Kane</td>
    <td>The Godfather</td>
    <td>Casablanca</td>
    <td>Raging Bull</td>
    <td>Singin' in the Rain</td>
  </tr>
  <tr>
    <td>Gone with the Wind</td>
    <td>Lawrence of Arabia</td>
    <td>Schindler's List</td>
    <td>Vertigo</td>
    <td>The Wizard of Oz</td>
  </tr>
  <tr>
    <td>City Lights</td>
    <td>The Searchers</td>
    <td>Star Wars</td>
    <td>Psycho</td>
    <td>2001: A Space Odyssey</td>
  </tr>
</table></html>
"""
    return result


def test_generate_html(items, expected_html):
    results = generate_html(items)
    assert results == expected_html
