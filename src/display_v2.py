from tkinter import Tk, Canvas, PhotoImage, mainloop
from sys import argv
from binascii import hexlify, unhexlify
from io import StringIO

debug = False
measure_time = True

if len(argv) != 2:
    raise ValueError('No filename provided')

f = open(argv[1], 'rb')
hexdata_stream = StringIO(hexlify(f.read()).decode())
f.close()
VERSION = int(hexdata_stream.read(2), 16)
WIDTH = int(hexdata_stream.read(4), 16)
HEIGHT = int(hexdata_stream.read(4), 16)
COMMENT_LENGTH = int(hexdata_stream.read(2), 16)
if debug:
    print('comment length:', COMMENT_LENGTH)
COMMENT = unhexlify(hexdata_stream.read(COMMENT_LENGTH * 2)).decode()
if debug:
     print('.cif spec v', VERSION, '\nwidth: ', WIDTH, '\nheight: ', HEIGHT, '\ncomment: "', COMMENT, '"', sep = '')

window = Tk()
canvas = Canvas(window, width = WIDTH, height = HEIGHT, bg = '#000000')
canvas.pack()
img = PhotoImage(width = WIDTH, height = HEIGHT)
canvas.create_image((WIDTH / 2 + 2, HEIGHT / 2 + 2), image = img, state = 'normal')

if measure_time:
    from time import perf_counter
    perf_counter()

for y in range(HEIGHT):
    for x in range(WIDTH):
        colour = '#' + hexdata_stream.read(6)
        img.put(colour, (x, y))
    if debug and y % 5 == 0:
        print('read and put pixel row', y, end = '\r')

if measure_time:
    print('Time it took to read and put pixel values:', round(perf_counter(), 2))

mainloop()
