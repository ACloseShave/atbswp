def collatz(number):
    if number % 2 == 0:
        result = number // 2
        print(result, end=' ')
        return result
    else:
        result = 3 * number + 1
        print(result, end=' ')
        return result

while True:
    print('Enter an integer:')
    try:
        user_input = int(input())
        if user_input < 0:
            raise ValueError('Positive integers only')
        while user_input != 1:
            user_input = collatz(user_input)
        break
    except ValueError:
        print('Error: Invalid value. You must enter a positive whole number only.')