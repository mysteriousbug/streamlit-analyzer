import pandas as pd
from app.utils import summarize_data

def test_summarize_data():
    df = pd.DataFrame({"A": [1, 2, None], "B": ["x", "y", "z"]})
    summary = summarize_data(df)
    assert summary["rows"] == 3
    assert "A" in summary["columns"]
    assert summary["missing_values"]["A"] == 1
