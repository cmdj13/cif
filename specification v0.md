__.cif (Custom Image Format) file specification v0__
====================================================

Header
------
+ __format version__ - *1 byte* (counting up start at 0) <br>
+ __image width in pixels__ - *2 bytes* <br>
+ __image height in pixels__ - *2 bytes* <br>
+ __comment length in bytes__ - *1 byte* <br>
+ __comment__ - *ascii encoding*, length variable (see *__comment length in bytes__*)

Image data
----------
+ __information per pixel__ - *3 bytes* (RGB value, no alpha channel)

ToDo in next version(s)
-----------------------
+ __image data compression__ *(gzip?)*
+ __alpha channel__ *(mayhaps?)*
