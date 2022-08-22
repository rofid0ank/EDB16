# !/usr/bin/env python3
# program untuk dekripsi file
# dibuat oleh rofi

import base64, os
from base64 import b16decode

def dekripsi_nama_file(nama_file):
    nama_file_enkripsi = nama_file.encode()
    nama_file_bytes = b16decode(nama_file_enkripsi)
    nama_file_asli = nama_file_bytes.decode()
    return nama_file_asli

def dekripsi_file(file_enkripsi):
    file_enkripsi_bytes = b16decode(file_enkripsi)
    return file_enkripsi_bytes

file = input("\nmasukan file yang mau didekripsi : ")

pemisah_extensions = os.path.splitext(file)
hapus_extensions_encrypt = pemisah_extensions[0]
nama_file_asli = dekripsi_nama_file(hapus_extensions_encrypt)

with open(file, "rb") as file_enkripsi:
    isi_file_enkripsi = file_enkripsi.read()
    
with open(nama_file_asli, "wb") as file_dekripsi:
    file_dekripsi.write(dekripsi_file(isi_file_enkripsi))
    file_dekripsi.close()
    os.system(f"rm {file}")
    print("file berhasil didekrisi\n")
    exit()
