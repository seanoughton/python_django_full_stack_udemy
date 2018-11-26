import re

# patterns = ["term1","term2"]
#
# text = "This is a string with term1, not the other!"
#
# for pattern in patterns:
#     print("I'm searching for: " + pattern)
#     #search function is part of regex module
#     #it takes the pattern and the string as arguments
#     #re.search returns a match object
#         if re.search(pattern,text):
#             print("Match")
#         else:
#             print("No Match")

    #match = re.search('term1',text)
    #match.start() = will return a number which represents the char index in the string where the match starts

    #you can use regex to split a string on a character
    #split_term = @
    #email = 'user@gmail.com'
    #print (re.split(split_term,email)) => ['user','gmail.com']

    #re.findall => will return a list of all non overlapping matches in a string
    #re.findall ('match','test phrase match in match middle')

    #METACHARACTER SYNTAX

    # There are five ways to express repetition in a pattern:
    #
    #     1.) A pattern followed by the meta-character * is repeated zero or more times.
    #     2.) Replace the * with + and the pattern must appear at least once.
    #     3.) Using ? means the pattern appears zero or one time.
    #     4.) For a specific number of occurrences, use {m} after the pattern, where
    #         m is replaced with the number of times the pattern should repeat.
    #     5.) Use {m,n} where m is the minimum number of repetitions and n is the
    #         maximum. Leaving out n ({m,}) means the value appears at least m times,
    #         with no maximum.

def multi_re_find(patterns,phrase):
    for pat in patterns:
        print("Searching for pattern {}".format(pat))
        print(re.findall(pat,phrase))
        print('\n')
        return (re.findall(pat,phrase))
#test_phrase = 'sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd'
#test_phrase = 'This is a string! But it has punctuation. How can we remove it?'
test_phrase = 'This is a string with some numbers 1233 and a symbol #hashtag'
test_patterns = [r'\d+']

multi_re_find(test_patterns,test_phrase)
