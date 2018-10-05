from intros import *

DATA_PATH = "../data/"
BOOKS = ["jungle_book.txt", "second_jungle_book.txt"]

SEARCH_TERM = "Shere Khan"

results = []

for book in BOOKS:
    lines = read_txt_file_to_list(DATA_PATH+book)
    for line in lines:
        if SEARCH_TERM in line:
            results.append(line.replace(SEARCH_TERM, "\t"+SEARCH_TERM+"\t"))

for result in results:
    print(result)
