from tkinter import Tk, Canvas, PhotoImage, mainloop
from sys import argv
from binascii import hexlify, unhexlify
from io import StringIO
from lz4framed import decompress
from os import name as os_name

debug = True #print debug information?
measure_time = False #test pixel peformance?

def debug(string = '', end = '\n'):
    if debug:
        print(string, end = end)

filename = None
if len(argv) != 2:
    print('No filename (or too many arguments) provided, using default file name (sample.cif).')
    filename = 'sample.cif'
else:
    filename = argv[1]
f = open(filename, 'rb')
hexdata_stream = StringIO(hexlify(f.read()).decode())
f.close()
VERSION = int(hexdata_stream.read(2), 16)
WIDTH = int(hexdata_stream.read(4), 16)
HEIGHT = int(hexdata_stream.read(4), 16)
COMMENT_LENGTH = int(hexdata_stream.read(2), 16)
debug('Comment length: '+ str(COMMENT_LENGTH))
COMMENT = unhexlify(hexdata_stream.read(COMMENT_LENGTH * 2)).decode()
debug('.cif spec v' + str(VERSION) + '\nWidth: ' + str(WIDTH) + '\nHeight: ' + str(HEIGHT) + '\nComment: "' + str(COMMENT) + '"')

window = Tk()
window.title(filename)
canvas = Canvas(window, width = WIDTH, height = HEIGHT, bg = '#000000')
canvas.pack()
img = PhotoImage(width = WIDTH, height = HEIGHT)
to_add = 2 if os_name == 'nt' else 1 #seems to work, don't ask
canvas.create_image((WIDTH / 2 + to_add, HEIGHT / 2 + to_add), image = img, state = 'normal')

if measure_time:
    from time import perf_counter
    perf_counter()
compressed = hexdata_stream.read().encode()
hexdata_stream_decompressed = StringIO(hexlify(decompress(unhexlify(compressed))).decode())
for y in range(HEIGHT):
    for x in range(WIDTH):
        colour = '#' + hexdata_stream_decompressed.read(6)
        img.put(colour, (x, y))
    if y % 5 == 0:
        debug('Read and put pixel row ' + str(y) + ' (' + str(int(y / HEIGHT * 100)) + '%)', end = '\r')

if measure_time:
    print('Time it took to decompress, read and put pixel values:', round(perf_counter(), 2))
else:
    debug() #make sure there is no debug message about pixel rows left
mainloop()
