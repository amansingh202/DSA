#brute force approach

def dec2bin(n):
    result = ''
    while n > 0:
        if (n % 2 == 1):
            result += '1'
        else:
            result += '0'

        n //= 2

    result = result[::-1]
    return result

binary = dec2bin(13)
print(binary)

def set_or_notSet(binary, index):
    n = len(binary)

    pos = n - index - 1

    if binary[pos] == '1':
        return True
    else:
        return False

print(set_or_notSet(binary, 2))