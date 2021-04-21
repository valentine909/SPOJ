number_of_cases = int(input())
for _ in range(number_of_cases):
    number_of_phone_numbers = int(input())
    list_of_numbers = []
    for i in range(number_of_phone_numbers):
        list_of_numbers.append(input())
    list_of_numbers.sort()


    def check():
        for j in range(number_of_phone_numbers - 1):
            if list_of_numbers[j + 1].startswith(list_of_numbers[j]):
                return 'NO'
        return 'YES'

    print(check())
