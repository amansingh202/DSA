def binary2dec(n):
    result = 0

    power = len(n) - 1

    for digit in n:
        if digit == '1':
            result = result + 2**power
        power -= 1

    return result


#print(binary2dec('1011'))

#or operator
def or_op(n1, n2):
    result = n1 | n2
    return result

#print(or_op(11,13))

#xor operator
def xor_op(n1, n2):
    result = n1 ^ n2
    return result

print(xor_op(11,13))


