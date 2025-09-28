import streamlit as st
import pandas as pd
from excel.loader import load_excel
from excel.cleaner import clean_dataframe
from excel.validator import validate_dataframe
from core.migrator import migrate

st.set_page_config(page_title="EX2DB", layout="centered")
st.title("EX2DB: Excel to Database Migrator")

uploaded_file = st.file_uploader("Upload an Excel file", type=["xlsx"])

st.subheader("Database Configuration")
db_type = st.selectbox("Choose database type", [
    "SQLite", "PostgreSQL", "MySQL", "Oracle"])

if db_type == "SQLite":
    db_path = st.text_input("SQLite file path", value="output.db")
    db_uri = f"sqlite:///{db_path}"

elif db_type == "PostgreSQL":
    pg_user = st.text_input("Username")
    pg_pwd = st.text_input("Password", type="password")
    pg_host = st.text_input("Host", value="localhost")
    pg_port = st.text_input("Port", value="5432")
    pg_db = st.text_input("Database name")
    db_uri = f"postgresql://{pg_user}:{pg_pwd}@{pg_host}:{pg_port}/{pg_db}"

elif db_type == "MySQL":
    my_user = st.text_input("Username")
    my_pwd = st.text_input("Password", type="password")
    my_host = st.text_input("Host", value="localhost")
    my_port = st.text_input("Port", value="3306")
    my_db = st.text_input("Database name")
    db_uri = f"mysql+pymysql://{my_user}:{my_pwd}@{my_host}:{my_port}/{my_db}"

elif db_type == "Oracle":
    ora_user = st.text_input("Username")
    ora_pwd = st.text_input("Password", type="password")
    ora_host = st.text_input("Host", value="localhost")
    ora_port = st.text_input("Port", value="1521")
    ora_sid = st.text_input("Service name")
    db_uri = f"oracle+cx_oracle://{ora_user}:{ora_pwd}@{ora_host}:{ora_port}/?service_name={ora_sid}"


if uploaded_file:
    sheets = load_excel(uploaded_file)
    sheet_names = list(sheets.keys())

    selected_sheets = st.multiselect(
        "Select sheets to migrate", sheet_names, default=sheet_names)

    # Preview data
    for sheet in selected_sheets:
        st.subheader(f"Preview: {sheet}")
        df_clean = clean_dataframe(sheets[sheet])
        st.dataframe(df_clean)

        st.caption("Validation Report")
        report = validate_dataframe(df_clean)
        st.json(report)

    # Migrate Data
    if st.button("Migrate to Database"):
        result = migrate(file_path=uploaded_file,
                         db_uri=db_uri, sheet_names=selected_sheets)

        for sheet, info in result.items():
            if info["status"] == "success":
                st.markdown(f"**Rows written:** {info['rows']}")
                st.markdown(f"**Columns:** `{', '.join(info['columns'])}`")
                st.success(
                    f"✅ :gray-background[{sheet}] migrated successfully to :gray-background[{db_type}] with table name as :gray-background[{info['table']}].")
            else:
                st.error(f"😔 {sheet} failed: {info['message']}")

st.markdown("""
    <a href="https://coff.ee/jncel" target="_blank">
        <img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" width="88">
    </a>
    """, unsafe_allow_html=True)
