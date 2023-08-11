#Character Identifiers

""" \d  - DIGIT  - file-25  
    \w - ALPHANUMERIC  - A-b_1
    \s - WHITE SPACE  - a b c
    \D - A NON DIGIT - ABC
    \W - NON-ALPHANUMERIC -   *-+=)
    \S -  NON-WHITESPACE - Yoyo
"""
import re

text = "myphone number is , 408-555-1234"

phone  = re.search(r'\d\d\d-\d\d\d-\d\d\d\d',text)
print(phone.group())