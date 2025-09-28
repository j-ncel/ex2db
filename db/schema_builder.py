from sqlalchemy import Table, Column, MetaData, Integer, Float, String, Boolean, DateTime
import pandas as pd


def map_dtype_to_sqlalchemy(dtype) -> type:
    if pd.api.types.is_integer_dtype(dtype):
        return Integer
    elif pd.api.types.is_float_dtype(dtype):
        return Float
    elif pd.api.types.is_bool_dtype(dtype):
        return Boolean
    elif pd.api.types.is_datetime64_any_dtype(dtype):
        return DateTime
    elif pd.api.types.is_string_dtype(dtype):
        return String
    else:
        return String


def build_table_schema(df: pd.DataFrame, table_name: str) -> Table:
    metadata = MetaData()
    columns = []

    for col_name, dtype in df.dtypes.items():
        col_type = map_dtype_to_sqlalchemy(dtype)
        is_nullable = df[col_name].isnull().any()
        is_primary = col_name.lower() == "id"

        column = Column(col_name, col_type,
                        nullable=is_nullable, primary_key=is_primary)
        columns.append(column)

    return Table(table_name, metadata, *columns)
