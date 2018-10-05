from intros import *

DATA_PATH = "../data/"
BOOKS = ["jungle_book.txt", "second_jungle_book.txt"]
CAP = 100

capitalized = {}
for book in BOOKS:
    lines = read_txt_file_to_list(DATA_PATH+book)
    for line in lines:
        words = line.split(" ")
        for word in words:
            if not word.islower():
                if word not in capitalized:
                    capitalized[word] = 1
                else:
                    capitalized[word] += 1

capitalized_sorted = sorted(capitalized.items(), key=lambda x:x[1], reverse=True)

print(capitalized_sorted[:CAP])
