TODO = 'todo'
TAG_NAMES = [TODO]


def annotated_tag(tag_name):
    return '<' + tag_name + '>'


def get_tag_name_from_line(line):
    first_word = line.split()[0]
    if first_word in TAG_NAMES:
        return first_word

    return None


def get_annotated_tag_from_line(line, tag_name):
    split_line = line.split()

    for word in split_line:
        if word == annotated_tag(tag_name):
            return word


def parse_line(line):
    tag_name = get_tag_name_from_line(line)
    line_body = get_line_body(line)

    return tag_name, line_body


def get_line_body(line):
    if line_has_tag(line):
        start_index = 1
    else:
        start_index = 0

    if line_has_status(line):
        return ' '.join(line.split()[start_index : -1])
    else:
        return ' '.join(line.split()[start_index:])


def line_has_tag(line):
    return bool(get_tag_name_from_line(line))


def line_has_status(line):
    return False
