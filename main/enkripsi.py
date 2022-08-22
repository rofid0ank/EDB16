#!/usr/bin/env python3
# program untuk enkripsi file
# dibuat oleh rofi

import base64, os
from os import chdir
from base64 import b16encode

def enkripsi_nama_file(nama_file):
    nama_file_enkripsi = nama_file.encode()
    base64_bytes = b16encode(nama_file_enkripsi)
    base64_message = base64_bytes.decode()
    return base64_message

def enkripsi_file(file): 
    file_enkripsi = b16encode(file)
    return file_enkripsi

file = input("\nmasukan file yang mau dienkripsi : ")

nama_file_enkripsi = enkripsi_nama_file(file)
extensions_encrypt = f"{nama_file_enkripsi}.base16"

with open(file, "rb") as file_asli:
    isi_file = file_asli.read() 

with open(extensions_encrypt, "wb") as file_enkripsi:
    file_enkripsi.write(enkripsi_file(isi_file))
    file_enkripsi.close()
    os.system(f"del {file}")
    print("file berhasil dienkripsi\n")
    exit()

