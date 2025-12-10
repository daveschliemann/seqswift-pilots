import gzip
import struct
from time import time

input_file = "GCA_000001405.15_GRCh38_no_alt_analysis_set.fna.gz"
output_file = "GRCh38_ref.bin"

base_map = {'A':0, 'C':1, 'G':2, 'T':3, 'N':0}
start = time()
total_bases = 0
byte_buffer = bytearray()

print("Streaming GRCh38 3.1B bases — low-memory mode — live on $140 Chromebook")

with gzip.open(input_file, 'rt') as f, open(output_file, 'wb') as out:
    for line in f:
        if line.startswith('>'): continue
        seq = line.strip().upper()
        for i in range(0, len(seq), 4):
            byte = 0
            for j in range(4):
                if i+j < len(seq):
                    byte = (byte << 2) | base_map.get(seq[i+j], 0)
                    total_bases += 1
                else:
                    byte <<= 2
            byte_buffer.append(byte)
            
            if total_bases % 100_000_000 == 0:
                print(f"{total_bases//1_000_000} million bases packed...")
                out.write(byte_buffer)
                byte_buffer.clear()

    # Final write
    out.write(byte_buffer)
    out.write(struct.pack('<Q', total_bases))  # header at end is fine for demo

elapsed = time() - start
print(f"\nSUCCESS — {total_bases:,} bases → {len(byte_buffer)//1_048_576} MB in {elapsed/60:.1f} min")
