from Tests.Program import assert_equal  # A Test Function


def first_character(word):
    return word[0, 1]


def last_character(word):
    return word[-1]


def middle_characters(word):
    return word[1, -1]


def is_palindrome(word):

    # Base Case 1: If the length of the string is '0' or '1', the string is palindrome
    if len(word) <= 1:
        return True

    # Base Case 2:  If the first and last characters of a string are different, then
    # we know immediately that the string is not a palindrome
    if first_character(word) != last_character(word):
        return False

    # Recursive Case: Use the substring remaining after removing the first and
    # last character to call the function from within the function
    return is_palindrome(middle_characters(word))


def check_palindrome(testString):
    print("Is this word a palindrome? ", testString)
    print(is_palindrome(testString))


# Tests
check_palindrome('s')
assert_equal(is_palindrome('s'), True)

check_palindrome('motor')
assert_equal(is_palindrome('motor'), False)

check_palindrome('tattarrattat')
assert_equal(is_palindrome('tattarrattat'), True)

check_palindrome('AmberHeard')
assert_equal(is_palindrome('AmberHeard'), False)

