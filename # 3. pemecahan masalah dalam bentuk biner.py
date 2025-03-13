# Diketahui

x = 100  # 1100100 dalam biner
y = 10   # 0001010 dalam biner
z = 68   # 1000100 dalam biner

hasil_a = x & y & z
print(f"Hasil a: {x} & {y} & {z} = {hasil_a} (biner: {bin(hasil_a)})")

hasil_b = (x ^ y) << 5 >> 2
print(f"Hasil b: ({x} ^ {y}) << 5 >> 2 = {hasil_b} (biner: {bin(hasil_b)})")

hasil_c = (~x & ~y) | ~z
print(f"Hasil c: (~{x} & ~{y}) | ~{z} = {hasil_c} (biner: {bin(hasil_c)})")

# Jumlah seluruhnya
print("\n=== HASIL AKHIR ===")
print(f"a. x & y & z = {hasil_a} (biner: {bin(hasil_a)})")
print(f"b. (x ^ y) << 5 >> 2 = {hasil_b} (biner: {bin(hasil_b)})")
print(f"c. (~x & ~y) | ~z = {hasil_c} (biner: {bin(hasil_c)})")
