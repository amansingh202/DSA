def binary2dec(n):
    result = 0

    power = len(n) - 1

    for digit in n:
        if digit == '1':
            result = result + 2**power
        power -= 1

    return result


print(binary2dec('1011'))

