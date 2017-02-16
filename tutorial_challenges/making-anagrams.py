"""
Check out the resources on the page's right side to learn more about arrays. 
The video tutorial is by Gayle Laakmann McDowell, 
author of the best-selling interview book Cracking the Coding Interview.

Input
Given two strings, a and b , that may or may not be of the same length, 
determine the minimum number of character deletions required to make a and b anagrams. 
Any characters can be deleted from either of the strings.

Output Format

Print a single integer denoting the number of characters you must delete 
to make the two strings anagrams of each other.

Sample Input
abc
dce

Sample Output
4

@aisabellafontes

"""
import math
import string

abc = list(string.ascii_lowercase)

def delta(first, second):
    if len(first) != len(second):
       return -1 #todo: better error handling
    delta = 0
    for i in first:
        difference = math.fabs(first[i] - second[i])
        delta += difference
    return int(delta)

def char_counts(s):
    letters = dict((el,0) for el in abc)
    for w in s:        
        letters[w] +=1
    return letters
    
def number_needed(a, b):
    first = char_counts(a)
    second = char_counts(b)
    return delta(first, second)
     
a = raw_input().strip()
b = raw_input().strip()

print number_needed(a, b)


