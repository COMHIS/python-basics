def read_txt_file_to_list(filename):
    with open(filename, 'r') as txtfile:
        lines = []
        for line in txtfile.readlines():
            lines.append(line)
    return lines


def write_lines_into_txt_file(filename, lines, add_newlines=False):
    with open(filename, 'w') as txtfile:
        for line in lines:
            line = str(line)
            if add_newlines:
                line = line + "\n"
            txtfile.write(line)
