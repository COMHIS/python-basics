
# Import the modules you need here at the top.
# csv is one for sure.

# Then use csv.DictReader to open the csv file you downloaded ...
# ... reading each line in the csv and adding it to a empty list
# you created for this purpose.


# --- All functions here ---

# Functions are usually defined at the start of a script.
# So, this would be a good place for the function that converts the
# age string to an int. Functions were defined like this:

# def get_age_int(age_str):
#     the_function_code_here...
#     return also_return_something


# --- Data processing here ---

# Iterate over the list of passengers (that you read earlier) and
# convert the ages for each of them with the age function you created.

# Also set the passenger age groups. You can do this in the same loop,
# or oterate over the passenger list again. Remeber to define another
# function to get the age groups and define that in the section above
# where you already defined the age_int function.


# --- Output preparation ---

# Now you have all the data you need for the first output.
# Create a dictionary that will be your output with the age groups as
# keys (so 0, 10, 20, ...) and to start with assign 0 to all of those
# keys.
# Then iterate over the passenger list again, and grow the value at the
# age group output dictionary at the corresponding key by one for each
# passenger.
# check that your output dictionary has what it should have.


# --- Writing the output as csv---

# The final step now is to get the results out from Python. We'll
# write the as a csv table. You can use the commented code below
# for that (but make sure you understand it):

# passenger_age_groups_outfile = "age_group_totals.csv"
# with open(passenger_age_groups_outfile, 'w') as outfile:
#     csvwriter = csv.writer(outfile)
#     csvwriter.writerow(['age_group', 'total'])
#     for key in age_groups_dict.keys():
#         csvwriter.writerow([key, age_groups_dict[key]])


# --- The rest then? ----

# If you managed to get this far and are wondering how to add the
# family -part into the script:
# Add another function for getting the family -status to the
# function definitions at the top. Remember to look back at the
# instructions document on tips for doing that.

# Then, iterate over the passenger list again, updating each
# passenger dictionary with the family -info. You'll have to iterate
# by list index this time (more on this in the instructions too)
# and cover two special cases (first and last entry).

# Then, modify your age group output code to take into account the
# two categories. Also modify the csv writing code, and you should be
# done.
