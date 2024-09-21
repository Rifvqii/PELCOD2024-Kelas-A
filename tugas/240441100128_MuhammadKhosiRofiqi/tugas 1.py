

#karakter 1
nama_1 = "irsyad"
hobi_1 = str(input(f"apa hobimu {nama_1}? "))
umur_1 = int(input(f"berapa umurmu {nama_1}? "))

#karakter 2
nama_2 = "jamal"
hobi_2 = str(input(f"apa hobimu {nama_2}? "))
umur_2 = int(input(f"berapa umurmu {nama_2}? "))

#DIALOG
print ("\n>>>MEMULAI DIALOGG<<<\n")

print(f"{nama_1}: Haii, apa hobimu {nama_2}? ")
print(f"{nama_2}: Wahh haii {nama_1}, hobiku {hobi_2}")

if hobi_1.lower() == hobi_2.lower() :
    print(f"{nama_1}: wahh ternyata hobi kita sama ya ")
    print(f"{nama_1}: lain waktu ayo bermain bareng")
else:
    print(f"{nama_1}: beda ya ternyata hobi kita ")
    print(f"{nama_1}: lain kali kamu harus nyoba hobiku {hobi_1}")
    print(f"{nama_2}: iya lain kali aku akan menyoba hobimu bermain {hobi_1}")


print(f"{nama_2}: btw, umurmu berapa?")
print(f"{nama_1}: umurku {umur_1}")
if umur_1 > umur_2 :
    print(f"{nama_2}: kamu sudah sepuh ya ternyata {nama_1} ang ang ang")
    print(f"{nama_1}: ya kamu bocil masih bau kencur")
elif umur_1 < umur_2 :
    print(f"{nama_2}: ternyata kamu masih bocil {nama_1}, HAHAHA")
    print(f"{nama_1}: ya kamu udah tua bau tanah-_-")
else :
    print(f"{nama_2}: ternyata kita sepantaran")

print(f"{nama_1}: yasudah aku pulang duluan ya {nama_2} udah sore ini")
print(f"{nama_2}: Yoii hati hati ya {nama_1}")





