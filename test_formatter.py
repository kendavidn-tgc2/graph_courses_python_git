import pandas as pd

df = pd.DataFrame({"a": [1, 2, 3, 4], "b": [5, 6, 7, 8]})
result = (
    df.groupby("a")
    .agg(c_sum=("b", "sum"))
    .reset_index()
    .sort_values("b", ascending=False)
    .head(2)
)
result
