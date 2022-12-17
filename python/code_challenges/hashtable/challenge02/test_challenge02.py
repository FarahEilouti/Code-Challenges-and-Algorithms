# Write your test here

import pytest 
from challenge02 import find_first_repeated_word



def test1_find_first_repeated_word():
    string1 = "This is a test string with no repeated words"
    assert find_first_repeated_word(string1) == None


def test2_find_first_repeated_word():
    string2 = "The quick brown fox jumps over the quick dog"
    assert find_first_repeated_word(string2) == 'quick'


def test3_find_first_repeated_word():
    string3 = "this is a trial to know which is the first repeated word in a sentence"
    assert find_first_repeated_word(string3) == 'is'


def test4_find_first_repeated_word():
    string4 = "Write a function that will take a string as a parameter and return the first repeated word in that string."
    assert find_first_repeated_word(string4) == 'a'        