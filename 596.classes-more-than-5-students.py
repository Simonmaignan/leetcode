import pandas as pd


def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    nb_students = courses.groupby("class", as_index=False).count()
    return nb_students[nb_students["count"] >= 5]
