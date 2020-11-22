# BAB 3

# Start program
lama=int(input("Lama Menginap ? ")) # Input lama
harga=int(input("Harga Kamar ? ")) # Input harga
jumlah=lama*harga # Formula jumlah
if jumlah > 300000: # If 1
    if harga > 50000: # If 2
        keterangan="Dapat kartu diskon"
    else: # End if 2
        keterangan="Tidak dapat kartu diskon"
else: # End if 1 
    keterangan="Tidak dapat kartu diskon"
if lama > 3: # If 3
    bayar=jumlah-(jumlah*0.3)
else: # End if 3
    bayar=jumlah
print("Jumlah RP." ,jumlah) # Output Jumlah
print("Keterangan ",keterangan) # Output keterangan
print("Bayar Akhir Rp.",bayar) # Output bayar
# End program