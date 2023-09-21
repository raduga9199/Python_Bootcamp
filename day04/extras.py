print('-------------------closure------------------')


def display_message():
    def method():
        print('Hello World')
        print('I love Python')

    method()
    method()
    method()
    method()


display_message()

print('-----------------------------------------------')


def display_palindromes(strings: list):
    def is_palindrome(s: str) -> bool:
        return s[::-1].lower() == s.lower()

    for s in strings:
        if is_palindrome(s):
            print(s)
        else:
            print('Not palindrome')


print('--------------------map---------------------------')


nums = [10, 20, 30, 40, 50, 60, 70, 80]

nums = list(map( lambda x: x * 10, nums))

print(nums)