__cif__
=======

Custom Image Format specification and reference implementation
--------------------------------------------------------------
*Note:* This is in a very early stage of development and not actually meant to be used productively but to learn a thing or two about (custom) file formats.

Usage
-----
Customize and run *create_sample.py*, which will create a .cif file you can display using either *display.py* or *display_v2.py*. The difference between the to display scripts is that the first version reads continuously from the image file while version two reads all the data at once and then reads from a string buffer.

Future of this project
----------------------
As said in the specification, compression of image data is still to be implemented. Furthermore, no alpha channel is used, which may change in a later version.
