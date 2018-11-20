#####################################
#### PART 9: FUNCTION EXERCISES #####
#####################################


# Complete the tasks below by writing functions! Keep in mind, these can be
# really tough, its all about breaking the problem down into smaller, logical
# steps. If you get stuck, don't feel bad about having to peek to the solutions!

#####################
## -- PROBLEM 1 -- ##
#####################

# Given a list of integers, return True if the sequence of numbers 1, 2, 3
# appears in the list somewhere.

# For example:

# arrayCheck([1, 1, 2, 3, 1]) → True
# arrayCheck([1, 1, 2, 4, 1]) → False
# arrayCheck([1, 1, 2, 1, 2, 3]) → True

def arrayCheck(nums):
    for item in range(len(nums)-2):
        seq = []
        seq.extend([nums[item],nums[item+1],nums[item+2]])
        if  seq == [1,2,3]:
            print (True)
            return True
    print (False)

#arrayCheck([1, 1, 2, 3, 1])
#####################
## -- PROBLEM 2 -- ##
#####################

# Given a string, return a new string made of every other character starting
# with the first, so "Hello" yields "Hlo".

# For example:

# stringBits('Hello') → 'Hlo'
# stringBits('Hi') → 'H'
# stringBits('Heeololeo') → 'Hello'



def stringBits(str):
    new_string = ""
    for i in range(0,len(str),2):
        new_string += str[i]
    #print (new_string)
    return new_string
  # CODE GOES HERE
#stringBits('Heeololeo')

#####################
## -- PROBLEM 3 -- ##
#####################

# Given two strings, return True if either of the strings appears at the very end
# of the other string, ignoring upper/lower case differences (in other words, the
# computation should not be "case sensitive").
#
# Note: s.lower() returns the lowercase version of a string.
#
# Examples:
#
# end_other('Hiabc', 'abc') → True
# end_other('AbC', 'HiaBc') → True
# end_other('abc', 'abXabc') → True


def end_other(a, b):
    a = a.lower()
    b = b.lower()

    # if a the last b length letters of a are equal to b
    # or
    #if the last a length letters of a are equal to b
    return a[-(len(b)):] == b or a == [-len(a):]

    # return (b.endswith(a) or a.endswith(b))

  # CODE GOES HERE
#end_other('AbC', 'HiaBc')
#####################
## -- PROBLEM 4 -- ##
#####################

# Given a string, return a string where for every char in the original,
# there are two chars.

# doubleChar('The') → 'TThhee'
# doubleChar('AAbb') → 'AAAAbbbb'
# doubleChar('Hi-There') → 'HHii--TThheerree'

def doubleChar(str):
    double = ""
    for char in str:
        double += (char + char)
    print (double)
    return double

  # CODE GOES HERE

#doubleChar('Hi-There')


#####################
## -- PROBLEM 5 -- ##
#####################

# Read this problem statement carefully!

# Given 3 int values, a b c, return their sum. However, if any of the values is a
# teen -- in the range 13-19 inclusive -- then that value counts as 0, except 15
# and 16 do not count as a teens. Write a separate helper "def fix_teen(n):"that
# takes in an int value and returns that value fixed for the teen rule.
#
# In this way, you avoid repeating the teen code 3 times (i.e. "decomposition").
# Define the helper below and at the same indent level as the main no_teen_sum().
# Again, you will have two functions for this problem!
#
# Examples:
#
# no_teen_sum(1, 2, 3) → 6
# no_teen_sum(2, 13, 1) → 3
# no_teen_sum(2, 1, 14) → 3

def fix_teen(n):
    # for i in range(13,20):
    #     if n == i and n != 15 and n != 16 :
    #         return 0
    # return n
    if n [13,14,17,18,19]:
        return 0
    return n


def no_teen_sum(a, b, c):
    sum = fix_teen(a) + fix_teen(b) + fix_teen(c)
    print (sum)
    return sum

#no_teen_sum(2, 1, 14)

#####################
## -- PROBLEM 6 -- ##
#####################

# Return the number of even integers in the given array.
#
# Examples:
#
# count_evens([2, 1, 2, 3, 4]) → 3
# count_evens([2, 2, 0]) → 3
# count_evens([1, 3, 5]) → 0

def count_evens(nums):
    even = 0
    for item in nums:
        if item%2 == 0:
            even += 1
    print(even)
    return even
  # CODE GOES HERE
count_evens([1, 3, 5])
