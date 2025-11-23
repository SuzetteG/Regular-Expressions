#Regular Expressions (or regex) in Python are used for pattern matching within strings.
# They allow you to search, match, and manipulate strings based on specific patterns.
# Here's a brief overview of how to use regex in Python using the `re` module.
#Regular expressions are especially useful in situations such as data validation, 
# web scraping, and parsing large volumes of data for specific formats, 
# like email addresses or phone numbers. 
# Regex can significantly simplify complex string operations, helping developers work 
# smarter and more efficiently.

#Validation: Checking if a string matches a specific pattern.
#Data Extraction: Extracting specific parts of a string based on patterns.
#Text Replacement: Replacing parts of a string that match a pattern.
#Splitting Strings: Dividing a string into a list based on a pattern.
#Searching for Patterns: Finding occurrences of a pattern within a string.

#Literal Characters, Metacharacters, and Special Sequences:
#regex utilizes combinations of different characters and letters to define search patterns. 
#Literal Characters: These are the exact characters you want to match in a string. 
# for example: the letter 'a' will match only the character 'a'.
#Metacharacters: These are special characters that have specific meanings in regex.
# for example: '.' matches any character except a newline, '*' matches zero or more occurences of 
# the preceding element, '^' matches the start of a string, '$' matches the end of a string, 
# and '[]' defines a character class.
#Special Sequences: These are shorthand notations for common character classes. Using \
# for example:  \d matches any digit, \w matches with a word character, \s matches any whitespace 
# character.

#Regex in Python: 
import re

#Understanding Regex Method (function) Parameters: 
# the re module provides several methods that allow you to search, match, split, or substitute
# strings based on regex patterns. Here are some commonly used methods:
# Pattern: The regex pattern you want to search for.
# Text: The string you want to search within.
# Flags: Optional parameters that modify the behavior of the regex search,
# such as making it case-insensitive (re.IGNORECASE) or allowing dot (.) to match newlines 
# (re.DOTALL).

#Finding all Matches re.findall():
#This method is used to find all non-overlapping matches of a pattern in a string.
# Pattern: r'\d+' (matches one or more digits)
# Text: 'There are 2 apples and 5 bananas.'
#Counting 'and' in a sentence. 
import re
text = "Hi my name is Travis, and I like to go and do things and stuff"
ands = re.findall(r"and", text)  
#re.findall() returns a list of all occurrances of the given regex pattern within the text.
print(ands)  # Output: ['and', 'and', 'and'] 
print(len(ands))  
# Output: 3 	Here we use the len() function to get the number of items in the list 
# that was returned to us
#Extracting hashtags
post = "I LOVE # learning #Python_is_lyfe and #Regex, this is so fun! #Code"
tags = re.findall(r"#\w+", post)
print(tags)  # Output: ['#Python_is_lyfe', '#Regex', '#Code']

#Extracting Email Addresses
import re
text = "Contact us at support@example.com or sales@example.com"
emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}",text)
print(emails)  

tweets = [
    "Loving the #sunset! So peaceful #nature #blessed",
    "Had a great day! #happy #friends #goodvibes",
    "Can't wait for the #weekend! #fun #relax"
]

# Write your code to extract hashtags below
all_hashtags = []
for tweet in tweets:
    hashtags = re.findall(r"#\w+", tweet)
    all_hashtags.extend(hashtags)

print(all_hashtags) #Output: ['#sunset', '#nature', '#blessed', '#happy', '#friends', '#goodvibes', '#weekend', '#fun', '#relax']

#Using re.search() to search a string for the first occurrence of a pattern and return a matching 
# object.
#re.search(pattern, text) 
email = "kareem33-34-28@gmail.com"
found = re.search(r"[\w.-]+@[\w-]+\.[a-z]{2,3}", email)
if found:
    print(f"{found.group()} is a valid email! Please click continue!")  
# Output: kareem33-34-28@gmail.com is a valid email! Please click continue!

#Finding all the email addresses in a text using re.findall()
text = "You can contact me at t.p@gmail.com or travis-p2@codingtemple.com, traviscpeck@email.com"
emails = re.findall(r"[\w.-]+@[\w-]+\.[a-z]{2,3}", text)
print(emails)  # Output: ['t.p@gmail.com', 'travis-p2@codingtemple.com', 'traviscpeck@email.com']
#Pattern: r"[\w.-]+@[\w-]+\.[a-z]{2,3}"
#Text: The string containing potential email addresses.
#re.search() finds the first match while re.findall() retrieves all matches in a list.

#Finding Phone Numbers in Text 
import re
text = "Contact us at (123) 456-7890 or 987-654-3210 for more information."
phones = re.findall(r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]\d{4}", text)
for phone in phones:
    print(f"Phone number found: {phone}")
