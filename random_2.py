# Given two strings s and t, determine whether some anagram of t is a
# substring of s.
# Here I'm iterating over all the substrings in 's' that are of length 't'.
# Time complexity in this case is O(n) where n is (length of s-length of t)+1 &
#  space complexity is O(t) where t is the length of 't'.

# Method 1 -


def question1(s, t):
    """ returns True if some anagram of 't' is a substring of 's' """
    if s is None or t is None:
        return "Error: Please enter valid strings"
    len_s = len(s)
    len_t = len(t)
    if len_s == 0 or len_s < len_t:
        return "Error: Length of s cannot be smaller than length of t"
    s = s.lower()
    t = t.lower()
    if len_t == 0:
        return True
    t = sorted(t)
    for i in range(len_s - len_t + 1):
        sub_s = s[i:i + len_t]
        if sorted(sub_s) == t:
            return True
    return False


# Method 2 -
# to find out whether one string is an anagram of another string, we just need
# to know if they contain the same characters. Sorting and comparing them is
# one way. A more efficient way is to count the number of occurrences of each
# distinct character. The result would be a dictionary mapping to each character
# the number of its occurrences. Then you just compare the dictionary of str1
# with the dictionary of str2, and if they are equal, the strings are anagrams
# of each other.


def make_dict(a):
    d = dict.fromkeys(a, 0)
    for c in a:
        d[c] += 1
    return d


def question1(s, t):
    if s is None or t is None:
        return "Error: Please enter valid strings"
    if len(s) == 0 or len(s) < len(t):
        return "Error: Length of s cannot be smaller than length of t"
    t_dict = make_dict(t)
    for i in range(len(s)):
        window = make_dict(s[i:i + len(t)])
        if t_dict == window:
            return True
    return False

