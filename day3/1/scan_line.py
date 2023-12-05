VALID_INTEGERS = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')


def scan_row(row, column, grid):
    """Find adjacent integers of a (row,column) coordinate.

    Scan a line, ['.', '.', 4, 2, 6, '.'] to extract int(426), given
    any coordinate of either the value 4, 2 or 6.
    
    The '.' symbol is a terminator, meaning there are no more digits.
    """

    # Check if any digits to the left
    start_column = find_start_column(grid[row], column)
    end_column = find_end_column(grid[row], column)

    return ''.join(grid[row][start_column:end_column+1])


def find_start_column(row, column):
    start_column = column

    try:
        while row[start_column-1] in VALID_INTEGERS:
            start_column = start_column-1
    except IndexError:
        # If the first VALID_INTEGER is in the start column
        # finding the next column results in an error.
        pass

    return start_column


def find_end_column(row, column):
    end_column = column

    try:
        while row[end_column+1] in VALID_INTEGERS:
            end_column = end_column+1
    except IndexError:
        # If the last VALID_INTEGER is in the end column
        # finding the next column results in an error.
        pass

    return end_column
