# BAB 3

# Start program
lama=int(input("Lama Menginap = ")) # Input lama menginap
harga=int(input("Harga Rp.")) # Input harga 
jumlah=lama*harga # Formulas jumlah
if jumlah > 300000: # Formula If & elif
    diskon=jumlah*0.3
elif jumlah > 200000 and jumlah <= 300000:
    diskon=jumlah*0.2
elif jumlah > 100000 and jumlah <= 200000:
    diskon=jumlah*0.1
else:
    diskon=0
if diskon > 0:
    keterangan="dapat diskon"
else:
    keterangan="tidak diskon" # End formulas of & elif
bayar=jumlah-diskon # Formulas bayar
print("Bayar=Rp.",bayar) # Output bayar
print("Keterangan.",keterangan) # Output keterangan
# End program