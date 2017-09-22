from intros import (read_txt_file_to_list,
                    write_lines_into_txt_file)

inputfile = "the_idiot.txt"
outputfile = "idiot_concordance.txt"
search_term = 'suddenly'

lines = read_txt_file_to_list(inputfile)

outlines = []

for line in lines:
    find_index = line.find(search_term)
    if find_index != -1:
        outlines.append(
            line[:find_index] +
            '\t' + search_term + '\t' +
            line[find_index + len(search_term):])

write_lines_into_txt_file(outputfile, outlines)

# Next, lets do some quantitative analysis of that text.

# First lets get the total number of occurences of the search term.
# We'll loop through all the lines, and add one to an index if the
# search term is found.

occurences = 0
for line in lines:
    find_index = line.find(search_term)
    if find_index != -1:
        occurences = occurences + 1

# let's print that result
print(search_term + " found " + str(occurences) + " times")

# but wait! that counts only exact matches, and we should not care about case
# eg. 'suddenly' is a match, but 'Suddenly' is not.
# ... so let's convert that original text to lower case before searching:

occurences_lower = 0
for line in lines:
    line_lower = line.lower()
    find_index = line_lower.find(search_term)
    if find_index != -1:
        occurences_lower = occurences_lower + 1

print(search_term + " now found " + str(occurences_lower) + " times")

# And let's get a frequency for that now:
frequency = occurences_lower / len(lines)

print("Freq: " + str(frequency))

# And finally, let's find out how this maps out on the text.
# We'll count the frequency for each point in the text,
# and add those to a list.

rolling_freq = []
occurences_so_far = 0
lines_processed = 0

for line in lines:
    lines_processed = lines_processed + 1
    find_index = line.lower().find(search_term)
    if find_index != -1:
        occurences_so_far = occurences_so_far + 1
    current_freq = occurences_so_far / lines_processed
    rolling_freq.append(current_freq)

# Finally we will save the results in a file.
# For that we need to convert it to string and add newlines.
rolling_freq_str = []
for item in rolling_freq:
    rolling_freq_str.append(str(item) + "\n")

write_lines_into_txt_file("rolling_freq.txt", rolling_freq_str)

#
