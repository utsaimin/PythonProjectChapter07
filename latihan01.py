try:
    file = input("Masukkan nama file: ")
    print('isi file', file, 'adalah: ')
    print(open(file, 'r').read())
except FileNotFoundError:
    print('File tidak ditemukan')