# Output: Phone number found: (123) 456-7890
#         Phone number found: 987-654-3210

#Matching patterns at the start of the string using re.match()
#This function checks whether the beginning of a string matches a specified pattern.
#It is different from search() because match() only checks the start of the string.
#If a match is found at the beginning, it returns a match object; otherwise, it returns None.
#This makes match ideal for validating formats that should appear at the start of a string,
# such as checking if a string starts with a specific prefix or validating input formats.
url = "https://something.com"
secure = re.match(r"https", url)
if secure:
    print("This link goes to a secure website!")  # Output: This link goes to a secure website!
#Pattern: r"https"
#Text: url string to be checked.

#Extracting specific information from Text

import re 
url = "https://www.example.com"
match = re.match(r"^https|http", url)
if match:
    print("Protocol found:", match.group())
    
#Splitting text with re.split()
#This method splits a string into a list based on a specified pattern.
#Pattern: r"\s+" (matches one or more whitespace characters)

text = 'Python,Regex;Splitting-Example. Fun, right!'
words = re.split(r"[\s,.;\-!]+", text)
print(words)  
# Output: ['Python', 'Regex', 'Splitting', 'Example', 'Fun', 'right', '']

#Pattern: , Comma ; Semicolon . Period - Hyphen ! Exclamation mark \s Whitespace characters
# + This ensures the consecutive occurrences of the delimiters are treated as a single split point.
#Text: The string contains multiple delimiters.
# Why did the empty string appear? The empty string appears because the pattern matches 
# the end of the string after the last delimiter, resulting in an empty split.

#Separating Data in a CSV String
import re
csv_data = "Name,Age,Occupation"
fields = re.split(r",", csv_data)
print(fields) 

#Substituting Text with re.sub(pattern, replacer, text)
#This method replaces occurrences of a pattern in a string with a specified replacement string.
#Pattern: r"cat" (matches the word "cat")
#Pattern: The regular expression pattern to search for.
#Replacer: The string to replace the matched pattern with.
#Text: The original string where replacements will be made.
#Phone Numbers: 
number = "(770) 888-1180"
formatted_number = re.sub(r"\D", '', number)
print(formatted_number)  # Output: 7708881180

#Anonymizing Chat User Mentions
#re.sub() to anonymize chat names and replace with placeholder @user-anon
chat = '''
@Yve-bee123 : "I think I love Regex"
@Travis : "Aren't you married?"
@Yve_bee123 : "It's just not the same"
@Travis : "They better not see this!"
'''

anon_chat = re.sub(r"@[\w-]+", '@user-anon', chat)
print(anon_chat)
#Pattern: r"@[\w-]+"
#Replacer: '@user-anon'
#Text: The original chat string containing user mentions.

#Text formatting: Standardizing phone numbers 
import re
phone = "Phone: +1 (123) 456-7890"
standard_phone = re.sub(r"\D", "", phone)
print(standard_phone)  # Output: 11234567890

#Grouping with Regex
#Grouping allows you to capture specific parts of a matched pattern for further processing.
#Parentheses () are used to define groups in a regex pattern.
#Each group can be accessed individually from the match object.
#Pattern: r"(\d{3})-(\d{2})-(\d{4})" (matches a pattern like 123-45-6789)
#Text: "My SSN is 123-45-6789."
#group(0): The entire matched string.
#group(1): The first captured group (first three digits).
#group(2): The second captured group (next two digits).
#group(3): The third captured group (last four digits).
#syntax: re.search(pattern, text).group(n)
#Pattern: regular expression that includes parentheses () to define groups.
#Text: The string to search within.
#n: The group number to retrieve (0 for the entire match, 1 for the first group, etc.).

text = "123-456"
pattern = r"(\d+)-(\d+)"
thematch = re.search(pattern, text)
if thematch:
    print(f"Group 1: {thematch.group(1)}")  # Output: 123
    print(f"Group 2: {thematch.group(2)}")  # Output: 456

#Pattern: r"(\d+)-(\d+)" uses two groups: (\d+) captures one or more digits before and after 
# the hyphen.
#Text: "123-456" is the string being searched.

#Final Challenge: Create a simple email validation script that accepts a list of emails and checks 
#if they are valid based on regex pattern. Print out valid and invalid emails separately.
emails = [
    "correct.email@example.com",
    "incorrect-email-at-example.com",
    "another.correct.email@example.org"
]

# Write your code below to validate the emails using re.search()

for email in emails:
    # Implement regex search here
    if re.search(r"[\w.-]+@[\w-]+\.[a-z]{2,3}", email):
        print(f"{email} is valid")
    else:
        print(f"{email} is invalid")

