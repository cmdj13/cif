from binascii import hexlify
from lz4framed import compress

debug = True #print debug information?

def debug(string = '', end = '\n'):
    if debug:
        print(string, end = end)

filename = 'sample.cif'
version = b'\x01'
width = b'\x01\x00'
height = b'\x01\x00'
comment_length = b'\x32'
comment = b'\x54\x68\x69\x73\x20\x69\x73\x20\x61\x20\x73\x61\x6D\x70\x6C\x65\x20\x2E\x63\x69\x66\x20\x66\x69\x6C\x65\x2C\x20\x65\x76\x65\x6E\x20\x77\x69\x74\x68\x20\x63\x6F\x6D\x70\x72\x65\x73\x73\x69\x6F\x6E\x21' #'This is a sample .cif file, even with compression!'
colour_one = b'\x00\x00\xff'
colour_two = b'\x00\xff\x00'
square_size = 4 #the size of a square of pixels

with open(filename, 'wb') as f:
    debug('Writing header...')
    f.write(version)
    f.write(width)
    f.write(height)
    f.write(comment_length)
    f.write(comment)
    uncompressed = {0: b'', 1: b'', 2: b'', 3: b'', 4: b'', 5: b'', 6: b'', 7: b'', 8: b'', 9: b''}
    debug('Building uncompressed image data string...')
    n = 0
    for y in range(int(hexlify(height), 16)): #this will result in a chess-board-like pattern of colout one and two
        for x in range(int(hexlify(width), 16)):
            if y % (square_size * 2) < square_size:
                n = int(y / int(hexlify(height), 16) * 10)
                if x % (square_size * 2) < square_size:
                    uncompressed[n] += colour_one
                else:
                    uncompressed[n] += colour_two
            else:
                if x % (square_size * 2) < square_size:
                    uncompressed[n] += colour_two
                else:
                    uncompressed[n] += colour_one
        if y % 5 == 0:
            debug('    Read and put pixel row ' + str(y) + ' (' + str(int(y / int(hexlify(height), 16) * 100)) + '%)', end = '\r')
    debug('Joining uncompressed image data strings...')
    uncompressed_as_one = b''
    for i in uncompressed:
        uncompressed_as_one += uncompressed[i]
    debug('Compressing image data string...')
    compressed = compress(uncompressed_as_one)
    debug('Writing compressed image data...')
    f.write(compressed)
    debug('Finished.')
