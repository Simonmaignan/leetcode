import pandas as pd


def find_customers(
    visits: pd.DataFrame, transactions: pd.DataFrame
) -> pd.DataFrame:
    merged_df = visits.merge(transactions, how="left", on="visit_id")
    no_trans_df = merged_df[merged_df["transaction_id"].isnull()][
        ["customer_id", "visit_id"]
    ]
    no_trans_df = no_trans_df.groupby("customer_id", as_index=False).count()
    return no_trans_df.rename(columns={"visit_id": "count_no_trans"})
