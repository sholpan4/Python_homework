import datetime
import pytz
# Получение времени с учетом временной зоны
ny_timezone = pytz.timezone("America/New_York")
ny_time = datetime.datetime.now(ny_timezone)
print(ny_time)
