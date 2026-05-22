def is_armstrong_number(number):
    # get the digit number
    digit_num = len(str(abs(number)))
    
    arms = 0
    num = number

    # do addition for armstrong number
    while num != 0:
        last_digit = num % 10
        arms += last_digit ** digit_num
        num //= 10

    # compare
    if arms == number:
        return True
    return False
