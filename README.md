# SeqSwift Pilots – Sub-second NGS on a $140 Chromebook

Full GRCh38 + pathogen/AMR pipeline in <25 min · 100% offline · works on every Chromebook.

### 3-minute quickstart
```bash
git clone https://github.com/daveschliemann/seqswift-pilots.git
cd seqswift-pilots/pilots
unzip -o seqswift_root.zip
chmod +x seqswift_processor.so.chromebook_safe

# Example: full HPV16 oncogene risk scoring (500+ isolates)
./seqswift_processor.so.chromebook_safe --hpv16-risk --panel full --output hpv16_report.json
Latest build: December 2025
No GPG · No email required · Universal Chromebook binary included
Questions → dave@seqswift.com
