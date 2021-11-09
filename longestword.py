"""
compute the longest word - or words - in a file
"""

# for punctuation
import string


def longest_word(filename):
    """
    the first one will do
    """
    max_word = ''
    with open(filename) as feed:
        for line in feed:
            for junk in string.punctuation:
                line = line.replace(junk, ' ')
            for word in line.split():
                if len(word) > len(max_word):
                    max_word = word
    return max_word

def longest_words(filename):
    """
    remember them all
    """
    max_words = []
    max_size = 0
    with open(filename) as feed:
        for line in feed:
            for junk in string.punctuation:
                line = line.replace(junk, ' ')
            for word in line.split():
                if len(word) > max_size:
                    max_words = [word]
                    max_size = len(word)
                elif len(word) == max_size:
                    max_words.append(word)
    return max_words
