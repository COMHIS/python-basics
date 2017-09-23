# Here we import a command that we defined in another script.
# This will be covered in more detail in part 3.
from intros import read_txt_file_to_list

inputfile = "the_idiot.txt"
# MODIFY HERE.
# Make the search_term - variable equal to the word we want to search for
search_term = "suddenly"

# We use the command we loaded from the another script to create a list
# of lines of text- a list of string-type variables. Lists will be covered
# properly next time.
lines = read_txt_file_to_list(inputfile)

# this here keeps track of how manyu lines have we found. We start at 0
total_lines_found = 0

# This here is a loop, another form of flow control. That too will be covered
# in the next part.
for line in lines:
    # The find() command returns the 'index' of the term that we are searching
    # for, or -1 if the term was not found at all.
    find_index = line.find(search_term)
    # MODIFY HERE.
    # We want the following if-statement to run if find_index does not equal -1
    # remember the operators? choose a correct one and put it on the following
    # line in place of the CHANGETHIS -text.
    if find_index CHANGETHIS -1:
        # If the word is found, we add one to total_lines_found and reassing
        # that value.
        total_lines_found = total_lines_found + 1

print("Total " +
      str(total_lines_found) +
      " lines with the term \"" +
      # MODIFY HERE.
      # change CHANGETHIS on the following line to the variable holding the
      # name of the term we were looking for.
      CHANGETHIS +
      "\" found."
      )
