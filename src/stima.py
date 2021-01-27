# Nama/NIM : Naufal Alexander Suryasumirat / 13519135
# Penyelesaian Cryptarithmetic dengan Algoritma Brute Force

import time

## Functions

# Membuat List yang berisi integer dimana semua angka dalam integer merupakan angka yang unik
# Yang memiliki panjang length (parameter function)
# Merupakan bagian dari algoritma brute force (men-generasi seluruh angka yang mungkin)
# Tidak digunakan, telah dibuat algoritma brute force yang lebih cepat
def permutation(length):
    return_list = [] # List yang akan dikembalikan
    for integer in range(0, 10**length):
    # Menggunakan range dari 0 sampai dengan 10 pangkat Length dari input function
        if len(set(str(integer))) == length:
        # Set berisi tiap angka / integer yang unik dalam str(integer) sehingga jika length dari set sama dengan length dari input,
        # Integer tersebut merupakan angka dengan panjang length yang tiap angkanya unik
            return_list.append(integer) # Mengambahkan integer ke return_list
        else:
            continue
    return return_list

# Membaca file (parameter filename yaitu test.txt)
# Mengembalikan tuple yang berisi kata yang akan digunakan untuk Cryptarithmetic dalam bentuk tuple
# Tuple merupakan sebuah List dengan sebuah string
# Contoh tuple: (['SEND', 'MORE'], 'MONEY')
def read_file(filename):
    local_list = []
    # Seluruh kata (dalam file) pada awalnya dimasukkan ke dalam local_list
    with open ("../test/" + filename, 'r') as file:
        for line in file:
            for word in line.split():
                word_append = word.replace("+", "").replace("-", "")
                # Menghilangkan tanda + dan -
                local_list.append(word_append)
                # Memasukkan tiap kata (tiap line berisi satu kata pada file) 
                # ke dalam local_list
    word_list = local_list[:-2]
        # Mengambil seluruh elemen dalam list local_list kecuali kedua terakhir
    result = local_list[len(local_list) - 1]
        # Menbamgil elemen terakhir list local_list
    return word_list, result # Mengembalikan dalam bentuk tuple ([List], 'string')

# Menggabungkan seluruh elemen dalam list of kata
def join_words(list_of_words):
    to_return = ""
    for word in list_of_words:
        to_return += word
    return to_return

# Mengembalikan huruf pertama tiap kata dalam bentuk list
def get_firstletters(list_of_words):
    to_return = []
    for word in list_of_words:
        to_return.append(word[0])
    return to_return

# Mengkonversikan huruf ke angka korespondensinya sesuai dictionary
# Mengembalikan value ber-tipe integer
def convert(word, dictionary):
    to_return = ""
    for character in word:
        to_return += dictionary.get(character) # Mengambil value dari karakter pada dictionary
    return int(to_return)

# Menghitung jika hasil penjumlahan cryptarithmetic dengan skema brute force benar atau tidak
# Mengembalikan value True or False
def calculate(word_list, result, dictionary):
    calculated = 0
    for word in word_list:
        calculated += convert(word, dictionary)
    return calculated == convert(result, dictionary)

# Menghasilkan dictionary korespondensi tiap karakter dengan angka yang merupakan solusi dari
# Cryptarithmetic Problem yang diberikan
# Tidak digunakan karena telah dibuat algoritma yang lebih cepat (cryptarithmetic_solve_another)
def cryptarithmetic_solve(local_tuple):
    return_dictionary = {}
    return_count = 0
    words = local_tuple[0]
    result = local_tuple[1]
    allwords = []
    for element in words:
        allwords.append(element)
    allwords.append(result)
        # Menggabungkan tuple menjadi sebuah list untuk digunakan selanjutnya
    onlywords = join_words(allwords)
        # Menggabungkan tiap elemen dalam list allwords menjadi satu string
        # Misal : ['SEND', 'MORE', 'MONEY']
        # Menjadi : 'SENDMOREMONEY'
    unique_letters = join_words(set(onlywords))
        # Membuat string onlywords menjadi sebuah set dengan elemen unik dan kemudian 
        # dijadikan string untuk dibuat dictionary
        # Misal : 'SENDMOREMONEY'
        # Menjadi : 'EODSYMNR'
    first_letters = get_firstletters(allwords)
    first_letters = list(dict.fromkeys(first_letters))
        # Menghilangkan duplikat karakter pertama tiap kata pada soal
        # Misal Soal : Send + More = Money
        # Menjadi : ['S', 'M']
        # Membuat list yang berisi karakter pertama tiap kata (agar tidak 0)
    permutations_list = permutation(len(unique_letters))
    found_solution = False # Indikator jika solusi sudah ditemukan
    # Algoritma brute force, mencoba seluruh kemungkinan tiap karakter pada soal
    for element in permutations_list:
        return_count += 1 # Menghitung berapa percobaan yang dilakukan
        zero_first_letter = False # Indikator jika hasil fungsi permutation menghasilkan huruf pertama yang bernilai 0
        dictionary = dict(zip(unique_letters, str(element)))
            # Menghasilkan dictionary korespondensi tiap karakter dengan angka
            # hasil dari fungsi permutation, yaitu permutations_list
            # Misal dua string yaitu "STR" dan "123"
            # Maka hasil dictionarynya adalah: {'S' : '1', 'T' = '2', 'R' = '3'}
            # Tiap key dan tiap valuenya ber-tipe str
        for letter in first_letters:
            if int(dictionary.get(letter)) == 0 :
                zero_first_letter = True
                # Mengecek jika huruf pertama soal Cryptarithmetic memiliki value 0 pada dictionary
                # Jika True, maka tidak dihitung
        if zero_first_letter == True:
            continue
        else:
            found_solution = calculate(words, result, dictionary)
            # Menghitung tiap hasil fungsi permutation untuk soal
            # Menghasilkan True or False
        if found_solution == True:
            return_dictionary = dictionary
            break
    if found_solution == False: # Jika solusi tidak ditemukan
        return None
    else:
        return return_dictionary, return_count

