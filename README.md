# The Inheritance Trap — Sanitized Research

**Summary:**  
This repository documents research into a systemic permission-inheritance pattern in cloud storage ecosystems — observed in Google Drive and potentially relevant elsewhere — where files nested inside publicly shared folders can expose sensitive metadata without the owner’s direct action.  
This is **not a user mistake**; the exposure occurs through recursive folder permissions and certain API metadata behaviors.  
All materials here are sanitized — no live credentials, emails, or file links.

---

## Quick Links
- **Medium write-up:** [Read the article](https://medium.com/@aei.ismaieel/the-inheritance-trap-how-cloud-folder-structures-can-silently-expose-metadata-at-scale-c6716bc56ac7)
- **Contact:** aei.ismaieel@gmail.com

---

## Executive Summary

<img width="1536" height="1024" alt="2" src="https://github.com/user-attachments/assets/3823cb43-2d00-4ed9-b750-103ef52e89b4" />
*Silent metadata leakage: when a shared folder exposes more than files — it exposes identities.*

When a folder is public in a cloud storage ecosystem, any files inside can inherit that visibility unless explicitly overridden.  
For affected services, unauthenticated API calls made with any valid API key (including leaked unrestricted ones) may return:

- Owner display name and email (SPII)
- File names, types, and extensions
- Created/modified timestamps
- Web view and download links
- Permission flags and parent folder IDs

Attackers could automate harvesting at scale, and modern AI tooling can accelerate scanning and analysis.

---

## Why This Is Not a User Mistake
- Owners never explicitly shared the affected files.
- No UI warning indicates that a file is public due to a parent folder’s settings.
- No audit trail flags inherited public access.
- Exploitable without authentication or collaboration from the file owner.

---

## Core Observation (Sanitized)
If a file’s `inheritedPermissionsDisabled` is `false` and its parent folder is public, the Drive API `files.get` endpoint (or an equivalent in other ecosystems) can return sensitive metadata with any valid API key.  
Publicly exposed keys in code repositories make this trivial to scale.

---

## Figures (Sanitized)
All figures are fully redacted to mask SPII and sensitive tokens:

- **Figure 1** — API Response Showing Metadata
  <img width="1093" height="532" alt="1" src="https://github.com/user-attachments/assets/00099bf1-2ed3-405b-b8f8-741ff761f941" />

- **Figure 2** — Parent Folder Confirming Public Sharing (`shared: true`)
  <img width="1308" height="628" alt="2" src="https://github.com/user-attachments/assets/c062bdd4-2798-4059-83c6-18d4e259435f" />
 
- **Figure 3** — Permission Flags (`writersCanShare: true`; `inheritedPermissionsDisabled: false`)
  <img width="1366" height="664" alt="3" src="https://github.com/user-attachments/assets/c5c34ac5-378e-48e7-89be-4b2c4e9408e7" />
 
- **Figure 4** — Full Metadata Tree   
<img width="1323" height="548" alt="4" src="https://github.com/user-attachments/assets/3c4c3500-1140-47cc-aac3-51755d109579" />

---

## Recommendations

### For Cloud Ecosystem Vendors
- Display clear UI banners for inherited public access.
- Mask owner SPII unless explicitly shared.
- Restrict sensitive metadata in unauthenticated API calls.
- Offer bulk audit/remediation tools for inherited exposures.
- Detect and alert on leaked API keys.

### For Users & Admins
- Audit folder trees for inherited exposure.
- Restrict & rotate API keys, scan repos for leaks.
- Use DLP tools to detect sensitive content exposure.

---

## Technical Appendix
This repository contains two **safe, non-actionable** example scripts in `/scripts`:

- **`cloud_metadata_inheritance_scanner.py`** — Pseudocode for scanning public folders and identifying inherited permissions.  
- **`spii_exposure_detector.py`** — Simulates detection of exposed SPII fields (e.g., `inheritedPermissionsDisabled: false`) using dummy data.

**Disclaimer:**  
Do not run these scripts against live systems without explicit authorization.  
This research is intended for security awareness and vendor collaboration.

---

## Responsible Communication (Summary)
- **Reported:** 2025-08-01  
- **Outcome:** Reviewed; classified under current design expectations.  
- **Goal:** Inform ecosystem vendors and encourage security improvements.

---

## License
Published under the MIT License (see `LICENSE`).
---

### Support
If you’d like to support future research: see **[SUPPORT.md](./SUPPORT.md)**.
