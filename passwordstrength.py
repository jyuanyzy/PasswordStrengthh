# PasswordStrength.py
# Name 
# Date 

""" Assesses passwords for their strength.
"""

import string
from math import *

SPECIAL= string.punctuation
DIGITS= string.digits
LOWER= string.letters[0:25]
UPPER= string.letters[25: ]
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
UPPER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LOWER = 'abcdefghijklmnopqrstuvwxyz'
#there are repetitions because we divided up the different tests and used different variables
DIGITS = '0123456789'
EVERYTHING = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()'
ROW2 = 'qwertyuiop'
ROW3 = 'asdfghjkl'
#global variables
def HowMany(s1,s2):
    num = 0
    for c in s1:
        if s2.count(c) > 0:
            num = num + 1
    return num
#counts how many characters in s1 are in s2
def HowManyTriplets(s1,s2):
    num=0
    for c in range(0,len(s1)):
        if s2.count(s1[c]) > 0:
            if (c+3)<=len(s1):
                if s1[c+1] in s2 and s1[c+2] in s2:
                    num+=1
        else:
            num=0
    return num
 #counts how many times there are three consecutive look-a-likes    
def B1(s):
    """ Returns an int that is a score associated
    with password length.
    
    PreC: s is a valid password string."""
    
    return 3*min(len(s),15)

def B2(s):
    '''returns bonus score for mix of upper and lower case letters'''
    L = HowMany(s, LOWER)#number of lower case letters
    N = HowMany(s, LOWER+UPPER) #number of lower and upper case letters in general
    U = HowMany(s, UPPER) #number of upper case letters
    if N == 0:
        return 0
        #if there is no letter, the score is zero
    else:
        return int(floor(40.0*(1-(float(L)/float(N)))*(1-(float(U)/float(N)))))
        #the bonus score formula when there are letters

def B3(s):
    """ Returns the number of digits (count)
    in password.
    
    PreC: s is a valid password string."""
    
    count = 0
    for c in range(0,len(s)):
        if s[c] in DIGITS:
            count += 1
    return 4*count

def B4(s):
   """  Returns an int that is a score associated 
   with the number of special characters in the password """
 
   N=HowMany(s,SPECIAL) #intializes counter that stores the number of special charaters
   return 6*N
    
def B5(s):
   """ Returns an int that is a score associated
   with the number of special charactes or digits in the password
   
   Attention: excludes the zeroth and last character in the password"""
   
   ns=s[1:(len(s)-1)]
   special=HowMany(ns, SPECIAL) 
   digits=HowMany(ns, DIGITS)
   
   N=special+digits
   return 3*N


def B6(s):
    """ Returns an int score of 10 if the password contains
    a lower case letter, an upper case letter, a special character,
    and a digit. Else, returns an int score of zero"""
    S=HowMany(s, SPECIAL)
    D=HowMany(s, DIGITS)
    L=HowMany(s, LOWER)
    U=HowMany(s, UPPER)
    
    if (S>0) and (D>0) and (L>0) and (U>0):
      B6=10
    else:
         B6=0
    return B6

def D1(s):
    """ Returns the length of password if it is comprised
    only of letters. Otherwise, returns zero.
    
    PreC: s is a valid password string."""
    
    n = len(s)
    if s.isalpha() == True:
        n = n
    else:
        n = 0
    return n
    
def D2(s):
    """ Returns the length of password if it is comprised
    only of digits. Otherwise, returns zero.
    
    PreC: s is a valid password string."""
    
    n = len(s)
    if s.isdigit() == True:
        n = n
    else:
        n = 0
    return n
    

def D3(s):
    """ Returns the length of the password subtract the number of
    characters in the password that appear exactly once multiply by three.
    Testing for repeated characters.
    
    PreC: s is a valid password string."""
    
    n = len(s)
    m = 0
    for c in s:
        if s.count(c) == 1:
            m += 1
    return 3*(n-m)

def D4(s):
    '''
    returns two times the total number of consecutive look-a-likes
    '''
    count = 0  #starts with user input
    N = len(s) # length of the password
    for i in range(N-1): # for every character in the range of the password
        ch1 = s[i] # one character
        ch2 = s[i+1] # the character after the previou sone
        if EVERYTHING.index(ch1) <= 25 and EVERYTHING.index(ch2) <= 25:
            count = count + 1
            # if the two characters are both upper case letters
        elif 26 <= EVERYTHING.index(ch1) <= 51 and 26 <= EVERYTHING.index(ch2) <= 51:
            count = count + 1
            #if the two characters are both lower case letters
        elif 52 <= EVERYTHING.index(ch1) <= 62 and 52 <= EVERYTHING.index(ch2) <= 62:
            count = count +1
            #if the two characters are both numbers
        elif 63 <= EVERYTHING.index(ch1) <= 71 and 63 <= EVERYTHING.index(ch2) <= 71:
            count = count +1
            #if the two characters are both special characters
    return count*2

            
def D5(s):
    ''' Returns number of triplets in password'''
    
    return 3*HowManyTriplets(s, DIGITS)

def D6(s):
    '''returns three times the total number of row-2 triplets'''
    return 3*HowManyTriplets(s,ROW2)

def D7(s):
    '''returns three times the total number of row-3 triplets'''
    return 3*HowManyTriplets(s,ROW3)

def D8(s):
   """ Returns an int that represents the deduction
   related to the number of row-4 triplets """
   
   row4='zxcvbnm'
   N=HowManyTriplets(s, row4)
   return 3*N 
    
def PWS(s):
    pass

if __name__ == '__main__':
    s = raw_input('Enter a string: ')
    print 'B1 = %2d' % (B1(s))
    print 'B2 = %2d' % (B2(s)) 
    print 'B3 = %2d' % (B3(s))
    print 'B4 = %2d' % (B4(s))
    print 'B5 = %2d' % (B5(s))
    print 'B6 = %2d' % (B6(s))
    print 'D1 = %2d' % (D1(s))
    print 'D2 = %2d' % (D2(s))
    print 'D3 = %2d' % (D3(s))
    print 'D4 = %2d' % (D4(s))
    print 'D5 = %2d' % (D5(s))
    print 'D6 = %2d' % (D6(s))
    print 'D7 = %2d' % (D7(s))
    print 'D8 = %2d' % (D8(s))
    
           
    

