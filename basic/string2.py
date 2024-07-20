#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Additional basic string exercises

# D. verbing
def verbing(s):
    if len(s) >= 3:
        if s.endswith('ing'):
            return s + 'ly'
        else:
            return s + 'ing'
    return s


# E. not_bad
def not_bad(s):
    not_index = s.find('not')
    bad_index = s.find('bad')
    if not_index != -1 and bad_index != -1 and bad_index > not_index:
        return s[:not_index] + 'good' + s[bad_index + 3:]
    return s


# F. front_back
def front_back(a, b):
    def split_string(s):
        mid = (len(s) + 1) // 2  # if odd, front half gets the extra char
        return s[:mid], s[mid:]
    
    a_front, a_back = split_string(a)
    b_front, b_back = split_string(b)
    
    return a_front + b_front + a_back + b_back


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# main() calls the above functions with interesting inputs,
# using the above test() to check if the result is correct or not.
def main():
    print('verbing')
    test(verbing('hail'), 'hailing')
    test(verbing('swiming'), 'swimingly')
    test(verbing('do'), 'do')

    print()
    print('not_bad')
    test(not_bad('This movie is not so bad'), 'This movie is good')
    test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
    test(not_bad('This tea is not hot'), 'This tea is not hot')
    test(not_bad("It's bad yet not"), "It's bad yet not")

    print()
    print('front_back')
    test(front_back('abcd', 'xy'), 'abxcdy')
    test(front_back('abcde', 'xyz'), 'abcxydez')
    test(front_back('Kitten', 'Donut'), 'KitDontenut')

if __name__ == '__main__':
    main()
