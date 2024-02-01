
def interleave_strings(string_1, string_2):
    """
    Interleaves characters from two strings.

    :param string_1: first input string
    :param string_2: second input string
    :return: interleaved string
    """
    result = ''
    for i, j in zip(string_1, string_2):
        result = result + i + j

    if len(string_1) > len(string_2):
        result = result + string_1[len(string_2):]
    elif len(string_2) > len(string_1):
        result = result + string_2[len(string_1):]

    return result
