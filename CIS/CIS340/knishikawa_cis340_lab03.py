# create function
def indent(text, spaces):
'''
***************************************************************************
Function: indent(text, spaces):
Parameters: string - string to be printed
 spaces - number of spaces to be indented for printing
Outputs: print the string with indentation specified by "spaces"
Returns: None
Author: ken nishikawa
Date: 2025.10.21
Modifications: 2025.10.21

Description:
Write a function called indent( . ) that indents a string by a certain number of spaces.
The function:

    accepts 2 arguments: a string and the number of spaces.
    returns: nothing
    outputs: prints the string after printing the specified number of spaces.
    Hint: read text Ch 2.6 about the * and + operator on strings and characters. You need to use them in writing up this function.
    write a docstring for the function; see Documentation Requirements below.

'''
  print('' * spaces + text)

# Test function
indent( "Hello", 0 )
indent( "Hi", 5 )
'''
Test case 
'''




# create two functions
def indent(text, spaces):
  print('' * spaces + text)
def center(text, width):
  spaces = (width - len(text)) // 2
  indent(text, spaces)
  return spaces
'''
Filename:      knishikawa_lab03_CIS340
Author:        Ken Nishikawa
Date:          2025.10.21
Modifications: Ken Nishikawa – 2025.10.21
Question 2
Description:   This module demonstrates the use of functions to:
*   that centers a string with respect to the screen width. 
*   accepts 2 arguments: a text string and a screen width
*   prints the text string in the center of the screen. This should be done by calling the indent() function, 
gotten from step 1 above, to indent by the appropriate number of spaces; i.e. composition
*   returns the number of indentation spaces
'''



def indent(text, spaces):
  print('' * spaces + text)
def center(text, width):
  spaces = (width - len(text)) // 2
  indent(text, spaces)
  return spaces
def read_n_center_text():
  text = input('Enter text: ')
  width = int(input('Enter screen width: '))
  spaces = center(text, width)
  print('Number of indentation spaces:', spaces)
'''
Filename:      knishikawa_lab03_CIS340
Author:        Ken Nishikawa
Date:          2025.10.21
Modifications: Ken Nishikawa – 2025.10.21
Question 3
Description:   Write a main function called read_n_center_text(), or another name you deem appropriate, 
that interacts with the user to print text strings that are centered.
This main function:

    prompts the user for a text string and then prompts the user for a screen width
    calls the center( . ) function, with the keyboard inputs as arguments
    receives the return value from center( . ) and prints the number of indentation

'''


if __name__ == '__main__':
  read_n_center_text()