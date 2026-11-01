def count_digits(n):
    if n < 10:
        return 1

    return 1 + count_digits(n // 10)


def power(base, exponent):
    if exponent == 0:
        return 1

    return base * power(base, exponent - 1)


def is_palindrome(text):
    if len(text) <= 1:
        return True
    if text[0] != text[-1]:
        return False

    return is_palindrome(text[1:-1])

if __name__ == "__main__":
    number = int(input("Enter a number: "))
    print(f"Number of digits in {number}: {count_digits(number)}")

    base = int(input("Enter the base: "))
    exponent = int(input("Enter the exponent: "))
    print(f"{base} raised to the power of {exponent} is: {power(base, exponent)}")

    text = input("Enter a string to check if it's a palindrome: ")
    if is_palindrome(text):
        print(f"{text} is a palindrome.")
    else:
        print(f"{text} is not a palindrome.")