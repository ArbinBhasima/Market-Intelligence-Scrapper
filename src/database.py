import os
import urllib.parse
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

# 1. Force load the .env file
load_dotenv()

# 2. Get variables (User-friendly fallbacks)
user = os.getenv("DB_USER", "Zion_tan")
# Use the RAW password here (e.g., "Zion@arbin3")
raw_pw = os.getenv("DB_PASSWORD", "Zion@arbin3")
host = os.getenv("DB_HOST", "localhost")
port = os.getenv("DB_PORT", "5432")
db_name = os.getenv("DB_NAME", "Zion_Database")

# 3. AUTOMATIC ENCODING
# This turns "Zion@arbin3" into "Zion%40arbin3" automatically
safe_pw = urllib.parse.quote_plus(raw_pw)

# 4. Construct the URL
DATABASE_URL = f"postgresql://{user}:{safe_pw}@{host}:{port}/{db_name}"

print(f"Connecting to: postgresql://{user}:***@{host}:{port}/{db_name}")

# 5. Create Engine
engine = create_engine(DATABASE_URL)


def save_to_db(title, content, url, report_date):
    """Saves a single scraped page into Zion_Database"""
    query = text(
        """
        INSERT INTO scraped_reports (title, content, url, report_date)
        VALUES (:title, :content, :url, :report_date)
        ON CONFLICT (url) DO NOTHING;
    """
    )

    try:
        with engine.connect() as conn:
            conn.execute(
                query,
                {
                    "title": title,
                    "content": content,
                    "url": url,
                    "report_date": report_date,
                },
            )
            conn.commit()
            print(f" Saved to DB: {title[:40]}...")
    except Exception as e:
        print(f" Database Error: {e}")
