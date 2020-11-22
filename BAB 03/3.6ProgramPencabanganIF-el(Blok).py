# BAB 3

# Start program
lama=int(input("Lama menginap ")) # Input value Lama menginap
harga=int(input("Harga kamar Rp.")) # Input value Harga kamar
jumlah=lama*harga # Formula jumlah
if jumlah > 1000000: # if jumlah > 1000000
    diskon=jumlah*0.1 # formula 
    keterangan="Dapat Diskon" # Output text keterangan
else:
    diskon=0
    keterangan="Tidak Dapat Diskon" # Output text keterangan
bayar=jumlah-diskon # Formula 
print("Bayar RP.",bayar) # Output value bayar
print("Keterangan",keterangan) #Output text keterangan
# End program