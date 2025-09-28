from sqlalchemy.exc import SQLAlchemyError


def write_dataframe_to_db(df, table, engine):
    try:
        table.metadata.create_all(engine)

        with engine.begin() as conn:
            conn.execute(table.insert(), df.to_dict(orient="records"))

        return True
    except SQLAlchemyError as e:
        raise RuntimeError(f"Failed to write data to DB: {e}")
