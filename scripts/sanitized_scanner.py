"""
sanitized_scanner.py
------------------------------------
SAFE PROOF-OF-CONCEPT (SANITIZED)

Demonstrates how inherited folder permissions in a cloud storage API
could lead to metadata exposure. This script is non-actionable and
uses only dummy keys and file IDs for safe reproduction.

Author: Haitham A. E. ISMAIEEL
Contact: aei.ismaieel@gmail.com
License: MIT
"""

import requests

# === CONFIG (DUMMY VALUES) ===
API_KEY = "AIzaSy********Hwg"  # <-- Dummy key, non-functional
FILE_ID = "1t1jH********NeV"   # <-- Dummy file ID
API_URL = f"https://www.googleapis.com/drive/v3/files/{FILE_ID}"

# === REQUEST PARAMETERS ===
params = {
    "fields": "*",   # Request all fields
    "key": API_KEY   # API key (dummy)
}

def fetch_metadata():
    """
    Fetch metadata for a given FILE_ID using a public API endpoint.
    This is a simulated example with dummy values.
    """
    try:
        print("[*] Fetching metadata (SANITIZED)...")
        resp = requests.get(API_URL, params=params)
        print(f"HTTP Status: {resp.status_code}")

        # In a real test, parse JSON here
        print("Response body (SANITIZED EXAMPLE):")
        print({
            "kind": "drive#file",
            "id": "1t1jH********NeV",
            "name": "ExampleDoc.pdf",
            "mimeType": "application/pdf",
            "owners": [{
                "displayName": "example_user",
                "emailAddress": "j***@example.com"
            }],
            "webViewLink": "https://drive.google.com/file/d/1t1jH********NeV/view",
            "writersCanShare": True,
            "inheritedPermissionsDisabled": False
        })

    except Exception as e:
        print(f"[!] Error: {e}")

if __name__ == "__main__":
    fetch_metadata()
