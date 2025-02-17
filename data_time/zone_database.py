from datetime import datetime
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

def get_local_time(city):
    """
    Returns the local time in the specified city. https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
    """
    try:
        tz = ZoneInfo(city)
        now = datetime.now(tz)
        return now.strftime("%Y-%m-%d %H:%M:%S %Z%z")
    except ZoneInfoNotFoundError:
        return f"City '{city}' not found. Please check the spelling and try again."

print(get_local_time("Europe/Minsk"))  # Exemple d'utilisation
print(get_local_time("Europe/Paris"))  # Exemple d'utilisation
