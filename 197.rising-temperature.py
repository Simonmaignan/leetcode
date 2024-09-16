from typing import List
import datetime as dt
import pandas as pd


def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    rising_temp_ids: List[int] = []
    if len(weather) == 0:
        return pd.DataFrame(rising_temp_ids, columns=["Id"])
    weather.sort_values(by="recordDate", inplace=True)
    prev_day: dt.date = weather.iloc[0].recordDate - dt.timedelta(days=2)
    prev_temp = float("inf")
    for _, row in weather.iterrows():
        if (
            prev_day == row.recordDate - dt.timedelta(days=1)
            and row.temperature > prev_temp
        ):
            rising_temp_ids.append(row.id)
        prev_temp = row.temperature
        prev_day = row.recordDate
    return pd.DataFrame(rising_temp_ids, columns=["Id"])
