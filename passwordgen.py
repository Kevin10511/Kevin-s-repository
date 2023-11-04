import random
caratteri = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
num = int(input('Scegli il numero di caratteri della password:'))
password = ""
for i in range(num):
    password +=  random.choice(caratteri)
print(password)
