from scan_line import scan_row

GRID = [
    ['.', '.', '4', '2', '6', '.', '.'],
    ['3', '2', '1', '.', '.', '.', '.'],
    ['.', '.', '.', '3', '.', '2', '1'],
]


def test_retrieving_middle_row_digits():
    row = 0 
    column = 3

    result = scan_row(row, column, GRID)
    assert result == '426'


def test_retrieving_start_row_digits():
    row = 1
    column = 2

    result = scan_row(row, column, GRID)
    assert result == '321'


def test_retrieving_end_row_digits():
    row = 2
    column = 5

    result = scan_row(row, column, GRID)
    assert result == '21'


def test_retrieving_isolated_digits():
    row = 2
    column = 3

    result = scan_row(row, column, GRID)
    assert result == '3'

