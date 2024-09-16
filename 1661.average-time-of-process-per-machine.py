import pandas as pd


def get_average_time(activity: pd.DataFrame) -> pd.DataFrame:
    processes_df = activity.groupby(
        ["machine_id", "process_id"], as_index=False
    )
    processes_df = processes_df.apply(
        lambda group: pd.Series(
            {
                "processing_time": group["timestamp"].max()
                - group["timestamp"].min()
            }
        )
    )

    machines_df = (
        processes_df.groupby("machine_id", as_index=False)
        .mean()
        .drop(columns=["process_id"])
    ).round(3)

    return machines_df
