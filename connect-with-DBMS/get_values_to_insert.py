from datetime import datetime, timedelta

import pandas as pd
from numpy.ma.core import append


def get_values_to_insert():
    values: str = ""
    data_df = pd.read_excel("/Users/macbook/Downloads/Salfeet AZP.xlsx")
    col = "AZP value - J-632 - Present Demand - Pressure (m H2O)"
    data = data_df[col].values
    start_time = datetime(2023, 4, 1, 12)
    for datum in data:
        values += f"('m-09974122f5e0', {datum}, {datum}, '{start_time}'),"
        start_time = start_time + timedelta(hours=1)
    values = values[:-1]
    datetime.replace(minute=0, second=0, microsecond=0)

    return values