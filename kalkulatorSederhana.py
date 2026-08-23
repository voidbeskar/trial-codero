"""kalkulator sederhana mendukung operasi: +, -, *, /"""

def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b == 0:
        raise ValueError("Tidak bisa membagi dengan nol.")
    return a / b


def main():
    while True:
        angka1 = input("Masukkan angka pertama: ")
        if angka1.lower() == 'exit':
            break

        operator = input("Masukkan operator (+, -, *, /): ")
        if operator.lower() == 'exit':
            break

        angka2 = input("Masukkan angka kedua: ")
        if angka2.lower() == 'exit':
            break

        try:
            angka1 = float(angka1)
            angka2 = float(angka2)
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka yang benar.\n")
            continue

        if operator == "+":
            hasil = tambah(angka1, angka2)
        elif operator == "-":
            hasil = kurang(angka1, angka2)
        elif operator == "*":
            hasil = kali(angka1, angka2)
        elif operator == "/":
            try:
                hasil = bagi(angka1, angka2)
            except ValueError as e:
                print(f"Error: {e}\n")
                continue
        else:
            print("Operator tidak valid. Silakan masukkan operator yang benar.\n")
            continue

        print(f"Hasil: {hasil}\n")


if __name__ == "__main__":
    main()