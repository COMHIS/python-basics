import csv


def read_txt_file_to_list(filename):
    with open(filename, 'r', encoding='utf-8') as txtfile:
        lines = []
        for line in txtfile.readlines():
            lines.append(line)
    print("Succesfully read: " + filename)
    return lines


def write_lines_into_txt_file(filename, lines, add_newlines=False):
    with open(filename, 'w', encoding='utf-8') as txtfile:
        for line in lines:
            line = str(line)
            if add_newlines:
                line = line + "\n"
            txtfile.write(line)
    print("Output written to: " + filename)


def write_dict_to_csvfile(dictionary, filename):
    with open(filename, 'w') as csvfile:
        fieldnames = ['key', 'value']
        writer = csv.writer(csvfile)
        writer.writerow(fieldnames)
        for key, value in dictionary.items():
            writer.writerow([key, value])
    print("Dictionary written to: " + filename)
