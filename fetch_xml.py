import requests

URL = "https://pan-gp-client.s3.amazonaws.com/"
OUTPUT_FILE = "globalprotect.xml"

def fetch_xml():
    response = requests.get(URL)
    if response.status_code == 200:
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            f.write(response.text)
        print(f"✅ XML fetched and saved to {OUTPUT_FILE}")
    else:
        print(f"❌ Failed to fetch XML: {response.status_code}")

if __name__ == "__main__":
    fetch_xml()
