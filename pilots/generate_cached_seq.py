#!/usr/bin/env python3

import argparse
import gzip
import struct
import time

# Mapping for 2-bit encoding: A=0, C=1, G=2, T=3, anything else (N, etc.) = 0
base_map = {
    'A': 0, 'C': 1, 'G': 2, 'T': 3,
    'a': 0, 'c': 1, 'g': 2, 't': 3,
}

def pack_2bit(input_file, output_file):
    start_time = time.time()

    # Correctly handle both .gz and uncompressed files
    opener = gzip.open if input_file.endswith('.gz') else open
    
    # 'rt' = read as text (decompresses gzip automatically)
    with opener(input_file, 'rt') as f_in, open(output_file, 'wb') as f_out:
        total_bases = 0
        packed_bytes = bytearray()
        seq = ''

        print("Reading and packing genome...")

        for line in f_in:
            line = line.strip()
            if not line or line.startswith('>'):
                # Skip headers and empty lines
                continue
            seq += line.upper()

        print(f"Total sequence length collected: {len(seq):,} bases")
        
        # Pack 4 bases into each byte
        for i in range(0, len(seq), 4):
            byte = 0
            for j in range(4):
                if i + j < len(seq):
                    base = seq[i + j]
                    byte = (byte << 2) | base_map.get(base, 0)  # N or unknown → 0
                    total_bases += 1
                else:
                    byte <<= 2  # pad remaining bits with 00
            packed_bytes.append(byte)

            if total_bases % 100_000_000 == 0:
                print(f"{total_bases // 1_000_000} million bases processed...")

        # Write simple header: total number of bases as 64-bit little-endian
        f_out.write(struct.pack('<Q', total_bases))
        f_out.write(packed_bytes)

    elapsed = time.time() - start_time
    file_mb = len(packed_bytes) // 1048576
    print(f"SUCCESS → {total_bases:,} bases packed (2-bit per base)")
    print(f"Output file size: {file_mb} MB (plus 8-byte header)")
    print(f"Time taken: {elapsed / 60:.1f} minutes")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Pack a FASTA genome into 2-bit format')
    parser.add_argument('--input', required=True, help='Input .fna or .fna.gz file')
    parser.add_argument('--output', required=True, help='Output .bin file')
    args = parser.parse_args()

    pack_2bit(args.input, args.output)
