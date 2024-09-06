import pandas as pd


def replace_employee_id(
    employees: pd.DataFrame, employee_uni: pd.DataFrame
) -> pd.DataFrame:
    df = employees.merge(employee_uni, how="left", on="id")
    df.drop("id", axis=1, inplace=True)
    # print(df.head())
    return df
