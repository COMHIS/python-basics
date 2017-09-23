# Now we import two additional functions, one for reading from a file
# and another for writing into one.
from intros import (read_txt_file_to_list,
                    write_lines_into_txt_file)

inputfile = "the_idiot.txt"
# MODIFY HERE. Look at the inputfile -variable. Assign the outputfile -variable
# below a filename too- a differnt one of course, and ending with .txt also.
outputfile = "idiot_concordance.txt"
search_term = 'suddenly'

lines = read_txt_file_to_list(inputfile)

# Now, instead of adding to a number when a line is found we add the line
# to a list. outlines = [] is an empty list that will store our results.
outlines = []
# We'll also keep track of the line number:
lines_processed = 0

for line in lines:
    # for each line, grow the number of lines processed by one.
    # += 1 is a shortcut to growing a number by one, and identical to
    # lines_processed = lines_processed + 1
    lines_processed += 1
    find_index = line.lower().find(search_term)
    if find_index != -1:
        # For each hit we add a line to our results, with the search
        # term flanked by tabs and the index of the line leading.
        # We are doing something called string slicing (= cutting a text
        # into smaller chunks) below.
        # More on that next time.
        outlines.append(
            str(lines_processed) + "\t" +
            line[:find_index] +
            '\t' + line[find_index:find_index + len(search_term)] + '\t' +
            line[find_index + len(search_term):])

# MODIFY HERE.
# Our results are stored in the outlines -variable, and should be written
# in the outputfile we specified earlier. write_lines_into_txt_file
# -function takes two variables as "parameters", file to write into and the
# data to be written there. We'll go into functions in more detail next time-
# for now fill in the names of those variables in their correct places.
write_lines_into_txt_file(filename=outputfile,
                          lines=outlines)

# # Next, lets do some quantitative analysis of that text.

# # First lets get the total number of occurences of the search term.
# # We'll loop through all the lines, and add one to an index if the
# # search term is found.

# occurences = 0
# for line in lines:
#     find_index = line.find(search_term)
#     if find_index != -1:
#         occurences = occurences + 1

# # let's print that result
# print(search_term + " found " + str(occurences) + " times")

# # but wait! that counts only exact matches, and we should not care about case
# # eg. 'suddenly' is a match, but 'Suddenly' is not.
# # ... so let's convert that original text to lower case before searching:

# occurences_lower = 0
# for line in lines:
#     line_lower = line.lower()
#     find_index = line_lower.find(search_term)
#     if find_index != -1:
#         occurences_lower = occurences_lower + 1

# print(search_term + " now found " + str(occurences_lower) + " times")

# # And let's get a frequency for that now:
# frequency = occurences_lower / len(lines)

# print("Freq: " + str(frequency))

# # And finally, let's find out how this maps out on the text.
# # We'll count the frequency for each point in the text,
# # and add those to a list.

# rolling_freq = []
# occurences_so_far = 0
# lines_processed = 0

# for line in lines:
#     lines_processed = lines_processed + 1
#     find_index = line.lower().find(search_term)
#     if find_index != -1:
#         occurences_so_far = occurences_so_far + 1
#     current_freq = occurences_so_far / lines_processed
#     rolling_freq.append(current_freq)

# # Finally we will save the results in a file.
# # For that we need to convert it to string and add newlines.
# rolling_freq_str = []
# for item in rolling_freq:
#     rolling_freq_str.append(str(item) + "\n")

# write_lines_into_txt_file("rolling_freq.txt", rolling_freq_str)

# #
