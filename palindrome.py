def palindrome(x):
    """
    checks if the input string is a palindrome
    """
    return x == x[::-1]

def display_palindrome(x):
    """
    display an explanation about why the input string
    is or is not a palindrome
    """
    print(x)
    y = x[::-1]
    print(y)
    if x == y:
        print('ok')
    else:
        for cx, cy in zip(x, y):
            print(" " if cx==cy else '^', end='')
        print()

if __name__ == '__main__':
    print(f"{palindrome('kayak')=}")
    print(f"{palindrome('follet')=}")
    display_palindrome('kayak')
    display_palindrome('follet')
