def is_armstrong_number(number):
    digit_num = len(str(abs(number)))
    arms = 0
    num = number
    while(num != 0):
        last_digit = num % 10
        arms += last_digit ** digit_num
        num //= 10
    if (arms == number):
        return True
    else: return False
