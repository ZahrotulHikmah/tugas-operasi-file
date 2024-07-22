print ("Zahrotul Hikmah 12 RPL 2")

def baca_file():
    nama_file = 'motivasi.txt'
    with open("motivasi.txt", "r") as baca:
        teks = baca.read()
        print(teks)

baca_file()

def tulis_file():
    teks = input("")
    with open("motivasi.txt", "a") as tulis:
        tulis.write(teks)
        print(teks)

tulis_file()
