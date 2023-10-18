import datetime
from zoneinfo import ZoneInfo, available_timezones

if __name__ == "__main__":
    # Get date today
    today = datetime.date.today()

    # Get the time now
    dt = datetime.datetime.now()

    # Get time now in utc
    dt = datetime.datetime.utcnow()

    # Create a datetime object
    dt = datetime.datetime(2008, 1, 1, 0, 0, 0)

    # Convert epoch time in seconds to datetime object
    # A timezone-naive timestamp
    # 2012-09-13 02:22:50
    dt = datetime.datetime.fromtimestamp(1347517370)

    # str representation of the datetime object
    # 2012-09-13 02:22:50
    fmt = "%Y-%m-%d %H:%M:%S.%f"
    datetime.datetime.strftime(dt, format=fmt)

    # 2012-09-13 02:22:50.000000
    dt.strftime(format=fmt)
    datetime.datetime.strftime(dt, format=fmt)

    # Create a datetime object from string
    dt = datetime.datetime.strptime("2012-10-11 05:33:47.345768", fmt)

    # # List timezones
    # list(map(print, sorted(available_timezones())))

    # A timezone-aware timestamp
    dt = datetime.datetime(2008, 1, 1, 0, 0, 0, tzinfo=ZoneInfo("America/Los_Angeles"))

    # Convert to another timezone
    dt = dt.astimezone(ZoneInfo("UTC"))

    # Subtract 1 day, 1 hour and 1 minute from dt
    dt = dt - datetime.timedelta(days=1, hours=1, minutes=1)
