# Scratography
A short project on encryption-decryption where I defined my very own module algorithm for encryption which is somewhat similar to RSA algorithm and user can generate a public and private key for encryption along with the level of encryption. The more the level of encryption the more time it is going to take more encrypting/decrypting the file and the harder it will be to crack and more secure the encrypted file will be.

***Here is how this project works :***
- First let me show around how this project structure is maintained.<img width="488" alt="output1" src="https://user-images.githubusercontent.com/35376376/121811532-57748180-cc82-11eb-8578-adb70eb50a58.PNG">
- We save the file that needs to be encrypted in the files folder<img width="561" alt="output5" src="https://user-images.githubusercontent.com/35376376/121811539-5a6f7200-cc82-11eb-8c4a-119447b70938.PNG">
- The encrypted_files folder contains all the encrypted files that gets saves after encryprion.<img width="960" alt="output2" src="https://user-images.githubusercontent.com/35376376/121811534-58a5ae80-cc82-11eb-9c1b-b4b041d64e55.PNG">
- The decrypted_files folder contains all the decrypted files that gets saved after decryption.<img width="557" alt="output3" src="https://user-images.githubusercontent.com/35376376/121811536-593e4500-cc82-11eb-88d0-ac17acb734a5.PNG">
- We can either generate a new key for encryption or use an existing key for encryption and also check whether the decrypted and original files are equal or not.<img width="960" alt="output4" src="https://user-images.githubusercontent.com/35376376/121811538-59d6db80-cc82-11eb-8659-62fee44ec726.PNG">

This encryption algorithm uses levels that we can choose in order to determine the level of encryption we want to put in on our file to prevent it from information leaking.

***Note: Remember the more the level of encryption the greater the time it will take to encrypt the file.***

 - For files that are generally of low size like text files etc. we can use higher level of encryption but for higher file size especially image & video files doesn't need much high level of
encryption as it becomes harder to crack such files with even small level of encryptions
