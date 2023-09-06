#!/usr/env python
import sys

# CONSTANTS
str1 = '$'
str2 = '*$'
str3 = '0\n'

invalidMsg = 'Invalid Entry!'
prompt='Enter the height of the pattern input (must be greater than 0):'
#----------------------------
# VARIABLES
buffer=''
#
def print_and_save(ch):
   global buffer
   sys.stdout.write(ch)
   buffer = buffer + ch

# Get the number of lines to print
while(True):
   ln_cnt = int(input(prompt));
   if ln_cnt <= 0:
       print(invalidMsg)
   else:
       break

ln_no=1   # first line number
while (ln_no<=ln_cnt):      # outer loop - exits past the last line
   print_and_save(str1);   # print first $
   ch_inx = 1 
   while (ch_inx < ln_no): # inner loop - for chars in line
      print_and_save(str2);   # print first star
      ch_inx += 1 
   print_and_save(str3);   # print last char
   ln_no += 1  # outer loop index

################################################
#   This is not part of the student's code.
################################################
# fname = 'lab3_output_n' + str(ln_cnt) + '.txt'
fname = 'lab3_output.txt'
f = open(fname, 'w')
f.write(buffer)

