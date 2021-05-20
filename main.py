# use https://www.rapidtables.com/convert/number/roman-numerals-converter.html to understand calculations

RD_MAP = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}


def roman_to_decimal(roman):

    decimal = 0
    
    roman_len = len(roman)
    invalid_str_message = "Please enter a valid Roman numeral string"

    for i, char_1 in enumerate(roman):

        try:
            char_1_value = RD_MAP[char_1]
        except KeyError:
            return invalid_str_message

        if i >= roman_len - 1:
            decimal += char_1_value
            break

        try:
            char_2_value = RD_MAP[roman[i + 1]]
        except KeyError:
            return invalid_str_message

        if char_2_value > char_1_value and char_2_value //



if __name__ == "__main__":
    roman = input("Enter the Roman numeral string: ")
    print(roman_to_decimal(roman))
