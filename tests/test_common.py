import pytest

from RPLCD import common


@pytest.mark.parametrize(['input_', 'lookahead', 'result'], [
    ('hi', 0, [('h',), ('i',)]),
    ('hi', 1, [('h', 'i'), ('i', ' ')]),
    ('hi', 2, [('h', 'i', ' '), ('i', ' ', ' ')]),
    ('', 0, []),
    ('', 1, []),
    ('', 7, []),
])
def test_window_function(input_, lookahead, result):
    assert list(common.sliding_window(input_, lookahead)) == result
