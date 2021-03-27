#Soal no 4

#usia minimal mendaftar kursus online
x = 21

#input usia
print("Berapakah usia anda sekarang?")
usia = float(input("Usia saya adalah : "))

#rumus
if usia >= x:
    print("Apakah Anda sudah lulus ujian kualifikasi (Y/T) ?")
    y = "Y"
    jawaban = input("")
    if jawaban == y:
        print("Anda dapat mendaftar di kursus kami")
    else:
        print("Anda tidak dapat mendaftar di kursus kami")
else:
    print("Anda tidak dapat mendaftar di kursus kami")
