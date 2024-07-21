#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys

def word_count_dict(filename):
    """Reads a file and builds and returns a word/count dict for it."""
    word_count = {}
    with open(filename, 'r') as file:
        for line in file:
            words = line.lower().split()
            for word in words:
                word = word.strip('.,!?";:()[]{}')  # strip punctuation
                if word:
                    if word in word_count:
                        word_count[word] += 1
                    else:
                        word_count[word] = 1
    return word_count

def print_words(filename):
    """Prints words and their counts sorted by word."""
    word_count = word_count_dict(filename)
    for word in sorted(word_count.keys()):
        print(f'{word} {word_count[word]}')

def print_top(filename):
    """Prints the top 20 most common words sorted by count."""
    word_count = word_count_dict(filename)
    sorted_words = sorted(word_count.items(), key=lambda item: item[1], reverse=True)
    for word, count in sorted_words[:20]:
        print(f'{word} {count}')

def main():
  

if __name__ == '__main__':
    main()
