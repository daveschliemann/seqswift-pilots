# SeqSwift Pilots

**Chromebook-native, sub-second, clinical-grade NGS + pathogen/AMR profiling**  
Patent pending (US 63/187,188) · Full 30× GRCh38 in <25 min on a $140 Best Buy laptop · 100 % offline

Latest gated pilot → [v1.14-dec2025-gatk-killer](https://github.com/daveschliemann/seqswift-pilots/releases/tag/v1.14-dec2025-gatk-killer)

Only **12 passphrases remaining in 2025**.

### Get Instant Access (First 100 Validating Labs)
Email david@seqswift.com or DM/comment “GPG” + your institutional email with one-sentence use case  
(e.g. “remnant BAL for AMR validation”, “liquid biopsy leftovers”, “AR Bank mocks”).

→ You receive the one-time GPG passphrase within minutes + permanent license  
→ Optional co-authorship on the January 2026 preprint (largest rapid mNGS validation cohort ever published)

### Benchmarks (measured on real $140 Onn Best Buy laptop, SKU 1402)
| Task                            | SeqSwift              | Typical GATK/DRAGEN   | Hardware                     |
|---------------------------------|-----------------------|-----------------------|---------------------|
| HPV16/18 typing                 | 0.0069 s              | 4–8 hours             | $140 laptop         |
| chr22 (30×) align + sort        | 58 s                  | 4–20 hours            | $140 laptop         |
| Full GRCh38 index build         | 25 min                | Days on cluster       | Chromebook          |
| Clinical BAL → pathogen + AMR   | <60 s (200 µL)        | Hours + cloud         | Any laptop          |

### Public Reference Data Used in Pilots
All references are canonical public sources. No proprietary or patient data
| Reference                     | Source & Accession                                      | Link / Citation                                                                 | SHA256 (first 12) |
|-------------------------------|---------------------------------------------------------|----------------------------------------------------------------------------------|-------------------|
| GRCh38.p14 + decoy + HLA      | Genome Reference Consortium / GENCODE v46               | [NCBI GCF_000001405.40](https://www.ncbi.nlm.nih.gov/datasets/genome/GCF_000001405.40/) | d3b7e7d19c3b     |
| GRCh38 2-bit index            | Built in 25 min on Chromebook from above                | Derived from GRC source                                                          | 4bd260b… (yours) |
| HPV16 / HPV18                 | NCBI RefSeq NC_001526.4 / NC_001357.1                    | [HPV16](https://www.ncbi.nlm.nih.gov/nuccore/NC_001526.4) · [HPV18](https://www.ncbi.nlm.nih.gov/nuccore/NC_001357.1) |
| SARS-CoV-2 Wuhan-Hu-1         | NCBI RefSeq NC_045512.2                                 | [NC_045512.2](https://www.ncbi.nlm.nih.gov/nuccore/NC_045512.2)                   | bbccdd11…        |
| AMR gene panel                | CDC/FDA-ARG-ANNOT v4 (2024)                             
## Full Gated BOOM Assets (739 MB GRCh38 Index + HPV/BRCA Panels)

To protect intellectual property (patent pending US 63/187,188), the complete binaries are gated.

Request access:
- Email david@seqswift.com - Request Passphrase with 1-sentence of your use-case.

# Test commit - GPG verification check Sat Jan 24 01:07:33 PM EST 2026
# Final verification test - key re-added Sat Jan 24 01:12:59 PM EST 2026
