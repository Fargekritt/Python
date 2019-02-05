#!/usr/bin/env checkio --domain=py run the-longest-palindromic

# https://py.checkio.org/mission/the-longest-palindromic/

# Write a function that finds the longestpalindromicsubstring of a given string. Try to be as efficient as possible!
# 
# If you find more than one substring you should return the one which is closer to the beginning.
# 
# Input:A text as a string.
# 
# Output:The longest palindromic substring.
# 
# Precondition:1 ≤ |text| ≤ 20
# The text contains only ASCII characters.
# 
# 
# END_DESC

def longest_palindromic(text):
    results = list()
    text_length = len(text)
    longest = ""
    for idx, char in enumerate(text):
        #finds all the odd length palindromics    
        start, end = idx - 1,idx + 1
        while start >= 0 and end < text_length and text[start] == text[end]:
            results.append(text[start:end+1])
            start -= 1
            end += 1
        #finds all the even length palindromics      
        start, end = idx, idx + 1
        while start >= 0 and end < text_length and text[start] == text[end]:
            results.append(text[start:end+1])
            start -= 1
            end += 1
    #fail safe for when there is no palindromic with more char then 1
    if len(results) == 0:
        results.append(text[0])
    #find the longest palindromic since list are in order if two words are the same length the first one will be "longest"
    for x in results:
        if len(x) > len(longest):
            longest = x
    return longest

if __name__ == '__main__':
    assert longest_palindromic("artrartrt") == "rtrartr", "The Longest"
    assert longest_palindromic("abacada") == "aba", "The First"
    assert longest_palindromic("aaaa") == "aaaa", "The A"