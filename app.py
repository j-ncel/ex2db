import streamlit as st
from excel.loader import ExcelLoader
from excel.cleaner import ExcelCleaner
from excel.validator import ExcelValidator
from core.migrator import Migrator
from db.schema_builder import SchemaBuilder


def configure_sqlite() -> str:
    db_path = st.text_input("SQLite file path", value="output.db")
    return f"sqlite:///{db_path}"


def configure_postgres() -> str:
    user = st.text_input("Username")
    pwd = st.text_input("Password", type="password")
    host = st.text_input("Host", value="localhost")
    port = st.text_input("Port", value="5432")
    db = st.text_input("Database name")
    return f"postgresql://{user}:{pwd}@{host}:{port}/{db}"


def configure_mysql() -> str:
    user = st.text_input("Username")
    pwd = st.text_input("Password", type="password")
    host = st.text_input("Host", value="localhost")
    port = st.text_input("Port", value="3306")
    db = st.text_input("Database name")
    return f"mysql+pymysql://{user}:{pwd}@{host}:{port}/{db}"


def configure_oracle() -> str:
    user = st.text_input("Username")
    pwd = st.text_input("Password", type="password")
    host = st.text_input("Host", value="localhost")
    port = st.text_input("Port", value="1521")
    sid = st.text_input("Service name")
    return f"oracle+cx_oracle://{user}:{pwd}@{host}:{port}/?service_name={sid}"


DB_CONFIGURATORS = {
    "SQLite": configure_sqlite,
    "PostgreSQL": configure_postgres,
    "MySQL": configure_mysql,
    "Oracle": configure_oracle
}


def render_footer():
    st.markdown("""
        <a href="https://github.com/j-ncel/ex2db" target="_blank" style="font-size: 12px; color: lime; text-decoration: none;">
            Github Repo (jncel)
        </a>
        <br>  
        <a href="https://coff.ee/jncel" target="_blank">
            <img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" width="100">
        </a>
        """, unsafe_allow_html=True)


def main():
    st.set_page_config(page_title="EX2DB", page_icon="🤝", layout="centered")
    st.title("EX2DB: Excel to Database Migrator")

    uploaded_file = st.file_uploader("Upload an Excel file",
                                     type=["xlsx", "xlsm"],
                                     help="Supports Excel Files only.")

    st.subheader("Database Configuration")
    db_type = st.selectbox("Choose database type", list(DB_CONFIGURATORS.keys()))

    db_uri = DB_CONFIGURATORS[db_type]()

    if uploaded_file:
        loader = ExcelLoader(uploaded_file)
        sheets = loader.load()
        sheet_names = list(sheets.keys())

        selected_sheets = st.multiselect(
            "Select sheets to migrate", sheet_names, default=sheet_names)

        cleaner = ExcelCleaner()
        validator = ExcelValidator()
        schema_builder = SchemaBuilder()

        # Preview data
        for sheet in selected_sheets:
            st.subheader(f"Preview: {sheet}")
            df_clean = cleaner.clean(sheets[sheet])
            st.dataframe(df_clean)

            st.caption("Validation Report")
            report = validator.validate(df_clean)
            st.json(report)

            st.caption("Inferred SQLAlchemy Types")
            sql_types = schema_builder.summarize_sqlalchemy_types(df_clean)
            st.json(sql_types)

        # Migrate Data
        if st.button("Migrate to Database"):
            migrator = Migrator(db_uri=db_uri)
            result = migrator.migrate(file_path=uploaded_file, sheet_names=selected_sheets)

            for sheet, info in result.items():
                if info["status"] == "success":
                    st.markdown(f"**Rows written:** {info['rows']}")
                    st.markdown(f"**Columns:** `{', '.join(info['columns'])}`")
                    st.success(
                        f"✅ :gray-background[{sheet}] migrated successfully to :gray-background[{db_type}] with table name as :gray-background[{info['table']}].")
                else:
                    st.error(f"😔 {sheet} failed: {info['message']}")

    render_footer()


if __name__ == "__main__":
    main()
