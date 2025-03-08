def count_digits(number):
    return len(str(abs(number)))
number = int(input("Enter a number: "))
digit_count = count_digits(number)
print(f"The number {number} has {digit_count} digits.")