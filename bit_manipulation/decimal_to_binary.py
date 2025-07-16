def dec_2_binary(n):
    result = ""

    while (n > 0):
        if n % 2 == 1:
            result += '1'
        else:
            result += '0'

        n //= 2

    reversed(result)
    return result


print(dec_2_binary(1))