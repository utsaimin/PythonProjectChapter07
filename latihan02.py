namafil = input('Masukkan nama file')
try:
    file = open(namafile, 'r')
    file =  open(namafile, 'a')
    teks = input('Data yang mau ditambahkan: ')
    file.write(teks)
    tanya = input('Mau lagi (y/n: ')
    while True:la
        if tanya == 'y' :
            teks = input('Data yang mau ditampilkan:m ')
            file.write(teks)
            tanya = input('Mau lagi (y/n): ')
        elif tanya ==  'n' :
            break
    file.close()
except FileNotFoundError:
    print('File tidak ditemukan')
            
