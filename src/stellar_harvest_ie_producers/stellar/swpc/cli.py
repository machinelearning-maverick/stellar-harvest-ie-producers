import typer
from .client import fetch_latest_raw

app = typer.Typer()


@app.command(name="live-swpc")
def live_swpc():
    """
    Fetch and print the latest raw K-Index entry from NOAA SWPC.
    """
    print("Running... live-swpc")
    entry = fetch_latest_raw()
    typer.echo(entry)
