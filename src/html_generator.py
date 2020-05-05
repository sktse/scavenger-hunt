from typing import Iterable, List, Tuple


def generate_html(items: List[str]) -> str:
    args = [iter(items)] * 5
    data_rows = zip(*args)
    table = "<html><table>\n"
    for data_row in data_rows:
        table += generate_html_row(data_row)
    table += "</table></html>\n"

    return table


def generate_html_row(items: Iterable[str]) -> str:
    table_row = "  <tr>\n"
    for item in items:
        table_row += f"    <td>{item}</td>\n"
    table_row += "  </tr>\n"

    return table_row
