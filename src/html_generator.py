from typing import Iterable, List


def generate_html(items: List[str]) -> str:
    args = [iter(items)] * 5
    data_rows = zip(*args)
    html = "<html>\n"
    html += "<h1>Scavenger Hunt List</h1>"
    html += "<table width=\"100%\" border=\"1\" style=\"border-collapse:collapse\">\n"
    for data_row in data_rows:
        html += generate_html_row(data_row)
    html += "</table>\n</html>\n"

    return html


def generate_html_row(items: Iterable[str]) -> str:
    table_row = "  <tr height=\"200\">\n"
    for item in items:
        table_row += f"    <td width=\"20%\" style=\"text-align:center;font-size:30px\">{item}</td>\n"
    table_row += "  </tr>\n"

    return table_row
