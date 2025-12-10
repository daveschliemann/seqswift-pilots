import argparse
import struct
import sys
from time import time
import gzip

def pack_2bit(input_file, output_file):
    base_map = {'A': 0, 'C': 1, 'G': 2, 'T': 3, 'N': 0}  # N as A
    start_time = time()
    with gzip.open(input_file, 'rt') as f_in, open(output_file, 'wb') as f_out:  # 'rt' for text decompression
        total_bases = 0
        packed_bytes = bytearray()
        seq = ''
        for line in f_in:
            if line.startswith('>'): continue
            seq += line.strip().upper()
        for i in range(0, len(seq), 4):
            byte = 0
            for j in range(4):
                if i + j < len(seq):
                    byte = (byte << 2) | base_map.get(seq[i + j], 0)
                    total_bases += 1
                else:
                    byte <<= 2
            packed_bytes.append(byte)
            if total_bases % 100000000 == 0:
                print(f"{total_bases // 1000000} million bases processed...")
        # Header
        f_out.write(struct.pack('<Q', total_bases))
        f_out.write(packed_bytes)
        elapsed = time() - start_time
        print(f"SUCCESS → {total_bases} bases packed (2-bit per base)")
        print(f"Final file size: {len(packed_bytes) // 1048576} MB")
        print(f"Time: ~{elapsed / 60:.0f} minutes")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    pack_2bit(args.input, args.output)
