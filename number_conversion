def number_binary():
    num = int(input('Enter the number: '))
    binary = '0b'
    raw_binary = ''
    if num == 0:
        return '0b0'
    else:
        while num > 1:
            x = num // 2
            raw_binary += str(num % 2)
            num = x
    binary += (raw_binary + '1')[::-1]
    return binary

print(number_binary())


def number_octal():
    num_1 = int(input('enter the number: '))
    octal = '0o'
    raw_octal = ''
    while num_1 > 1:
        y = num_1 // 8
        raw_octal += str(num_1 % 8)
        num_1 = y
    octal += (raw_octal + '1')[::-1]
    return octal
print(number_octal())
