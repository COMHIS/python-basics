from intros import (read_txt_file_to_list,
                    write_dict_to_csvfile)
import string


def strip_punctuation(text):
    # strip out all punctuation characters
    exclude_characters = set(string.punctuation)
    # some add additional characters we want to strip
    exclude_characters = exclude_characters.union(set("“”"))
    for character in exclude_characters:
        text = text.replace(character, "")
    return text


# bonus assignment: make this work with a list of filter words
def filter_term(text_list, term):
    results = []
    for item in text_list:
        if item != term:
            results.append(item)
    return results


inputfile = "brothers_karamazov.txt"
outputfile = "suddenly_2grams.csv"
search_term = 'suddenly'

lines = read_txt_file_to_list(inputfile)

# Join all the separate lines of text into one string
text_combined = ''.join(lines)
# make everything lowercase
text_combined = text_combined.lower()
# strip punctuation
text_combined = strip_punctuation(text_combined)

# Create text tokens
# meaning a list of all the words in the text
text_tokens = text_combined.split()

# later -- let's filter out some of the tokens
text_tokens = filter_term(text_tokens, "a")
text_tokens = filter_term(text_tokens, "the")
text_tokens = filter_term(text_tokens, "and")
text_tokens = filter_term(text_tokens, "in")
text_tokens = filter_term(text_tokens, "to")
text_tokens = filter_term(text_tokens, "as")
text_tokens = filter_term(text_tokens, "with")
text_tokens = filter_term(text_tokens, "from")
text_tokens = filter_term(text_tokens, "at")
text_tokens = filter_term(text_tokens, "for")
text_tokens = filter_term(text_tokens, "that")
text_tokens = filter_term(text_tokens, "into")
text_tokens = filter_term(text_tokens, "an")

tokens_with_search_term_first = []

for i in range(0, len(text_tokens) - 2):
    tokenpair = text_tokens[i:i + 2]
    if search_term == tokenpair[0]:
        tokens_with_search_term_first.append(tokenpair[1])

# find unique terms in our group of terms:
tokens_set = set(tokens_with_search_term_first)
token_counts_dict = {}

for token in tokens_set:
    occurences = tokens_with_search_term_first.count(token)
    token_counts_dict[token] = occurences

write_dict_to_csvfile(token_counts_dict, outputfile)
