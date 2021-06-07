# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 13:10:28 2021

@author: subhankar
"""

from RSA2 import *
import time
import os

reading_units = 1024

#       ENCRYPTION

def encrypt_file(filename):
    total_encrypted = 0
    
    file_size = os.path.getsize('files/' + filename) 
    file = open("files/" + filename, "rb")
    encrypted_file = open("encrypted_files/encrypted_" + filename, "wb")
    
    
    print('Size of file is', file_size, 'bytes')
    
    read_by = reading_units * 4        # read 64 bytes of data from the file one by one
    byte = file.read(read_by)
    
    while byte:
        encrypted_data = RSAencrypt(byte)
        total_encrypted += read_by
        # print(len(encrypted_data))
        for data in encrypted_data:
            encrypted_file.write(data)    
        print("\r",((total_encrypted*100)//file_size), end="% done")
        byte = file.read(read_by)
        
    encrypted_file.close()
    file.close()
    
    print("\nencryption done.\nFile is saved in location:")
    print("encrypted_files/encrypted_" + filename)
    return "encrypted_" + filename
    

#       DECRYPTION

def decrypt_file(filename):
    total_encrypted = 0
    
    file_size = os.path.getsize('encrypted_files/' + filename) 
    encrypted_file = open("encrypted_files/" + filename, "rb")
    decrypted_file = open("decrypted_files/de_" + filename, "wb") 
    
    print('Size of file is', file_size, 'bytes')
    
    read_by = reading_units
    byte = encrypted_file.read(read_by)
    
    while byte:
        decrypted_data = RSAdecrypt2(byte)
        total_encrypted += read_by
        for data in decrypted_data:
            decrypted_file.write(data)
        print("\r",((total_encrypted*100)//file_size), end="% done")
        byte = encrypted_file.read(read_by)    
    encrypted_file.close()
    decrypted_file.close()
    
    print("\ndecryption done.\nFile is saved in location:")
    print("decrypted_files/de_" + filename)
    return "de_" + filename


#       CHECK FOR FILE CONVERSION ERRORS

def check_files(path1, path2):
    file = open(path1, "rb")
    decrypted_file = open(path2, "rb")
    file_read = file.read()
    decrypted_file_read = decrypted_file.read()
    if(file_read == decrypted_file_read):
        print("It's equal")
    else:
        print("It's not equal")
        
    file.close()
    decrypted_file.close()

start_time = time.time()
encrypted_filename = encrypt_file("image2.jpg")
decrypted_filename = decrypt_file(encrypted_filename)
check_files("files/text.txt","decrypted_files/" + decrypted_filename)
print(f'execution completes in {(time.time() - start_time)} seconds')