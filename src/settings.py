import os
from os.path import join
from dotenv import load_dotenv

dotenv_path = join("../pythonTestPostgres_Python", '.env')
load_dotenv(dotenv_path)

DATABASE_DNS = os.environ.get("DATABASE_DNS")
DATABASE_URI = os.environ.get("DATABASE_URI")
