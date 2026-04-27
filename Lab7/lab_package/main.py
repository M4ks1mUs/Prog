import typer
from typing import List
from lab_package import (
    is_palindrom, is_palindrom_rec, get_x, get_x_rec,
    create_file_logger,
    find_color_in_image
    )

app = typer.Typer()

@app.command()
def palindrome_check(numbers: List[int], method: str = "iterative"):
    from lab_package import is_palindrom, is_palindrom_rec
    if method == "iterative":
        result = is_palindrom(numbers)
    else:
        result = is_palindrom_rec(numbers)
    typer.echo(f"Результат: {result}")

@app.command()
def sequence(index: int, method: str = "iterative"):
    from lab_package import get_x, get_x_rec
    if method == "iterative":
        result = get_x(index)
    else:
        result = get_x_rec(index)
    typer.echo(f"x[{index}] = {result}")

@app.command()
def log_messages(filepath: str, messages: List[str]):
    from lab_package import create_file_logger
    log = create_file_logger(filepath)
    for msg in messages:
        log(msg)
    typer.echo("Основной поток свободен!")

@app.command()
def find_color(image_path: str, red: int, green: int, blue: int):
    from lab_package import find_color_in_image
    find_color_in_image(image_path, (red, green, blue))

if __name__ == "__main__":
    app()