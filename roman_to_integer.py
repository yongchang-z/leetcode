"""
Given a roman numeral, convert it to an integer."""

def romanToInt(s):
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    result = 0
    prev = 0

    for char in s:
        curr = roman_dict[char]
        result += curr

        if curr > prev:
            result -= 2 * prev
        prev = curr
    return result

