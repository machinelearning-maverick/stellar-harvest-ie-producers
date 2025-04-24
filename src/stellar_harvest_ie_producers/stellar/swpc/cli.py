import typer
from stellar_harvest_ie_producers.logging_config import setup_logging
from .client import fetch_planetary_kp_index, fetch_latest_raw

app = typer.Typer()


@app.callback(invoke_without_command=True)
def initialize(ctx: typer.Context):
    """This function runs before any sub-command. It sets up logging."""
    setup_logging()
    # If no sub-command was provided, show help and exit
    if ctx.invoked_subcommand is None:
        typer.echo(ctx.get_help())
        raise typer.Exit()


@app.command(name="raw-swcp")
def raw_swpc():
    """Fetch and print all raw K-Index entry from NOAA SWPC."""
    entries = fetch_planetary_kp_index()
    typer.echo(entries)


@app.command(name="latest-raw-swpc")
def latest_raw_swpc():
    """Fetch and print the latest raw K-Index entry from NOAA SWPC."""
    entry = fetch_latest_raw()
    typer.echo(entry)
