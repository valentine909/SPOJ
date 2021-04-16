from collections import Counter
vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'


def encrypt(message):
    count_dictionary = Counter()
    output = ""
    for char in message:
        count_dictionary[char] += 1
        if char in vowels:
            output += consonants[((count_dictionary[char] - 1) * len(vowels) + vowels.index(char)) % len(consonants)]
        else:
            output += vowels[((count_dictionary[char] - 1) * len(consonants) + consonants.index(char)) % len(vowels)]
    return output


def main(number_of_test_cases):
    for i in range(number_of_test_cases):
        print(encrypt(input()))


if __name__ == '__main__':
    main(int(input()))
