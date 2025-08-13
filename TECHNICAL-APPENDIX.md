# Technical Appendix — Sanitized PoC Flow

## Overview
The following describes the logic used in the proof-of-concept (PoC).  
All identifiers are synthetic; the example cannot be used to retrieve real data.

---

## PoC Flow (Sanitized)
1. **Enumerate file IDs** from public sources (e.g., search engine dorks).
2. **Use any valid API key** (registered or public) to call:
    ```bash
    curl "https://www.googleapis.com/drive/v3/files/{FILE_ID}?fields=*&key={VALID_API_KEY}"
    ```
3. **Inspect returned metadata**:
    - `owners.displayName`
    - `owners.emailAddress`
    - `webViewLink`
    - `writersCanShare`
    - `inheritedPermissionsDisabled`
4. **Map inheritance** via `parents[]` to confirm exposure path.

---

## Figures Reference
Figures are stored in the `/figures` directory:
- fig1_api_response.png — API metadata excerpt
- fig2_parent_shared_true.png — Parent folder sharing flag
- fig3_permission_flags.png — writersCanShare & inheritedPermissionsDisabled
- fig4_metadata_tree.png — Full metadata tree (sanitized)
- fig5_access_scope.png — Access scope example (sanitized)
