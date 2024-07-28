import zlib
import base64
import re

obfuscated_code = 'PUT THE OBFUSCATED STRING HERE NOT THE ENTIRE CODE OF THE FILE'


def deobfuscate(code):
    try:
        reversed_code = code[::-1]
        decoded_data = base64.b64decode(reversed_code)
        decompressed_data = zlib.decompress(decoded_data)
        return decompressed_data.decode()
    except Exception as e:
        print(f"Erreur lors de la déobfuscation: {e}")
        return None

current_code = obfuscated_code
while True:
    print(f"Déobfuscation en cours : {current_code}")
    deobfuscated_code = deobfuscate(current_code.encode())
    if deobfuscated_code is None or "exec((_)(b'" not in deobfuscated_code:
        break
    match = re.search(r"exec\(\(_\)\(b'(.*?)'\)\)", deobfuscated_code)
    if match:
        current_code = match.group(1)
    else:
        break

print("Code final déobfusqué :")
print(deobfuscated_code)
