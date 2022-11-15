import requests
import click


@click.command()
@click.argument("metric", required=True)
@click.option(
    "--latitude",
    "-lat",
    default=40.71,
    type=float,
    required=False,
    help="latitude (in degrees), default 40.71")
@click.option(
    "--longitude",
    "-lon",
    default=-74.01,
    type=float,
    required=False,
    help="longitude (in degrees), default -74.01")
def cli(metric: str, latitude: float, longitude: float) -> None:
    r = requests.get(
        "https://api.open-meteo.com/v1/forecast?"
        f"latitude={latitude}"
        f"&longitude={longitude}"
        "&current_weather=true")
    if r.status_code == 200:
        if metric in r.json()["current_weather"]:
            print(r.json()['current_weather'][metric])
        else:
            print("Metric not supported!")
    else:
        print("Open-Meteo is down!")


if __name__ == "__main__":
    cli()
