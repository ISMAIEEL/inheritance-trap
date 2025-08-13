# The Inheritance Trap — Sanitized Research

**Analyzing a potential cloud security behavior:** a researcher’s perspective on inherited folder permissions, metadata exposure, and why small design choices matter.

- Medium write-up (redacted): https://medium.com/@aei.ismaieel/the-inheritance-trap-how-cloud-folder-structures-can-silently-expose-metadata-at-scale-c6716bc56ac7  
- Contact: aei.ismaieel@gmail.com

---

## Executive Summary
This repository documents a systemic permission-inheritance pattern in cloud storage ecosystems—observed in Google Drive and plausibly relevant elsewhere—where files nested inside publicly shared folders can expose sensitive metadata to unauthenticated API calls made with a valid API key. Exposed fields may include owner display name and email (SPII), filenames/types, timestamps, web view/download links, and permission flags.

This repo contains **sanitized** figures and excerpts. It does **not** include live emails, API keys, or active file links.

---

## Why This Is Not a User Mistake
- Owners often **did not explicitly share** the file; exposure occurs via **recursive folder inheritance**.
- There is **no clear UI banner/warning** indicating a file is public due to parent settings.
- The behavior is **exploitable without authentication** or direct collaboration with the owner.
- The same exposure path works with **any valid API key** (newly registered or leaked/unrestricted).

---

## Core Observation (Sanitized)
When a file’s `inheritedPermissionsDisabled` is `false` and the parent folder is public, the Drive API `files.get` endpoint may return metadata using any valid API key. While one can register a new key, the prevalence of **publicly exposed keys** makes automated harvesting easier. With modern AI tooling, attackers can generate adaptive collection scripts that scale quickly.

---

## Figures (Sanitized)
All figures are redacted to mask SPII and sensitive tokens 

 **Figure 1 — API Response Showing Metadata**
    
  <img width="1093" height="532" alt="1" src="https://github.com/user-attachments/assets/247ea64c-9548-4eb7-b586-efccfe26bfe7" />

 **Figure 2 — Parent Folder Confirming Public Sharing (shared: true)**
   
 <img width="1308" height="628" alt="2" src="https://github.com/user-attachments/assets/2aa5e95a-0d55-4548-b03e-9789f82f93fc" />

 **Figure 3 — Permission Flags (e.g., writersCanShare: true; inheritedPermissionsDisabled: false)**
  
 <img width="1366" height="664" alt="3" src="https://github.com/user-attachments/assets/f3c97652-1e9e-4891-af5e-276f81cdfcd2" />

 **Figure 4 — Mass PII, PSII and Metadata Tree (Sanitized)**

  <img width="1323" height="548" alt="4" src="https://github.com/user-attachments/assets/cd63ea11-7aee-4410-bbe4-8318475fa99d" />

 **Figure 5 — Access Scope Example (Sanitized)**
 
  <img width="1366" height="664" alt="5" src="https://github.com/user-attachments/assets/5d45d656-5821-43e9-ae7f-cf7b7ab5fc38" />

---

## Technical Appendix
See [`TECHNICAL-APPENDIX.md`](TECHNICAL-APPENDIX.md) for a sanitized PoC flow, redaction rules, and non-actionable pseudocode.

---

## Responsible Communication (Summary)
- Reported: 2025-08-01 (Google VRP)
- Outcome: reviewed; classified under current design expectations
- Goal of publication: inform users and vendors; encourage improvements that reduce unintended SPII exposure across the ecosystem

See [`appendix/vendor_communication_summary.md`](appendix/vendor_communication_summary.md) for a concise timeline (redacted).

---

## License & Use
- Research is published under the MIT License (see [`LICENSE`](LICENSE)).
- **No mass scanning. No targeting of individuals.** See [`SECURITY.md`](SECURITY.md) and [`DISCLAIMER.md`](DISCLAIMER.md).

---

## Links
- Medium: https://medium.com/@aei.ismaieel/the-inheritance-trap-how-cloud-folder-structures-can-silently-expose-metadata-at-scale-c6716bc56ac7  
- GitHub repo : [https://github.com/ISMAIEEL/inheritance-trap/new/main](https://github.com/ISMAIEEL/inheritance-trap)
