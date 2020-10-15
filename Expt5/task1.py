import numpy as np


def even_parity(sequence):
    '''
    Checks if given sequence has even parity
    '''
    result = 0
    for i in sequence:
        result ^= i
    if result == 0: return True
    return False


def rect_parity(codeword,nrows,ncols):
    codeword = np.array(codeword)
    k = nrows * ncols
    # Extract message, row and column parity from given codeword.
    message = codeword[:k]
    row_p = codeword[k: k + nrows]
    col_p = codeword[k + nrows: k + nrows + ncols]
        
    message_array = message.reshape((nrows, ncols))

    row_n, col_n = -1, -1
    number_of_rows_errors, number_of_column_errors = 0, 0
    
    for i, row in enumerate(message_array):
        parity = 0 if even_parity(row) else 1
        if parity != row_p[i]:
            row_n = i
            number_of_rows_errors += 1

    for i, col in enumerate(message_array.T):
        parity = 0 if even_parity(col) else 1
        if parity != col_p[i]:
            col_n = i
            number_of_column_errors += 1

    if (number_of_column_errors == 1) and (number_of_rows_errors == 1):
        message_array[row_n][col_n] = int(not message_array[row_n][col_n])
        return message_array.reshape((nrows*ncols, ))
    else:
        return message


if __name__ == '__main__':
    nrows = 2
    ncols = 4

    codeword_1 = np.array([0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1]) # Message is received without errros
    codeword_2 = np.array([1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0]) # Original Message = 10000010
    codeword_3 = np.array([0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0]) # Last column bit is wrong 
    print(f'Codeword 1 = {codeword_1}')
    print(f'Received Message = {codeword_1[: (nrows*ncols)]}')
    
    corrected_message_1 = rect_parity(codeword_1,nrows,ncols)
    print(f'Corrected Message = {corrected_message_1}')

    print(f'\nCodeword 2 = {codeword_2}')
    print(f'Received Message = {codeword_2[: (nrows*ncols)]}')
    corrected_message_2 = rect_parity(codeword_2,nrows,ncols)
    print(f'Corrected Message = {corrected_message_2}')
    
    print(f'\nCodeword 3 = {codeword_3}')
    print(f'Received Message = {codeword_3[: (nrows*ncols)]}')
    corrected_message_3 = rect_parity(codeword_3,nrows,ncols)
    print(f'Corrected Message = {corrected_message_3}')