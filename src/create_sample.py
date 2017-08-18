from binascii import hexlify

filename = 'sample.cif'
version = b'\x00'
width = b'\x02\x00'
height = b'\x02\x00'
comment_length = b'\x1B'
comment = b'\x54\x68\x69\x73\x20\x69\x73\x20\x61\x20\x73\x61\x6D\x70\x6C\x65\x20\x2E\x63\x69\x66\x20\x66\x69\x6C\x65\x2E' #'This is a sample .cif file.'
colour_one = b'\x00\x00\xff'
colour_two = b'\x00\xff\x00'
square_size = 8 #the size of a square of pixels

with open(filename, 'wb') as f:
    f.write(version)
    f.write(width)
    f.write(height)
    f.write(comment_length)
    f.write(comment)
    for y in range(int(hexlify(height), 16)): #this will result in a chess-board-like pattern of colout one and two
        for x in range(int(hexlify(width), 16)):
            if y % (square_size * 2) < square_size:
                if x % (square_size * 2) < square_size:
                    f.write(colour_one)
                else:
                    f.write(colour_two)
            else:
                if x % (square_size * 2) < square_size:
                    f.write(colour_two)
                else:
                    f.write(colour_one)
