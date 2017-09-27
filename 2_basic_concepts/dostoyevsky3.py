from intros import (read_txt_file_to_list,
                    write_lines_into_txt_file)

inputfile = "the_idiot.txt"
# MODIFY THIS. Give the following variable filename where to save our results.
# The filename should have an extension .csv for it to be recognised by
# a spreadsheet program. An example would be "idiot_suddenliness.csv".
outputfile = CHANGETHIS
search_term = 'suddenly'

# MODIFY HERE. Change the parameter given to the function read_txt_file_to_list
# to the variable name that holds our input filename. Have a look at the previous
# dostoyevskyX.py -files to get a clue on how this should look.
lines = read_txt_file_to_list(CHANGETHIS)

# MODIFY HERE. give the window_size variable a suitable value, and after running
# the code successfully with one value, try another one and see how the results
# differ. You could try starting with 150, as suggested previously.
window_size = CHANGETHIS

# We are again keeping track of the number of lines processed, and now have two
# lists. One keeps track of the current "window" of lines, and another one is
# a list of results based on how many hits were in the window. Don't worry if this
# seems complicated now, we'll go into more detail on these later.
lines_processed = 0
terms_found_in_window = []
# This is where we save our results:
rolling_window_results = []

for line in lines:
    lines_processed += 1
    find_index = line.lower().find(search_term)
    # If the line has our search term we'll add the number 1 to our list,
    # and if it doesn't we'll add 0. So, our list, which represents our 'window'
    # will start to look something like this: [0, 0, 0, 1, 0, 0, 0, 1] ... etc. 
    if find_index != -1:
        terms_found_in_window.append(1)
    else:
        terms_found_in_window.append(0)
    # when the list of terms found reaches our window size, we
    # need to start dropping off old data from the start:
    if len(terms_found_in_window) == window_size:
        # When we reach our window size, we need to sum the results and
        # save that sum in our list of results.
        lines_hit_in_window = sum(terms_found_in_window)
        rolling_window_results.append(lines_hit_in_window)
        # We also need to keep the window to the correct size, so we will keep on
        # removing the first (meaning the oldest addition) element of our window.
        # The command del removes an element from a list by index. The first
        # element of any list has index of 0, so we are dropping it. 
        del terms_found_in_window[0]

# Now we are again ready to write our results.
# There's one more detail to pay attention to:
# Our writer -function will just mash everything together, so we
# have to tell it to add a character for newline to make the output
# sensible. This was not necessary before, as the source text that we
# modified for our output already had those newlines.

# MODIFY THIS. Like previously, change the filename -parameter to match
# the variable where our output filename is saved.
# also save the lines- parameter to match the variable in which we saved our results.
write_lines_into_txt_file(filename=CHANGETHIS,
                          lines=CHANGETHIS,
                          add_newlines=True)

