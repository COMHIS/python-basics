from intros import (read_txt_file_to_list,
                    write_dict_to_csvfile)
import string

inputfile = "brothers_karamazov.txt"
search_term = 'suddenly'


def strip_punctuation(text):
    # strip out all punctuation characters
    exclude_characters = set(string.punctuation)
    # some add additional characters we want to strip
    exclude_characters = exclude_characters.union(set("“”"))
    for character in exclude_characters:
        text = text.replace(character, "")
    return text


# read our text file into a list
lines = read_txt_file_to_list(inputfile)

# Join all the separate lines of text into one string
text_combined = ''.join(lines)

# make everything lowercase
text_combined = text_combined.lower()

# strip punctuation
text_combined = strip_punctuation(text_combined)

# Create text tokens - that is, a list of all the words in th text
text_tokens = text_combined.split()

# create an empty list
tokens_with_search_term_preceding = []

for i in range(0, len(text_tokens) - 2):
    tokenpair = text_tokens[i:i + 2]
    if search_term == tokenpair[0]:
        tokens_with_search_term_preceding.append(tokenpair[1])

# find unique terms in our group of terms:
tokens_set = set(tokens_with_search_term_preceding)
token_counts_dict = {}

# count the number of occurences for each item in set
for token in tokens_set:
    occurrences = tokens_with_search_term_preceding.count(token)
    token_counts_dict[token] = occurrences

outputfile = "suddenly_2grams.csv"
write_dict_to_csvfile(token_counts_dict, outputfile)
