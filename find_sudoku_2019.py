import numpy
import time
start = time.time()

retry_times = 0

#Easy
board = numpy.matrix([[8, 7, 6, 9, 0, 0, 0, 0, 0],
                      [0, 1, 0, 0, 0, 6, 0, 0, 0],
                      [0, 4, 0, 3, 0, 5, 8, 0, 0],
                      [4, 0, 0, 0, 0, 0, 2, 1, 0],
                      [0, 9, 0, 5, 0, 0, 0, 0, 0],
                      [0, 5, 0, 0, 4, 0, 3, 0, 6],
                      [0, 2, 9, 0, 0, 0, 0, 0, 8],
                      [0, 0, 4, 6, 9, 0, 1, 7, 3],
                      [0, 0, 0, 0, 0, 1, 0, 0, 4]])

original_board = numpy.copy(board)

# Return the values 1 to 9 that are missing
def find_inverse(array):
    new_array = []
    for i in range(1,10):
        if not i in array:
            new_array.append(i)
    return new_array


def find_sub_matrix(board, column, row):        
    def return_range(number):
        if number >= 0 and number <= 2:
            a = 0
            b = 3
        elif number >= 3 and number <= 5:
            a = 3
            b = 6     
        elif number >= 6 and number <= 8:
            a = 6
            b = 9
        else: 
            raise Exception(ValueError)
        return a, b 
    a, b = return_range(row)
    c, d = return_range(column)
    return board[a:b, c:d]


print(f'Remaining numbers: {numpy.sum(board == 0)}')
while 0 in board:
    if retry_times >= 20000:
        print("Could not find solution :(")
        print(f'Remaining numbers: {numpy.sum(board == 0)}')
        print("Here's where I got to though:")
        break
    for column_number in range(0,9):
        for row_number in range(0,9):
            if board[row_number, column_number] == 0:
                # Get current row
                current_row = board[row_number].tolist()[0]

                # Get current Row
                current_column = board[:,column_number].tolist()
                current_column = [b for a in current_column for b in a]

                # Get current Matrix
                current_matrix = find_sub_matrix(board, column_number, row_number)
                current_matrix_list = [
                    b for a in current_matrix.tolist() for b in a if b] # All non-zero numbers

                # What's not in each one?
                not_in_row = find_inverse(current_row)
                not_in_column = find_inverse(current_column)
                not_in_matrix = find_inverse(current_matrix_list)

                # Is there something that's not in all three?
                intersection = set(not_in_row).intersection(not_in_column, not_in_matrix)
                if len(intersection) == 1:
                    board[row_number, column_number] = list(intersection)[0]
                    print(
                        f'Found number ({list(intersection)[0]})at {row_number},{column_number}')
                    print(f'Remaining numbers: {numpy.sum(board == 0)}')
                    retry_times = 0
                retry_times += 1 
            
            #print(board)
            

if 0 not in board:
    print("SOLVED!!!!!")
print(board)
print("Original Board:")
print(original_board)
print('It took', time.time()-start, 'seconds.')
