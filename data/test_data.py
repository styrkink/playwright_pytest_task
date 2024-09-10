import os
from dotenv import load_dotenv

load_dotenv()

email1 = os.getenv("EMAIL1")
email2 = os.getenv("EMAIL2")
password = os.getenv("PASSWORD")
file_path = "/Users/kirill/Desktop/projects/playwright+pytest/data/random_attachment_file.txt"