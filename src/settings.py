import os
from os.path import join
from dotenv import load_dotenv

path = os.getcwd()
dotenv_path = join(path, '.env')
load_dotenv(dotenv_path)

DATABASE_URI = os.environ.get("DATABASE_URI")
