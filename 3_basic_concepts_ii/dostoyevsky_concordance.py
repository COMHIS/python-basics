from intros import (read_txt_file_to_list,
                    write_lines_into_txt_file)

inputfile = "brothers_karamazov.txt"
outputfile = "karamazov_concordance.tsv"
search_term = 'suddenly'

lines = read_txt_file_to_list(inputfile)

outlines = []
lines_processed = 0

for line in lines:
    lines_processed += 1
    find_index = line.lower().find(search_term)

    if find_index != -1:
        outlines.append(
            str(lines_processed) + "\t" +
            line[:find_index] +
            '\t' + line[find_index:find_index + len(search_term)] +
            '\t' +
            line[find_index + len(search_term):])

write_lines_into_txt_file(filename=outputfile,
                          lines=outlines)
