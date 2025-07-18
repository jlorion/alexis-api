from dotenv import load_dotenv
import os 
load_dotenv()

db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASS")
db_url = os.getenv("DB_URL")
db_port = os.getenv("DB_PORT")
db_table = os.getenv("DB_TABLE")
DATABASE_URL = f"postgresql+asyncpg://{db_user}:{db_pass}@{db_url}:{db_port}/{db_table}"
MIGRATION_URL = f"postgresql://{db_user}:{db_pass}@{db_url}:{db_port}/{db_table}"