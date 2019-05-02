#!/usr/bin/python
#
# ~/.vimrc - set modeline
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
#
# Program Description:
# Program Requires:
# Created By: Kowen Houston
#

# Define modules
import numpy

# Define and Declare Variables


def check_row(rowtocheck, column):
    #print rowtocheck[0,1], column
    if rowtocheck == 0:
        
        for b in range(8):
            print(column[b,0])

one = two = three = four = five = six = seven = eight = nine = board = numpy.zeros((9, 9))


board = numpy.matrix([[5, 0, 0, 4, 0, 6, 1, 3, 0],
                      [0, 3, 0, 0, 1, 8, 0, 6, 0],
                      [0, 6, 0, 0, 0, 5, 8, 7, 2],
                      [4, 0, 0, 0, 8, 0, 0, 0, 0],
                      [2, 9, 0, 0, 0, 0, 7, 1, 4],
                      [7, 0, 6, 9, 9, 9, 9, 8, 9],
                      [3, 0, 9, 0, 0, 0, 5, 2, 0],
                      [0, 7, 1, 0, 0, 2, 9, 8, 0],
                      [0, 0, 5, 3, 0, 1, 6, 4, 0]])

# Horizontal Row Checking
for n in range(8):
    for m in range(8):
        check_row(board[n,m], board[:,n])

# Vertical Row
#for n in range(8):
#    check_row(board[:,n])
