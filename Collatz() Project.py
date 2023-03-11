# Collatz function
def collatz(number):
    if number % 2 == 0:  # check if number is even
        result = number // 2
        print(result)
        return result
    else:  # number is if it isnt even odd
        result = 3 * number + 1
        print(result)
        return result


while True: # Creates loop to ensure input can be made into an integer
    try:
        num = int(input("Enter a number: "))
        break # breaks loop if code is int
    except ValueError: ''' if value error occurs due to str or float not being able to be turned into int,
                            prints error and returns you to step 1'''
        print('Enter a integer')

while True: # creates loop, returning value until collatz(num) == 1
    if collatz(num) != 1:
        num = collatz(num)
        collatz(num)
    else:
        print('Reached 1')
        break
