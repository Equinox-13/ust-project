
def generate_numbers_divisible_by_5_and_7(n):
    """
    Generate numbers between 0 and the given number (inclusive) that are divisible by both 5 and 7.

    :param n: The upper limit for the range of numbers.
    :return: A generator yielding numbers divisible by both 5 and 7.
    """
    for num in range(n+1):
        if num % 5 == 0 and num % 7 == 0:
            yield num
