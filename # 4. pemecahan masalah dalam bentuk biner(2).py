# Diketahui
x = 0b1100100  # 100 dalam desimal
y = 0b1100010  # 98 dalam desimal
z = 0b101      # 5 dalam desimal

hasil_a = (x - y) // z  # Menggunakan // agar hasilnya bilangan bulat
print(f"Hasil a: ({x} - {y}) / {z} = {hasil_a} (biner: {bin(hasil_a)})")

hasil_b = ((x * z) + y) // (x - z + z)  # Gunakan // agar hasil bulat
print(f"Hasil b: (({x} * {z}) + {y}) / ({x} - {z} + {z}) = {hasil_b} (biner: {bin(hasil_b)})")

print("HASIL AKHIR")
print(f"a. ({x} - {y}) / {z} = {hasil_a} (biner: {bin(hasil_a)})")
print(f"b. (({x} * {z}) + {y}) / ({x} - {z} + {z}) = {hasil_b} (biner: {bin(hasil_b)})")


