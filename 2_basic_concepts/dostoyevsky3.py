from intros import (read_txt_file_to_list,
                    write_lines_into_txt_file)

inputfile = "the_idiot.txt"
outputfile = "idiot_suddenliness.csv"
search_term = 'suddenly'

lines = read_txt_file_to_list(inputfile)

window_size = 300

lines_processed = 0
terms_found_in_window = []
rolling_window_results = []

for line in lines:
    lines_processed += 1
    find_index = line.lower().find(search_term)
    # like previously we increase the amount of terms found by
    # one if the line satisfies our search criteria.
    if find_index != -1:
        terms_found_in_window.append(1)
    else:
        terms_found_in_window.append(0)
    # when the list of terms found reaches our window size, we
    # need to start dropping off old data from the start:
    if len(terms_found_in_window) == window_size + 1:
        # del removes an element from list by index
        del terms_found_in_window[0]
        # here is also a handly place to add the data to our results
        lines_hit_in_window = sum(terms_found_in_window)
        rolling_window_results.append(lines_hit_in_window)

# Now we are again ready to write our results.
# There's one more detail to pay attention to:
# Our writer -function will just mash everything together, so we
# have to tell it to add a character for newline to make the output
# sensible. This was not necessary before, as the source text that we
# modified for our output already had those newlines.

write_lines_into_txt_file(filename=outputfile,
                          lines=rolling_window_results,
                          add_newlines=True)
