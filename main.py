# Complexity is equal to O(n)
def max_of_one_digit_ints(integers):
    max_one_digit = -10
    for i in integers:
        if i > -10 and i < 10 and i > max_one_digit:
            max_one_digit = i
    return None if max_one_digit == -10 else max_one_digit


# Complexity is equal to O(n)
def max_number_of_candies_types(candies):
    number_candies_types = len(set(candies))
    number_candies_shared = len(candies) / 2
    return min(number_candies_shared, number_candies_types)


# 
def digits_sequence(n):
    if n >= 0:
        if n <= 1:
            return n
        else:
            count = 2
            n2 = 0
            n1 = 1
            while (count <= n):
                nth = sum_digits(n2) + sum_digits(n1)
                n2 = n1
                n1 = nth
                count += 1
            return nth


# Sum of digits of a number
def sum_digits(number):
    digits = [int(digit) for digit in str(number)]
    return sum(digits)


if __name__ == '__main__':
    assert max_of_one_digit_ints(
        [-6, -91, 1011, -100, 84, -22, 0, 1, 473]) == 1
    assert max_of_one_digit_ints(
        [-66, -91, 1011, -100, 84, -22, 13, 473]) == None

    assert max_number_of_candies_types([3, 4, 7, 7, 6, 6]) == 3

    # All candies are different
    assert max_number_of_candies_types([3, 4, 6, 7, 8, 9]) == 3
    # Mary and her brither share the same variety of candies
    assert max_number_of_candies_types([3, 4, 3, 4, 6, 6]) == 3
    # All canies are the same
    assert max_number_of_candies_types([3, 3, 3, 3, 3, 3]) == 1

    assert digits_sequence(0) == 0
    assert digits_sequence(1) == 1
    assert digits_sequence(2) == 1
    assert digits_sequence(3) == 2
    assert digits_sequence(6) == 8
    assert digits_sequence(10) == 10
    assert digits_sequence(11) == 8
