# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 13:10:28 2021

@author: subhankar
"""

import scratch_encrypt as se
import time
import os

reading_units = 512

#       ENCRYPTION

def encrypt_file(filename, scratches):
    total_encrypted = 0
    
    file_size = os.path.getsize('files/' + filename) 
    file = open("files/" + filename, "rb")
    encrypted_file = open("encrypted_files/encrypted_" + filename, "wb")
    
    
    print('Size of file is', file_size, 'bytes')
    
    
    read_by = reading_units * 4        # read 64 bytes of data from the file one by one
    byte = file.read(read_by)
    
    while byte:
        encrypted_data = scratches.encrypt(byte)
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

def decrypt_file(filename, scratches):
    total_encrypted = 0
    
    file_size = os.path.getsize('encrypted_files/' + filename) 
    encrypted_file = open("encrypted_files/" + filename, "rb")
    decrypted_file = open("decrypted_files/de_" + filename, "wb") 
    
    print('Size of file is', file_size, 'bytes')
    
    read_by = reading_units
    byte = encrypted_file.read(read_by)
    
    while byte:
        decrypted_data = scratches.decrypt(byte)
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
        print("Encryption Decryption successful")
    else:
        print("Files didn't match...Encryption or Decryption went wrong check the logs")
        
    file.close()
    decrypted_file.close()

filename = input("Enter filename with extension: ")
generator = input("Press 'G' for generating a new key or just press enter to enter ur keys: ")
if not generator == 'G':
    choice = input("'E' for encryption, 'D' for decryption, 'B' for both or 'C' for check: ")
    if choice == 'E':
        E = int(input("Enter public key : "))
        N = int(input("Enter universal key: "))
        start_time = time.time()
        scratches = se.scratch_encrypt(e=E, n=N, generate_key=False)
        encrypted_filename = encrypt_file(filename, scratches)
    elif choice == 'D':
        D = int(input("Enter private key : "))
        N = int(input("Enter universal key: "))
        start_time = time.time()
        scratches = se.scratch_encrypt(d=D, n=N, generate_key=False)
        decrypted_filename = decrypt_file(filename, scratches)
    elif choice == 'B':
        E = int(input("Enter public key : "))
        E = int(input("Enter private key : "))
        N = int(input("Enter universal key: "))
        start_time = time.time()
        scratches = se.scratch_encrypt(e=E, n=N, d=D, generate_key=False)
        encrypted_filename = encrypt_file(filename, scratches)
        decrypted_filename = decrypt_file(encrypted_filename, scratches)
    elif choice == 'C':
        decrypted_filename = input("Enter decrypted filename with extension: ")
        start_time = time.time()
        check_files("files/" + filename,"decrypted_files/" + decrypted_filename)
else:
    Level = int(input("Enter level of encryption u want: "))
    start_time = time.time()
    scratches = se.scratch_encrypt(level = Level)
    encrypted_filename = encrypt_file(filename, scratches)
    decrypted_filename = decrypt_file(encrypted_filename, scratches)
    print("Checking validity of the files: ", end="")
    check_files("files/" + filename,"decrypted_files/" + decrypted_filename)
print(f'execution completed in {(time.time() - start_time)} seconds')