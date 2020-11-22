# BAB 3

# Start program
diskon=0 # value diskon
qty=int(input("Banyak Barang = ")) # Input value banyak barang
harga=int(input("Harga Barang = ")) # Input value harga barang
jumlah=qty*harga    # Formula jumlah
if jumlah > 1000000: # IF
    diskon=jumlah*0.1 # End IF
bayar=jumlah-diskon # Formula diskon
print("Bayar = Rp.",bayar) # Output value bayar
# End program