def summarize_data(df):
    return {
        "rows": len(df),
        "columns": list(df.columns),
        "missing_values": df.isnull().sum().to_dict(),
        "data_types": df.dtypes.apply(str).to_dict()
    }
