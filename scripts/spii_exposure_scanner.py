"""
spii_exposure_scanner.py
------------------------------------
SAFE SIMULATION — NON-ACTIONABLE

Simulates detection of potential SPII exposure in a cloud storage API
caused by inherited folder permissions and publicly exposed API keys.

This script uses ONLY dummy keys, file IDs, and metadata examples.

Author: Haitham A. E. ISMAIEEL
License: MIT
"""

# === Dummy leaked API keys harvested from public repos (simulated) ===
LEAKED_KEYS = [
    "AIzaSy********Hwg",  # Dummy Google-style key
    "ABCD1234********XYZ" # Dummy placeholder
]

# === Dummy file IDs discovered from search/indexing (simulated) ===
FILE_IDS = [
    "1t1jH********NeV",  # Example doc
    "1Jws********ftOf"   # Example PDF
]

# === Dummy parent folder IDs (simulated) ===
PARENT_IDS = [
    "0Bxx********AAQ",   # Public folder example
    "0Cyy********BBR"    # Another example
]

# === Simulated API metadata responses with potential SPII ===
SIMULATED_METADATA = {
    "1t1jH********NeV": {
        "kind": "drive#file",
        "id": "1t1jH********NeV",
        "name": "ExampleDoc.pdf",
        "mimeType": "application/pdf",
        "owners": [{
            "displayName": "John Example",
            "emailAddress": "j***@example.com"
        }],
        "webViewLink": "https://drive.google.com/file/d/1t1jH********NeV/view",
        "webContentLink": "https://drive.google.com/uc?id=1t1jH********NeV",
        "writersCanShare": True,
        "inheritedPermissionsDisabled": False,
        "parents": ["0Bxx********AAQ"]
    },
    "1Jws********ftOf": {
        "kind": "drive#file",
        "id": "1Jws********ftOf",
        "name": "Invoice_2025.pdf",
        "mimeType": "application/pdf",
        "owners": [{
            "displayName": "Jane Demo",
            "emailAddress": "j***@demo.com"
        }],
        "webViewLink": "https://drive.google.com/file/d/1Jws********ftOf/view",
        "writersCanShare": True,
        "inheritedPermissionsDisabled": False,
        "parents": ["0Cyy********BBR"]
    }
}

def detect_exposure():
    print("[*] Simulating SPII exposure scan...")
    print(f"[*] Loaded {len(LEAKED_KEYS)} leaked API keys (dummy).")
    print(f"[*] Loaded {len(FILE_IDS)} discovered file IDs.")

    for file_id in FILE_IDS:
        meta = SIMULATED_METADATA.get(file_id)
        if not meta:
            continue

        # SPII detection
        owner_email = meta["owners"][0]["emailAddress"]
        inherited_flag = not meta["inheritedPermissionsDisabled"]
        writers_share = meta["writersCanShare"]

        # Risk conditions
        if inherited_flag or writers_share:
            print("\n[!] POTENTIAL EXPOSURE DETECTED")
            print(f"    File ID: {file_id}")
            print(f"    Name: {meta['name']}")
            print(f"    Owner Email (masked): {owner_email}")
            print(f"    Parent Folder(s): {', '.join(meta['parents'])}")
            print(f"    inheritedPermissionsDisabled: {meta['inheritedPermissionsDisabled']}")
            print(f"    writersCanShare: {writers_share}")
            print("    --> This file inherits permissions from a public parent folder.")
            print("    --> Metadata includes SPII (owner email, display name).")
            print("    --> Exposure possible without owner explicitly sharing.")

    print("\n[*] Scan complete — simulated results only (safe).")

if __name__ == "__main__":
    detect_exposure()
