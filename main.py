import os, requests
from dotenv import load_dotenv

# load token from .env
load_dotenv()
JOPLIN_TOKEN = os.getenv("JOPLIN_TOKEN")
BASE_URL = "http://127.0.0.1:41184"

def fetch_notes():
    if not JOPLIN_TOKEN:
        print("❌ No token found. Please check your .env file")
        return

    url = f"{BASE_URL}/notes?token={JOPLIN_TOKEN}"
    r = requests.get(url)

    if r.status_code == 200:
        notes = r.json().get("items", [])
        if not notes:
            print("✅ Connected, but no notes found in Joplin")
        for note in notes:
            print("Title:", note["title"])
            print("Body:", note["body"][:200], "\n")
    else:
        print("❌ Error from Joplin API:", r.text)

if __name__ == "__main__":
    fetch_notes()
