"""
Problem 17: Number letter counts

If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains  letters and  (one hundred and fifteen) contains  letters.
The use of "and" when writing out numbers is in compliance with British usage.
"""


def get_written(number):
    number_dict = {
        0: "",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety",
    }

    if number < 20:
        return number_dict[number]
    elif number < 100:
        return number_dict[(number // 10 * 10)] + get_written(number % 10)
    elif number < 1000:
        return (
            number_dict[number // 100]
            + "hundred"
            + ("and" + get_written(number % 100) if number % 100 != 0 else "")
        )
    elif number == 1000:
        return get_written(number // 1000) + "thousand"
    else:
        raise ValueError


def solution():
    sum_ = 0
    for number in range(1, 1001):
        sum_ += len(get_written(number))
    return sum_


if __name__ == "__main__":
    print(solution())
