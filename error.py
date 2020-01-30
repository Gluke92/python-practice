# Error handling

while True:
    try:
        age = int(input('what is your age? '))
        10/age
    except ValueError:
        print('YOU HAVE AN ERROR BRO. ENTER A NUMBER!')
    except ZeroDivisionError:
        print('YOU HAVE AN ERROR BRO. ENTER A NUMBER!')
    # except block will run only one of hte errors, so if we repeat Value, no go
    # consult docs for more errors
    else:
        print('thanks!')
        break

    # We need this last guy to leave

# how can we clean this?


def sum1(num1, num2):
    return num1 + num2

#print(sum1('1', 2))

# try a try-catch block


def sum2():
    num1 = input("Enter num1")
    num2 = input("Enter num2")
    try:
        if num1 is int and num2 is int:
            return num1 + num2
        else:
            raise ValueError
    except ValueError as err:
        # except (ValueError, TypeError) as err => will return whichever err errored
        # Can be used in place of just mentioning one
        print(f'Please enter two numbers, and try again. Error: {err}')


print(sum2())

while True:
    try:
        age = int(input('what is your age? '))
        10/age
        # raise ValueError('hey cut it out') => throws err to console
        # raise Exception('hey cut it out') => similar to above
    except ZeroDivisionError:
        print('please enter age higher than 0')
        break
    else:
        print('thank you!')
    finally:
        print('ok, i am finally done!')
    print('can you hear me?')
    break
