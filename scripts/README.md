# Scripts — Educational Proof-of-Concepts (Sanitized)

This folder contains **redacted, non-actionable** scripts designed to illustrate the mechanics of inherited permission exposure in cloud storage ecosystems.  
All data in these scripts is **synthetic** — no live file IDs, API keys, or personal identifiers are included.

---

## 1. `pseudocode_sanitized_scanner.py`
**Purpose:**  
Demonstrates, in pseudocode form, how an automated scanner might detect files that inherit permissions from publicly shared parent folders.

**Key Concepts:**
- Checking the `inheritedPermissionsDisabled` flag.
- Confirming the parent folder `shared: true`.
- Extracting metadata fields such as owner info, file names, and timestamps (simulated).

---

## 2. `spii_exposure_scanner.py`
**Purpose:**  
Simulates scanning for SPII exposure using **dummy** API keys, file IDs, and metadata responses.

**Risk Indicators Flagged:**
- `inheritedPermissionsDisabled: false`
- `writersCanShare: true`
- Metadata containing synthetic SPII (e.g., `owner.emailAddress`)

**Educational Value:**  
Shows how attackers could theoretically:
1. Enumerate file IDs from public sources.
2. Use valid API keys (new or leaked) to retrieve metadata.
3. Identify exposed SPII without file content access.

---

## Usage
These scripts are for **educational and vendor-awareness purposes only**.  
They must **never** be used on live systems without explicit authorization.

---

## Related Research
Full write-up: [Medium Article](https://medium.com/@aei.ismaieel/the-inheritance-trap-how-cloud-folder-structures-can-silently-expose-metadata-at-scale-c6716bc56ac7)  
Repository: [GitHub Repo](https://github.com/ISMAIEEL/inheritance-trap)
