nomor = [1,2,3,4,5,6,7,8] #List angka untuk pesanan
sosis = ['original','blackpapper','cheese','Sosis ayam','jumbo cheese','jumbo ori','jumbo blackpapper'] # List sosis
harga_sosis = [12000,18000,18000,12000,17000,23000,23000] #list harga sosis
simpanan = [] # list untuk menyimpan nama pesanan 
simpanan_harga = [] # list untuk menyimpan harga pesanan 
jumlah_barang = [] # list untuk menyimpan jumlah 

# fungsi fungsi untuk memanggil
def strip (): #fungsi memanggil strip
    print("-"*50) #output strip
def open(): #Fungsi Memanggil Kasir
    print("Sosis bakar 99".center(50)) #fungsi menampilkan nama total_pesanan(center untuk menampilkan tulisan ke tengah)
# fungsi untuk memanggil pesanan lagi
def ulangi():# fungsi untuk memanggil ulangi
    ulangi = input("Ingin pesan Lagi? (ya/tidak)")#input untuk mengulangi pesanan
    if ulangi == 'ya': #jika ingin mpesan lagi ketik 'ya'
        strip() #untuk memanggil strip
        bakar_sosis() #untuk memanggil bakar_sosis
    elif ulangi == 'tidak':# jika tidak inngin pesan ketik "tidak"
        total_pesanan()#untuk memanggil total pesanan
    else:
        print("Input Anda Tidak Benar")#kesalahan jika menginput
# fungsi untuk memanggil menu sosis
def bakar_sosis():
    strip()
    print("Menu Sosis Bakar".center(50))
    strip()
    for a,b,c in zip(nomor,sosis,harga_sosis):#pengulangan list(menggunakan)
        print('{}.{}\t\t{:00}'.format(a,b,c))#output perulangan
    strip()
    pilih_sosis = int(input('Pilih Pesanan Anda(1-7) : '))# 
    mukbang = sosis[pilih_sosis-1]#output untuk pilihan sosis
    bakar_sosis = harga_sosis[pilih_sosis-1]
    banyak_sosis = input('Masukan Jumlah {} : '.format(mukbang))
    simpanan.append(mukbang)#Menambahkan objek obj ke list
    jumlah_barang.append(banyak_sosis)
    banyaknya = int(banyak_sosis) *int(bakar_sosis)
    simpanan_harga.append(banyaknya)#append berfungsi untk menambahkan objek kedalam list
    ulangi()
# fungsi memampilkan total_pesanan
def total_pesanan():
    strip()
    print("Pesanan Anda".center(50))
    strip()
    for h,i,k,l in zip(nomor,simpanan,jumlah_barang,simpanan_harga):#pengulangan list
        print('{}.{}\t{}\t{:00}'.format(h,i,k,l))#output perulangan
    total = sum(simpanan_harga)
    strip()
    print('Total Pesanan Anda Adalah Rp.{},-'.format(total)) # total pesanan yang harus di bayar
    strip()
    pembayaran ()
def pembayaran ():

    total = sum(simpanan_harga)

    pembayaran_total = int(input('Masukkan Uang Anda : Rp.'))# input untuk memasukan uang
    if pembayaran_total >= total :
        kembalian = pembayaran_total - total#kembalian uang anda
        print('Kembalian Anda : Rp. {},-'.format(kembalian))
        strip()
        print('Terima Kasih'.center(50))
        strip()
    elif pembayaran_total < total :
        kurang = total - pembayaran_total
        print('Uang Anda Kurang {}'.format(kurang))# logika jika uang kurang
        pembayaran()
# membuat fungsi authentifikasi sederhana
def get_login():
    print('=' * 30)
    print('silahkan login')
    print('='*30)
    username = input('masukan username kasir anda: ')
    password = input('masukan password: ')
 
    if username == 'bagus' and password == '2070231079':
        print('login berhasil...\n\n')
        strip()
        open()
        bakar_sosis()
    else:
        print('username or password salah..')
        get_login()
 
def tanya():
    tanya = input('kembali ke menu..? (y/n)')
    if tanya == 'y':
        strip()
        
    elif tanya == 't':
        exit()
    else:
        print('input salah')
        print('masukan input dengan benar')
 
get_login()
strip()
open()
bakar_sosis()