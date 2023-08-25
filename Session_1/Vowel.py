
'''
character=input("Enter the char : ")

vowels=['a','o','i','u','e','A','O','I','U','E']

if character in vowels:
    print("The Character '{character}' is vowel ")
else:
    print("The Character '{character}' is consonant")
'''


#-----------------------------------------------------------------------------------------
import os
  
# access environment variable
print(os.environ['HOME'])
print('*----------------------------------*')
print(os.environ['PATH'])
