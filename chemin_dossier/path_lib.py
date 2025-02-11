from pathlib import Path

p = Path.home() # "c:/Users/dmard/Desktop/Study/La formation Python/20250131/path_lib.py"
Path.cwd() # "c:/Users/dmard/Desktop/Study/

p / "Documents"

p.joinpath("Images", "photo.jpg").suffix # ".jpg"