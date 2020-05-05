import click

from src.html_generator import generate_html
from src.item_picker import pick_items


@click.command()
@click.option("--filename", prompt="Output file name", help="The output HTML file name.")
def scavenger_hunt(filename: str) -> None:
    items = pick_items()
    html = generate_html(items)

    html_filename = filename if filename.endswith(".html") else f"{filename}.html"
    file_path = f"output/{html_filename}"
    with open(file_path, "w") as fs:
        fs.write(html)

    print(f"Finished writing scavenger hunt items to {file_path}")


if __name__ == '__main__':
    scavenger_hunt()