# Algoritma kedua lebih cepat untuk mendapatkan hasilnya
def cryptarithmetic_solve_another(local_tuple):
    return_dictionary = {}
    return_count = 0
    words = local_tuple[0]
    result = local_tuple[1]
    allwords = []
    for element in words:
        allwords.append(element)
    allwords.append(result)
        # Menggabungkan tuple menjadi sebuah list untuk digunakan selanjutnya
    onlywords = join_words(allwords)
        # Menggabungkan tiap elemen dalam list allwords menjadi satu string
        # Misal : ['SEND', 'MORE', 'MONEY']
        # Menjadi : 'SENDMOREMONEY'
    unique_letters = join_words(set(onlywords))
        # Membuat string onlywords menjadi sebuah set dengan elemen unik dan kemudian 
        # dijadikan string untuk dibuat dictionary
        # Misal : 'SENDMOREMONEY'
        # Menjadi : 'EODSYMNR'
    if len(unique_letters) > 10 :
        return None
    first_letters = get_firstletters(allwords)
    first_letters = list(dict.fromkeys(first_letters))
        # Menghilangkan duplikat karakter pertama tiap kata pada soal
        # Misal Soal : Send + More = Money
        # Menjadi : ['S', 'M']
        # Membuat list yang berisi karakter pertama tiap kata (agar tidak 0)
    for permute in range(10**(len(unique_letters) - 1), 10**len(unique_letters)):
        # Mencoba kemungkinan kombinasi angka yang mungkin sesuai banyaknya huruf yang unik pada persoalan
        # For loop ini mencoba untuk mereplikasi permutasi angka 0 sampai dengan 9 tanpa repetisi sesuai banyak huruf yang unik pada soal Cryptarithmetic
        if len(set(str(permute))) == len(unique_letters):
            # Mengecek jika integer yang di-generate merupakan angka yang unik tanpa repetisi angka
            return_count += 1
            zero_first_letter = False # Indikator jika huruf pertama pada sebuah kata bernilai 0
            dictionary = dict(zip(unique_letters, str(permute))) 
                # Menghasilkan dictionary korespondensi tiap karakter dengan angka
                # hasil dari fungsi permutation, yaitu permutations_list
                # Misal dua string yaitu "STR" dan "123"
                # Maka hasil dictionarynya adalah: {'S' : '1', 'T' = '2', 'R' = '3'}
                # Tiap key dan tiap valuenya ber-tipe str
            for letter in first_letters:
                if int(dictionary.get(letter)) == 0:
                    zero_first_letter = True
            if zero_first_letter == True:
                continue
            else:
                found_solution = calculate(words, result, dictionary)
                    # Menghitung tiap hasil fungsi permutation untuk soal
                    # Menghasilkan True or False
            if found_solution == True: # Jika solusi ditemukan
                return_dictionary = dictionary
                # return_dictionary menjadi dictionary yang berisi solusi dari soal Cryptarithmetic
                break
        else:
            continue
    if found_solution == False:
        return None
    else:
        return return_dictionary, return_count # Tuple (Dictionary, Integer)
        # Mengembalikan dalam bentuk Tuple seperti di atas ^

# Fungsi untuk output solusi dari soal Cryptarithmetic
def print_solution(words, result, dictionary, count, time):
    word_list = []
    for word in words:
        word_list.append(convert(word, dictionary))
    print("Solusi:")
    print(dictionary.__str__().replace("{", "").replace("}", "").replace("'", ""))
        # Format hasil output dictionary agar menghilangkan "{" dan "}"
    print(*word_list, sep = " + ", end = " = ")
    print(convert(result, dictionary))
    print("Jumlah percobaan :", count, "kali")
    print("Waktu percobaan  :", time, "detik")

## Main Program

print("List nama file berada pada folder test")
print("List nama file : test, test2, test3, test4, test5, test6, test7, test8, test9, test10, test11, testdummy, testdummy2")
print("Silahkan input nama file Cryptarithmetic yang akan diselesaikan")

nama_file = input()
problem = read_file(nama_file + '.txt') # Pembacaan file
    # Untuk mengganti soal yang akan dikerjakan, jalankan program dan tuliskan nama file yang ingin diselesaikan
    # List nama file: test, test2, test3, test4, test5, test6, test7, test8, test9, test10, test11 (semua dalam format .txt)
    # testdummy.txt = Contoh soal tanpa solusi, testdummy2.txt = Contoh soal dengan lebih dari 10 karakter unik

print("Soal:")
words = problem[0]
result = problem[1]
print(*words, sep = " + ", end = " = ")
    # Meng-output list dengan separator tiap elemen " + " dan tanpa newline
print(result)
    # Hasil format : Kata1 + Kata2 + ... = KataHasil
print("")

starttime = time.time() # Waktu mulai
solution = cryptarithmetic_solve_another(problem)
endtime = time.time() # Waktu selesai
runtime = endtime - starttime # Menghitung runtime program yang dijalankan (Algoritma brute force)
    # Tidak termasuk membaca input dari file
if solution != None:
    print_solution(words, result, solution[0], solution[1], runtime)
else:
    print("Tidak ada solusi untuk persoalan Cryptarithmetic di atas")

# Agar executable file tidak langsung tertutup setelah output selesai
close_console = input("Ketik apapun lalu tekan Enter untuk menutup program\n")