import os
from dotenv import load_dotenv

load_dotenv()


def get_env_db_uri(var_name: str = "DATABASE_URI") -> str:
    uri = os.getenv(var_name)
    if not uri:
        raise RuntimeError(f"Environment variable '{var_name}' not found.")
    return uri


print(get_env_db_uri())
