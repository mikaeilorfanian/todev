from helpers import full_test_file_path
from todev.main import annotate_all_lines, annotate_todo_line, read_user_file
from todev.tags import (
    annotated_tag,
    get_annotated_tag_from_line,
    get_line_body,
    get_tag_name_from_line,
    TODO,
)


class TestAnnotateTodoLineFunction:

    def test_processed_line_has_correct_tag(self):
        line = 'this is my first todo'

        processed_line = annotate_todo_line(line)
        assert annotated_tag(TODO) == get_annotated_tag_from_line(processed_line, TODO)


TODO_LINE = 'todo this and that'


def test_get_tag_name_from_line():
    assert get_tag_name_from_line(TODO_LINE) == TODO


class TestGetLineBodyFunction:

    def test_line_body_doesnt_include_tag(self):
        assert get_line_body(TODO_LINE) == 'this and that'



class TestOutput:

    def test_one_todo_line_text_file(self):
        file_name = full_test_file_path('notes1.txt')

        annotated_lines = annotate_all_lines(read_user_file(file_name))
        assert len(annotated_lines) == 1
        assert annotated_lines[0] == '<todo> first task'

    def test_one_line_with_no_tags(self):
        file_name = full_test_file_path('notes2.txt')

        annotated_lines = annotate_all_lines(read_user_file(file_name))
        assert len(annotated_lines) == 1
        assert annotated_lines[0] == 'first task'

    def test_two_lines_one_line_is_simple_note_another_is_todo(self):
        file_name = full_test_file_path('notes3.txt')

        annotated_lines = annotate_all_lines(read_user_file(file_name))
        assert len(annotated_lines) == 2
        assert annotated_lines[0] == '<todo> first task'
        assert annotated_lines[1] == 'random note'
