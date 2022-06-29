import pandas as pd
import datetime

# Countdown to Christmas 2021
print("Happy New Year! Welcome 2021")
current_date = datetime.datetime.now()
future_date = datetime.datetime(2021,12,25)
delta = future_date - current_date
print(delta)

