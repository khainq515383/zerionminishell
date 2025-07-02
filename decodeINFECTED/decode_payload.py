import base64
import zlib

# Load the payload from file
with open('payload', 'r') as f:
    encoded = f.read().strip()

try:
    # Step 1: Base64 decode
    decoded_data = base64.b64decode(encoded)

    # Step 2: zlib decompress (raw inflate, wbits=-15)
    decompressed = zlib.decompress(decoded_data, wbits=-15)

    # Output the final decoded PHP code
    print(decompressed.decode('utf-8', errors='replace'))


except Exception as e:
    print(f"[!] Decoding failed: {e}")
