import sys

from todev.tags import (
    annotated_tag,
    get_line_body,
    get_tag_name_from_line,
    parse_line,
    TODO,
)

def main():
    file_name = sys.argv[1]
    lines = read_user_file(file_name)
    tag = get_tag_name_from_line(lines[0])
    line_body = get_line_body(lines[0])
    print('tag: ', tag)
    print('line body: ', line_body)


def read_user_file(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()

    return lines


def annotate_all_lines(lines):
    annotated_lines = []
    for line in lines:
        annotated_lines.append(annotate_one_line(line))

    return annotated_lines


def annotate_one_line(line):
    if get_tag_name_from_line(line) == TODO:
        return annotate_todo_line(line)
    else:
        return line.strip()


def annotate_todo_line(line):
    new_line = annotated_tag(TODO) + ' ' + get_line_body(line)
    return new_line


if __name__ == '__main__':
    main()
