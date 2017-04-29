cipherArr = [
                [ 'A', 'B', 'D', 'C', 'E', '#' ],
                [ 'F', '(', 'H', 'I', 'J', 'G' ],
                [ ')', 'L', 'O', 'M', 'N', 'K' ],
                [ 'P', '^', 'S', 'Q', 'R', 'T' ],
                [ 'U', '*', 'W', 'X', 'V', 'Y' ],
                [ '$', 'Z', ' ', '%', '@', '!' ]
            ]
cipherArr = [ [ 'A', 'B', 'D', 'C', 'E', '#' ], [ 'F', '(', 'H', 'I', 'J', 'G' ], [ ')', 'L', 'O', 'M', 'N', 'K' ], [ 'P', '^', 'S', 'Q', 'R', 'T' ], [ 'U', '*', 'W', 'X', 'V', 'Y' ], [ '$', 'Z', ' ', '%', '@', '!' ] ]
def cipher(input):
    out = ""
    for inpI in range( len(input) ):
        for row in range( len(cipherArr) ):
            for col in range( len(cipherArr[row]) ):
                if cipherArr[row][col] is input[inpI]:
                    out += cipherArr[col][row]
    return out
inputX = raw_input("Input text to cipher/decipher: ")
print(''.join(cipher(inputX)))
