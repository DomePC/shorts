binary = list(input("Enter a binary number: "))
value = 0
for decimal in range(len(binary)):
    digit = binary.pop()
    if digit == '1':
        value = value + pow(2, decimal)
print(f'The value of the binary number to decimal is {value}')
