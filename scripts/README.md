# Scripts — The Inheritance Trap (Sanitized Demonstrations)

This folder contains **vendor-agnostic, non-actionable** example scripts supporting the research paper  
[*The Inheritance Trap — How Cloud Folder Structures Can Silently Expose Metadata at Scale*](https://medium.com/@aei.ismaieel/the-inheritance-trap-how-cloud-folder-structures-can-silently-expose-metadata-at-scale-c6716bc56ac7).

## Scripts

1. **cloud_metadata_inheritance_scanner.py**  
   - Demonstrates how inherited folder permissions can lead to metadata exposure.
   - Checks for public parent folders (`shared: true`) and inheritance enabled (`inheritedPermissionsDisabled: false`).
   - Prints safe, synthetic metadata for educational purposes.

2. **spii_exposure_detector.py**  
   - Simulates detection of sensitive personally identifiable information (SPII) in exposed metadata.
   - Flags display names, email addresses, and other sensitive fields when found in files with public parents.

## Disclaimer
These scripts are for **educational demonstration only**.  
They do not contain live API endpoints, keys, or identifiers, and cannot be used to scan real cloud environments.

## License
MIT License — see [LICENSE](../LICENSE).
