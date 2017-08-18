from tkinter import Tk, Canvas, PhotoImage, mainloop
from sys import argv
from binascii import hexlify

debug = False #print debug information?
measure_time = True #test pixel peformance?

if len(argv) != 2:
    raise ValueError('No filename provided')

f = open(argv[1], 'rb')
VERSION = int(hexlify(f.read(1)).decode(), 16)
WIDTH = int(hexlify(f.read(2)).decode(), 16)
HEIGHT = int(hexlify(f.read(2)).decode(), 16)
COMMENT_LENGTH = int(hexlify(f.read(1)).decode(), 16)
if debug:
    print('comment length:', COMMENT_LENGTH)
COMMENT = f.read(COMMENT_LENGTH).decode()
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
        colour = '#' + str(hexlify(f.read(3)).decode())
        img.put(colour, (x, y))
        if debug and y % 5 == 0:
            print('read and put pixel row', y, end = '\r')

if measure_time:
    print('Time it took to read and put pixel values:', round(perf_counter(), 2))

f.close()
mainloop()
