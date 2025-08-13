"""
spii_exposure_detector.py
-------------------------
Vendor-agnostic pseudocode to flag SPII exposure in metadata responses.

DISCLAIMER: No live API calls. Uses synthetic metadata objects for safe demonstration.
"""

# Sample synthetic metadata set
sample_metadata_responses = [
    {
        "id": "fileA123",
        "owners": [{"displayName": "John Doe", "emailAddress": "j***@example.com"}],
        "webViewLink": "https://examplecloud.com/file/fileA123/view",
        "mimeType": "application/pdf",
        "inheritedPermissionsDisabled": False,
        "parents": [{"id": "parent12345", "shared": True}],
    },
    {
        "id": "fileB456",
        "owners": [{"displayName": "Anonymous", "emailAddress": None}],
        "webViewLink": None,
        "mimeType": "image/png",
        "inheritedPermissionsDisabled": True,
        "parents": [{"id": "parent99999", "shared": False}],
    }
]

SENSITIVE_FIELDS = ["emailAddress", "displayName"]

def detect_spii_exposure(metadata_list):
    """Scan metadata objects for potential SPII leaks."""
    for meta in metadata_list:
        shared_parent = any(p.get("shared", False) for p in meta.get("parents", []))
        inheritance_enabled = not meta.get("inheritedPermissionsDisabled", True)
        
        if shared_parent and inheritance_enabled:
            print(f"[!] File {meta['id']} may expose SPII:")
            for owner in meta.get("owners", []):
                for field in SENSITIVE_FIELDS:
                    value = owner.get(field)
                    if value:
                        print(f"    {field}: {value}")
            print(f"    webViewLink: {meta.get('webViewLink')}")
            print("-" * 50)

if __name__ == "__main__":
    detect_spii_exposure(sample_metadata_responses)
