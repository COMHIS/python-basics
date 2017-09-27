# Now we import two additional functions, one for reading from a file
# and another for writing into one.
from intros import (read_txt_file_to_list,
                    write_lines_into_txt_file)

inputfile = "the_idiot.txt"
# MODIFY HERE. Look at the inputfile -variable. Assign the outputfile -variable
# below a filename too in the same way-
# a different one of course, and ending with .txt also.
outputfile = "CHANGETHIS"
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
write_lines_into_txt_file(filename=CHANGETHIS,
                          lines=CHANGETHIS)

