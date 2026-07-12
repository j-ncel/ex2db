import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    def __init__(self, var_name: str = "DATABASE_URI"):
        self.var_name = var_name

    def get_env_db_uri(self) -> str:
        uri = os.getenv(self.var_name)
        if not uri:
            raise RuntimeError(f"Environment variable '{self.var_name}' not found.")
        return uri