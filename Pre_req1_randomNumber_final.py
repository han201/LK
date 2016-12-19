# Write a program to generate 100 random integers between 1 and 100.
# It should generate exactly the same numbers each time you run it.
# Bonus: If you wonder whether the distribution should be normal or uniform, give yourself extra points.: Uniform distribution

from EulerProject_HanFunctions import digits

import random
v = list()
random.seed( 1 )      # guarantees the same random numbers
for i in range(0, 100):
    b = random.randint(1, 100)   # from Uniform distribution
    v.append(b)
print v

# Write a program to sort a list of numbers provided on standard input (for instance, the numbers you generated above).
# You are NOT allowed to call external routines to do the sorting for you.
# After sorting the numbers, print them out. Focus on a simple method (not an efficient method).

for i in range(0, 100):
    for j in range(i, 100):
        if v[i]>v[j]:
            temp = v[i]
            v[i]=v[j]
            v[j]= temp
print v

# Write a program that can read in a list of words and convert each word into an integer, and a separate program that convert integers into words.
# The program should work with words up to 10 characters in length.
# It should generate integers in the range 0 to N^10, where N is the number of characters in the alphabet you are using.
# If N=26, then your maximum value would be 26^10 = 141167095653376.
# => I think the maximum number should be 26^10 + 26^9 + 26^8 + ... + 26^2+26^1 + 1

# We want to convert words to numbers such a way that a is 1, aa is 27 (1*26 + 1 ), aaa is 80(26*2 + 1+ 26*1 +1 + 1), etc
# z is 26, zz is 702 (26*26+26)

n = input("Enter how many words to convert: ")
a = list()
converted = list()

for i in range(0, n):
    v = raw_input("Enter each word: ")
    v = v.lower()     # Convert everything into a lower case
    output = []
    conversion = 0
    for character in v:
        number = ord(character) - 96   # Use ASCII
        output.append(number)
        #print number
    for j in range(0, len(output)):
        conversion = conversion + output[j]*26**(len(output)-j-1)
    converted.append(conversion)
    print output, conversion
    a.append(v)
print a, converted

'''
sum = 0
for k in range(0, 11):
    sum = sum + 26**k
    print 26**k, sum
'''

# Define a special 'digits26' function with mod 26, but does not allow 0. Instead, it allows 26.
def digit26(N):
    digit=list()
    while (N >0):
        if (N%26==0):
            digit.append(26)    # If divided by 26 (z), choose to have 26 instead of having 0
            N=N/26-1            # Reduce the next digit by 1 to represent the next digit not being 0, but being 26
        else:
            digit.append(N%26)
            N=N/26
    digitFront = list()
    for i in range(1, len(digit) + 1):
        digitFront.append(digit[len(digit) - i])
    return digitFront

#Next, we want to convert integers into words
n2 = input("Enter how many integers to convert: ")
a2 = list()
converted2 = list()

for i in range(0, n2):
    v2 = input("Enter each integer: ")
    output2 = []
    mod26 = digit26(v2)
    for k in mod26:
        k2 = unichr(k + 96)
        output2.append(k2)

    lst_str = ''.join(map(str, output2))           # combines each character into word
    print v2, lst_str