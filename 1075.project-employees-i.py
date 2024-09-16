import pandas as pd


def project_employees_i(
    project: pd.DataFrame, employee: pd.DataFrame
) -> pd.DataFrame:
    project_df = project.merge(employee, how="left", on="employee_id")[
        ["project_id", "experience_years"]
    ]
    project_df = (
        project_df.groupby("project_id", as_index=False).mean().round(2)
    )
    return project_df.rename(columns={"experience_years": "average_years"})
