menu = ["Kopi Susu", "Matcha Latte", "Americano"]
harga = [18000, 22000, 15000]
jumlah = [4, 3, 5]
biaya_operasional = 15000

sub_kopi = harga[0] * jumlah[0]
sub_matcha = harga[1] * jumlah[1]
sub_americano = harga[2] * jumlah[2]

subtotal_pendapatan = [sub_kopi, sub_matcha, sub_americano]

total_seluruh = sum(subtotal_pendapatan)

pendapatan_bersih = total_seluruh-biaya_operasional

jumlah_barang = sum(jumlah)

target_pencapaian = pendapatan_bersih > 200.000 and jumlah_barang > 10

print("")
print("Subtotal Pendapatan :")
print("     Jumlah Harga Kopi Susu      : Rp", sub_kopi)
print("     Jumlah Harga Matcha Latte   : Rp.",sub_matcha)
print("     Jumlah Harga Americano      : Rp.",sub_americano)
print("     List Pendapatan             :", subtotal_pendapatan)
print("")
print("Pendapatan Bersih            : Rp.",pendapatan_bersih)
print("")
print("Target Pencapaian            :", target_pencapaian)
print("")


