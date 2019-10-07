import random
def password_generator():
    passwords = '' # password warehouse
    alphabets = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') #alphab # et inventory
    numbers= list('1234567890') #numericals inventory
    symbols= list("/.,;'\][=-`<?><:|}{+_!@$%^&*()~}") # special character inventory
    for x in range(20): # for producing 20 passwords
        for c in range(5):                           '''
            passwords+=(random.choice(alphabets))
        for c in range(3):
            passwords+=(random.choice(numbers))
        for c in range(2):
            passwords+=(random.choice(symbols))
        print(passwords)
        passwords = ''
    return ''
    
print(password_generator())
print(input('__Press enter to quit__'))
