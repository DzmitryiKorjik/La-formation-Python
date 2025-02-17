# /// script
# requires-python = ">=3.8"
# dependencies = [
#   "typer"
# ]
# ///

import typer
import time

def main():
    prenoms = ["time", "sleep", "ctime", "gmtime", "localtime", "mktime", "strftime", "strptime", "time", "timezone", "tzname", "tzset"]
    with typer.progressbar(prenoms) as progress:
        for prenom in progress:
            time.sleep(1)

    typer.echo("Fin de la boucle.")

if __name__ == "__main__":
    typer.run(main)