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
import os

#====================================SOLUTION STARTS====================================
# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

# This function opens the file and return a word/count dict
def word_count_dict(filename):
  word_count = {} # word_count mapping
  
  input_file = open(filename, encoding='utf-8')
  for line in input_file:
    words = line.split()
    for word in words:
      word = word.lower()
      
      # Check if we have seen this word before
      if not word in word_count:
        word_count[word] = 1
      else:
        word_count[word] = word_count[word] + 1
  return word_count

# This function print out and sort the words
def print_words(filename):
  word_count = word_count_dict(filename)
  words = sorted(word_count.keys()) #Sort
  for word in words:
    print(word, word_count[word])

# Return count tuple
def get_count(word_count_tuple):
  return word_count_tuple[1]

def print_top(filename):
    """Prints the top 20 most common words sorted by their count in descending order."""
    word_count = read_file_and_count_words(filename)
    most_common_words = word_count.most_common(20)
    for word, count in most_common_words:
        print(f"{word} {count}")

  # Print the first 20
  for item in items[:20]:
    print(item[0], item[1])

#====================================SOLUTION END====================================
    
# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
  if len(sys.argv) != 3:
    print('usage: ./wordcount.py {--count | --topcount} file')
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print('unknown option: ' + option)
    sys.exit(1)

  # Keep the input prompt open until a key is pressed
  input("Press Enter to exit...")

if __name__ == '__main__':
  main()
