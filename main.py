RD_MAP = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}


def roman_to_decimal(roman):

    for i, char in enumerate(roman):
        print(i, char)

    return "thanks!"


if __name__ == "__main__":
    roman = input("Enter the Roman numeral string: ")
    print(roman_to_decimal(roman))
