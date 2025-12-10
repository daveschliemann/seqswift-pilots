# SeqSwift: Sub-Second NGS Alignment + Pathogen/AMR Profiling on a $140 Laptop

[![Chromebook](https://img.shields.io/badge/Hardware-Chromebook%20%7C%20$140%20Onn-brightgreen)](https://www.bestbuy.com/site/onn-14-laptop-intel-celeron-4gb-memory-64gb-emmc-jet-black/6535398.p?skuId=6535398) [![Offline](https://img.shields.io/badge/Cloud-Zero%20Dependence-blue)](https://seqswift.com) [![Patent Pending](https://img.shields.io/badge/Patent-US%2063%2F187%2C188-orange)](https://seqswift.com)

**Replace GATK/BWA in 0.0069s. Full GRCh38 germline pipeline in <25 min on a $140 Best Buy laptop (SKU 1402). 100% offline, no cluster, no cloud bills.**

Built by a solo founder on a Chromebook to fight diagnostic delays in global health (inspired by sepsis runs in rural Kenya). Already validated on 50M+ synthetic variants + TCGA/GEO/SRA/clinical datasets. [Live demos](https://www.seqswift.com#demos).

## 🚀 Quickstart (5 Minutes to First Run)

This is a **gated pilot release**—binaries are GPG-encrypted for security. Free for the first 100 validating labs (IRB-exempt remnants only).

### 1. Grab the Pilot
- Download from [v1.13 Release](https://github.com/daveschliemann/seqswift-pilots/releases/tag/v1.13-crostini-killer):
  - `SeqSwift_ecoli_BOOM_Nov20.zip.gpg` (E. coli mock community)
  - `SeqSwift_HPV16_18_BOOM_Nov18.zip.gpg` (HPV typing, 0.0069s)
  - `SeqSwift_SARS2_BOOM_Nov20.zip.gpg` (SARS-CoV-2 profiling)
  - `GRCh38_ref.bin` (739 MB 2-bit human genome index—built in 25 min on Chromebook)
- Verify integrity: Run `sha256sum <file>` and match against release hashes.

### 2. Decrypt (GPG Required)
Email `license@seqswift.com` with:
- "GPG" + your institutional email
- Lab focus (e.g., "remnant BAL for AMR validation")
- Why you qualify (e.g., access to AR Bank mocks)

Reply in <24h with one-time passphrase. Then:
```bash
# Install GPG if needed (Ubuntu/Debian: sudo apt install gnupg)
gpg --batch --yes --passphrase="YOUR_PASSPHRASE" -d SeqSwift_HPV16_18_BOOM_Nov18.zip.gpg > pilot.zip
unzip pilot.zip
chmod +x seqswift  # Make executable
