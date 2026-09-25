import random

number = random.randint(1,20)
max_tries = 2
win = False
tries = 0

print("=== selamat datang di game tebak angka ===")
print(f"kamu hanya memiliki {max_tries} percobaan")

name = input("masukan nama anda")

print ("hallo", name)

question = input("apakah kamu ingin bermain tebak angka [y/n]")

if question.lower() == "n" :
    print ("oh ok")
    exit()
if question.lower() == "y" :
    print("saya mempunyai angka 1-20 yang harus di tebak")

while not win and tries < max_tries :
    print (f"kesempatan ke {tries + 1}")
    guess = int(input("masukan angka"))
    tries += 1
    if guess ==number : 
        win = True
    if guess <number :
        print("angka terlalu kecil, coba lebih besar")
    if guess >number :
        print("angka terlalu besar, coba lebih kecil")

if win :
    print (f"selamat anda menang dalam {tries} percobaan dengan angka {number}")
else :
    print (f"kesempatan habis angka saya adalah {number}")                            